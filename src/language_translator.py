import json
from googletrans import Translator
from tqdm import tqdm
import random
import time

class LanguageTranslator:
    ''' A class for translating texts from one language to another using Google Translate API.'''
    def __init__(self, checkpoint_file='_translation_checkpoint.json'):
        self.checkpoint_file = checkpoint_file

    def _save_checkpoint(self, progress):
        '''Save the progress of the translation to a translation checkpoint file.'''
        with open(self.checkpoint_file, 'w', encoding='utf-8') as file:
            json.dump(progress, file)

    def _load_checkpoint(self):
        '''Load the progress of the translation from a translation checkpoint file.'''
        try:
            with open(self.checkpoint_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {'translated_texts': [], 'last_index': 0}  # Initialize progress if file doesn't exist

    def translate_text(self, text, src_lang='en', dest_lang='no'):
        '''Translate a single text from source language to destination language.'''
        translator = Translator()
        return translator.translate_text(text, src=src_lang, dest=dest_lang).text

    def translate_list(self, texts, src_lang='en', dest_lang='no', output_format='list', sleep_range=(0.2, 3), checkpoint=False, load_from_checkpoint=True):
        '''Translate a list of texts from source language to destination language with progress checkpointing.'''
        
        if checkpoint:
            # Use checkpoint if specified
            if load_from_checkpoint:
                # Load progress from checkpoint file
                progress = self._load_checkpoint()
            else:
                # Create new and empty checkpoint
                progress = {'translated_texts': [], 'last_index': 0}
                self._save_checkpoint(progress)
            translated_texts = progress.get('translated_texts', [])
            start_index = progress.get('last_index', 0)
        else:
            # No checkpointing
            translated_texts = []
            start_index = 0

        # Set up tqdm progress bar
        with tqdm(total=len(input_texts), initial=start_index, desc="Translating texts") as pbar:
            for index in range(start_index, len(input_texts)):
                try:
                    translated_text = self.translate_text(input_texts[index], src_lang, dest_lang)
                    if output_format == 'list':
                        translated_texts.append(translated_text)
                    elif output_format == 'json':
                        translated_texts.append({
                            'src_lang': src_lang,
                            'dest_lang': dest_lang,
                            'src_text': input_texts[index],
                            'dest_text': translated_text
                        })
                    # Save progress
                    progress = {'translated_texts': translated_texts, 'last_index': index + 1}
                    if checkpoint:
                        self._save_checkpoint(progress)
                    pbar.update(1)  # Update progress bar
                except Exception as e:
                    print(f"Error translating text at index {index}: {e}")
                    break

                if sleep_range is not None:
                    # Sleep for a random duration between 0.2 and max_sleep seconds
                    sleep_duration = random.uniform(*sleep_range)
                    time.sleep(sleep_duration)

        return translated_texts

# Usage example

# Read input texts from a text file
with open('input_texts.txt', 'r', encoding='utf-8') as file:
    input_texts = file.read().splitlines()

# Translate texts from Norwegian to English with progress checkpointing
translator = LanguageTranslator()
translated_texts = translator.translate_list(
    input_texts,
    src_lang='no',
    dest_lang='en',
    output_format='list',
    load_from_checkpoint=True
)

# Save translated texts to a JSON file
with open('translated_texts.json', 'w', encoding='utf-8') as file:
    json.dump(translated_texts, file, ensure_ascii=False, indent=4)
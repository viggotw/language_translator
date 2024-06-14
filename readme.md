# Language Translator
This is a simple language translator using the google translate API. The code is written in Python and is a wrapper for the googletrans module. The package allows for translating a single string or a list of strings from one language to another.

For large number of translations, the package allows for using checkpoints to save the state of the translation process. This is useful when the translation process is interrupted and you want to continue from where you left off. By default is also applies a random delay between 0.2 and 3 seconds to avoid being blocked by the google translate API.

## Installation
To install the `language_translator` package, run the following command in the root directory of the project:
```bash
pip install .
```

## Translate single string
```python
from language_translator import LanguageTranslator

translator = LanguageTranslator()
translated_text = translator.translate_text(text="Hello, how are you", src_lang='en', dest_lang='fr')
print(translated_text)
# >>> "Bonjour, comment ça va"
```

## Translate multiple strings
```python
from language_translator import LanguageTranslator

translator = LanguageTranslator()
texts = ["Hello, how are you", "I am fine, thank you"]
translated_texts = translator.translate_list(texts=texts, src_lang='en', dest_lang='fr')

print(translated_texts)
# >>> ["Bonjour, comment ça va", "Je vais bien, merci"]
```

## Translate large number of strings using checkpoints

```python
from language_translator import LanguageTranslator

translator = LanguageTranslator()
texts = ["Hello, how are you", "I am fine, thank you"]*100
translated_texts = translator.translate_list(texts=texts, src_lang='en', dest_lang='fr', checkpoint=True)
```
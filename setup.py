from setuptools import setup, find_packages

setup(
    name="language_translator",
    version="0.1",
    packages=find_packages(where='src'),
    install_requires=[
        "googletrans==3.1.0a0",
        "tqdm"
    ]
)

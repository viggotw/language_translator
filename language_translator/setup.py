from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "googletrans==3.1.0a0",
        "tqdm"
    ]
)

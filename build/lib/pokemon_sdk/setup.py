from setuptools import setup, find_packages

setup(
    name="pokemon_sdk",
    version="0.1",
    description='A Python SDK for the PokeAPI.',
    author='Shirly Manor',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
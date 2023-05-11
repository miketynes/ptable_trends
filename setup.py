from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.readlines()

setup(
    name='ptable_trends',
    version='0.0.1',
    packages=['ptable_trends'],
    install_requires=install_requires,
)
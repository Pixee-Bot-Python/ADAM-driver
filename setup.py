# setup.py
from setuptools import setup, find_packages

setup(
    name="adamlib",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pyModbusTCP'
    ],
    author="BBenchoff",
    author_email="brian.benchoff@span.io",
    description="A library to interact with ADAM devices",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
)
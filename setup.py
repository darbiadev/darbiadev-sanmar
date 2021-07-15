#!/usr/bin/env python

import pathlib

from setuptools import find_packages, setup

setup(
    name='darbiadev-sanmar',
    version='0.2.0',
    description='darbiadev-sanmar',
    url='https://gitlab.com/darbia/darbiadev-sanmar',
    long_description=(pathlib.Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    author='Bradley Reynolds',
    author_email='bradley.reynolds@darbia.dev',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    install_requires=[
        'suds-community',
        'xmltodict',
        'python-benedict',
    ], extras_require={
        'docs': [
            'sphinx',
            'sphinx-autodoc-annotation',
            'sphinxcontrib-packages',
            'sphinxcontrib-napoleon',
            'sphinxcontrib-apidoc',
            'sphinx_rtd_theme',
        ],
        'tests': [
            'pytest',
            'tox'
        ]
    }
)

# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='nli_python',
    version='1.0.0',
    author='YAT, LLC',
    author_email='rgoss@yat.ai, jhart@yat.ai',
    packages=['nli_python'],
    license="MIT",
    url='https://github.com/yat-co/nli-python',
    install_requires=[],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description='An elegantly simple Encoding and Decoding of Location to eNLI Codes (Natural Location Identifier).',
    long_description=open('README.md').read(),
    zip_safe=True,
)
#!/usr/bin/env python
"""
keychain
==============

"""

from setuptools import setup, find_packages

setup(
    name='keychain',
    version='0.14.2.0',
    url='https://github.com/blockstack/keychain-manager-py',
    license='MIT',
    author='Blockstack Developers',
    author_email='support@blockstack.com',
    description="""Library for BIP32 hierarchical deterministic keychains / wallets.""",
    keywords='bitcoin blockchain bip32 HD hierarchical deterministic keychain wallet',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'bitmerchant>=0.1.8',
        'keylib>=0.1.0',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

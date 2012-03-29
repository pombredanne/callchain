#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''setup callchain'''

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_requires = ['twoq>=0.4.8', 'appspace>=0.5.3', 'stuf>=0.8.11']

setup(
    name='callchain',
    version='0.2.3',
    url='http://bitbucket.com/lcrees/callchain',
    description='callables and components joined in one big happy call chain',
    long_description=open(os.path.join(os.getcwd(), 'README.rst'), 'r').read(),
    author='L. C. Rees',
    license='BSD',
    author_email='lcrees@gmail.com',
    packages=['callchain'],
    tests='callchain.tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
    install_requires=install_requires,
    zip_safe=False,
)

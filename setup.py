#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''setup for callchain'''

from os import getcwd
from os.path import join
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from callchain import __version__

install_requires = list(l for l in open(
    join(getcwd(), 'requirements.txt'), 'r',
).readlines())

setup(
    name='callchain',
    version='{}.{}.{}'.format(*__version__),
    description='callables and components joined in one big happy chain',
    long_description=open(join(getcwd(), 'README.rst'), 'r').read(),
    keywords='component architecture injection aspect-oriented appspace '
        'generator iterator functional',
    license='BSD',
    author='L. C. Rees',
    author_email='lcrees@gmail.com',
    url='https://bitbucket.org/lcrees/callchain',
    packages=[
        l.strip() for l in open(join(getcwd(), 'packages'), 'r').xreadlines()
    ],
    test_suite='callchain.tests',
    zip_safe=False,
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)

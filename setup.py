# -*- coding: utf-8 -*-
'''setup for callchain'''

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_requires = [
    'twoq>0.2.1', 'appspace>=0.5.1', 'zope.interface>=3.8.0', 'stuf>=0.8.6',
]
if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    install_requires.extend(['importlib', 'ordereddict', 'unittest2'])

setup(
    name='callchain',
    version='0.1.1',
    url='http://bitbucket.com/lcrees/callchain',
    description='callables and components joined in one big happy chain',
    long_description=open(os.path.join(os.getcwd(), 'README.rst'), 'r').read(),
    author='L. C. Rees',
    license='MIT',
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
    requirements=install_requires,
    zip_safe=False,
)

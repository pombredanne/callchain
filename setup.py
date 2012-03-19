# -*- coding: utf-8 -*-
'''setup callchain'''

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_requires = ['twoq>=0.2.3', 'appspace>=0.5.3']

setup(
    name='callchain',
    version='0.2.0',
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
    install_requires=install_requires,
    zip_safe=False,
)

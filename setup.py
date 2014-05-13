#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    "wheel==0.22.0",
    "Flask==0.10.1",
    "Jinja2==2.7.2",
    "MarkupSafe==0.23",
    "Werkzeug==0.9.4",
    "argparse==1.2.1",
    "beautifulsoup4",
    "distlib==0.1.8",
    "futures==2.1.6",
    "gnureadline==6.3.3",
    "ipython==2.0.0",
    "itsdangerous==0.24",
    "requests==2.2.1",
    "wsgiref==0.1.2"
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='zalando',
    version='0.1.0',
    description='Python web scrapping utils',
    long_description=readme + '\n\n' + history,
    author='Nar Kumar Chhantyal',
    author_email='noblenara@gmail.com',
    url='https://github.com/chhantyal/zalando',
    packages=[
        'zalando',
    ],
    package_dir={'zalando':
                 'zalando'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=True,
    keywords='zalando',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    console=['zalando'],
    entry_points={
        'console_scripts': ['zalando = zalando.__main__.main'],
    },

)
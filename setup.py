#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
from dj_admin_bootstrapped import __version__

try:
    long_description = open('README.rst').read()
except:
    long_description = "Admin UI customization for Django"

try:
    license = open('LICENSE.txt').read()
except:
    license = "MIT License"


REQUIREMENTS = [
    'django>=1.8.0',
]

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup(
    name='dj_admin_bootstrapped',
    version=__version__,
    description='Admin UI customization for Django',
    author='Carlos Martínez',
    author_email='carlosmart626@gmail.com',
    url='https://github.com/CarlosMart626/dj_admin_bootstrapped',
    packages=find_packages(),
    package_data={'': ['README.md']},
    install_requires=REQUIREMENTS,
    license=license,
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=long_description,
    include_package_data=True,
    zip_safe=False,
    test_suite='tests.settings.run',
)

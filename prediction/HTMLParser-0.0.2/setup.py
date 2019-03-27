#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages  # noqa

rel_file = lambda *args: os.path.join(
        os.path.dirname(os.path.abspath(__file__)), *args)


def get_file(filename):
    with open(rel_file(filename)) as f:
        return f.read()


def get_description():
    return get_file('README.md')

setup(
    name="HTMLParser",
    version="0.0.2",
    description="Backport of HTMLParser from python 2.7",
    author="Jason Ward",
    author_email="jason.louard.ward@gmail.com",
    url="http://github.com/PolicyStat/HTMLParser/",
    platforms=["any"],
    license="BSD",
    packages=find_packages(),
    scripts=[],
    zip_safe=False,
    install_requires=[],
    cmdclass={},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    py_modules=['HTMLParser'],
    long_description=get_description(),
)

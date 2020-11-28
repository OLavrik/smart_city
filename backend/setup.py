#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import re

from setuptools import find_packages, setup

VERSION_FILE = "smartcity/__init__.py"


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version():
    version_file = read(VERSION_FILE)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="smartcity",
    version=get_version(),
    packages=find_packages(),
)

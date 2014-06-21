#!/usr/bin/env python

from setuptools import setup
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='elixir',
    version='0.1.0',
    description='An AngularJS app generator',
    author='Zach McGrenere & Neil-the danger-Chudleigh',
    author_email='zach@mcgrenere.com',
    url='http://flongular.com/elixir',
    py_modules=['elixir'],
    license='MIT',
    install_requires=REQUIREMENTS
)

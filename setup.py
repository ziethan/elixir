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
    package_dir = {'':'elixir'},
    py_modules=['elixir'],
    license='MIT',
    entry_points="""
    [console_scripts]
    elixir = elixir
    """,
    include_package_data=True,
    install_requires=REQUIREMENTS,
    scripts = ["elixir"]
)

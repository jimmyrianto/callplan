# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in call_plan/__init__.py
from call_plan import __version__ as version

setup(
	name='call_plan',
	version=version,
	description='Salesman Scheduled Visit',
	author='Handoko',
	author_email='handoko.apps@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

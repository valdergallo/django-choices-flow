#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

import django_choices_flow

install_requires = [
    'django>=1.2',
]

files = [
    "./django_choices_flow/__init__.py",
    "./django_choices_flow/base.py",
    "./django_choices_flow/models.py",
]

setup(name='django_choices_flow',
      url='https://github.com/valdergallo/django-choices-flow',
      author="valdergallo",
      author_email='valdergallo@gmail.com',
      keywords='Django choices flow overflow',
      description='Simple library with flow in choices values for Django',
      license='FREEBSD',
      long_description=('''Django Choices Flow simple library to control flow with choices in Django Model'''),
      classifiers=[
          'Framework :: Django',
          'Operating System :: OS Independent',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
      ],
      include_package_data=True,
      version=django_choices_flow.__version__,
      install_requires=install_requires,
      packages=['django_choices_flow'],
      package_data={'package': files},
)

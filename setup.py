#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup
import django_choices_flow

os.system('rm -rf ./build')

install_requires = [
    'django>=1.2',
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
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Topic :: Utilities'
      ],
      include_package_data=True,
      version=django_choices_flow.__version__,
      install_requires=install_requires,
      packages=['django_choices_flow'],
      exclude_package_data={'django_choices_flow': ['models_test.py']},
)

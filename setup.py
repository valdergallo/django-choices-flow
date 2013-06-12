#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

install_requires = [
    'django>=1.2',
]

setup(name='django_choices_flow',
      url='https://github.com/valdergallo/django-choice-flow',
      author="valdergallo",
      author_email='valdergallo@gmail.com',
      keywords='Django choices flow overflow',
      description='Simple library with flow in choices values for Django',
      license='FREEBSD',
      long_description=('''Django Choices Flow simple library to control flow with choices in Django Model'''),
      classifiers=[
          'Framework :: Django',
          'Operating System :: OS Independent',
          'Topic :: Utilities'
      ],
      version='0.6.2',
      install_requires=install_requires,
      exclude_package_data={'': ['django_choices_flow/models_test.py']},
      packages=find_packages(exclude=['django_choices_flow.tests', 'django_choices_flow.models_test']),
      package_data = {'': ['LICENSE', 'README.md']},
)

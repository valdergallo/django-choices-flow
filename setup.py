#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import django_choices_flow

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
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Topic :: Utilities'
      ],
      version=django_choices_flow.__version__,
      install_requires=install_requires,
      packages=find_packages(exclude=['*test*', 'models_test*',
                             'django_choices_flow/models_test.py']),
      package_data={'': ['__init__.py', 'base.py', 'models.py']},
      exclude_package_data={'': ['models_test', 'models_test.py',
      'django_choices_flow/models_test.py']},
)

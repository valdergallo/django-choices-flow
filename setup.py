#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

import django_choices_flow

install_requires = [
    'django>=1.2',
]

def readme():
    try:
        os.system('pandoc --from=markdown --to=rst README.md -o README.rst')
        with open('README.rst') as f:
            return f.read()
    except:
        return '''Django Choices Flow simple library to control flow with choices in Django Model'''

files = [
    "./django_choices_flow/__init__.py",
    "./django_choices_flow/base.py",
    "./django_choices_flow/models.py",
]

setup(name='django_choices_flow',
      url='https://github.com/valdergallo/django-choices-flow',
      download_url='https://github.com/valdergallo/django-choices-flow/tarball/v%s/' % django_choices_flow.__version__,
      author="valdergallo",
      author_email='valdergallo@gmail.com',
      keywords=['django', 'choices', 'field', 'flow', 'choicesfield', 'control'],
      description='Simple library with flow in choices values for Django',
      license='FREEBSD',
      long_description=readme(),
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

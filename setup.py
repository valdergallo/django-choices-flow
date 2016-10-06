#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import django_choices_flow

install_requires = [
    'django>=1.2',
]

tests_requires = [
    'pytest==3.0.2',
    'pytest-django==2.9.1',
    'pytest-cov==2.3.1',
]

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests', '--cov=django_choices_flow', '-vrsx']
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


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
      tests_require=tests_requires,
      cmdclass = {'test': PyTest},
      packages=['django_choices_flow'],
      package_data={'package': files},
      zip_safe=False,
      platforms='any',
)

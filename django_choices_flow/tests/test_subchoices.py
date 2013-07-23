#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django_choices_flow import Choices


mexican_food_list = ((1, 'nacho'), (2, 'qualcamole'), (3, 'taco'))
brazil_food_list = ((4, 'burger'), (5, 'pizza'), (6, 'feijoada'))


class MyChoices(Choices):
    FOODS = (('mexican', mexican_food_list),
             ('brazil', brazil_food_list),)


class TestChoices(TestCase):

    def setUp(self):
        self.choices = MyChoices

    def test_key_value_first(self):
        self.assertEqual(self.choices.FOODS['mexican'],
                         ((1, 'nacho'), (2, 'qualcamole'), (3, 'taco')))

    def test_key_value_second(self):
        self.assertEqual(self.choices.FOODS['brazil'],
                         ((4, 'burger'), (5, 'pizza'), (6, 'feijoada')))

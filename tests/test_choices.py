# -*- coding: utf-8 -*-
from django.test import TestCase
from lib.choices import Choices


class MyChoices(Choices):
    NEW = 1, 'New content'  # 'New content' is the display text
    WAIT = 2, 'Wait'
    CANCELED = -1, 'Canceled'
    ERROR = -2, 'Error'
    INVOICED = 3, 'Invoiced'

    # set transaction rules
    NEW_RULES = [WAIT, INVOICED, CANCELED, ERROR]
    WAIT_RULES = [CANCELED, ERROR, INVOICED]
    INVOICED_RULES = [CANCELED]


class TestChoices(TestCase):

    def setUp(self):
        self.choices = MyChoices()

    def test_key_valeu(self):
        self.assertEqual(self.choices.NEW, 1)
        self.assertEqual(self.choices.WAIT, 2)
        self.assertEqual(self.choices.CANCELED, -1)
        self.assertEqual(self.choices.ERROR, -2)
        self.assertEqual(self.choices.INVOICED, 3)

    def test_len_choices(self):
        self.assertEqual(len(self.choices), 5)

    def test_iter_list(self):
        self.assertEquals(list(self.choices), [(-2, 'Error'), (-1, 'Canceled'),
                          (3, 'Invoiced'), (1, 'New content'), (2, 'Wait')])

    def test_repr_choice(self):
        self.assertEqual(str(self.choices), str([(-2, 'Error'), (-1, 'Canceled'),
                         (3, 'Invoiced'), (1, 'New content'), (2, 'Wait')]))

    def test_get_value(self):
        self.assertEqual(self.choices.get_value(1), 'New content')

    def test_rules_transaction_return_ok(self):
        self.assertEqual(self.choices.validate(self.choices.NEW, self.choices.WAIT), 2)

    def test_rules_transaction_return_false(self):
        self.assertEqual(self.choices.validate(self.choices.INVOICED, self.choices.WAIT), False)

# -*- coding: utf-8 -*-

from django.test import TestCase
from django_choices_flow import Choices


class MyChoices(Choices):
    NEW = (1, 'New content')  # 'New content' is the display text
    WAIT = (2, 'Wait')
    CANCELED = (-1, 'Canceled')
    ERROR = (-2, 'Error')
    INVOICED = (3, 'Invoiced')
    INVOICED_VALIDATION_NAME = (4, 'Invoiced Validation Name')

    # set transaction rules
    NEW_RULES = [WAIT, INVOICED, CANCELED, ERROR]
    WAIT_RULES = [CANCELED, ERROR, INVOICED]
    INVOICED_RULES = [CANCELED]


class TestChoices(TestCase):

    def setUp(self):
        self.choices = MyChoices

    def test_key_value(self):
        self.assertEqual(self.choices.NEW, 1)
        self.assertEqual(self.choices.WAIT, 2)
        self.assertEqual(self.choices.CANCELED, -1)
        self.assertEqual(self.choices.ERROR, -2)
        self.assertEqual(self.choices.INVOICED, 3)

    def test_len_choices(self):
        self.assertEqual(len(self.choices), 6)

    def test_iter_list(self):
        self.assertEquals(sorted(list(self.choices)),
                          sorted([(-1, 'Canceled'), (-2, 'Error'), (3, 'Invoiced'),
                          (1, 'New content'), (2, 'Wait'), (4, 'Invoiced Validation Name')]), self.choices)

    def test_repr_choice(self):
        self.assertEqual(str(sorted(self.choices)),
                         str(sorted([(-1, 'Canceled'), (-2, 'Error'), (3, 'Invoiced'),
                          (1, 'New content'), (2, 'Wait'), (4, 'Invoiced Validation Name')])), self.choices)

    def test_get_value(self):
        self.assertEqual(self.choices.get_value(1), 'New content')

    def test_rules_transaction_return_ok(self):
        self.assertEqual(self.choices.validate(self.choices.NEW, self.choices.WAIT), 2)

    def test_rules_transaction_return_false(self):
        self.assertEqual(self.choices.validate(self.choices.INVOICED, self.choices.WAIT), False)


class MyChoicesSingle(Choices):
    NEW = 1
    WAIT = 2
    CANCELED = -1
    ERROR = -2
    INVOICED = 3

    # set transaction rules
    NEW_RULES = [WAIT, INVOICED, CANCELED, ERROR]
    WAIT_RULES = [CANCELED, ERROR, INVOICED]
    INVOICED_RULES = [CANCELED]


class TestChoicesSingle(TestCase):

    def setUp(self):
        self.choices = MyChoicesSingle

    def test_key_value(self):
        self.assertEqual(self.choices.NEW, 1)
        self.assertEqual(self.choices.WAIT, 2)
        self.assertEqual(self.choices.CANCELED, -1)
        self.assertEqual(self.choices.ERROR, -2)
        self.assertEqual(self.choices.INVOICED, 3)

    def test_len_choices(self):
        self.assertEqual(len(self.choices), 5)

    def test_iter_list(self):
        self.assertEquals(sorted(list(self.choices)), sorted([(-1, 'CANCELED'), (-2, 'ERROR'),
                          (3, 'INVOICED'), (1, 'NEW'), (2, 'WAIT')]), self.choices)

    def test_repr_choice(self):
        self.assertEqual(str(sorted(self.choices)),
                         str(sorted([(-1, 'CANCELED'), (-2, 'ERROR'),
                          (3, 'INVOICED'), (1, 'NEW'), (2, 'WAIT')])), self.choices)

    def test_get_value(self):
        self.assertEqual(self.choices.get_value(1), 'NEW')

    def test_rules_transaction_return_ok(self):
        self.assertEqual(self.choices.validate(self.choices.NEW, self.choices.WAIT), 2)

    def test_rules_transaction_return_false(self):
        self.assertEqual(self.choices.validate(self.choices.INVOICED, self.choices.WAIT), False)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django_choices_flow.models_test import MyIntegerInvoide, IntegerChoices, \
    CharChoices, MyCharInvoide
from django.core import exceptions


class FlowIntegerFieldTest(TestCase):

    def test_create_invoice(self):
        invoice = MyIntegerInvoide()
        invoice.number = 1234
        invoice.full_clean()
        invoice.save()

        self.assertTrue(MyIntegerInvoide.objects.count())

    def test_status_invoice(self):
        invoice = MyIntegerInvoide()
        invoice.number = 1234
        invoice.full_clean()
        invoice.save()

        self.assertEqual(invoice.status, 1)

    def test_flow_control(self):
        invoice = MyIntegerInvoide()
        invoice.number = 1234
        invoice.full_clean()
        invoice.save()

        self.assertEqual(invoice.status, IntegerChoices.NEW)

        invoice.status = IntegerChoices.INVOICED

        # Raise ValidationError when validate status
        self.assertRaises(exceptions.ValidationError, lambda: invoice.full_clean())


class FlowCharFieldTest(TestCase):

    def test_create_invoice(self):
        invoice = MyCharInvoide()
        invoice.number = 1234
        invoice.full_clean()
        invoice.save()

        self.assertTrue(MyCharInvoide.objects.count())

    def test_status_invoice(self):
        invoice = MyCharInvoide()
        invoice.number = 1234
        invoice.full_clean()
        invoice.save()

        self.assertEqual(invoice.status, 'NW')

    def test_flow_control(self):
        invoice = MyCharInvoide()
        invoice.number = 1234
        invoice.full_clean()
        invoice.save()

        self.assertEqual(invoice.status, CharChoices.NEW)

        invoice.status = CharChoices.INVOICED

        # Raise ValidationError when validate status
        self.assertRaises(exceptions.ValidationError, lambda: invoice.full_clean())

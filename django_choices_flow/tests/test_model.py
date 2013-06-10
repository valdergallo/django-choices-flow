#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django_choices_flow.models_test import MyModelInvoide, MyChoices
from django.core import exceptions


class ModelChoiceFlowTest(TestCase):

    def test_create_invoice(self):
        invoice = MyModelInvoide()
        # invoice.status = MyChoices.WAIT
        invoice.number = 1234
        invoice.full_clean()
        invoice.save()

        self.assertTrue(MyModelInvoide.objects.count())

    def test_flow_control(self):
        invoice = MyModelInvoide()
        invoice.number = 1234
        invoice.full_clean()
        invoice.save()

        self.assertEqual(invoice.status, MyChoices.NEW)

        invoice.status = MyChoices.INVOICED
        invoice.full_clean()
        invoice.save()

        self.assertEqual(invoice.status, MyChoices.INVOICED)

        invoice.status = MyChoices.WAIT

        with self.assertRaises(exceptions.ValidationError):
            invoice.full_clean()
            invoice.save()

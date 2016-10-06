# -*- coding: utf-8 -*-

from django.forms import ModelForm
from example.models import (MyIntegerInvoide, MyCharInvoide,
                             IntegerChoices, CharChoices,
                             CustomerErrorMsgChoices,
                             CustomerErrorMsgInvoide)
from django.test import TestCase


class IntegerFormModel(ModelForm):
    class Meta:
        model = MyIntegerInvoide


class CharFormModel(ModelForm):
    class Meta:
        model = MyCharInvoide


class CustomerErrorMsgChoicesFormModel(ModelForm):
    class Meta:
        model = CustomerErrorMsgInvoide


class IntegerFormModelTest(TestCase):

    def create_new_test(self):
        data = {'number': 1234, 'status': 1}
        invoice = IntegerFormModel(data)
        self.assertTrue(invoice.is_valid(), invoice.errors)
        invoice.save()

        self.assertEqual(MyIntegerInvoide.objects.all().count(), 1)

    def test_number_error(self):
        data = {'status': 1}
        invoice = IntegerFormModel(data)
        self.assertFalse(invoice.is_valid(), invoice.errors)
        self.assertEqual(invoice.errors, {'number': [u'This field is required.']}, invoice.errors)

    def test_status_error(self):
        data = {'number': 2}
        invoice = IntegerFormModel(data)
        self.assertFalse(invoice.is_valid(), invoice.errors)
        self.assertEqual(invoice.errors, {'status': [u'This field is required.']}, invoice.errors)

    def test_invalid_flow(self):
        invoice_instance = MyIntegerInvoide.objects.create(number=1234)
        data = {'status': IntegerChoices.INVOICED, 'number': 1234}

        invoice = IntegerFormModel(data, instance=invoice_instance)

        self.assertFalse(invoice.is_valid())
        self.assertEqual(invoice.errors, {'status': [u'Invalid choice: Invoiced']}, invoice.errors)

    def test_valid_flow(self):
        invoice_instance = MyIntegerInvoide.objects.create(number=1234)
        data = {'status': IntegerChoices.WAIT, 'number': 1234}

        invoice = IntegerFormModel(data, instance=invoice_instance)

        self.assertTrue(invoice.is_valid())


class CharFormModelTest(TestCase):

    def create_new_test(self):
        data = {'number': 1234, 'status': 'NW'}
        invoice = CharFormModel(data)
        self.assertTrue(invoice.is_valid(), invoice.errors)
        invoice.save()

        self.assertEqual(MyCharInvoide.objects.all().count(), 1)

    def test_number_error(self):
        data = {'status': 'NW'}
        invoice = CharFormModel(data)
        self.assertFalse(invoice.is_valid(), invoice.errors)
        self.assertEqual(invoice.errors, {'number': [u'This field is required.']}, invoice.errors)

    def test_status_error(self):
        data = {'number': 2}
        invoice = CharFormModel(data)
        self.assertFalse(invoice.is_valid(), invoice.errors)
        self.assertEqual(invoice.errors, {'status': [u'This field is required.']}, invoice.errors)

    def test_invalid_flow(self):
        invoice_instance = MyCharInvoide.objects.create(number=1234)
        data = {'status': CharChoices.INVOICED, 'number': 1234}

        invoice = CharFormModel(data, instance=invoice_instance)

        self.assertFalse(invoice.is_valid())
        self.assertEqual(invoice.errors, {'status': [u'Invalid choice: Invoiced']}, invoice.errors)

    def test_valid_flow(self):
        invoice_instance = MyCharInvoide.objects.create(number=1234)
        data = {'status': CharChoices.WAIT, 'number': 1234}

        invoice = CharFormModel(data, instance=invoice_instance)

        self.assertTrue(invoice.is_valid())


class CustomErrorMsgTest(TestCase):

    def test_invalid_flow(self):
        invoice_instance = CustomerErrorMsgInvoide.objects.create(number=1234)
        data = {'status': CustomerErrorMsgChoices.INVOICED, 'number': 1234}

        invoice = CustomerErrorMsgChoicesFormModel(data, instance=invoice_instance)

        self.assertFalse(invoice.is_valid())
        self.assertEqual(invoice.errors, {'status': [u'My Custom Error Message: Invoiced']}, invoice.errors)


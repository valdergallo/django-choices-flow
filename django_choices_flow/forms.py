#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core import exceptions


class FlowCharField(forms.CharField):

    @staticmethod
    def get_db_value(model_instance):
        if model_instance.id:
            return model_instance.__class__.objects.get(id=model_instance.id)

    def validate(self, value, model_instance):
        # validate choice flow
        if model_instance.id:
            db_value = self.get_db_value(model_instance)
            if not self.choices.validate(getattr(db_value, self.name), value):
                raise exceptions.ValidationError(_('%s is a invalid choice in this flow' % value))

        super(FlowIntegerField, self).validate(value, model_instance)


class FlowIntegerField(forms.IntegerField):

    @staticmethod
    def get_db_value(model_instance):
        if model_instance.id:
            return model_instance.__class__.objects.get(id=model_instance.id)

    def validate(self, value, model_instance):
        # validate choice flow
        if model_instance.id:
            db_value = self.get_db_value(model_instance)
            if not self.choices.validate(getattr(db_value, self.name), value):
                raise exceptions.ValidationError(_('%s is a invalid choice in this flow' % value))

        super(FlowIntegerField, self).validate(value, model_instance)

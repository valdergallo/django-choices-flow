#!/usr/bin/env python
# -*- coding: utf-8 -*-

#/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core import exceptions


class FlowCharField(forms.CharField):

    def validate(self, value, model_instance):
        """
        Validates value and throws ValidationError. Subclasses should override
        this to provide validation logic.
        """
        super(FlowCharField, self).validate(value, model_instance)
        # validate choice flow
        if self.choices.validate(getattr(model_instance, self.name), value):
            return
        else:
            raise exceptions.ValidationError(_('%s Invalid Choice Flow' % value))


class FlowIntegerField(forms.IntegerField):

    def validate(self, value, model_instance):
        """
        Validates value and throws ValidationError. Subclasses should override
        this to provide validation logic.
        """
        super(FlowIntegerField, self).validate(value, model_instance)
        # validate choice flow
        if self.choices.validate(getattr(model_instance, self.name), value):
            return
        else:
            raise exceptions.ValidationError(_('%s Invalid Choice Flow' % value))

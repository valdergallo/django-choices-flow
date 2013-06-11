#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from django.core import exceptions
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FlowCharField(models.CharField):

    def __init__(self, *args, **kwargs):
        super(FlowCharField, self).__init__(*args, **kwargs)
        if not self.max_length:
            self.max_length = max([i[0] for i in self.choices])

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


class FlowIntegerField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        super(FlowIntegerField, self).__init__(*args, **kwargs)

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

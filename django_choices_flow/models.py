#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.core import exceptions
from django.utils.translation import ugettext_lazy as _


class FlowCharField(models.CharField):

    def __init__(self, *args, **kwargs):
        super(FlowCharField, self).__init__(*args, **kwargs)
        self.db_index = True
        if not self.max_length:
            self.max_length = max([i[0] for i in self.choices])

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


class FlowIntegerField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        super(FlowIntegerField, self).__init__(*args, **kwargs)
        self.db_index = True

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

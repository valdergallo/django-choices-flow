#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core import exceptions
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FlowCharField(models.CharField):
    "Custom CharField with workflow validation"

    @staticmethod
    def get_db_value(model_instance):
        "Get database value"
        if model_instance.id:
            return model_instance.__class__.objects.get(id=model_instance.id)

    def validate(self, value, model_instance):
        "Validate choice workflow"
        if model_instance.id:
            db_value = self.get_db_value(model_instance)
            if not self.choices.validate(getattr(db_value, self.name), value):
                raise exceptions.ValidationError(_('%s %s' % (self.choices.error_msg,
                                                 self.choices.get_value(value))))

        super(FlowCharField, self).validate(value, model_instance)


class FlowIntegerField(models.IntegerField):
    "Custom IntegerField with workflow validation"

    @staticmethod
    def get_db_value(model_instance):
        "Get database value"
        if model_instance.id:
            return model_instance.__class__.objects.get(id=model_instance.id)

    def validate(self, value, model_instance):
        "Validate choice workflow"
        if model_instance.id:
            db_value = self.get_db_value(model_instance)
            if not self.choices.validate(getattr(db_value, self.name), value):
                raise exceptions.ValidationError(_('%s %s' % (self.choices.error_msg,
                                                 self.choices.get_value(value))))

        super(FlowIntegerField, self).validate(value, model_instance)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^django_choices_flow\.models\.(FlowCharField|FlowIntegerField)"])
except ImportError:
    pass

#/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def flow_validator(to_value):
    import ipdb; ipdb.set_trace()
    if not self.choices.validate(to_value):
        raise ValidationError(u'%s Invalid Choice' % to_value)


class ChoicesFlowField(forms.Field):
    default_error_messages = {
        'invalid_flow': _(u'Invalid Choice'),
    }

    def validate(self, value):
        if not self.choices.validate(self.status, value):
            raise ValidationError(self.error_messages['invalid_flow'])

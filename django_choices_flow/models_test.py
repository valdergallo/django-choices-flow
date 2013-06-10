#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django_choices_flow import Choices
from django_choices_flow.models import FlowIntegerField


class MyChoices(Choices):
    NEW = 1, 'New content'  # 'New content' is the display text
    WAIT = 2, 'Wait'
    CANCELED = -1, 'Canceled'
    ERROR = -2, 'Error'
    INVOICED = 3, 'Invoiced'

    # set transaction rules
    NEW_RULES = [WAIT, INVOICED, CANCELED, ERROR]
    WAIT_RULES = [CANCELED, ERROR, INVOICED]
    INVOICED_RULES = [CANCELED]


class MyModelInvoide(models.Model):
    status = FlowIntegerField(choices=MyChoices, default=MyChoices.NEW)
    number = models.IntegerField()

    def __unicode__(self):
        return self.number

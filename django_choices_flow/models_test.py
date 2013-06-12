#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django_choices_flow import Choices
from django_choices_flow.models import FlowIntegerField, FlowCharField


class IntegerChoices(Choices):
    NEW = 1, 'New content'  # 'New content' is the display text
    WAIT = 2, 'Wait'
    CANCELED = -1, 'Canceled'
    ERROR = -2, 'Error'
    INVOICED = 3, 'Invoiced'

    # set transaction rules
    NEW_RULES = [WAIT, CANCELED, ERROR]
    WAIT_RULES = [CANCELED, ERROR, INVOICED]
    INVOICED_RULES = [CANCELED]


class MyIntegerInvoide(models.Model):
    status = FlowIntegerField(choices=IntegerChoices, default=IntegerChoices.NEW, db_index=True)
    number = models.IntegerField()


class CharChoices(Choices):
    NEW = 'NW', 'New'
    WAIT = 'WT', 'Wait'
    CANCELED = 'CA', 'Canceled'
    ERROR = 'ER', 'Error'
    INVOICED = 'IV', 'Invoiced'

    #set rules
    NEW_RULES = [WAIT, CANCELED, ERROR]


class MyCharInvoide(models.Model):
    status = FlowCharField(choices=CharChoices,
                           default=CharChoices.NEW,
                           max_length=2, db_index=True)
    number = models.IntegerField()

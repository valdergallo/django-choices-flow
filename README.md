django-choices-flow
==================

Meta Choice with simple flow and rules

[![Build Status](https://travis-ci.org/valdergallo/django-choice-flow.png?branch=master)](https://travis-ci.org/valdergallo/django-choice-flow)

## Usage


```python
from django.db import models
from django_choices_flow import Choices
from django_choices_flow.models import FlowIntegerField


class MyChoices(Choices):
    NEW = 1, 'New content' # 'New content' is the display text
    WAIT = 2, 'Wait'
    CANCELED = -1, 'Canceled'
    ERROR = -2, 'Error'
    INVOICED = 3, 'Invoiced'

    # set transaction rules
    NEW_RULES = [NEW, INVOICED, CANCELED, ERROR]
    WAIT_RULES = [CANCELED, ERROR, INVOICED]
    INVOICED_RULES = [CANCELED]


class Invoces(models.Model):
	"""
	To use only choices
	"""
    number = models.IntegerField()
    status = models.IntegerField(choices=MyChoices, default=MyChoices.NEW)

    def __unicode__(self):
        return self.number


class FlowInvoice(models.Model):
	"""
	To validate flow in choices
	"""

	number = models.IntegerField()
	status = FlowIntegerField(choices=MyChoices, default=MyChoices.NEW)

	def __unicode__(self):
        return self.number
```

### Shell

```python
>>> flow = FlowInvoice.objects.create(number=1234)
>>> flow.status
1
>>> flow.status = MyChoices.INVOICED
>>> flow.full_clean()
>>> flow.save()
>>> flow.status
3
>>> flow.status = MyChoices.WAIT
>>> flow.full_clean()
ValidationError: {'status': [u'2 is a invalid choice in this flow']}
```

## Developer

```bash
# download code
git clone git@github.com:valdergallo/django-choice-flow.git

# install developer packages
make

# test project
make test
```


------------------------
> **License type:** FREEBSD

> **Coverage:** 82%

> **Version:** 0.6.0

> Tested in Django: 1.2.7; 1.3.7; 1.4.5; 1.5.1

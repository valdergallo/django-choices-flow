.. _usage:

Usage
======


Model example
--------------

.. code-block:: python
    :linenos:

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

Set Error Message
-----------------

**CHANGE ALL MESSAGE**

To change error message for all ChoiceFlow set nem messagem on **Django.settings**

.. code-block:: python
    :linenos:
    DJANGO_CHOICES_FLOW_ERROR_MESSAGE = "My custom message error for all choices flow"


**CHANGE ONLY ONE MESSAGE**

To change error message only in one ChoiceFlow, set **error_msg** on ChoicesFlow

.. code-block:: python
    :linenos:

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

        error_msg = "My Custom Error Message for this ChoicesFlow"


Shell example
-------------

.. code-block:: bash
    :linenos:

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
    ValidationError: {'status': [u'Invalid choice: Wait']}

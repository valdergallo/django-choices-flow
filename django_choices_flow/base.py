# -*- coding: utf-8 -*-
try:
    from django.conf import settings
except ImportError:
    settings = None

if hasattr(settings, 'DJANGO_CHOICES_FLOW_ERROR_MESSAGE'):
    DEFAULT_DJANGO_CHOICES_FLOW_ERROR_MESSAGE = settings.DJANGO_CHOICES_FLOW_ERROR_MESSAGE
else:
    DEFAULT_DJANGO_CHOICES_FLOW_ERROR_MESSAGE = 'Invalid choice:'


class MetaChoice(type):
    """
        - Convert attributes to Tuples
        - Add interator in class attributes
    """
    def __init__(cls, *args, **kwargs):
        cls._rules = {}
        cls._data = []
        cls.__validate_msg = DEFAULT_DJANGO_CHOICES_FLOW_ERROR_MESSAGE

        items = cls.__dict__.items()
        for name, value in items:
            cls._set_data(name, value)
        cls._hash = dict(cls._data)

    def _set_data(cls, name, value, parent_name=None):
        "Update tuplas to objects"
        if not name.startswith('_') and not callable(value):
            if isinstance(value, tuple) and len(value) > 1:
                data = value
            else:
                data = (value, name)

            if isinstance(value, list) and '_RULES' in name.upper():
                cls._set_rules(name, value)
            else:
                cls._data.append(data)
                if isinstance(data[0], tuple):
                    setattr(cls, name, dict(data))
                else:
                    setattr(cls, name, data[0])

    def _set_rules(cls, name, value):
        "If attribute has _RULES add validations rules"
        updated_name = name.split('_')[0]
        value_key = getattr(cls, updated_name)

        if isinstance(value_key, tuple):
            value_key = value_key[0]

        values = [isinstance(i, tuple) and i[0] or i for i in value]
        cls._rules.update({value_key: values})

    def __iter__(cls, *args, **kwds):
        for value, data in cls._data:
            yield (value, data)

    def __len__(cls, *args, **kwds):
        return len(cls._data)

    def __repr__(cls, *args, **kargs):
        return str(list(cls._data))

    @property
    def error_msg(cls):
        "get default error message"
        return cls.__validate_msg

    @error_msg.setter
    def error_msg(cls, value):
        "set default error message for instance"
        cls.__validate_msg = value

    def get_value(cls, key):
        return cls._hash.get(key)

    def validate(cls, status, new_status):
        " Validate workflow "
        if not status:
            return new_status

        if repr(status) == repr(new_status):
            return new_status

        if not cls._rules.get(status) or \
            new_status not in cls._rules.get(status):
            return False

        return new_status

#: Set metaclass in Python 2.x and 3.x
Choices = MetaChoice('Choices', (object, ), {})

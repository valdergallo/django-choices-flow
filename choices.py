#/usr/bin/python
# -*- coding: utf-8 -*-


class MetaChoice(type):
    def __init__(cls, *args, **kwargs):
        cls._rules = {}
        cls._data = []

        for name, value in cls.__dict__.items():
            if not name.startswith('_') and not callable(value):
                if isinstance(value, tuple) and len(value) > 1:
                    data = value
                else:
                    data = (value, name)

                if isinstance(value, list) and '_RULES' in name.upper():
                    updated_name = name.split('_')[0]
                    value_key = getattr(cls, updated_name)

                    if isinstance(value_key, tuple):
                        value_key = value_key[0]

                    values = [isinstance(i, tuple) and i[0] or i for i in value]
                    cls._rules.update({value_key: values})

                else:
                    cls._data.append(data)
                    setattr(cls, name, data[0])

        cls._hash = dict(cls._data)


class Choices(object):
    """
    Usage:

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

    """
    __metaclass__ = MetaChoice

    def __iter__(self):
        for value, data in self._data:
            yield (value, data)

    def __repr__(self):
        return str(list(self._data))

    def __len__(self):
        return len(self._data)

    def get_value(self, key):
        return self._hash.get(key)

    def validate(self, status, new_status):
        if not self._rules.get(status) or new_status not in self._rules.get(status):
            return False
        return new_status

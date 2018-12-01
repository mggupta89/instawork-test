'''
Just having only one custom exception to keep the assignment short
We can obviously have multiple exceptions
'''
from builtins import Exception


class InstaworkException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
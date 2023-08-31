"""
Developer made a mistake in code below
Make the 'message' an abstract property in BaseValidator
Implement 'message' in MaxValueValidator
Run the code to see if it works
"""

from abc import ABC, abstractmethod


class BaseValidator:
    code = "limit_value"

    def __init__(self, limit_value, message=None):
        self.limit_value = limit_value
        if message:
            self.message = message

    def __call__(self, value):
        cleaned = self.clean(value)
        limit_value = (
            self.limit_value() if callable(self.limit_value) else self.limit_value
        )
        params = {"limit_value": limit_value, "show_value": cleaned, "value": value}
        if self.compare(cleaned, limit_value):
            raise ValueError(self.message)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (
            self.limit_value == other.limit_value
            and self.message == other.message
            and self.code == other.code
        )

    def compare(self, a, b):
        return a is not b

    def clean(self, x):
        return x


class MaxValueValidator(BaseValidator):
    code = "max_value"

    def compare(self, a, b):
        return a > b


max_value_validator = MaxValueValidator(limit_value=10)
max_value_validator(value=11)

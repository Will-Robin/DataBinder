"""
A structure containing condition information.
"""


class Condition:
    def __init__(self, iden, value, unit):
        """
        Attributes
        ----------
        """

        self.id = iden
        self.value = value
        self.unit = unit


class ConditionValue(Condition):
    """
    Stores a single condition value.
    """


class ConditionArray(Condition):
    """
    Stores a condition as an array.
    """

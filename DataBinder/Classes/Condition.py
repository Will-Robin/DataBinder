class Condition:
    """
    A structure containing condition information.
    """

    def __init__(self, iden, value, unit):
        """
        Attributes
        ----------
        id: str
        value: float|list
        unit: str
        """

        self.id = iden
        self.value = value
        self.unit = unit


class ConditionValue(Condition):
    """
    A variant of a Condition when the value attribute is a single float.
    """


class ConditionArray(Condition):
    """
    A variant of a Condition when the value attribute is a list of floats.
    """

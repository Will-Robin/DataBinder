class Condition:
    """
    A structure containing condition information.
    """

    def __init__(self, iden: str, unit: str):
        """
        Attributes
        ----------
        id: str
        unit: str
        """

        self.id = iden
        self.unit = unit


class ConditionValue(Condition):
    """
    A variant of a Condition when the value attribute is a single float.
    """

    def __init__(self, iden: str, value: float, unit: str):
        """
        Attributes
        ----------
        id: str
        value: float
        unit: str
        """
        super().__init__(iden, unit)

        self.value = value


class ConditionArray(Condition):
    """
    A variant of a Condition when the value attribute is a list of floats.
    """

    def __init__(self, iden: str, value: list, unit: str):
        """
        Attributes
        ----------
        id: str
        value: list
        unit: str
        """
        super().__init__(iden, unit)

        self.value = value
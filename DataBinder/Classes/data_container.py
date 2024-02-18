"""
A structure containing data.
"""

from .conditions import ConditionValue, ConditionArray


class DataContainer:
    """
    An structure for storing experimental data and
    conditions.
    """

    def __init__(self):
        """
        Create an empty DataContainer.

        Attributes
        ----------
        filename: str
        experiment_code: str
        value_conditions: list[DataBinder.Classes.ConditionValue]
        array_conditions: list[DataBinder.Classes.ConditionArray]
        analysis_details: dict()
        series_values: numpy.ndarray
        series_unit: str
        data: dict()
        errors: dict()
        """

        self.filename: str = "not specified"
        self.experiment_code: str = "not specified"
        self.value_conditions: list[ConditionValue] = []
        self.array_conditions: list[ConditionArray] = []
        self.series_values: list = []
        self.series_unit: str = "not specified"
        self.data: dict = {}
        self.errors: dict = {}

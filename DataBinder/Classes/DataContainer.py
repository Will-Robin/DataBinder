class DataContainer:
    """
    An structure for storing experimental data.
    """

    def __init__(self):
        """
        Create an empty DataContainer.

        Attributes
        ----------
        filename: str
        experiment_code: str
        conditions: list[DataBinder.Classes.Condition]
        analysis_details: dict()
        series_values: numpy.ndarray
        series_unit: str
        data: dict()
        errors: dict()
        """

        self.filename = "not specified"
        self.experiment_code = "not specified"
        self.conditions = []
        self.series_values = []
        self.series_unit = "not specified"
        self.data = dict()
        self.errors = dict()

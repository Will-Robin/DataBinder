from DataBinder.Classes import DataContainer
from DataBinder.Inspectors import patterns
from DataBinder.Classes import ConditionValue
from DataBinder.Classes import ConditionArray
from .module import process_lines
from .module import parse_element


def data_container_from_string(text: str) -> DataContainer:
    """
    Create a DataContainer from a string.

    Expected structure example:

    ```
    Dataset,example
    start_conditions
    reactor_volume/ μL,411
    O=C(CO)CO/ M,2
    [OH-]/ M,0.12
    O/ M,55.5
    flow_profile_time/ s,0,1,2,3,800,1000,1200,1400,1600,1800
    O=C(CO)CO_flow_rate/ µl/h,9308.25,9308.25,9308.25,9308.25
    end_conditions
    start_data
    time/ s,compound_1/ M,compound_2/ M,compound_3/ M
    0,0.0002,0.0003,0.0007
    end_data
    ```

    Parameters
    ----------
    text: str

    Returns
    -------
    data_container: DataBinder.Classes.DataContainer
        DataContainer constructed from the file.
    """

    # Extract out data blocks
    exp_code_text = patterns.exp_code_pattern.findall(text)
    conditions_text = patterns.conditions_pattern.findall(text)
    data_text = patterns.data_pattern.findall(text)
    error_text = patterns.error_pattern.findall(text)

    # Process the data blocks
    exp_code = exp_code_text[0]

    # Parse conditions
    array_conditions = []
    value_conditions = []
    for block in conditions_text:
        condition_lines = process_lines(block)
        for element in condition_lines:
            iden, value, unit = parse_element(element)

            if len(element) > 2:
                array_conditions.append(ConditionArray(iden, value, unit))
            else:
                value_conditions.append(ConditionValue(iden, value[0], unit))

    # Parse data
    series_data: dict = {}
    data: dict = {}
    for block in data_text:
        data_lines = process_lines(block)
        transpose_lines = [list(i) for i in zip(*data_lines)]

        series_data[transpose_lines[0][0]] = transpose_lines[0][1:]

        for element in transpose_lines[1:]:
            data[element[0]] = element[1:]

    # Parse data errors
    errors: dict = {}
    for block in error_text:
        error_lines = process_lines(block)
        transpose_lines = [list(i) for i in zip(*error_lines)]
        for element in transpose_lines[1:]:
            errors[element[0]] = element[1:]

    # Get the series unit
    if len(series_data) == 0:
        ser_unit = ""
        series_values = []
    else:
        ser_unit = list(series_data)[0]
        series_values = series_data[ser_unit]

    # Initialise DataContainer
    data_container = DataContainer()

    data_container.filename = ""
    data_container.experiment_code = exp_code
    data_container.value_conditions = value_conditions
    data_container.array_conditions = array_conditions
    data_container.series_values = series_values
    data_container.series_unit = ser_unit
    data_container.data = data
    data_container.errors = errors

    return data_container

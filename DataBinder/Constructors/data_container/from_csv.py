from pathlib import Path
from DataBinder.Classes import DataContainer
from .module import from_string


def data_container_from_csv(filename: str) -> DataContainer:
    """
    Load a DataContainer from a structured .csv file.

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
    filename: str
        Name of the file containing the data.

    Returns
    -------
    data_container: DataBinder.Classes.DataContainer
        DataContainer constructed from the file.
    """

    # Read in file as text
    text = Path(filename).read_text()

    data_container = from_string(text)

    data_container.filename = filename

    return data_container

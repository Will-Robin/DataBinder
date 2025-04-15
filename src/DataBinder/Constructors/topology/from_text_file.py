from pathlib import Path
from DataBinder.Classes import Topology
from .from_string import topology_from_string


def topology_from_text_file(filename: str) -> Topology:
    """
    Load a Topology structure from a file containing transformations.

    Example expected format:

    ```
    A.B>>C
    C.D>>E.F
    ```

    Parameters
    ----------
    filename: str
        Name of the file containing the data

    Returns
    -------
    topology: Classes.Topology
        Created topology structure.
    """

    # Load file contents as text
    text = Path(filename).read_text()

    topology = topology_from_string(text)

    return topology

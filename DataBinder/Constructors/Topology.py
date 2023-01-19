"""
For loading Topology structures from files and strings.
"""
from pathlib import Path

from DataBinder.Classes import Entity
from DataBinder.Classes import Topology
from DataBinder.Classes import Transformation
from .Transformation import from_string as transformation_from_string


def from_string(text: str) -> Topology:
    """
    Create a topology from a string of transformation tokens separatad by
    newlines.

    Parameters
    ----------
    text: str

    Returns
    -------
    topology: Classes.Topology
        Created topology structure.
    """

    transform_strings = [x for x in text.split("\n") if x != ""]

    topology = Topology()
    for transf in transform_strings:
        sides = transf.split(">>")
        LHS = sides[0]
        RHS = sides[1]

        inputs = LHS.split(".")
        outputs = RHS.split(".")

        [topology.add_entity(Entity(i)) for i in inputs]
        [topology.add_entity(Entity(o)) for o in outputs]

        transform: Transformation = transformation_from_string(transf)

        topology.add_transformation(transform)

    return topology


def from_text(filename: str) -> Topology:
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

    topology = from_string(text)

    return topology

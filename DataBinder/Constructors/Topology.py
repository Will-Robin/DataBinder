from DataBinder.Classes import Topology
from DataBinder.Classes import Entity
from DataBinder.Classes import Transformation


def from_text(filename):
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
    with open(filename, "r") as file:
        text = file.read()

    transform_strings = [x for x in text.split("\n") if x != ""]

    topology = Topology()
    for transform in transform_strings:
        sides = transform.split(">>")
        LHS = sides[0]
        RHS = sides[1]

        inputs = LHS.split(".")
        outputs = RHS.split(".")

        [topology.add_entity(Entity(i)) for i in inputs]
        [topology.add_entity(Entity(o)) for o in outputs]

        transform = Transformation(transform)
        transform.requires = inputs
        transform.creates = outputs

        topology.add_transformation(transform)

    return topology

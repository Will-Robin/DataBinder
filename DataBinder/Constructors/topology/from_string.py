from DataBinder.Classes import Topology
from .from_list import topology_from_list


def topology_from_string(text: str) -> Topology:
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

    topology = topology_from_list(transform_strings)

    return topology

from DataBinder.Classes import Entity
from DataBinder.Classes import Topology
from DataBinder.Classes import Transformation
from ..transformation.from_string import transformation_from_string


def topology_from_list(terms: list[str]) -> Topology:
    """
    Create a topology from a string of transformation tokens separatad by
    newlines.

    Parameters
    ----------
    terms: list[str]

    Returns
    -------
    topology: Classes.Topology
        Created topology structure.
    """

    topology = Topology()
    for transf in terms:
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

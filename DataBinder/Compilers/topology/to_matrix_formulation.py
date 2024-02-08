from DataBinder.Classes import Topology


def topology_to_matrix_formulation(
    topology: Topology,
) -> tuple[list[list[str]], list[str]]:
    """
    Create a matrix representation of a chemical reaction network.

    Parameters
    ----------
    topology: Topology

    Returns
    -------
    rate_constants, species
    """

    entities = topology.entities
    transformations = topology.transformations
    entity_tokens = [e for e in entities]
    complexes = {
        ".".join(transformations[t].requires): f"k[{c}]"
        for c, t in enumerate(transformations)
    }

    forward_processes = [[] * complexes] * len(complexes)

    backwards_processes = []

    forwards_processes + backwards_processes

    [-kforward][complexes] + [kbackwards][complexes]

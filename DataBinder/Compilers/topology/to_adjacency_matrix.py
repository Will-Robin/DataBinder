"""
Convert a topology to an adjacency matrix.
"""
from DataBinder.Classes import Topology


def topology_to_adjacency_matrix(topology: Topology) -> list[list[int]]:
    """
    Create an adjacency matrix from a topology.

    Prototype: transformations are edges, a '1' indicates an edge between two
    entities. This does not cover phenonmena such as bimolecular reactions (the
    presence of an edge is dependent on the presence of another entity).

    - A value of 1 in A_ij_ means an edge from i to j

    Parameters
    ----------
    topology: DataBinder.Classes.Topology
        Topology to be converted.

    Returns
    -------
    adjacency_matrix: list[list]
        Adjacency matrix.
    """

    combined_entities = topology.entities | topology.constants
    combined_transformations = (
        topology.transformations | topology.inputs | topology.outputs
    )

    adjacency_matrix = [[0 for x in combined_entities] for x in combined_entities]

    entity_indices = {iden: c for c, iden in enumerate(combined_entities)}

    for entity in combined_entities:
        idx_1 = entity_indices[entity]

        # Trace forwards (1 in A_ij_ means an edge from i to j)
        for transform in combined_entities[entity].required_by:
            for creation in combined_transformations[transform].creates:
                idx_2 = entity_indices[creation]
                adjacency_matrix[idx_1][idx_2] = 1

    return adjacency_matrix

"""
Convert a topology to an stoichiometric matrix.
"""

from DataBinder.Classes import Topology


def topology_to_stoichiometric_matrix(topology: Topology) -> list[list[int]]:
    """
    Create an stoichiometric matrix from a topology.

    Parameters
    ----------
    topology: DataBinder.Classes.Topology
        Topology to be converted.

    Returns
    -------
    stoichiometric_matrix: list[list]
        Adjacency matrix.
    """

    combined_entities = topology.entities | topology.constants
    combined_transformations = (
        topology.transformations | topology.inputs | topology.outputs
    )

    stoichiometric_matrix = [
        [0 for x in combined_transformations] for x in combined_entities
    ]

    entity_indices = {iden: c for c, iden in enumerate(combined_entities)}

    for col_idx, id in enumerate(combined_transformations):
        transform = combined_transformations[id]
        for entity in transform.requires:
            row_idx = entity_indices[entity]
            stoichiometric_matrix[row_idx][col_idx] -= 1
        for entity in transform.creates:
            row_idx = entity_indices[entity]
            stoichiometric_matrix[row_idx][col_idx] += 1

    return stoichiometric_matrix

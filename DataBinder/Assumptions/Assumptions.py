from DataBinder.Classes import Topology


def pre_equilibrium(topology: Topology, transformation: str) -> Topology:
    """
    Applies a pre-equilibrium approximation to a transformation.

    - The transformation and the entities involved are removed.
    - New transformations bridging the 'dangling' transformations are created
      and added to the topology. They contain new tokens corresponding to
      the combination of the removed entities.

    A ← B ←→ C → D
    E → B
    F → C

    After pre-equilibrium approximation:

    B and C turn into Z, portions of which react to form D, and other portions
    react to form A.

    E and F both produce Z

    Z = B + C
    Z * constant → A
    Z * 1/constant → D
    E → Z
    F → Z

    >> Replacements with a additional constants. <<

    Bimolecular reactions?

    A + B → C + D

    K = A*B/C*D

    A = K*C*D/B = K*(C*D/B)
    B = K*C*D/A = K*(C*D/A)
    C = A*B/K*D = 1/K*(A*B/D)
    D = A*B/K*C = 1/K*(A*B/C)

    Z = A + B + C + D

    What about when entities are involved in multiple pre-equilibria?

    Parameters
    ----------
    topology: DataBinder.Classes.Topology
    transformation: str
        Token for transformation to apply assumption to.

    Returns
    -------
    topology: DataBinder.Classes.Topology
        Modified topology.
    """
    # TODO
    return topology


def pseudo_first_order(topology: Topology, entity: str):
    """
    Apply a pseudo first-order approximation for all transformations in a
    topology containing the entity specified by the entity token.

    All constants involving this entity are removed/become 0.0?

    - Find all transformation connected to the entity
    - Create new transformations without the entity present.
    - Delete the transformations containing the entity
    - Delete the entity
    - Add the newly created transformations (copies of deleted ones without the
      entity)

    (or some variation of the above)

    Parameters
    ----------
    topology: DataBinder.Classes.Topology
    entity: str
        Token for the entity to be removed by the approximation.

    Returns
    -------
    topology: DataBinder.Classes.Topology
        Modified topology.
    """
    # TODO
    return topology


def pseudo_first_order_targeted(topology, transformation, entity):
    """
    Apply a pseudo first-order approximation for specific transformation
    (specified by its token) in a topology containing the entity specified by
    the entity token.

    All constants involving this entity are removed/become 0.0?

    - Find all transformation connected to the entity
    - Create new transformations without the entity present.
    - Delete the transformations containing the entity
    - Delete the entity
    - Add the newly created transformations (copies of deleted ones without the
      entity)

    (or some variation of the above)

    Parameters
    ----------
    topology: DataBinder.Classes.Topology
    entity: str
        Token for the entity to be removed by the approximation.

    Returns
    -------
    topology: DataBinder.Classes.Topology
        Modified topology.
    """
    # TODO
    return topology

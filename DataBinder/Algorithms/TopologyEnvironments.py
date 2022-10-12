from DataBinder.Classes import Topology
from DataBinder.Inspectors import test_for


def generate_primes(num: int) -> list[int]:
    """
    Generate the first `num` prime numbers.

    From this stack overflow answer ('historic' version):
    https://stackoverflow.com/questions/1628949/to-find-first-n-prime-numbers-in-python
    date of access: 04/10/2022

    Parameters
    ----------
    num: int

    Returns
    -------
    primes: list[int]
    """

    primes = set([2])
    i, p = 2, 0
    while True:
        if test_for.is_prime(i, primes):
            p += 1
            if p == num:
                return list(primes)
        i += 1


def rank_list(a_list: list[int]) -> list[int]:
    """
    Rank a list including duplicates.

    Parameters
    ----------
    a_list: list[int]

    Returns
    -------
    ranking: list[int]
    """

    # get all individual values in order
    unique = []
    for x in a_list:
        if x not in unique:
            unique.append(x)

    ranking = [sorted(unique).index(l) + 1 for l in a_list]

    return ranking


def prime_ranking(ranking: list[int]) -> list[int]:
    """
    Map a ranking to prime numbers.

    Parameters
    ----------
    ranking: list[int]

    Returns
    -------
    prime_ranking: list[int]
    """

    unique_ranks = []

    for r in ranking:
        if r not in unique_ranks:
            unique_ranks.append(r)

    num = len(unique_ranks)

    prime_numbers = generate_primes(num)

    indices = [sorted(unique_ranks).index(l) for l in ranking]

    prime_ranking = [prime_numbers[i] for i in indices]

    return prime_ranking


def two_level_ranking(list_1: list[int], list_2: list[int]) -> list[int]:
    """
    Rank by list_1 then list_2.

    Parameters
    ----------
    list_1: list[int]
    list_2: list[int]

    Returns
    -------
    ranking: list[int]
    """

    new_list = [(x, y) for x, y in zip(list_1, list_2)]

    sorted_list = sorted(new_list, key=lambda x: (x[0], x[1]))

    single_level = [x[0] for x in sorted_list]

    ranking = [single_level.index(l) for l in list_1]

    return ranking


def assign_entity_environments(topology: Topology) -> dict[str, int]:
    """
    Assigning each Entity an environment based on the
    CANGEN algorithm.

    1. Create initial invariants for entities based on:
        a. Number of creating transformations
        b. Number of using transformations

    2. Transform the initial invariants into ranks
        (Rank according to sum of creating + using transformations)
        Note that two entities can have the same rank
        (-> actually, ranking can be left out for small numbers of invariants)

    3. Map each rank to a corresponding prime

    4. Create a new invariant where the primes of
       neighbors are multiplied.

       Neighbours are any entity attached to the same transformation.

    5. Determine new ranks based on
        a. old ranks
        b. new invariants

    6. Repeat from 2 with new ranks until ranking is stable

    If entities are symmetric, they should have the same rank

    Parameters
    ----------
    topology: DataBinder.Classes.Topology

    Returns
    -------
    labels: dict
    """

    # list of entities
    entities = [*topology.entities]

    initial_invariants = []
    # create initial invariants
    for e in entities:
        current_invariant = 0
        # used by
        for transform in topology.entities[e].used_by:
            current_invariant += len(topology.transformations[transform].requires) - 1
            current_invariant += len(topology.transformations[transform].creates)

        # created by
        for transform in topology.entities[e].created_by:
            current_invariant += len(topology.transformations[transform].requires)
            current_invariant += len(topology.transformations[transform].creates) - 1

        initial_invariants.append(current_invariant)

    # rank invariants
    prime_rank = prime_ranking(initial_invariants)
    current_rank = rank_list(prime_rank)
    updated_rank = [0 for _ in current_rank]
    next_rank = [0 for _ in current_rank]

    while True:

        # Calculate the multiples of primes around each entity to create
        # next_rank
        for c, e in enumerate(entities):

            current_invariant = 1

            # used by
            for transform in topology.entities[e].used_by:
                for r in topology.transformations[transform].requires:
                    if r != e:
                        current_invariant *= prime_rank[entities.index(r)]
                for r in topology.transformations[transform].creates:
                    current_invariant *= prime_rank[entities.index(r)]

            # created by
            for transform in topology.entities[e].created_by:
                for r in topology.transformations[transform].requires:
                    current_invariant *= prime_rank[entities.index(r)]
                for r in topology.transformations[transform].creates:
                    if r != e:
                        current_invariant *= prime_rank[entities.index(r)]

            next_rank[c] = int(current_invariant)

        # Generate a prime ranking for the new_ranking
        new_prime_rank = prime_ranking(next_rank)

        # Update the previous ordering with that provided by the latest round
        # of prime multiples
        updated_rank = two_level_ranking(current_rank, new_prime_rank)

        test = [x == y for x, y in zip(updated_rank, current_rank)]

        # Update current ranking
        current_rank = [x for x in updated_rank]
        prime_rank = prime_ranking(current_rank)

        if all(test):
            break

    return {e: x for e, x in zip(entities, current_rank)}


def assign_transformation_environments(
    topology: Topology,
) -> dict[str, int]:
    """
    Assigning each Tranformation an environment based on the
    CANGEN algorithm.

    1. Create initial invariants for transformations based on:
        a. Number of entities used by the transformation
        b. Number of entities created by the transformation

    2. Transform the initial invariants into ranks
        (Rank according to sum of used + created entities)
        Note that two transformations can have the same rank
        (-> actually, ranking can be left out for small numbers of invariants)

    3. Map each rank to a corresponding prime

    4. Create a new invariant where the primes of
       neighbors are multiplied.

       Neighbours are any entity attached to the same entity.

    5. Determine new ranks based on
        a. old ranks
        b. new invariants

    6. Repeat from 2 with new ranks until ranking is stable

    If transformations are symmetric, they should have the same rank

    Parameters
    ----------
    topology: DataBinder.Classes.Topology

    Returns
    -------
    labels: dict
    """

    # list of entities
    transformations = [*topology.transformations]

    initial_invariants = []
    # create initial invariants
    for e in transformations:
        current_invariant = 0
        # used by
        for entity in topology.transformations[e].requires:
            current_invariant += len(topology.entities[entity].used_by) - 1
            current_invariant += len(topology.entities[entity].created_by)

        # created by
        for entity in topology.transformations[e].creates:
            current_invariant += len(topology.entities[entity].used_by)
            current_invariant += len(topology.entities[entity].created_by) - 1

        initial_invariants.append(current_invariant)

    # rank invariants
    prime_rank = prime_ranking(initial_invariants)
    current_rank = rank_list(prime_rank)
    updated_rank = [0 for _ in current_rank]
    next_rank = [0 for _ in current_rank]

    while True:

        # Calculate the multiples of primes around each transformation to
        # create next_rank
        for c, e in enumerate(transformations):

            current_invariant = 1

            # requires
            for entity in topology.transformations[e].requires:
                for r in topology.entities[entity].used_by:
                    if r != e:
                        current_invariant *= prime_rank[transformations.index(r)]
                for r in topology.entities[entity].created_by:
                    current_invariant *= prime_rank[transformations.index(r)]

            # creates
            for entity in topology.transformations[e].creates:
                for r in topology.entities[entity].used_by:
                    current_invariant *= prime_rank[transformations.index(r)]
                for r in topology.entities[entity].created_by:
                    if r != e:
                        current_invariant *= prime_rank[transformations.index(r)]

            next_rank[c] = current_invariant

        # Generate a prime ranking for the new_ranking
        new_prime_rank = prime_ranking(next_rank)

        # Update the previous ordering with that provided by the latest round
        # of prime multiples
        updated_rank = two_level_ranking(current_rank, new_prime_rank)

        # Basis for test if the while loop should halt
        test = [x == y for x, y in zip(updated_rank, current_rank)]

        # Update current ranking
        current_rank = [x for x in updated_rank]
        prime_rank = prime_ranking(current_rank)

        if all(test):
            break

    return {e: x for e, x in zip(transformations, current_rank)}

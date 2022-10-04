def is_prime(number, primes_list):
    """
    Test if a number is prime.
    Parameters
    ----------
    number: int

    Returns
    -------
    bool
    """

    for prime in primes_list:
        if not (number == prime or number % prime):
            return False

    primes_list.add(number)
    return number


def generate_primes(num):
    """
    Generate the first `num` prime numbers.

    From this stack overflow answer:
    https://stackoverflow.com/questions/1628949/to-find-first-n-prime-numbers-in-python

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
        if is_prime(i, primes):
            p += 1
            if p == num:
                return list(primes)
        i += 1


def rank_list(a_list):
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


def prime_ranking(ranking):
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


def assign_environments(topology, radius=2):
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

    6. Repeat until ranking is stable

    If entities are symmetric, they should have the same rank

    Parameters
    ----------
    topology: DataBinder.Classes.Topology
    radius: int

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
    current_rank = rank_list(initial_invariants)
    next_rank = [0.0 for x in current_rank]
    prime_rank = prime_ranking(current_rank)

    while True:

        for c, e in enumerate(entities):

            current_invariant = 1.0

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

            next_rank[c] = current_invariant

        updated_rank = [n + p for n, p in zip(next_rank, prime_rank)]

        new_prime_rank = prime_ranking(updated_rank)

        test = [x == y for x, y in zip(prime_rank, new_prime_rank)]

        if all(test):
            prime_rank = [x for x in new_prime_rank]
            break

        prime_rank = [x for x in new_prime_rank]

    return {e: x for e, x in zip(entities, prime_rank)}

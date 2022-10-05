"""
Functions which test for things.
"""
from DataBinder.Inspectors import patterns


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


def is_float(thing):
    """
    Test if an thing (e.g. str) can be converted to a float.

    Parameters
    ----------
    x: any type

    Returns
    -------
    bool
    """

    try:
        float(thing)
        return True
    except ValueError:
        return False


def is_concentration_unit(text):
    """
    Determine if the argument contains a concentration unit.

    Parameters
    ----------
    text: str

    Returns
    -------
    bool
    """

    hits = []
    for regex in patterns.conc_units:
        hits.extend(regex.findall(text))

    if len(hits) > 0:
        return True

    return False


def is_flow_unit(text):
    """
    Determine if the argument contains a flow rate unit.

    Parameters
    ----------
    text: str

    Returns
    -------
    bool
    """

    hits = []
    for regex in patterns.flow_units:
        hits.extend(regex.findall(text))

    if len(hits) > 0:
        return True

    return False


def is_time_unit(text):
    """
    Determine if the argument contains a concentration unit.

    Parameters
    ----------
    text: str

    Returns
    -------
    bool
    """

    hits = []
    for regex in patterns.time_units:
        hits.extend(regex.findall(text))

    if len(hits) > 0:
        return True

    return False

"""
Functions which test for things.
"""


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

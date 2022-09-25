from DataBinder.Inspectors import patterns


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

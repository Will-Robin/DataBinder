from .equation_system import write_equations


TAB_SPACES = "    "


def to_function(topology):
    """
    Create a python function from a topology.

    Parameters
    ----------
    topology: DataBinder.Classes.Topology

    Returns
    -------
    function_text: str
    """

    equation_text = write_equations(topology)

    equation_lines = [x for x in equation_text.split("\n") if x != ""]

    indented_equation_text = f"\n{TAB_SPACES}".join(equation_lines)

    arguments = ["time", "S", "k", "inp", "out"]

    arg_string = ", ".join(arguments)

    arg_docstring = f"\n{TAB_SPACES}".join(arguments)

    function_text = f'''
def function({arg_string}):
    """
    Function docstring.

    Parameters
    ----------
    {arg_docstring}

    Returns
    -------
    P: List[float]
    """

    P = [0.0 for x in S]

    {indented_equation_text}

    return P
    '''

    return function_text

from .equation_system import write_equations


TAB_SPACES = "    "


def to_function(topology, unwrap_constants=False):
    """
    Create a python function from a topology.

    Parameters
    ----------
    topology: DataBinder.Classes.Topology
    unwrap_constants: bool
        True: write the value stored in a Constant into output (e.g. 1.0).
        False: write a token value for a Constant into output (e.g. C[n]).

    Returns
    -------
    function_text: str
    """

    equation_text = write_equations(topology, unwrap_constants=unwrap_constants)

    equation_lines = [x for x in equation_text.split("\n") if x != ""]

    indented_equation_text = f"\n{TAB_SPACES}".join(equation_lines)

    arguments = ["time", "S", "k"]

    if len(topology.inputs) > 0:
        arguments.append("inp")

    if len(topology.outputs) > 0:
        arguments.append("out")

    arg_string = ", ".join(arguments)

    arg_docstring = f"\n{TAB_SPACES}".join(arguments)

    function_text = f'''
def model_function({arg_string}):
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

    return P'''

    return function_text

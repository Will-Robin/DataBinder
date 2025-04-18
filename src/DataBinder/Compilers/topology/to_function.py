"""
Convert a topology to a python function.
"""

from DataBinder.Classes import Topology
from .to_equation_system import create_token_lookup
from .to_equation_system import topology_to_equation_system


TAB_SPACES = "    "


def topology_to_function(
    topology: Topology,
    function_name: str = "model_function",
    unwrap_constants: bool = False,
) -> str:
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

    equation_text = topology_to_equation_system(
        topology, unwrap_constants=unwrap_constants
    )

    equation_lines = [x for x in equation_text.split("\n") if x != ""]

    indented_equation_text = f"\n{TAB_SPACES}".join(equation_lines)

    arguments = ["time", "S", "k"]

    if len(topology.inputs) > 0:
        arguments.append("inp")

    if len(topology.outputs) > 0:
        arguments.append("out")

    if len(topology.constants) > 0:
        arguments.append("C")

    arg_string = ", ".join(arguments)

    arg_docstring = f"\n{TAB_SPACES}".join(arguments)

    # Indicate which indices map to which entities
    token_tables = create_token_lookup(topology)
    for table in token_tables:
        for t in token_tables[table]:
            arg_docstring += f"\n{TAB_SPACES}{token_tables[table][t]}: {t}"
        arg_docstring += "\n"

    function_text = f'''
def {function_name}({arg_string}):
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

    return [x + y for x,y in zip(S, P)]'''

    return function_text

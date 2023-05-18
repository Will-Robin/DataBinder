"""
Convert a topology to a system of equations.
"""
from DataBinder.Classes import Topology


def topology_to_equation_system(
    topology: Topology, unwrap_constants: bool = False
) -> str:
    """
    Create a system of equations from a topology

    Parameters
    ----------
    topology: DataBinder.Classes.Topology
        Topology to be converted.
    unwrap_constants: bool
        True: write the value stored in a Constant into output (e.g. 1.0).
        False: write a token value for a Constant into output (e.g. C[n]).

    Returns
    -------
    equations: str
        System of equations derived from the topology.
    """

    # aliases for topology attributes
    entities = topology.entities
    constants = topology.constants
    transformations = topology.transformations
    inputs = topology.inputs
    outputs = topology.outputs

    # Create tokens for the equation output
    entity_tokens = {iden: f"S[{c}]" for c, iden in enumerate(entities)}

    constant_tokens = {iden: f"C[{c}]" for c, iden in enumerate(constants)}

    rate_constants = {iden: f"k[{c}]" for c, iden in enumerate(transformations)}

    input_rates = {iden: f"inp[{c}]" for c, iden in enumerate(inputs)}

    output_rates = {iden: f"out[{c}]" for c, iden in enumerate(outputs)}

    # Tokens for the output expression.
    result_tokens = {iden: f"P[{c}]" for c, iden in enumerate(entities)}

    # Write equations
    equations = ""
    for _, entity in enumerate(entities):

        current_token = f"{result_tokens[entity]} = "

        # Write incoming expressions
        for creator in entities[entity].created_by:

            # Transformations
            if creator in transformations:
                input_set = transformations
                current_token += f"+{rate_constants[creator]}"
                for requirement in input_set[creator].requires:
                    current_token += f"*{entity_tokens[requirement]}"
            # Inputs
            else:
                input_set = inputs
                current_token += f"+{input_rates[creator]}"
                for requirement in input_set[creator].requires:
                    if unwrap_constants:
                        val = constants[requirement].value
                    else:
                        val = constant_tokens[requirement]
                    current_token += f"*{val}"

        # Write outgoing expressions
        for user in entities[entity].required_by:

            # Transformations
            if user in transformations:
                output_set = transformations
                current_token += f"-{rate_constants[user]}"
            # Outputs
            else:
                output_set = outputs
                current_token += f"-{output_rates[user]}"

            for requirement in output_set[user].requires:
                current_token += f"*{entity_tokens[requirement]}"

        current_token += "\n"

        equations += current_token

    return equations

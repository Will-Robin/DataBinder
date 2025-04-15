"""
Convert a topology to an equation system.
"""

from DataBinder.Classes import Topology
from .to_equation_system import create_token_lookup

ILLEGAL_SYMBOLS = {"-": "_", "*": "m", "/": "d", "+": "p", ".": "o"}

NUMBERS = {
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VIII",
    "9": "IX",
    "0": "X",
}


def sanitise_token(token: str) -> str:
    """
    Sanitise a token by replacing operator characters which will interfere with
    its mathematical interpretation.

    Parameters
    ----------
    token: str

    Returns
    -------
    sanitised_token: str
    """

    # Tokens cannot start with numbers
    if token[0] in NUMBERS:
        sanitised_token = NUMBERS[token[0]]
    else:
        sanitised_token = token[0]

    # Replace operators
    for char in token[1:]:
        if char in ILLEGAL_SYMBOLS:
            replacement = ILLEGAL_SYMBOLS[char]
        else:
            replacement = char

        sanitised_token += replacement

    return sanitised_token


def topology_to_equation(topology: Topology, unwrap_constants: bool = False) -> str:
    """
    Convert a topology to an equation string.

    Parameters
    ----------
    topology: Topology

    Returns
    -------
    equation: str
    """

    token_lookup = create_token_lookup(topology)

    entity_tokens = token_lookup["entity_tokens"]
    constant_tokens = token_lookup["constant_tokens"]
    rate_constants = token_lookup["rate_constants"]
    input_rates = token_lookup["input_rates"]
    output_rates = token_lookup["output_rates"]
    result_tokens = token_lookup["result_tokens"]

    # aliases for topology attributes
    entities = topology.entities
    constants = topology.constants
    transformations = topology.transformations
    inputs = topology.inputs
    outputs = topology.outputs

    lines = []
    # Write equations
    equations = ""
    for _, entity in enumerate(entities):
        current_token = f"d({sanitise_token(entity)})_dt = "

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

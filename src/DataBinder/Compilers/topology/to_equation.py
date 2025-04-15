"""
Convert a topology to an equation system.
"""

from DataBinder.Classes import Topology

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


def topology_to_equation(topology: Topology) -> str:
    """
    Convert a topology to an equation string.

    Parameters
    ----------
    topology: Topology

    Returns
    -------
    equation: str
    """

    rate_constants = {t: f"k{c}" for c, t in enumerate(topology.transformations)}

    lines = []
    for e in topology.entities:
        entity = topology.entities[e]
        ent_eq = f"d{sanitise_token(e)}_dt = "

        # Incoming transformations
        for inc in entity.created_by:
            transform = topology.transformations[inc]
            dependencies = transform.requires
            ent_eq += f"+{rate_constants[inc]}"
            for d in dependencies:
                ent_eq += f"*{sanitise_token(d)}"

        # Outgoing transformations
        for inc in entity.required_by:
            transform = topology.transformations[inc]
            dependencies = transform.requires
            ent_eq += f"-{rate_constants[inc]}"
            for d in dependencies:
                ent_eq += f"*{sanitise_token(d)}"

        lines.append(ent_eq)

    return "\n".join(lines)

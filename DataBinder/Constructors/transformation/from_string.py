"""
For loading Transformations from files and strings.
"""
from DataBinder.Classes import Transformation


def transformation_from_string(text: str) -> Transformation:
    """
    Create a transformation from a string.

    e.g. A.B>>C.D

    Parameters
    ----------
    text: str

    Returns
    -------
    transform: Classes.Transformation
    """

    sides = text.split(">>")
    LHS = sides[0]
    RHS = sides[1]

    inputs = LHS.split(".")
    outputs = RHS.split(".")

    transform: Transformation = Transformation(text)
    transform.requires = inputs
    transform.creates = outputs

    return transform

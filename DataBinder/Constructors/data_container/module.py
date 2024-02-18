"""
Constructors for a DataContainer object.
"""

from pathlib import Path
from typing import Any

from DataBinder.Classes import DataContainer
from DataBinder.Classes import ConditionValue
from DataBinder.Classes import ConditionArray
from DataBinder.Inspectors import patterns
from DataBinder.Inspectors import test_for


def process_lines(text: str) -> list[list[Any]]:
    """
    Convert a text block into a list.

    Parameters
    ----------
    text: string

    Returns
    -------
    output: list[list]
    """

    lines = text.split("\n")

    output = []
    for line in lines:
        contents = [x for x in line.split(",") if x != ""]

        if len(contents) == 0:
            continue

        str_values = []
        float_values = []
        for c in contents:
            if test_for.is_float(c):
                float_values.append(float(c))
            else:
                str_values.append(c)

        output.append(str_values + float_values)

    return output


def parse_element(element: list[Any]) -> tuple[str, list[float], str]:
    """

    Parameters
    ----------
    element: list

    Returns
    -------
    (str, list, str)
    """

    iden = patterns.variable_pattern.findall(element[0])
    value = element[1:]
    unit = patterns.unit_pattern.findall(element[0])

    return iden[0], value, unit[0]

"""
For applying assumptions to topologies (e.g. fast pre-equilibrium,
etc.)
"""

from .Assumptions import pseudo_first_order_transformation
from .Assumptions import pseudo_first_order_entity
from .Assumptions import pre_equilibrium

__all__ = [
    "pseudo_first_order_transformation",
    "pseudo_first_order_entity",
    "pre_equilibrium",
]

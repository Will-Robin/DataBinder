"""
For compiling structures into other encoded forms.
"""

from .topology import topology_to_adjacency_matrix
from .topology import topology_to_equation
from .topology import topology_to_equation_system
from .topology import topology_to_stoichiometric_matrix
from .topology import topology_to_function
from .topology import topology_to_matrix_formulation

__all__ = [
    "topology_to_adjacency_matrix",
    "topology_to_equation",
    "topology_to_equation_system",
    "topology_to_stoichiometric_matrix",
    "topology_to_function",
    "topology_to_matrix_formulation",
]

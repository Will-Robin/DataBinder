from DataBinder.Constructors import topology_from_text_file
from DataBinder.Compilers import topology_to_matrix_formulation

# load topology
topology_file = "data/simple_reaction_list.txt"
topology_container = topology_from_text_file(topology_file)

result = topology_to_matrix_formulation(topology_container)

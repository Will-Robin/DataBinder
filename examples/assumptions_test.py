"""
This script tests assumption-applying functions
"""
from DataBinder.Constructors import topology_from_text_file
from DataBinder.Assumptions import pseudo_first_order_transformation
from DataBinder.Assumptions import pseudo_first_order_entity


# load topology
topology_file = "data/exampleReactionList.txt"
topology = topology_from_text_file(topology_file)

# Specify tokens involved in assumptions
entity_token = "O"
transform_token = "O.OC=C(O)CO>>O.O=C[C@H](O)CO"

# apply a pseudo-first order approximation to a single transformation
# top_1 = pseudo_first_order_transformation(topology, transform_token, entity_token)

# apply a pseudo-first order approximation to all of the transformations
# involving a specified entity
top_2 = pseudo_first_order_entity(topology, entity_token)

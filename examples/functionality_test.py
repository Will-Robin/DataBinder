"""
This script calls key functions from DataBinder.
"""
from DataBinder.Constructors import DataContainer as cont
from DataBinder.Constructors import Topology as topol
from DataBinder.Compilers import to_function
from DataBinder.Compilers import write_adjacency_matrix
from DataBinder.Binders import data_topology
from DataBinder.Visualisation import Layouts


# load data
data_file = "data/exampleData.csv"
data_container = cont.from_csv(data_file)

# load topology
topology_file = "data/exampleReactionList.txt"
topology_container = topol.from_text(topology_file)

# Validate that the data and topology are compatible
messages = data_topology.validate(data_container, topology_container)
if len(messages) > 0:
    print(f"# Found {len(messages)} issue(s):")
    for c, m in enumerate(messages, 1):
        print(f"# {c}. {m}")
print()

# Put information from the data into the topology
bound = data_topology.bind_data_topology(data_container, topology_container)

# Create python code for the topology
function_text = to_function(topology_container)

print("Example function compilation:\n")
print(function_text)

# Create an adjacency matrix
adj_list = write_adjacency_matrix(topology_container)

print("Example adjacency list compilation:\n")
for a in adj_list:
    print(a)

# Generate a layout
pos = Layouts.generate_topology_layout(topology_container, algorithm="fdp")

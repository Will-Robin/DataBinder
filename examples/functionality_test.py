"""
This script calls key functions from DataBinder.
"""
from DataBinder.Constructors import data_container_from_csv
from DataBinder.Constructors import topology_from_text_file
from DataBinder.Compilers import topology_to_function
from DataBinder.Compilers import topology_to_adjacency_matrix
from DataBinder.Binders import data_topology

# Loading a data file with string based series values
test_data_file = "data/exampleData_2.csv"
test_data_container = data_container_from_csv(test_data_file)

# load data
data_file = "data/exampleData.csv"
data_container = data_container_from_csv(data_file)

# load topology
topology_file = "data/exampleReactionList.txt"
topology_container = topology_from_text_file(topology_file)

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
function_text = topology_to_function(topology_container)

print("Example function compilation:\n")
print(function_text)

# Create an adjacency matrix
adj_list = topology_to_adjacency_matrix(topology_container)

print("Example adjacency list compilation:\n")
for a in adj_list:
    print(a)

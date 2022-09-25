from DataBinder.Constructors import DataContainer as cont
from DataBinder.Constructors import Topology as topol
from DataBinder.Compilers import equation_system
from DataBinder.Compilers import to_function
from DataBinder.Compilers import write_adjacency_matrix
from DataBinder.Binders import data_topology
from DataBinder.Visualisation import Layouts


# load data
data_container = cont.from_csv("example_data/exampleData.csv")

# load topology
topology_container = topol.from_text("example_data/exampleReactionList.txt")

# Validate that the data and topology are compatible
messages = data_topology.validate(data_container, topology_container)
if len(messages) > 0:
    print("# Found issues:")
    for m in messages:
        print(f"# {m}")

# Put information from the data into the topology
bound = data_topology.bind_data_topology(data_container, topology_container)

# Generate a layout
pos = Layouts.generate_topology_layout(topology_container, algorithm="fdp")

# Create python code for the topology
function_text = to_function(topology_container)

# Create an adjacency matrix
adj_list = write_adjacency_matrix(topology_container)

for a in adj_list:
    print(a)

from DataBinder.Constructors import Topology as topol
from DataBinder.Compilers import to_function
from DataBinder.Visualisation import Layouts

topology_file = "data/trypsin_oscillator.txt"

# load topology
topology = topol.from_text(topology_file)

function_text = to_function(topology)

print(function_text)

# Generate a layout
pos = Layouts.generate_topology_layout(topology, algorithm = "sfdp")

for p in pos:
    print(f"{p}: x: {pos[p][0]}, y: {pos[p][1]}")

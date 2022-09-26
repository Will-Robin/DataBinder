from DataBinder.Constructors import Topology as topol
from DataBinder.Compilers import to_function

topology_file = "../data/trypsin_oscillator.txt"

# load topology
topology = topol.from_text(topology_file)

function_text = to_function(topology)

print(function_text)

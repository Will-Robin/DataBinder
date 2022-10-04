from DataBinder.Constructors import Topology as topol
from DataBinder.Algorithms import GraphEnvironments

# load topology
topology_file = "data/thiol_network.txt"
topology = topol.from_text(topology_file)

result = GraphEnvironments.assign_environments(topology)

for r in result:
    print(r, result[r])

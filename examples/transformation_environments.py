from DataBinder.Constructors import Topology as topol
from DataBinder.Algorithms import TopologyEnvironments

# load topology
topology_file = f"data/thiol_network.txt"
topology = topol.from_text(topology_file)

result = TopologyEnvironments.assign_transformation_environments(topology)

# reverse results:
environments = {}
for r in result:
    env = result[r]
    if env not in environments:
        environments[env] = []
    environments[env].append(r)

labels = list(result.values())

unique_environments = []
for r in result:
    if result[r] not in unique_environments:
        unique_environments.append(result[r])

print(f"Entities: {len(topology.entities)}")

print(f"Unique environments: {len(unique_environments)}\n")

for u in unique_environments:
    if labels.count(u) > 1:
        print(f"Env {u}: ", labels.count(u))
print()
for r in result:
    print(f"Entity: {r} ({result[r]})")

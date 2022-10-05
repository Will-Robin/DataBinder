from DataBinder.Constructors import Topology as topol
from DataBinder.Algorithms import TopologyEnvironments
from DataBinder.Visualisation import Layouts

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

# Visualise the environments
pos = Layouts.generate_topology_layout(topology, algorithm="neato")

# Generate scatter for each environment
scatters = []
for env in environments:
    scatter_x = []
    scatter_y = []
    entities = environments[env]

    for e in entities:
        scatter_x.append(pos[e][0])
        scatter_y.append(pos[e][1])

    scatters.append((scatter_x, scatter_y))

# Create lineplot
line_x = []
line_y = []
for e in topology.entities:
    root_x = pos[e][0]
    root_y = pos[e][1]

    for r in topology.entities[e].used_by:
        target_x = pos[r][0]
        target_y = pos[r][1]

        line_x.extend([root_x, target_x, None])
        line_y.extend([root_y, target_y, None])

    for r in topology.entities[e].created_by:
        target_x = pos[r][0]
        target_y = pos[r][1]

        line_x.extend([root_x, target_x, None])
        line_y.extend([root_y, target_y, None])

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot(line_x, line_y, c="k", zorder=0)

for x in scatters:
    ax.scatter(x[0], x[1])

for e in topology.entities:
    ax.annotate(e, xy=pos[e])

plt.show()

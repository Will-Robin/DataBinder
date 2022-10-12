"""
Generate layouts for topologies using Graphviz.
"""
import json
from DataBinder.Classes import Topology

try:
    import graphviz
    from graphviz import Digraph
except ImportError:
    print(
        """\033[1m\033[91m
ImportError: graphviz not installed, DataBinder.Visualisation module will crash!
\033[0m"""
    )


def create_edges(container: dict, graph: graphviz.Digraph):
    """
    container: dict()
    graph: graphviz.Digraph
    """
    for transform in container:

        graph.node(transform, transform)

        requirements = container[transform].requires
        creations = container[transform].creates

        for req in requirements:
            graph.edge(req, transform)

        for create in creations:
            graph.edge(transform, create)

    return graph


def generate_topology_layout(
    topology: Topology, algorithm: str = "fdp"
) -> dict[str, list[float]]:
    """
    Uses graphviz to generate a layout from a Topology.

    Layouts from the graphviz documentation:
    dot − filter for drawing directed graphs
    neato − filter for drawing undirected graphs
    twopi − filter for radial layouts of graphs
    circo − filter for circular layout of graphs
    fdp − filter for drawing undirected graphs
    sfdp − filter for drawing large undirected graphs
    patchwork − filter for squarified tree maps
    osage − filter for array-based layouts

    Parameters
    ----------
    topology: DataBinder.Classes.Topology
        Topology object.
    render_engine: str
        Layout render engine for graphviz.

    Returns
    -------
    pos: dict
        Entity and Transformation tokens are keys to (x,y) coordinates.
        {token:[float(x),float(y)]}
    """

    # Create a graph with graphviz to plot a scheme of the network
    dot = Digraph(comment="", engine=algorithm, strict="True", format="json")

    # Create nodes for entities
    for node in topology.entities:
        dot.node(node, node)

    # Create nodes for constants
    for node in topology.constants:
        dot.node(node, node)

    # Create edges for transformations
    create_edges(topology.transformations, dot)

    # Create edges for inputs
    create_edges(topology.inputs, dot)

    # Create edges for outputs
    create_edges(topology.outputs, dot)

    json_string = dot.pipe().decode()

    layout = json.loads(json_string)

    pos = {}
    for node in layout["objects"]:
        name = node["name"]
        coordinate = [float(x) for x in node["pos"].split(",")]
        pos[name] = coordinate

    return pos

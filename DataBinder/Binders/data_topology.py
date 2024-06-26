"""
Binds data to a topology.
"""

from DataBinder.Classes import Input
from DataBinder.Classes import Output
from DataBinder.Classes import Constant
from DataBinder.Classes import Topology
from DataBinder.Classes import DataContainer
from DataBinder.Inspectors import patterns
from DataBinder.Inspectors import test_for


# Names which cannot be used as tokens for entities or transformations
reserved_names = ["inflow", "outflow"]


def validate(data: DataContainer, topology: Topology) -> list[str]:
    """
    Check the data and topology for compatibility, omissions in data, etc.

    Parameters
    ----------
    data: DataBinder.Classes.DataContainer
    topology: DataBinder.Classes.Topology

    Returns
    -------
    error_report: list[str]
        List of error messages.
    """

    error_report = []

    # Get a list of tokens in the data
    data_tokens = []
    for variable in data.data:
        no_units = patterns.variable_pattern.findall(variable)
        first_match = no_units[0]
        data_tokens.append(first_match)

    # Check that there are no reserved names in the data or topology
    for entity in topology.entities:
        if entity in reserved_names:
            error_report.append(
                f"The reserved name {entity} is used as an entity id in the topology."
            )

    for entity in data_tokens:
        if entity in reserved_names:
            error_report.append(
                f"The reserved name {entity} is used as a token in the data."
            )

    # Check for species compatibility
    # If entities in the data are not in the topology, then the topology is not
    # compatible with the data.
    for variable in data_tokens:
        if variable not in topology.entities:
            error_report.append(
                f"The entity {variable} (present in the data) is not present in the topology."
            )

    return error_report


def bind_data_topology(data: DataContainer, topology: Topology) -> Topology:
    """
    Bind data and topology together into a model.

    Parameters
    ----------
    data: DataBinder.Classes.DataContainer
    topology: DataBinder.Classes.Topology

    Returns
    -------
    topology: DataBinder.Classes.Topology
        Topology containing information from the data conditions.
    """

    # Reconcile experiment inputs with the topology.
    # Scan for flow inputs
    inflow_register = []
    for entity in topology.entities:
        for array_c in data.array_conditions:
            token = patterns.token_pattern.findall(array_c.id)[0]
            if token == entity:
                if test_for.is_flow_unit(array_c.unit):
                    # Keep track of inflows
                    inflow_register.append(entity)

    # Scan for input concentrations
    input_counter = 1
    for entity in inflow_register:
        for value_c in data.value_conditions:
            token = patterns.token_pattern.findall(value_c.id)[0]
            if token == entity and test_for.is_concentration_unit(value_c.unit):
                # Create a new token for the input source
                flow_token = f"{value_c.id}_flow"
                input_counter += 1

                # Create a new token for the input
                input_token = f"{flow_token}>>{entity}"

                # Get the concentration value
                value = value_c.value

                # Create a constant to be combined with an input
                flow_entity = Constant(flow_token, value)

                # Create the input to be added to the topology
                inp = Input(input_token)
                inp.requires.append(flow_token)
                inp.creates.append(entity)

                # Add the newly created objects to the topology
                topology.add_input(inp)
                topology.add_constant(flow_entity)

    # Assume for now that there is one output to which all entities are
    # connected.
    output_tokens = ["#0"]
    for output_token in output_tokens:
        value = 0.0

        # Create a token and object for the outlet
        outlet = Constant(output_token, value)
        topology.add_constant(outlet)

        for e in topology.entities:
            # Create a token for the output process
            new_output_token = f"{e}>>{output_token}"

            output = Output(new_output_token)
            output.requires.append(e)
            output.creates.append(output_token)

            topology.add_output(output)

    return topology

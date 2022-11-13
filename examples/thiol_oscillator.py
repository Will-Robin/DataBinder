from DataBinder.Constructors import Topology as topol
from DataBinder.Compilers import to_function
from DataBinder.Classes import Input
from DataBinder.Classes import Output
from DataBinder.Classes import Constant

topology_file = "data/thiol_network.txt"

###############
# load topology
###############
topology = topol.from_text(topology_file)

#################
# Add input flows
#################
Mal = Constant("Mal_flow", 1.0)
topology.add_constant(Mal)
Mal_input = Input("Mal_flow>>Mal")
Mal_input.requires.append("Mal_flow")
Mal_input.creates.append("Mal")
topology.add_input(Mal_input)

AlaSEt = Constant("AlaSEt_flow", 1.0)
topology.add_constant(AlaSEt)
AlaSEt_input = Input("AlaSEt_flow>>AlaSEt")
AlaSEt_input.requires.append("AlaSEt_flow")
AlaSEt_input.creates.append("AlaSEt")
topology.add_input(AlaSEt_input)

disulf = Constant("H2NCCSSCCNH2_flow", 1.0)
topology.add_constant(disulf)
disulf_input = Input("disulf_flow>>disulf")
disulf_input.requires.append("disulf_flow")
disulf_input.creates.append("disulf")
topology.add_input(disulf_input)

_10 = Constant("10_flow", 1.0)
topology.add_constant(_10)
_10_input = Input("_10_flow>>_10")
_10_input.requires.append("_10_flow")
_10_input.creates.append("_10")
topology.add_input(_10_input)

#############
# Add outputs
#############
output_const_token = "#0"
outlet = Constant(output_const_token, 0.0)  # value not relevant to outputs
topology.add_constant(outlet)

# Each entity leaves via the single output.
for e in topology.entities:
    # Create a token for the output process
    output_token = f"{e}>>{output_const_token}"
    output = Output(output_token)
    output.requires.append(e)
    output.creates.append(output_const_token)

    topology.add_output(output)

#########################
# Create the ODE function
#########################
function_text = to_function(topology, unwrap_constants=True)

print(function_text, "\n")

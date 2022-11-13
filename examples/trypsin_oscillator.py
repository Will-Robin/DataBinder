from DataBinder.Constructors import Topology as topol
from DataBinder.Compilers import to_function
from DataBinder.Classes import Input
from DataBinder.Classes import Output
from DataBinder.Classes import Constant

topology_file = "data/trypsin_oscillator.txt"

###############
# load topology
###############
topology = topol.from_text(topology_file)

#################
# Add input flows
#################
# Create a constant to describe the input flow
Tr_conc_0 = 0.05
Tr_flow = Constant("Tr_flow", Tr_conc_0)
topology.add_constant(Tr_flow)
# Connect Constant to Entity with an Input
Tr_input = Input("Tr_flow>>Tr")
Tr_input.requires.append("Tr_flow")
Tr_input.creates.append("Tr")
topology.add_input(Tr_input)

# Create a constant to describe the input flow
_2_conc_0 = 0.05
_2_flow = Constant("2_flow", _2_conc_0)
topology.add_constant(_2_flow)
# Connect Constant to Entity with an Input
_2_input = Input("2_flow>>2")
_2_input.requires.append("2_flow")
_2_input.creates.append("2")
topology.add_input(_2_input)

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

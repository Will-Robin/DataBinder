from DataBinder.Constructors import topology_from_text_file
from DataBinder.Compilers import topology_to_equation
from DataBinder.Classes import Input
from DataBinder.Classes import Output
from DataBinder.Classes import Constant

topology_file = "data/trypsin_oscillator.txt"

###############
# load topology
###############
topology = topology_from_text_file(topology_file)

sympy_text = topology_to_equation(topology)

print(sympy_text)

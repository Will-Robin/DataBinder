from DataBinder.Constructors import Topology as topol
from DataBinder.Compilers import to_equation
from DataBinder.Visualisation import Layouts
from DataBinder.Classes import Input
from DataBinder.Classes import Output
from DataBinder.Classes import Constant

topology_file = "data/trypsin_oscillator.txt"

###############
# load topology
###############
topology = topol.from_text(topology_file)

sympy_text = to_equation(topology)

print(sympy_text)

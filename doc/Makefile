
ASSUMPTIONS = ../DataBinder/Assumptions/*.py
BINDERS = ../DataBinder/Binders/*.py
CLASSES = ../DataBinder/Classes/*.py
COMPILERS = ../DataBinder/Compilers/*.py
CONSTRUCTORS = ../DataBinder/Constructors/*.py
INSPECTORS = ../DataBinder/Inspectors/*.py
ALGORITHMS = ../DataBinder/Algorithms/*.py


DATABINDER=$(ASSUMPTIONS) $(BINDERS) $(CLASSES) \
	$(COMPILERS) $(CONSTRUCTORS) $(INSPECTORS) \
	$(ALGORITHMS)

all: index.html

index.html: $(DATABINDER)
	pdoc ../DataBinder -d "numpy" -o ./

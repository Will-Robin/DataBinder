
ASSUMPTIONS = ../src/DataBinder/Assumptions/*.py
BINDERS = ../src/DataBinder/Binders/*.py
CLASSES = ../src/DataBinder/Classes/*.py
COMPILERS = ../src/DataBinder/Compilers/*.py
CONSTRUCTORS = ../src/DataBinder/Constructors/*.py
INSPECTORS = ../src/DataBinder/Inspectors/*.py
ALGORITHMS = ../src/DataBinder/Algorithms/*.py


DATABINDER=$(ASSUMPTIONS) $(BINDERS) $(CLASSES) \
	$(COMPILERS) $(CONSTRUCTORS) $(INSPECTORS) \
	$(ALGORITHMS)

all: index.html

index.html: $(DATABINDER)
	pdoc ../src/DataBinder -d "numpy" -o ./

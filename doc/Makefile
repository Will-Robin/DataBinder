
ASSUMPTIONS = ../DataBinder/Assumptions/*.py
BINDERS = ../DataBinder/Binders/*.py
CLASSES = ../DataBinder/Classes/*.py
COMPILERS = ../DataBinder/Compilers/*.py
CONSTRUCTORS = ../DataBinder/Constructors/*.py
INSPECTORS = ../DataBinder/Inspectors/*.py
VISUALISATION = ../DataBinder/Visualisation/*.py


DATABINDER=$(ASSUMPTIONS) $(BINDERS) $(CLASSES) \
	$(COMPILERS) $(CONSTRUCTORS) $(INSPECTORS) \
	$(VISUALISATION)

all: index.html

index.html: $(DATABINDER)
	pdoc ../DataBinder -d "numpy" -o ./

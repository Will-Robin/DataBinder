class Entity:
    """
    An individual unit in a structure.
    """

    def __init__(self, iden: str):
        """
        Attributes
        ----------
        iden: str
            Unique id for the entity

        created_by: list[str]
            List of ids of Transformations which create this
            entity.

        used_by: list[str]
            List of ids of Transformations which use this
            entity in a transformation.
        """

        self.id: str = iden
        self.created_by: list = []
        self.used_by: list = []


class Constant(Entity):
    """
    A structure for storing constants.

    An alias for Entity, emphasising that it is derived from data.
    """

    def __init__(self, iden: str, value: float):
        super().__init__(iden)
        self.value = value


class Transformation:
    """
    A transformation describes the conversion between entities.
    """

    def __init__(self, iden: str):
        """
        Attributes
        ----------
        iden: str
            Unique id for the transformations.

        requires: list[str]
            List of ids of entities which are required by this
            transformation.

        creates: list[str]
            List of ids of entities which are created by this
            transformation.
        """

        self.id: str = iden
        self.requires: list = []
        self.creates: list = []


class Input(Transformation):
    """
    A structure for storing input data.

    This is an alias for a Transformation to emphasise its derivation from
    conditional information.
    """


class Output(Transformation):
    """
    A structure for storing output data.

    This is an alias for a Transformation to emphasise its derivation from
    conditional information.
    """


class Topology:
    """
    Stores the relationships between Entities, Transformations and their
    derived types in a system.
    """

    def __init__(self):
        """
        Attributes
        ----------
        entities: dict()
            Entities are things like chemical compounds.
        transformations: dict()
            Transformations connect entities (like chemical
            reactions connect compounds)
        constants: dict()
            Constants are floats to mulitply certain entities by.
        inputs: dict()
            Inputs into the systems (transformation-like)
            - connects a constant to an entity.
        outputs: dict()
            Outputs from the system (transformation-like)
            - connects an entity to a constant.
        """

        self.entities: dict = {}
        self.transformations: dict = {}
        self.constants: dict = {}
        self.inputs: dict = {}
        self.outputs: dict = {}

    def add_entity(self, addition: Entity):
        if addition.id not in self.entities:
            self.entities[addition.id] = addition

    def add_transformation(self, addition: Transformation):
        if addition.id not in self.transformations:
            for requirement in addition.requires:
                self.add_entity(Entity(requirement))
                self.entities[requirement].used_by.append(addition.id)

            for creation in addition.creates:
                self.add_entity(Entity(creation))
                self.entities[creation].created_by.append(addition.id)

            self.transformations[addition.id] = addition

    def add_constant(self, cons: Constant):
        if cons.id not in self.constants:
            self.constants[cons.id] = cons
        elif self.constants[cons.id].value == 0.0:
            self.constants[cons.id].value = cons.value

    def add_input(self, inp: Input):
        if inp.id not in self.inputs:
            for requirement in inp.requires:
                self.add_constant(Constant(requirement, 0.0))
                self.constants[requirement].used_by.append(inp.id)

            for creation in inp.creates:
                self.add_entity(Entity(creation))
                self.entities[creation].created_by.append(inp.id)

            self.inputs[inp.id] = inp

    def add_output(self, output: Output):
        if output.id not in self.outputs:
            for requirement in output.requires:
                self.add_entity(Entity(requirement))
                self.entities[requirement].used_by.append(output.id)

            for creation in output.creates:
                self.add_constant(Constant(creation, 0.0))
                self.constants[creation].created_by.append(output.id)

            self.outputs[output.id] = output
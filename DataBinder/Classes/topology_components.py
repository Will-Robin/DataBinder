"""
The Topology structure and its components.
"""


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

        required_by: list[str]
            List of ids of Transformations which use this
            entity in a transformation.
        """

        self.id: str = iden
        self.created_by: list[str] = []
        self.required_by: list[str] = []

    def __repr__(self):
        return f"Entity: {self.id}"

    def __str__(self):
        return f"{self.id}"

    def associated_transformation_keys(self) -> list[str]:
        """
        Get the combined keys of transformations which create the entity and
        transformations which require the entity.

        Parameters
        ----------

        Returns
        -------
        list[str]
        """
        return self.created_by + self.required_by


class Constant(Entity):
    """
    A structure for storing constants.

    An alias for Entity, emphasising that it is derived from data.
    """

    def __init__(self, iden: str, value: float):
        super().__init__(iden)
        self.value: float = value


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

    def __repr__(self):
        return f"Transformation: {self.id}"

    def __str__(self):
        return f"{self.id}"

    def associated_entity_keys(self) -> list[str]:
        """
        Get all of the entities required and created by the transformation.

        Parameters
        ----------

        Returns
        -------
        list[str]
        """
        return self.requires + self.creates


class Input(Transformation):
    """
    A structure for storing input data.

    This is an alias for a Transformation to emphasise its derivation from
    conditional information.
    """

    def __init__(self, iden: str):
        super().__init__(iden)


class Output(Transformation):
    """
    A structure for storing output data.

    This is an alias for a Transformation to emphasise its derivation from
    conditional information.
    """

    def __init__(self, iden: str):
        super().__init__(iden)


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
        """
        Add an entity to the topology.

        Parameters
        ----------
        addition: DataBinder.Classes.Entity

        Returns
        -------
        None
        """

        if addition.id not in self.entities:
            self.entities[addition.id] = addition

    def remove_entity(self, removal: Entity):
        """
        Remove an entity from the topology.

        Parameters
        ----------
        removal: DataBinder.Classes.Entity

        Returns
        -------
        None
        """

        token = removal.id
        remove_transformations = []
        # Remove the entity from associated transformations
        for transf in self.entities[token].required_by:
            self.transformations[transf].requires.remove(token)
            if len(self.transformations[transf].requires) == 0:
                remove_transformations.append(transf)
        for transf in self.entities[token].created_by:
            self.transformations[transf].creates.remove(token)
            if len(self.transformations[transf].creates) == 0:
                remove_transformations.append(transf)

        for transf in remove_transformations:
            self.remove_transformation(self.transformations[transf])

        del self.entities[token]

    def add_transformation(self, addition: Transformation):
        """
        Add a transformation to the topology.

        Parameters
        ----------
        addition: DataBinder.Classes.Transformation

        Returns
        -------
        None
        """

        if addition.id not in self.transformations:
            for requirement in addition.requires:
                self.add_entity(Entity(requirement))
                self.entities[requirement].required_by.append(addition.id)

            for creation in addition.creates:
                self.add_entity(Entity(creation))
                self.entities[creation].created_by.append(addition.id)

            self.transformations[addition.id] = addition

    def remove_transformation(self, removal: Transformation):
        """
        Remove a transformation from the topology.

        Parameters
        ----------
        removal: DataBinder.Classes.Transformation

        Returns
        -------
        None
        """

        token = removal.id
        tagged_entities = []

        # Remove connections to entities
        for entity in self.transformations[token].requires:
            self.entities[entity].required_by.remove(token)
            tagged_entities.append(entity)
        for entity in self.transformations[token].creates:
            self.entities[entity].created_by.remove(token)
            tagged_entities.append(entity)

        # Remove the transformation
        del self.transformations[token]

        # Remove entities which are not connected to any others.
        remove_list = []
        for entity in tagged_entities:
            ent_obj = self.entities[entity]
            if len(ent_obj.required_by) == 0 and len(ent_obj.created_by) == 0:
                if entity not in remove_list:
                    remove_list.append(entity)

        for ent in remove_list:
            del self.entities[ent]

    def add_constant(self, cons: Constant):
        """
        Add a constant to the topology.

        Parameters
        ----------
        cons: DataBinder.Classes.Constant

        Returns
        -------
        None
        """

        if cons.id not in self.constants:
            self.constants[cons.id] = cons
        elif self.constants[cons.id].value == 0.0:
            self.constants[cons.id].value = cons.value

    def add_input(self, inp: Input):
        """
        Add an input to the topology.

        Parameters
        ----------
        inp: DataBinder.Classes.Input

        Returns
        -------
        None
        """

        if inp.id not in self.inputs:
            for requirement in inp.requires:
                self.add_constant(Constant(requirement, 0.0))
                self.constants[requirement].required_by.append(inp.id)

            for creation in inp.creates:
                self.add_entity(Entity(creation))
                self.entities[creation].created_by.append(inp.id)

            self.inputs[inp.id] = inp

    def add_output(self, output: Output):
        """
        Add an output to the topology.

        Parameters
        ----------
        inp: DataBinder.Classes.Output

        Returns
        -------
        None
        """

        if output.id not in self.outputs:
            for requirement in output.requires:
                self.add_entity(Entity(requirement))
                self.entities[requirement].required_by.append(output.id)

            for creation in output.creates:
                self.add_constant(Constant(creation, 0.0))
                self.constants[creation].created_by.append(output.id)

            self.outputs[output.id] = output

    def get_forward_entities(self, entity: Entity) -> list[Entity]:
        """
        Find all entities that a given entity is transformed into.

        Parameters
        ----------
        Entity: DataBinder.Classes.Entity

        Returns
        -------
        forward_entities: list[Entity]
        """

        forward_entities = []

        for t in self.entities[entity.id].required_by:
            forward_entities.extend(
                [self.entities[e] for e in self.transformations[t].creates]
            )

        return forward_entities

    def get_backward_entities(self, entity: Entity):
        """
        Find all entities that contribute to creating the given entity.

        Parameters
        ----------
        Entity: DataBinder.Classes.Entity

        Returns
        -------
        backward_entities: list[Entity]
        """

        backward_entities = []

        for t in self.entities[entity.id].created_by:
            backward_entities.extend(
                [self.entities[e] for e in self.transformations[t].requires]
            )

        return backward_entities

    def get_surrounding_entities(self, entity: Entity) -> list[Entity]:
        """
        Find all of the entities surrounding the given entity (those connected
        to the same transformations as it is).

        Parameters
        ----------
        Entity: DataBinder.Classes.Entity

        Returns
        -------
        surrounding_entities: list[Entity]
        """

        surrounding_transforms = entity.associated_transformation_keys()

        surrounding_entities = []
        for t in surrounding_transforms:
            entity_keys = self.transformations[t].associated_entity_keys()
            surrounding_entities.extend([self.entities[e] for e in entity_keys])

        return surrounding_entities

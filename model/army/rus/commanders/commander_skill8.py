from model.army.basic_commander import BasicCommander


class CommanderSkill8(BasicCommander):
    """Class describes a common commander stats with CS 8 """

    presence: int = 1

    def __init__(self):
        self.name: str = "a Commander. CS 8"
        self.cost: int = 20
        self.special: set[str] = {"none"}

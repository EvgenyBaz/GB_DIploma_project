from model.army.basic_commander import BasicCommander


class CommanderSkill7(BasicCommander):
    """Class describes a common commander stats with CS 7 """

    presence: int = 1

    def __init__(self):
        self.name: str = "a Commander. CS 7"
        self.cost: int = 0
        self.special: set[str] = {"none"}

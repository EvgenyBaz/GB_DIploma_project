from model.army.basic_commander import BasicCommander


class Wurttemberg(BasicCommander):
    """Class describes commander Wurttemberg stats """

    def __init__(self):
        self.name: str = "Major General Eugene von Wurttemberg. CS 8 "
        self.cost: int = 100
        self.special: set[str] = {
            "Headsrtong. Combat attack +2 Dice"
        }

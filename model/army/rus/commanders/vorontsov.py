from model.army.basic_commander import BasicCommander


class Vorontsov(BasicCommander):
    """Class describes commander Vorontsov stats """

    def __init__(self):
        self.name: str = "Major General Mikhail Vorontsov. CS 8 "
        self.cost: int = 75
        self.special: set[str] = {
            "Combat attack +1 Dice. Decisive."
        }

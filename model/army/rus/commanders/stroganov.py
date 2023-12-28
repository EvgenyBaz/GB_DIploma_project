from model.army.basic_commander import BasicCommander


class Stroganov(BasicCommander):
    """Class describes commander Stroganov stats """
    def __init__(self):
        self.name: str = "Major General Pavel Stroganov. CS 7 "
        self.cost: int = 25
        self.special: set[str] = {
            "Combat attack +1 Dice. Decisive. Irresponsible"
        }

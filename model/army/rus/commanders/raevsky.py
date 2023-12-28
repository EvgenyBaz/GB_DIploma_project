from model.army.basic_commander import BasicCommander


class Raevsky(BasicCommander):
    """Class describes commander Raevsky stats """

    def __init__(self):
        self.name: str = "Lieutenant General  Nikolay Nikolaevitch Raevsky. CS 8"
        self.cost: int = 100
        self.special: set[str] = {
            "Combat attack +2 Dice. Inspirational."
        }

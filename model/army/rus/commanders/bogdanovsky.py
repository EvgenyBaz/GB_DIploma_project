from model.army.basic_commander import BasicCommander


class Bogdanovsky(BasicCommander):
    """Class describes commander Bogdanovsky stats """

    presence: int = 1

    def __init__(self):
        self.name: str = "Lieutenant Colonel Andrei Bogdanovsky. CS 7 "
        self.cost: int = 25
        self.special: set[str] = {
            "Combat attack +1 Dice. Aggressive, Irresponsible"
        }

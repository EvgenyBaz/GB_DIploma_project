from model.army.basic_commander import BasicCommander


class Kutaisov(BasicCommander):
    """Class describes commander Kutaisov stats """

    def __init__(self):

        self.name: str = "Major General Aleksander Ivanovich Kutaisov. CS 7 "
        self.cost: int = 150
        self.special: set[str] = {
            "Combat attack +1 Dice. Decisive. Headstrong. Aggressive. Russian batteries ignore their proximity rule."
        }

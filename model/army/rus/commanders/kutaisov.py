from model.army.basic_commander import BasicCommander


class Kutaisov(BasicCommander):
    def __init__(self):
        """Class describes commander Kutaisov stats """

        self.name: str = "Major General Aleksander Ivanovich Kutaisov. CS 7 "
        self.costL: int = 150
        self.special: set[str] = {
            "Combat attack +1 Dice. Decisive. Headstrong. Aggressive. Russian batteries ignore their proximity rule."
        }

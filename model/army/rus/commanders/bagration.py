from model.army.basic_commander import BasicCommander


class Bagration(BasicCommander):
    """Class describes commander Bagration stats """

    presence: int = 1

    def __init__(self):
        self.name: str = "General of Infantry Pyotr Ivanovich Bargation. CS 9 "
        self.cost: int = 175
        self.special: set[str] = {
            "Combat attack +2 Dice. Decisive. Inspirational. 'Lion of the army': \
Once per game a Russian unit of cavalry or infantry can re-roll a Break test results as if it were Valiant"
        }

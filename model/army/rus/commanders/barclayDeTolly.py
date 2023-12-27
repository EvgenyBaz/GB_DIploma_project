from model.army.basic_commander import BasicCommander


class BarklayDeTolly(BasicCommander):
    """Class describes commander Barklay de Tolly stats """

    presence: int = 1

    def __init__(self):
        self.name: str = "General of Infantry Mikhail Bogdanovich Barklay de Tolly. CS 8 "
        self.cost: int = 100
        self.special: set[str] = {
            "Combat attack +1 Dice. Decisive. If he fails to give an order to a unit/s \
he can continue to give one more order to a different unit on a D6 roll of 4+"
        }

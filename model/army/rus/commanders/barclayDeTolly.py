from model.army.basic_commander import BasicCommander
class BarklayDeTolly(BasicCommander):
    def __init__(self):
        self.name = "General of Infantry Mikhail Bogdanovich Barklay de Tolly. CS 8 "
        self.cost = 100
        self.special = {
            "Combat attack +1 Dice. Decisive. If he fails to give an order to a unit/s \
he can continue to give one more order to a different unit on a D6 roll of 4+"
        }
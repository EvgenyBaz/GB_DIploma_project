from model.army.basic_commander import BasicCommander
class Bogdanovsky(BasicCommander):
    def __init__(self):
        self.name = "Lieutenant Colonel Andrei Bpgfsnovsky. CS 7 "
        self.cost = 25
        self.special = {
            "Combat attack +1 Dice. Aggressive, Irresponsible"
        }
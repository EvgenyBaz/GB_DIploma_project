from model.army.basic_commander import BasicCommander
class GeneralDeDivisionCountJeanDominiqueCompans(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "General de Division Count Jean Dominique Compans. CS 8"
        self.cost = 125
        self.special = {"Combat attack +2 Dice. Aggressive. Inspirational."}
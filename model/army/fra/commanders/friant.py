from model.army.basic_commander import BasicCommander
class GeneralDeDivisionLouisFriant(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "General de Division Louis Friant. CS 9"
        self.cost = 175
        self.special = {"Combat attack +3 Dice. Decisive. Independent."}
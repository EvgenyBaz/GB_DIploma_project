from model.army.basic_commander import BasicCommander
class GeneralDeDivisionJeanGabrielMarchand(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "General de Division Jean Gabriel Marchand. CS 9"
        self.cost = 125
        self.special = {"Combat attack +2 Dice. Decisive."}
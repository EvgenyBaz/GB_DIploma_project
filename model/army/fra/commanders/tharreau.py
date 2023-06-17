from model.army.basic_commander import BasicCommander
class GeneralDeDivisionJeanVictorTharreau(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "General de Division Jean Victor Tharreau. CS 8"
        self.cost = 100
        self.special = {"Combat attack +2 Dice. Headstrong."}
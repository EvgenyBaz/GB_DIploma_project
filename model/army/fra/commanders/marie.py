from model.army.basic_commander import BasicCommander
class GeneralDeDivisionJosefMarieCountDessaix(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "General de Division Josef Marie, Count Dessaix. CS 9"
        self.cost = 100
        self.special = {"Combat attack +1 Dice. Aggressive."}
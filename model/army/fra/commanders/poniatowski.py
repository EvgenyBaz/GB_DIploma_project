from model.army.basic_commander import BasicCommander
class Poniatowski(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "Marshal Josef Antoni, Prince of Poniatowski"
        self.cost = 150
        self.special = {'Combat attack +2 Dice. Inspirational to Polish formations. SR 9'}
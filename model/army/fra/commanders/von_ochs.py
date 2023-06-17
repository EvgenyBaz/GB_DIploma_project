from model.army.basic_commander import BasicCommander
class GeneralDeDivisionAdamLudwigVonOchs(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "General de Division Adam Ludwig von Ochs. CS 7"
        self.cost = 0
        self.special = {"Combat attack +1 Dice. Irresponsible."}
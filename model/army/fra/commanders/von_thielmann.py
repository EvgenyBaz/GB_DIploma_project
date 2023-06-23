from model.army.basic_commander import BasicCommander
class JohannAfolfFreiherrVonThielmann(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "Johann Afolf, Freiherr von Thielmann"
        self.cost = 150
        self.special = {'Combat attack +3 Dice. Aggressive. Headstrong. SR 8'}
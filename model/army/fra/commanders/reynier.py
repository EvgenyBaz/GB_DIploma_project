from model.army.basic_commander import BasicCommander
class JeanLouisEbenezerReynier(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "Jean-Louis-Ebenezer Reynier"
        self.cost = 125
        self.special = {'Combat attack +2 Dice. Decisive. Aggressive. SR 8'}
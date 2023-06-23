from model.army.basic_commander import BasicCommander
class KarlPhilippFurstZuSchwarzenberg(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "Karl Philipp, Furst zu Schwarzenberg"
        self.cost = 75
        self.special = {'Combat attack +1 Dice. Decisive. Aggressive. SR 8'}
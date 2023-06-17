from model.army.basic_commander import BasicCommander
class FeldmarschalLeutnantVincenzoFedericoBlanchi(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "Feldmarschal-Leutnant Vincenzo Federico Blanchi. CS 7"
        self.cost = 75
        self.special = {"Combat attack +2 Dice. Decisive."}
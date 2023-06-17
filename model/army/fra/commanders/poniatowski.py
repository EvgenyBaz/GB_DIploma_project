from model.army.basic_commander import BasicCommander
class Poniatowski(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "Marshal Josef Antoni, Prince of Poniatowski"
        self.cost = 150
        self.special = {"add..."}
from model.army.basic_commander import BasicCommander
class CommanderSkill8(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "a Commander. CS 8"
        self.cost = 25
        self.special = {}
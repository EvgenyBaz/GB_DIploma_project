from model.army.basic_commander import BasicCommander
class CommanderSkill9(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "a Commander. CS 9"
        self.cost = 50
        self.special = {}
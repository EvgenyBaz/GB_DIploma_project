from model.army.basic_commander import BasicCommander
class CarlChristianErdmannEdlerVonLeCoq(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "Carl Christian Erdmann Edler von Le Coq"
        self.cost = 150
        self.special = {'Combat attack +2 Dice. Decisive. Inspirational. "Hero of the Army". A Saxson army with\
         Le Cog in command has D3 units that are Valiant. SR 8'}
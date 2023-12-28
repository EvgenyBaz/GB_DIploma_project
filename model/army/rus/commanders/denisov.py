from model.army.basic_commander import BasicCommander
class Denisov(BasicCommander):
    """Class describes commander Denisov stats """
    def __init__(self):
        self.name: str = "Major General Vasili Denisov. CS 8 "
        self.cost: int = 100
        self.special: set[str] = {
            "Combat attack +1 Dice. Cossack cavalry under his command can charge normally"
        }
from model.army.cavalry import Cavalry
class PolishUlan(Cavalry):
    name = "Polish Ulan"
    def __init__(self):

        self.type = "Regular Cavalry"
        self.armament = "Lance"
        self.hand_to_hand = 5
        self.shooting = 0
        self.morale = 4
        self.stamina = 2
        self.special = {
            "Lancer",
            "Marauder",
            "Small"
        }
        self.cost = 40
        self.bonus = {}
        self.bonus_cost = 0

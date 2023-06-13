from model.army.cavalry import Cavalry
class Lancer(Cavalry):
    name = "Lancer"
    def __init__(self):

        self.type = "Regular Cavalry"
        self.armament = "Lance"
        self.hand_to_hand = 7
        self.shooting = 0
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Lancer",
            "Marauder"
        }
        self.cost = 48
        self.bonus = {}
        self.bonus_cost = 0

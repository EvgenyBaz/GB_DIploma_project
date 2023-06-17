from model.army.cavalry import Cavalry
class Dragoon(Cavalry):
    name = "Dragoon"
    def __init__(self):

        self.type = "Regular Cavalry"
        self.armament = "Sabre"
        self.hand_to_hand = 8
        self.shooting = 0
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Heavy Cavalry D1"
        }
        self.cost = 44
        self.bonus = {}
        self.bonus_cost = 0

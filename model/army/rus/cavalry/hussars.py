from model.army.cavalry import *
class Hussars(Cavalry):
    name = "Hussars"
    presence = 1
    def __init__(self):

        self.type = "Regular Cavalry"
        self.armament = "Sabre"
        self.hand_to_hand = 6
        self.shooting = 0
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Lancer",
            "Marauder"
        }
        self.cost = 46
        self.bonus = {}
        self.bonus_cost = 0

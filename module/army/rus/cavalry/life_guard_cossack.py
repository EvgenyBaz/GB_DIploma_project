from module.army.cavalry import *
class LifeGuardCossack(Cavalry):

    def __init__(self):
        self.name = "Life Guard Cossack"
        self.type = "Regular Cavalry"
        self.armament = "Lance"
        self.hand_to_hand = 8
        self.shooting = 0
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Reliable",
            "Lancer",
            "Marauder"
        }
        self.cost = 54

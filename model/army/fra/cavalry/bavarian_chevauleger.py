from model.army.cavalry import Cavalry
class BavarianChevauleger(Cavalry):
    name = "Bavarian Chevauleger"
    def __init__(self):

        self.type = "Regular Cavalry"
        self.armament = "Sabre"
        self.hand_to_hand = 6
        self.shooting = 0
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Marauder"
        }
        self.cost = 41
        self.bonus = {}
        self.bonus_cost = 0

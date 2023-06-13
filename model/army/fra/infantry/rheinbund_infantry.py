from model.army.infantry import Infantry
class ReinbundInfantry(Infantry):
    name = "Reinbund Infantry"
    def __init__(self):
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 5
        self.shooting = 3
        self.morale = 5
        self.stamina = 3
        self.special = {
        }
        self.cost = 31
        self.bonus = {}
        self.bonus_cost = 0
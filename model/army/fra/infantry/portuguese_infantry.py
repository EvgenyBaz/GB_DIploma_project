from model.army.infantry import Infantry
class PortugueseInfantry(Infantry):
    name = "Portuguese Infantry"
    def __init__(self):
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 6
        self.shooting = 3
        self.morale = 4
        self.stamina = 3
        self.special = {
        }
        self.cost = 36
        self.bonus = {}
        self.bonus_cost = 0
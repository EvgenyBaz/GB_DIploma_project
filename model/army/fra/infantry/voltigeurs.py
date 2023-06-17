from model.army.infantry import Infantry
class Voltigeurs(Infantry):
    name = "Voltigeurs"
    def __init__(self):
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 6
        self.shooting = 4
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Pas de charge",
            "Light Infantry",
            "Mixed Formation",
            "Skirmisher",
            "Sharpshooter"
        }
        self.cost = 41
        self.bonus = {}
        self.bonus_cost = 0
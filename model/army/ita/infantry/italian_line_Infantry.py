from model.army.infantry import Infantry
class ItalianLineInfantry(Infantry):

    name = "Italian Line Infantry"
    def __init__(self):
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 6
        self.shooting = 3
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Pas de charge"
        }
        self.cost = 38
        self.bonus = {}
        self.bonus_cost = 0


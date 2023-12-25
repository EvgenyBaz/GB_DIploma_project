from model.army.infantry import Infantry


class Grenadier(Infantry):
    name = "Grenadier"

    def __init__(self):
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 7
        self.shooting = 3
        self.morale = 4
        self.stamina = 4
        self.special = {
            "Tough Fighter",
            "Poor",
            "Skirmisher",
            "Lacking Initiative",
            "Elite 4+"
        }
        self.cost = 48
        self.bonus = {}
        self.bonus_cost = 0

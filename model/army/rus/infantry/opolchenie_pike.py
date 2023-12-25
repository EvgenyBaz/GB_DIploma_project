from model.army.infantry import Infantry


class OpolcheniePike(Infantry):
    name = "Opolchenie with Pike"

    def __init__(self):
        self.type = "Regular Infantry"
        self.armament = "Pike"
        self.hand_to_hand = 5
        self.shooting = 0
        self.morale = 5
        self.stamina = 3
        self.special = {
            "Militia",
            "Untested",
            "Unreliable",
            "Lacking Initiative"
        }
        self.cost = 19
        self.bonus = {}
        self.bonus_cost = 0

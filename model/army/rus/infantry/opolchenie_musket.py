from model.army.infantry import Infantry


class OpolchenieMusket(Infantry):
    name = "Opolchenie with Musket"

    def __init__(self):
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 5
        self.shooting = 2
        self.morale = 5
        self.stamina = 3
        self.special = {
            "Militia",
            "Untested",
            "Unreliable",
            "Lacking Initiative"
        }
        self.cost = 23
        self.bonus = {}
        self.bonus_cost = 0

from model.army.infantry import Infantry


class OpolchenieJager(Infantry):
    name = "Opolchenie Jager"

    def __init__(self):
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket and Rifled Musket"
        self.hand_to_hand = 5
        self.shooting = 2
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Militia",
            "Poor Skirmisher",
            "Lacking Initiative"
        }
        self.cost = 30
        self.bonus = {}
        self.bonus_cost = 0

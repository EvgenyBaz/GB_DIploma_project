from model.army.infantry import Infantry


class LifeGuardJager(Infantry):
    name = "Life guard Jager"

    def __init__(self):
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 6
        self.shooting = 3
        self.morale = 3
        self.stamina = 4
        self.special = {
            "Rifle Mixed Formation",
            "Light Infantry Mixed Formation",
            "Skirmisher",
            "Reliable",
            "Elite 4+",
            "Sharpshooter"
        }
        self.cost = 59
        self.bonus = {}
        self.bonus_cost = 0

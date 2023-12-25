from model.army.infantry import Infantry


class DragoonOnFoot(Infantry):
    name = "Dragoon on foot"

    def __init__(self):
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 4
        self.shooting = 2
        self.morale = 4
        self.stamina = 2
        self.special = {
            "Skirmisher",
            "Small"
        }
        self.cost = 28
        self.bonus = {}
        self.bonus_cost = 0

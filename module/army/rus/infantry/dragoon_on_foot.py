from module.army.infantry import *
class DragoonOnFoot(Infantry):

    def __init__(self):
        self.name = "Dragoon on foot"
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

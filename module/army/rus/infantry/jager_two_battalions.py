from module.army.infantry import *
class JagerTwoBattalions(Infantry):

    def __init__(self):
        self.name = "Jager 2 battalions"
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 6
        self.shooting = 3
        self.morale = 4
        self.stamina = 4
        self.special = {
            "Rifle Mixed Formation"
            "Light Infantry"
            "Mixed Formation"
            "Tough Fighter",
            "Skirmisher",
            "Lacking Initiative"
            "Sharpshooter"
        }
        self.cost = 90

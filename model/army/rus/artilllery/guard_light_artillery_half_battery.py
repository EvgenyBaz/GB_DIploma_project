from model.army.artillery import Artillery
class GuardLightArtilleryHalfBattery(Artillery):
    name = "Guard Light Artillery Half Battery"
    def __init__(self):

        self.type = "Regular Artillery"
        self.armament = "Smoothbore Artillery"
        self.hand_to_hand = 1
        self.shooting = (3, 1, 1)
        self.morale = 3
        self.stamina = 2
        self.special = {
            "Reliable",
            "Elite 4+"
        }
        self.cost = 36
        self.bonus = {}
        self.bonus_cost = 0

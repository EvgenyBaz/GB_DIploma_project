from model.army.artillery import Artillery
class HalfFootArtilleryBattery(Artillery):
    name = "Half Foot Artillery Battery"
    def __init__(self):

        self.type = "Regular Artillery"
        self.armament = "Smoothbore Artillery"
        self.hand_to_hand = 1
        self.shooting = (2, 1, 1)
        self.morale = 4
        self.stamina = 1
        self.special = {
        }
        self.cost = 19
        self.bonus = {}
        self.bonus_cost = 0
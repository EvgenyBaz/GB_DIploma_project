from model.army.artillery import Artillery
class LightArtilleryHalfBattery(Artillery):
    name = "Light Artillery Half Battery"
    def __init__(self):

        self.type = "Regular Artilery"
        self.armament = "Smoothbore Artillery"
        self.hand_to_hand = 1
        self.shooting = (3, 1, 1)
        self.morale = 4
        self.stamina = 2
        self.special = {

        }
        self.cost = 24
        self.bonus = {}
        self.bonus_cost = 0
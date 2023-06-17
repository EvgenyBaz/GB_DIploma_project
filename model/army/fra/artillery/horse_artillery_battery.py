from model.army.artillery import Artillery
class HorseArtilleryBattery(Artillery):
    name = "Horse Artillery Battery"
    def __init__(self):

        self.type = "Regular Artillery"
        self.armament = "Smoothbore Artillery"
        self.hand_to_hand = 1
        self.shooting = (3, 2, 1)
        self.morale = 4
        self.stamina = 1
        self.special = {
            "Marauder"
        }
        self.cost = 30
        self.bonus = {}
        self.bonus_cost = 0
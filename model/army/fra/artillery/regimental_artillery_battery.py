from model.army.artillery import Artillery
class RegimentalArtilleryBattery(Artillery):
    name = "Regimental Artillery Battery"
    def __init__(self):

        self.type = "Regular Artillery"
        self.armament = "Smoothbore Battalion Artillery"
        self.hand_to_hand = 1
        self.shooting = (3, 2, 1)
        self.morale = 4
        self.stamina = 2
        self.special = {
        }
        self.cost = 19
        self.bonus = {}
        self.bonus_cost = 0
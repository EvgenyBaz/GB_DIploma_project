from model.army.artillery import Artillery
class RegimentalArtillerySection(Artillery):
    name = "Regimental Artillery Section"
    def __init__(self):

        self.type = "Regular Artillery"
        self.armament = "Smoothbore Battalion Artillery"
        self.hand_to_hand = 1
        self.shooting = (1, 1, 1)
        self.morale = 4
        self.stamina = 1
        self.special = {
        }
        self.cost = 11
        self.bonus = {}
        self.bonus_cost = 0
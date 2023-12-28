from model.army.artillery import Artillery


class LightArtilleryHalfBattery(Artillery):
    """Class describes light artillery half battery """

    name: str = "Light Artillery Half Battery"

    def __init__(self):
        self.type: str = "Regular Artilery"
        self.armament: str = "Smoothbore Artillery"
        self.hand_to_hand: int = 1
        self.shooting: tuple[int, int, int] = (3, 1, 1)
        self.morale: int = 4
        self.stamina: int = 2
        self.special: set[str] = {
            "none"
        }
        self.cost: int = 24
        self.bonus: dict = {}
        self.bonus_cost: int = 0

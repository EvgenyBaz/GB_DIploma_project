from model.army.artillery import Artillery


class HorseArtilleryHalfBattery(Artillery):
    """Class describes horse artillery half battery """

    name: str = "Horse Artillery Half Battery"

    def __init__(self):
        self.type: str = "Regular Artillery"
        self.armament: str = "Smoothbore Artillery"
        self.hand_to_hand: int = 1
        self.shooting: tuple[int, int, int] = (3, 1, 1)
        self.morale: int = 4
        self.stamina: int = 1
        self.special: set[str] = {
            "Marauder"
        }
        self.cost: int = 27
        self.bonus: dict = {}
        self.bonus_cost: int = 0

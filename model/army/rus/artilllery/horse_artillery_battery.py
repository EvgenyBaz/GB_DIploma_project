from model.army.artillery import Artillery


class HorseArtilleryBattery(Artillery):
    """Class describes horse artillery battery """

    name: str = "Horse Artillery Battery"

    def __init__(self):
        self.type: str = "Regular Artillery"
        self.armament: str = "Smoothbore Artillery"
        self.hand_to_hand: int = 2
        self.shooting: tuple[int, int, int] = (4, 2, 2)
        self.morale: int = 4
        self.stamina: int = 2
        self.special: set[str] = {
            "Marauder",
            "Large"
        }
        self.cost: int = 39
        self.bonus: dict = {}
        self.bonus_cost: int = 0

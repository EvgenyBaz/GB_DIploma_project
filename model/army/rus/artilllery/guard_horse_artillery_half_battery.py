from model.army.artillery import Artillery


class GuardHorseArtilleryHalfBattery(Artillery):
    """Class describes Guard horse artillery half battery """

    name: str = "Guard Horse Artillery Half Battery"

    def __init__(self):
        self.type: str = "Regular Artillery"
        self.armament: str = "Smoothbore Artillery"
        self.hand_to_hand: int = 1
        self.shooting: tuple[int, int, int] = (3, 1, 1)
        self.morale: int = 3
        self.stamina: int = 1
        self.special: set[str] = {
            "Marauder",
            "Reliable",
            "Elite 4+"
        }
        self.cost: int = 39
        self.bonus: dict = {}
        self.bonus_cost: int = 0

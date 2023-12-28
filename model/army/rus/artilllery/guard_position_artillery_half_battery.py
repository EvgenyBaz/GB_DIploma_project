from model.army.artillery import Artillery


class GuardPositionArtilleryHalfBattery(Artillery):
    """Class describes Guard position artillery half battery """

    name: str = "Guard Position Artillery Half Battery"

    def __init__(self):
        self.type: str = "Regular Artillery"
        self.armament: str = "Smoothbore Heavy Artillery"
        self.hand_to_hand: int = 1
        self.shooting: tuple[int, int, int] = (3, 1, 1)
        self.morale: int = 3
        self.stamina: int = 2
        self.special: set[str] = {
            "Reliable",
            "Elite 4+"
        }
        self.cost: int = 40
        self.bonus: dict = {}
        self.bonus_cost: int = 0

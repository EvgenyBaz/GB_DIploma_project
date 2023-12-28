from model.army.artillery import Artillery


class PositionArtilleryHalfBattery(Artillery):
    """Class describes position artillery half battery """

    name: str = "Position Artillery Half Battery"

    def __init__(self):
        self.type: str = "Regular Artillery"
        self.armament: str = "Smoothbore Heavy Artillery"
        self.hand_to_hand: int = 1
        self.shooting: tuple[int, int, int] = (3, 1, 1)
        self.morale: int = 4
        self.stamina: int = 2
        self.special: set[str] = {
            "none"
        }
        self.cost: int = 28
        self.bonus: dict = {}
        self.bonus_cost: int = 0

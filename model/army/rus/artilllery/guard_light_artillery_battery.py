from model.army.artillery import Artillery


class GuardLightArtilleryBattery(Artillery):
    """Class describes Guard light artillery battery """

    name: str = "Guard Light Artillery Battery"

    def __init__(self):
        self.type: str = "Regular Artillery"
        self.armament: str = "Smoothbore Artillery"
        self.hand_to_hand: int = 2
        self.shooting: tuple[int, int, int] = (4, 2, 2)
        self.morale: int = 3
        self.stamina: int = 3
        self.special: set[str] = {
            "Reliable",
            "Elite 4+",
            'Large'
        }
        self.cost: int = 48
        self.bonus: dict = {}
        self.bonus_cost: int = 0

from model.army.artillery import Artillery


class GuardPositionArtilleryBattery(Artillery):
    """Class describes Guard position artillery battery """

    name: str = "Guard Position Artillery Battery"

    def __init__(self):
        self.type: str = "Regular Artillery"
        self.armament: str = "Smoothbore Heavy Artillery"
        self.hand_to_hand: int = 2
        self.shooting: tuple[int, int, int] = (4, 2, 2)
        self.morale: int = 3
        self.stamina: int = 3
        self.special: set[str] = {
            "Reliable",
            "Elite 4+",
            "Large"
        }
        self.cost: int = 52
        self.bonus: dict = {}
        self.bonus_cost: int = 0

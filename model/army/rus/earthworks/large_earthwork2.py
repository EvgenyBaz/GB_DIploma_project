from model.army.earthworks import EarthWorks


class LargeEarthWork2(EarthWorks):
    """Class describes large earthwork with save +2 """

    name: str = "Large EarthWork save +2"

    def __init__(self):
        self.type: str = "EarthWork"
        self.armament: str = "none"
        self.hand_to_hand: int = 0
        self.shooting: int = 0
        self.morale: int = 0
        self.stamina: int = 0
        self.special: set[str] = {"save +2"}
        self.cost: int = 35
        self.bonus: dict = {}
        self.bonus_cost: int = 0

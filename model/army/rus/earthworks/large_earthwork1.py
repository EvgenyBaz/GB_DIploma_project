from model.army.earthworks import EarthWorks


class LargeEarthWork1(EarthWorks):
    """Class describes large earthwork with save +1 """

    name: str = "Large EarthWork save +1"

    def __init__(self):
        self.type: str = "EarthWork"
        self.armament: str = "none"
        self.hand_to_hand: int = 0
        self.shooting: int = 0
        self.morale: int = 0
        self.stamina: int = 0
        self.special: set[str] = {"save +1"}
        self.cost: int = 25
        self.bonus: dict = {}
        self.bonus_cost: int = 0

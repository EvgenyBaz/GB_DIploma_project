from model.army.earthworks import EarthWorks


class StandardEarthWork(EarthWorks):
    """Class describes standard earthwork """

    name: str = "Standard EarthWork"

    def __init__(self):
        self.type: str = "EarthWork"
        self.armament: str = "none"
        self.hand_to_hand: int = 0
        self.shooting: int = 0
        self.morale: int = 0
        self.stamina: int = 0
        self.special: set[str] = {"none"}
        self.cost: int = 15
        self.bonus: dict = {}
        self.bonus_cost: int = 0

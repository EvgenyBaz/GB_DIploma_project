from model.army.cavalry import Cavalry


class Cuirassier(Cavalry):
    """Class describes cuirassier regiment """

    name: str = "Cuirassier"

    def __init__(self):
        self.type: str = "Regular Cavalry"
        self.armament: str = "Sabre"
        self.hand_to_hand: int = 9
        self.shooting: int = 0
        self.morale: int = 3
        self.stamina: int = 3
        self.special: set[str] = {
            "Reliable",
            "Heavy Cavalry D3"
        }
        self.cost: int = 58
        self.bonus: dict = {}
        self.bonus_cost: int = 0

from model.army.cavalry import Cavalry


class Dragoon(Cavalry):
    """Class describes dragoon regiment """

    name: str = "Dragoon"

    def __init__(self):
        self.type: str = "Regular Cavalry"
        self.armament: str = "Sabre"
        self.hand_to_hand: int = 8
        self.shooting: int = 0
        self.morale: int = 4
        self.stamina: int = 3
        self.special: set[str] = {
            "Heavy Cavalry D1"
        }
        self.cost: int = 44
        self.bonus: dict = {}
        self.bonus_cost: int = 0

from model.army.cavalry import Cavalry


class Ulan(Cavalry):
    """Class describes ulan regiment """

    name: str = "Ulan"

    def __init__(self):
        self.type: str = "Regular Cavalry"
        self.armament: str = "Lance"
        self.hand_to_hand: int = 7
        self.shooting: int = 0
        self.morale: int = 4
        self.stamina: int = 3
        self.special: set[str] = {
            "Lancer",
            "Marauder"
        }
        self.cost: int = 48
        self.bonus: dict = {}
        self.bonus_cost: int = 0

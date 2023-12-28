from model.army.cavalry import Cavalry


class Hussars(Cavalry):
    """Class describes hussars regiment """

    name: str = "Hussars"

    def __init__(self):
        self.type: str = "Regular Cavalry"
        self.armament: str = "Lance"
        self.hand_to_hand: int = 6
        self.shooting: int = 0
        self.morale: int = 4
        self.stamina: int = 3
        self.special: set[str] = {
            "Lancer",
            "Marauder"
        }
        self.cost: int = 46
        self.bonus: dict = {}
        self.bonus_cost: int = 0

from model.army.cavalry import Cavalry


class MountedCossackRegular(Cavalry):
    """Class describes mounted cossack regiment """

    name: str = "Mounted Cossack"

    def __init__(self):
        self.type: str = "Regular Cavalry"
        self.armament: str = "Lance"
        self.hand_to_hand: int = 5
        self.shooting: int = 0
        self.morale: int = 5
        self.stamina: int = 3
        self.special: set[str] = {
            "Lancer",
            "Marauder",
            "Unreliable"
        }
        self.cost: int = 39
        self.bonus: dict = {}
        self.bonus_cost: int = 0

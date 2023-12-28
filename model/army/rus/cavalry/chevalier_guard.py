from model.army.cavalry import Cavalry


class ChevalierGuard(Cavalry):
    """Class describes chevalier guard regiment """

    name: str = "Chevalier Guard"

    def __init__(self):
        self.type: str = "Regular Cavalry"
        self.armament: str = "Sabre"
        self.hand_to_hand: int = 10
        self.shooting: int = 0
        self.morale: int = 3
        self.stamina: int = 3
        self.special: set[str] = {
            "Reliable",
            "Heavy Cavalry D3"
        }
        self.cost: int = 60
        self.bonus: dict = {}
        self.bonus_cost: int = 0

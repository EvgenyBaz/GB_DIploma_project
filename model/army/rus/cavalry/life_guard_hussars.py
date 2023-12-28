from model.army.cavalry import Cavalry


class LifeGuardHussars(Cavalry):
    """Class describes Life Guard hussars regiment """

    name: str = "Life Guard Hussars"

    def __init__(self):
        self.type: str = "Regular Cavalry"
        self.armament: str = "Sabre"
        self.hand_to_hand: int = 7
        self.shooting: int = 0
        self.morale: int = 4
        self.stamina: int = 3
        self.special: set[str] = {
            "Reliable",
            "Marauder"
        }
        self.cost: int = 47
        self.bonus: dict = {}
        self.bonus_cost: int = 0

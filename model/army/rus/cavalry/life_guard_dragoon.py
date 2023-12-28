from model.army.cavalry import Cavalry


class LifeGuardDragoon(Cavalry):
    """Class describes Life Guard dragoon regiment """

    name: str = "Life Guard Dragoon"

    def __init__(self):
        self.type: str = "Regular Cavalry"
        self.armament: str = "Sabre"
        self.hand_to_hand: int = 9
        self.shooting: int = 0
        self.morale: int = 4
        self.stamina: int = 3
        self.special: set[str] = {
            "Reliable",
            "Heavy Cavalry D1"
        }
        self.cost: int = 54
        self.bonus: dict = {}
        self.bonus_cost: int = 0

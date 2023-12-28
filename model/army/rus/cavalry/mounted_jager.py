from model.army.cavalry import Cavalry


class MountedJager(Cavalry):
    """Class describes mounted jager regiment """

    name: str = "Mounted Jager"

    def __init__(self):
        self.type: str = "Regular Cavalry"
        self.armament: str = "Sabre"
        self.hand_to_hand: int = 6
        self.shooting: int = 0
        self.morale: int = 4
        self.stamina: int = 3
        self.special: set[str] = {
            "Marauder"
        }
        self.cost: int = 41
        self.bonus: dict = {}
        self.bonus_cost: int = 0

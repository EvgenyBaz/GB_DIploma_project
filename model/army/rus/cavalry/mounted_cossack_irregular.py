from model.army.cavalry import Cavalry


class MountedCossackIrregular(Cavalry):
    """Class describes irregular mounted cossack regiment """

    name: str = "Irregular Mounted Cossack"

    def __init__(self):
        self.type: str = "Irregular Cavalry"
        self.armament: str = "Lance or Bow"
        self.hand_to_hand: int = 5
        self.shooting: int = 2
        self.morale: int = 5
        self.stamina: int = 3
        self.special: set[str] = {
            "Lancer",
            "Marauder",
            "Unreliable"
        }
        self.cost: int = 37
        self.bonus: dict = {}
        self.bonus_cost: int = 0

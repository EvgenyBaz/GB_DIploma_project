from model.army.cavalry import Cavalry


class LifeGuardCossack(Cavalry):
    """Class describes Life Guard cossack regiment """

    name: str = "Life Guard Cossack"

    def __init__(self):
        self.type: str = "Regular Cavalry"
        self.armament: str = "Lance"
        self.hand_to_hand: int = 8
        self.shooting: int = 0
        self.morale: int = 4
        self.stamina: int = 3
        self.special: set[str] = {
            "Reliable",
            "Lancer",
            "Marauder"
        }
        self.cost: int = 54
        self.bonus: dict = {}
        self.bonus_cost: int = 0

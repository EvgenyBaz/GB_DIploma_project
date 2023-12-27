from model.army.infantry import Infantry


class LifeGuardInfantry(Infantry):
    """Class describes Life Guard infantry battalion """

    name: str = "Life guard Infantry"

    def __init__(self):
        self.type: str = "Regular Infantry"
        self.armament: str = "Smoothbore Musket"
        self.hand_to_hand: int = 7
        self.shooting: int = 3
        self.morale: int = 3
        self.stamina: int = 4
        self.special: set[str] = {
            "Tough Fighter",
            "Poor Skirmisher",
            "Reliable",
            "Elite 3+",
            "Valiant"
        }
        self.cost: int = 61
        self.bonus: dict = {}
        self.bonus_cost: int = 0

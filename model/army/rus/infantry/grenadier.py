from model.army.infantry import Infantry


class Grenadier(Infantry):
    """Class describes grenadier's battalion """
    name = "Grenadier"

    def __init__(self):
        self.type: str = "Regular Infantry"
        self.armament: str = "Smoothbore Musket"
        self.hand_to_hand: int = 7
        self.shooting: int = 3
        self.morale: int = 4
        self.stamina: int = 4
        self.special: set[str] = {
            "Tough Fighter",
            "Poor",
            "Skirmisher",
            "Lacking Initiative",
            "Elite 4+"
        }
        self.cost: int = 48
        self.bonus: dict = {}
        self.bonus_cost: int = 0

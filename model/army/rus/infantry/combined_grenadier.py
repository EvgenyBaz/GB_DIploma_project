from model.army.infantry import Infantry


class CombinedGrenadier(Infantry):
    """Class describes combined grenadier battalion """

    name: str = "Combined Grenadier"

    def __init__(self):
        self.type: str = "Regular Infantry"
        self.armament: str = "Smoothbore Musket"
        self.hand_to_hand: int = 6
        self.shooting: int = 3
        self.morale: int = 4
        self.stamina: int = 4
        self.special: set[str] = {
            "Tough Fighter",
            "Poor Skirmisher",
            "Lacking Initiative"
        }
        self.cost: int = 41
        self.bonus: dict = {}
        self.bonus_cost: int = 0

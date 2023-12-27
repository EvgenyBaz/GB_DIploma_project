from model.army.infantry import Infantry


class OpolcheniePike(Infantry):
    """Class describes opolchenie with pike battalion """

    name: str = "Opolchenie with Pike"

    def __init__(self):
        self.type: str = "Regular Infantry"
        self.armament: str = "Pike"
        self.hand_to_hand: int = 5
        self.shooting: int = 0
        self.morale: int = 5
        self.stamina: int = 3
        self.special: set[str] = {
            "Militia",
            "Untested",
            "Unreliable",
            "Lacking Initiative"
        }
        self.cost: int = 19
        self.bonus: dict = {}
        self.bonus_cost: int = 0

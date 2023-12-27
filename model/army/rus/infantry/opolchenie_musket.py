from model.army.infantry import Infantry


class OpolchenieMusket(Infantry):
    """Class describes opolchenie with musket battalion """

    name: str = "Opolchenie with Musket"

    def __init__(self):
        self.type: str = "Regular Infantry"
        self.armament: str = "Smoothbore Musket"
        self.hand_to_hand: int = 5
        self.shooting: int = 2
        self.morale: int = 5
        self.stamina: int = 3
        self.special: set[str] = {
            "Militia",
            "Untested",
            "Unreliable",
            "Lacking Initiative"
        }
        self.cost: int = 23
        self.bonus: dict = {}
        self.bonus_cost: int = 0

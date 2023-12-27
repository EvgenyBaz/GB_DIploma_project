from model.army.infantry import Infantry


class OpolchenieJager(Infantry):
    """Class describes opolchenie jagger battalion """

    name: str = "Opolchenie Jager"

    def __init__(self):
        self.type: str = "Regular Infantry"
        self.armament: str = "Smoothbore Musket and Rifled Musket"
        self.hand_to_hand: int = 5
        self.shooting: int = 2
        self.morale: int = 4
        self.stamina: int = 3
        self.special: set[str] = {
            "Militia",
            "Poor Skirmisher",
            "Lacking Initiative"
        }
        self.cost: int = 30
        self.bonus: dict = {}
        self.bonus_cost: int = 0

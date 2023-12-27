from model.army.infantry import Infantry


class Jager(Infantry):
    """Class describes jager's battalion """

    name: str = "Jager"

    def __init__(self):
        self.type: str = "Regular Infantry"
        self.armament: str = "Smoothbore Musket"
        self.hand_to_hand: int = 6
        self.shooting: int = 3
        self.morale: int = 4
        self.stamina: int = 4
        self.special: set[str] = {
            "Rifle Mixed Formation",
            "Light Infantry Mixed Formation",
            "Tough Fighter",
            "Skirmisher",
            "Lacking Initiative",
            "Sharpshooter"
        }
        self.cost: int = 45
        self.bonus: dict = {}
        self.bonus_cost: int = 0

from model.army.infantry import Infantry


class LifeGuardJager(Infantry):
    """Class describes Life Guard jagger battalion """

    name: str = "Life guard Jager"

    def __init__(self):
        self.type: str = "Regular Infantry"
        self.armament: str = "Smoothbore Musket"
        self.hand_to_hand: int = 6
        self.shooting: int = 3
        self.morale: int = 3
        self.stamina: int = 4
        self.special: set[str] = {
            "Rifle Mixed Formation",
            "Light Infantry Mixed Formation",
            "Skirmisher",
            "Reliable",
            "Elite 4+",
            "Sharpshooter"
        }
        self.cost: int = 59
        self.bonus: dict = {}
        self.bonus_cost: int = 0

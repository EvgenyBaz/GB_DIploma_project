from model.army.infantry import Infantry


class VolunteerJagerRifle(Infantry):
    """Class describes volunteer jager with rifle battalion """

    name: str = "Volunteer Jager with Rifle"

    def __init__(self):
        self.type: str = "Regular Infantry"
        self.armament: str = "Rifle"
        self.hand_to_hand: int = 6
        self.shooting: int = 3
        self.morale: int = 4
        self.stamina: int = 4
        self.special: set[str] = {
            "Militia",
            "Untested",
            "Unreliable",
            "Lacking Initiative"
        }
        self.cost: int = 40
        self.bonus: dict = {}
        self.bonus_cost: int = 0

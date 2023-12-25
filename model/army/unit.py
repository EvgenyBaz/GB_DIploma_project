class Unit:
    """ Basic class for all units contains common methods for all units"""

    name = "empty"
    presence = 0

    def __init__(self):
        self.type: str = "unit"
        self.armament: str = "weapon"
        self.hand_to_hand: int = 0
        self.shooting: int = 0
        self.morale: int = 0
        self.stamina: int = 0
        self.special: set[str] = {
            "property"
        }
        self.cost: int = 0
        self.bonus: dict = {}
        self.bonus_cost: int = 0

    def get_cost_of_battalion(self) -> int:
        """ Returns the battalion cost """

        return self.cost

    def get_bonus_of_battalion(self) -> str:
        """ Returns string with battalion bonuses """

        result = "  "
        for bonus in self.bonus:
            result = result + bonus + ", "
        return result[0:-2]

    @classmethod
    def get_name_of_battalion(cls) -> str:
        """ Returns the battalion name """

        return cls.name







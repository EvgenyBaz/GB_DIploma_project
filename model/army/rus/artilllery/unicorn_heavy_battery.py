from model.army.artillery import Artillery


class UnicornHeavyBattery(Artillery):
    """Class describes unicorn heavy battery """

    name: str = "Unicorn Heavy Battery"

    def __init__(self):
        self.type: str = "Regular Artillery"
        self.armament: str = "Smoothbore Heavy Howitzer"
        self.hand_to_hand: int = 1
        self.shooting: tuple[int, int, int] = (2, 2, 2)
        self.morale: int = 4
        self.stamina: int = 2
        self.special: set[str] = {
            "20 pdr"
        }
        self.cost: int = 27
        self.bonus: dict = {}
        self.bonus_cost: int = 0

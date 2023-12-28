from model.army.artillery import Artillery


class UnicornFieldBattery(Artillery):
    """Class describes unicorn field battery """

    name: str = "Unicorn Field Battery"

    def __init__(self):
        self.type: str = "Regular Artilery"
        self.armament: str = "Smoothbore Field Howizer"
        self.hand_to_hand: int = 1
        self.shooting: tuple[int, int, int] = (2, 2, 2)
        self.morale: int = 4
        self.stamina: int = 2
        self.special: set[str] = {
            "10 pdr"
        }
        self.cost: int = 23
        self.bonus: dict = {}
        self.bonus_cost: int = 0

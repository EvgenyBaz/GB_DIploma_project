from model.army.infantry import Infantry


class DragoonOnFoot(Infantry):
    """Class describes dragoon on foot battalion """

    name: str = "Dragoon on foot"

    def __init__(self):
        self.type: str = "Regular Infantry"
        self.armament: str = "Smoothbore Musket"
        self.hand_to_hand: int = 4
        self.shooting: int = 2
        self.morale: int = 4
        self.stamina: int = 2
        self.special: set[str] = {
            "Skirmisher",
            "Small"
        }
        self.cost: int = 28
        self.bonus: dict = {}
        self.bonus_cost: int = 0

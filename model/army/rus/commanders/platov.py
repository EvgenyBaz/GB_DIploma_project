from model.army.basic_commander import BasicCommander


class Platov(BasicCommander):
    """Class describes commander Platov stats """

    def __init__(self):
        self.name: str = "General of Cavalry Matvei Platov. CS 8 "
        self.cost: int = 150
        self.special: set[str] = {
            "Combat attack +2 Dice. Your army receives an additional free Cossack cavalry. Once per game Platov can issue a Follow Me order \
a Light cavalry brigade rather than single cavalry regiment. Place Platov with a Brigade commander who is with 12\" of\
 him and then move that commander's brigade up to three moves. Then place the Brigade commander and Plato with one of\
  the units in the brigade. If the unit is in combat only Platov's additional dice are added to the combat"
        }

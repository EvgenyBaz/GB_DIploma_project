from model.army.basic_commander import BasicCommander


class Kutuzov(BasicCommander):
    """Class describes commander Kutuzov stats """

    def __init__(self):
        self.name: str = "General of Infantry Mikhail Illarionovich Golenischev-Kutuzov. CS 7 "
        self.cost: int = 75
        self.special: set[str] = {
            "Combat attack +1 Dice. 'Saviour of the Motherland': All Russian troops within 12\"\
 of Kutuzov add +1 to the dice rolled for a Break test. Kutuzov is also classed as 'Immobile' this means that once \
placed on the table top he is unable to move, unless enemy come within proximity range. If he has any enemy units \
within proximity range at the start of his turn Kutuzov may move freely. He has a Command Distance of 18\""
        }

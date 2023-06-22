from model.army.basic_commander import BasicCommander
class Murat(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "Marshal Joachim Murat, King of Naples"
        self.cost = 200
        self.special = {'Combat attack +2 Dice. Aggressive. "Well, are you going to let as be devoured by these people"\
         - one per game Murat can perform a Follow Me order to a cavalry brigade and not a single cavalry regiment.\
         Place Murat with a brigade commander who is with 12" of him and then move that commander\'s brigade up to three\
         moves. Then place the brigade commander and Murat with one of the units in the brigade. If the unit is in\
         combat only Murat\'s additional dice are added to the combat. SR 9'}
from model.army.division import Division

from model.army.ita.infantry_brigade import InfantryBrigade
from model.army.ita.cavalry_brigade import CavalryBrigade
from model.army.ita.italian_guard_brigade import ItalianGuardBrigade
from model.army.ita.all_artillery import AllArtillery

from model.army.ita.commanders.commander_skill7 import CommanderSkill7
from model.army.ita.commanders.commander_skill8 import CommanderSkill8

class ItaDivision(Division):

    def __init__(self):
        self.division_list = [
            InfantryBrigade(),              #0
            InfantryBrigade(),              #1
            InfantryBrigade(),              #2
            CavalryBrigade(),               #3
            ItalianGuardBrigade(),          #4
            AllArtillery()                  #5
        ]

        self.division_commanders_list = [
            CommanderSkill7(),
            CommanderSkill8(),
        ]




from model.army.ita.infantry_brigade import InfantryBrigade
from model.army.ita.cavalry_brigade import CavalryBrigade
from model.army.ita.italian_guard_brigade import ItalianGuardBrigade

from model.army.ita.commanders.commander_skill7 import CommanderSkill7
from model.army.ita.commanders.commander_skill8 import CommanderSkill8

class ItaDivision:

    def __init__(self):
        self.division_list = [
            InfantryBrigade(),              #0
            InfantryBrigade(),              #1
            InfantryBrigade(),              #2
            CavalryBrigade(),               #3
            ItalianGuardBrigade(),          #4
            # AllArtillery()                  #5
        ]

        self.division_commanders_list = [
            CommanderSkill7(),
            CommanderSkill8(),
        ]

    def get_list_commanders_names(self):
        division_cmndrs_names = []
        for cmndr in self.division_commanders_list:
            division_cmndrs_names.append(cmndr.get_name_of_commander())
        return division_cmndrs_names

    # по порядковому номеру в списке командиров возвращает имя
    def get_name_of_commander(self, index):
        return self.division_commanders_list[index].get_name_of_commander()
    # по порядковому номеру в списке командиров возвращает его стоимость
    def get_cost_of_commander(self, index):
        return self.division_commanders_list[index].get_cost_of_commander()

    def get_skills_of_commander(self, index):
        return self.division_commanders_list[index].get_skills_of_commander()
    def get_list_of_division(self):
        return self.division_list

    def get_brigade(self, brigade_order):
        return self.division_list[brigade_order]

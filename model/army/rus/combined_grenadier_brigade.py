from model.army.brigade import Brigade

from model.army.unit import Unit
from model.army.rus.infantry.combined_grenadier import CombinedGrenadier

from model.army.basic_commander import BasicCommander
from model.army.rus.commanders.commander_skill7 import CommanderSkill7
from model.army.rus.commanders.commander_skill8 import CommanderSkill8

class CombinedGrenadierBrigade(Brigade):

    def __init__(self):
        self.brigade_commanders_list = []
        self.brigade_commanders_list.append(BasicCommander())
        self.brigade_commanders_list.append(CommanderSkill7())
        self.brigade_commanders_list.append(CommanderSkill8())

        # список батальонов (обьектов) включенных в бригаду - по умолчанию unit - тоесть пустышка
        self.brigade_list = []
        self.brigade_list.append(Unit())  # первый батальон
        self.brigade_list.append(Unit())  # второй батальон
        self.brigade_list.append(Unit())  # третий батальон
        self.brigade_list.append(Unit())  # четвертый батальон
        self.brigade_list.append(Unit())  # пятый батальон
        self.brigade_list.append(Unit())  # шестой батальон
        self.brigade_list.append(Unit())  # седьмой батальон

        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list = []
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # второй батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # третий батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # четвертый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # пятый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # шестой батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # седьмой батальон - варианты

        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list = []
        self.brigade_bonus_list.append(["Veteran", 8])
        self.brigade_bonus_list.append(["Small", -8])

        self.brigade_bonus_battalion_correspondence = {}
        self.brigade_bonus_battalion_correspondence = \
            {"Veteran": [CombinedGrenadier.get_name_of_battalion()],
             "Small": [CombinedGrenadier.get_name_of_battalion()]
             }

    def main_battalion_list(self):
        return [
            Unit(),
            CombinedGrenadier()
        ]
from model.army.brigade import Brigade

from model.army.unit import Unit
from model.army.rus.infantry.line_Infantry import LineInfantry
from model.army.rus.infantry.combined_grenadier import CombinedGrenadier
from model.army.rus.infantry.opolchenie_pike import OpolcheniePike
from model.army.rus.infantry.opolchenie_musket import OpolchenieMusket
from model.army.rus.infantry.opolchenie_jager import OpolchenieJager
from model.army.rus.infantry.volunteer_jager_musket import VolunteerJagerMusket
from model.army.rus.infantry.volunteer_jager_rifle import VolunteerJagerRifle
from model.army.rus.infantry.jager import Jager

from model.army.basic_commander import BasicCommander
from model.army.rus.commanders.commander_skill7 import CommanderSkill7
from model.army.rus.commanders.commander_skill8 import CommanderSkill8


class InfantryBrigade(Brigade):

    def __init__(self):
        # список командиров
        self.brigade_commanders_list: list[BasicCommander] = []
        self.brigade_commanders_list.append(BasicCommander())
        self.brigade_commanders_list.append(CommanderSkill7())
        self.brigade_commanders_list.append(CommanderSkill8())

        # список батальонов (объектов) включенных в бригаду - по умолчанию unit - то есть пустышка
        self.brigade_list: list[Unit] = []
        self.brigade_list.append(Unit())  # первый батальон
        self.brigade_list.append(Unit())  # второй батальон
        self.brigade_list.append(Unit())  # третий батальон
        self.brigade_list.append(Unit())  # четвертый батальон
        self.brigade_list.append(Unit())  # дополнительный батальон
        self.brigade_list.append(Unit())  # дополнительный батальон - егеря

        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list: list[list[Unit]] = []
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # второй батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # третий батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # четвертый батальон - варианты
        self.brigade_list_battalion_list.append(
            self.additional_battalion_list())  # дополнительный батальон - варианты
        self.brigade_list_battalion_list.append(
            self.additional_jgr_battalion_list())  # дополнительный батальон ereря

        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list: list[list[str, int]] = []
        self.brigade_bonus_list.append(["Veteran", 8])
        self.brigade_bonus_list.append(["Small", -8])
        self.brigade_bonus_list.append(["Sharpshooter", 3])

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence: dict[str: list[str]] = {}
        self.brigade_bonus_battalion_correspondence = \
            {"Veteran": [LineInfantry.get_name_of_battalion(),
                         CombinedGrenadier.get_name_of_battalion(),
                         Jager.get_name_of_battalion(),
                         VolunteerJagerRifle.get_name_of_battalion(),
                         VolunteerJagerMusket.get_name_of_battalion()],
             "Small": [LineInfantry.get_name_of_battalion(),
                       CombinedGrenadier.get_name_of_battalion(),
                       Jager.get_name_of_battalion(),
                       OpolcheniePike.get_name_of_battalion(),
                       OpolchenieMusket.get_name_of_battalion(),
                       OpolchenieJager.get_name_of_battalion(),
                       VolunteerJagerRifle.get_name_of_battalion(),
                       VolunteerJagerMusket.get_name_of_battalion()],
             "Sharpshooter": [VolunteerJagerRifle.get_name_of_battalion(),
                              VolunteerJagerMusket.get_name_of_battalion()]
             }

    def main_battalion_list(self) -> list[Unit]:
        """ Returns list of core battalions in the brigade"""

        return [
            Unit(),
            LineInfantry()
        ]

    def additional_battalion_list(self) -> list[Unit]:
        """ Returns list of auxiliary battalions in the brigade"""

        return [
            Unit(),
            CombinedGrenadier(),
            OpolcheniePike(),
            OpolchenieMusket(),
            OpolchenieJager(),
            VolunteerJagerMusket(),
            VolunteerJagerRifle(),
            Jager()
        ]

    def additional_jgr_battalion_list(self) -> list[Unit]:
        """ Returns list of special auxiliary battalions in the brigade"""

        return [
            Unit(),
            Jager()
        ]

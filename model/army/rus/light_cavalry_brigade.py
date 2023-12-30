from model.army.brigade import Brigade

from model.army.unit import Unit
from model.army.rus.cavalry.dragoon import Dragoon
from model.army.rus.cavalry.hussars import Hussars
from model.army.rus.cavalry.ulan import Ulan
from model.army.rus.cavalry.mounted_cossack_regular import MountedCossackRegular
from model.army.rus.cavalry.mounted_cossack_irregular import MountedCossackIrregular
from model.army.rus.cavalry.free_cossack import FreeCossack


from model.army.basic_commander import BasicCommander
from model.army.rus.commanders.commander_skill7 import CommanderSkill7
from model.army.rus.commanders.commander_skill8 import CommanderSkill8


class LightCavalryBrigade(Brigade):
    """ class describing the composition of the light cavalry brigade.
    commanders list and battalion list"""

    def __init__(self):
        # список командиров
        self.brigade_commanders_list: list[BasicCommander] = []
        self.brigade_commanders_list.append(BasicCommander())
        self.brigade_commanders_list.append(CommanderSkill7())
        self.brigade_commanders_list.append(CommanderSkill8())

        # список батальонов (объектов) включенных в бригаду - по умолчанию unit - тоесть пустышка
        self.brigade_list: list[Unit] = []
        self.brigade_list.append(Unit())  # первый батальон
        self.brigade_list.append(Unit())  # второй батальон
        self.brigade_list.append(Unit())  # третий батальон

        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list: list[list[Unit]] = []
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # второй батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # третий батальон - варианты

        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list: list[list[str, int]] = []
        self.brigade_bonus_list.append(["Veteran", 6])
        self.brigade_bonus_list.append(["Large", 8])
        self.brigade_bonus_list.append(["Small", -8])
        self.brigade_bonus_list.append(["Large free", 0])
        self.brigade_bonus_list.append(["Small free", 0])

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence: dict[str: list[str]] = {}
        self.brigade_bonus_battalion_correspondence = \
            {"Veteran": [Dragoon.get_name_of_battalion(),
                         Hussars.get_name_of_battalion(),
                         Ulan.get_name_of_battalion()],
             "Large": [Dragoon.get_name_of_battalion(),
                       Hussars.get_name_of_battalion(),
                       Ulan.get_name_of_battalion(),
                       MountedCossackRegular.get_name_of_battalion(),
                       MountedCossackIrregular.get_name_of_battalion()],
             "Small": [Dragoon.get_name_of_battalion(),
                       Hussars.get_name_of_battalion(),
                       Ulan.get_name_of_battalion(),
                       MountedCossackRegular.get_name_of_battalion(),
                       MountedCossackIrregular.get_name_of_battalion()],
             "Large free": [FreeCossack.get_name_of_battalion()],
             "Small free": [FreeCossack.get_name_of_battalion()]
             }

    def main_battalion_list(self) -> list[Unit]:
        """

        :return: list of core battalions in the brigade
        """

        return [
            Unit(),
            Dragoon(),
            Hussars(),
            Ulan(),
            MountedCossackRegular(),
            MountedCossackIrregular(),
            FreeCossack()
        ]



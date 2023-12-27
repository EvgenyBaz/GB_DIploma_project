from model.army.brigade import Brigade

from model.army.unit import Unit
from model.army.rus.cavalry.life_guard_cuirassier import LifeGuardCuirassier
from model.army.rus.cavalry.chevalier_guard import ChevalierGuard
from model.army.rus.cavalry.life_guard_horse import LifeGuardHorse
from model.army.rus.artilllery.guard_horse_artillery_battery import GuardHorseArtilleryBattery
from model.army.rus.artilllery.guard_horse_artillery_half_battery import GuardHorseArtilleryHalfBattery

from model.army.basic_commander import BasicCommander
from model.army.rus.commanders.commander_skill7 import CommanderSkill7
from model.army.rus.commanders.commander_skill8 import CommanderSkill8


class LifeGuadHeavyCavalryBrigade(Brigade):
    """ class describing the composition of the imperial guard heavy cavalry brigade.
    commanders list and battalion list"""

    def __init__(self):
        # список командиров
        self.brigade_commanders_list: list[BasicCommander] = []
        self.brigade_commanders_list.append(BasicCommander())
        self.brigade_commanders_list.append(CommanderSkill7())
        self.brigade_commanders_list.append(CommanderSkill8())

        # список батальонов (обьектов) включенных в бригаду - по умолчанию unit - тоесть пустышка
        self.brigade_list: list[Unit] = []
        self.brigade_list.append(Unit())  # первый батальон
        self.brigade_list.append(Unit())  # второй батальон

        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list: list[list[Unit]] = []
        self.brigade_list_battalion_list.append(self.first_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # второй батальон - варианты

        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list: list[list[str, int]] = []
        self.brigade_bonus_list.append(["Large", 8])
        self.brigade_bonus_list.append(["Small", -8])

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence: dict[str: list[str]] = {}
        self.brigade_bonus_battalion_correspondence = \
            {"Large": [LifeGuardCuirassier.get_name_of_battalion(),
                       ChevalierGuard.get_name_of_battalion(),
                       LifeGuardHorse.get_name_of_battalion()],
             "Small": [LifeGuardCuirassier.get_name_of_battalion(),
                       ChevalierGuard.get_name_of_battalion(),
                       LifeGuardHorse.get_name_of_battalion()]
             }

    def main_battalion_list(self) -> list[Unit]:
        """ Returns list of core battalions in the brigade"""

        return [
            Unit(),
            LifeGuardCuirassier(),
            ChevalierGuard(),
            LifeGuardHorse(),
            GuardHorseArtilleryBattery(),
            GuardHorseArtilleryHalfBattery()
        ]

    def first_battalion_list(self) -> list[Unit]:
        """ Returns list of battalions at first place in the brigade"""

        return [
            Unit(),
            LifeGuardCuirassier(),
            ChevalierGuard(),
            LifeGuardHorse()
        ]

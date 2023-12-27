from model.army.brigade import Brigade
from model.army.basic_commander import BasicCommander

from model.army.unit import Unit
from model.army.rus.earthworks.standard_earthwork import StandardEarthWork
from model.army.rus.earthworks.large_earthwork1 import LargeEarthWork1
from model.army.rus.earthworks.large_earthwork2 import LargeEarthWork2


class EarthWorks(Brigade):
    """ class describing the composition of earth works"""

    def __init__(self):
        # список командиров
        self.brigade_commanders_list: list[BasicCommander] = []

        # список батальонов (обьектов) включенных в бригаду - по умолчанию unit - тоесть пустышка
        self.brigade_list: list[Unit] = []
        self.brigade_list.append(Unit())  # первое укрепление
        self.brigade_list.append(Unit())  # второе укрепление

        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list: list[list[Unit]] = []
        self.brigade_list_battalion_list.append(self.earth_works_list())  # первое укрепление - варианты     0
        self.brigade_list_battalion_list.append(self.earth_works_list())  # второе укрепление - варианты     1

        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list: list[list[str, int]] = []

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence: dict[str: list[str]] = {}

    def earth_works_list(self) -> list[Unit]:
        """ Returns list of earthworks in the brigade"""

        return [
            Unit(),
            StandardEarthWork(),
            LargeEarthWork1(),
            LargeEarthWork2(),
        ]

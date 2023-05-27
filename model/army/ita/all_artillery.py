from model.army.brigade import Brigade

from model.army.unit import Unit
from model.army.ita.artillery.foot_artillery_battery import FootArtilleryBattery
from model.army.ita.artillery.half_foot_artillery_battery import HalfFootArtilleryBattery
from model.army.ita.artillery.horse_artillery_battery import HorseArtilleryBattery
from model.army.ita.artillery.half_horse_artillery_battery import HalfHorseArtilleryBattery
from model.army.ita.artillery.heavy_foot_artillery_battery import HeavyFootArtilleryBattery
from model.army.ita.artillery.half_heavy_foot_artillery_battery import HalfHeavyFootArtilleryBattery

class AllArtillery(Brigade):

    def __init__(self):
        # список командиров
        self.brigade_commanders_list = []

        # список батальонов (обьектов) включенных в бригаду - по умолчанию unit - то есть пустышка
        self.brigade_list = []
        self.brigade_list.append(Unit())  # первая пешей артиллерии
        self.brigade_list.append(Unit())  # вторая пешей артиллерии
        self.brigade_list.append(Unit())  # третья пешей артиллерии
        self.brigade_list.append(Unit())  # первая конная рота
        self.brigade_list.append(Unit())  # вторая конная рота
        self.brigade_list.append(Unit())  # третья конная рота
        self.brigade_list.append(Unit())  # первая тяжелая рота
        self.brigade_list.append(Unit())  # вторая тяжелая рота
        self.brigade_list.append(Unit())  # третья тяжелая рота


        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list = []
        self.brigade_list_battalion_list.append(self.foot_battery_list())  # первая легкая рота - варианты     0
        self.brigade_list_battalion_list.append(self.foot_battery_list())  # вторая легкая рота - варианты     1
        self.brigade_list_battalion_list.append(self.foot_battery_list())  # третья легкая рота - варианты     2
        self.brigade_list_battalion_list.append(self.horse_battery_list())  # первая конная рота               3
        self.brigade_list_battalion_list.append(self.horse_battery_list())  # вторая конная рота               4
        self.brigade_list_battalion_list.append(self.horse_battery_list())  # третья конная рота               5
        self.brigade_list_battalion_list.append(self.heavy_battery_list())  # первая тяжелая рота              6
        self.brigade_list_battalion_list.append(self.heavy_battery_list())  # вторая тяжелая рота              7
        self.brigade_list_battalion_list.append(self.heavy_battery_list())  # третья тяжелая рота              8



        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list = []
        self.brigade_bonus_list.append(["Veteran", 8])

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence = \
        {"Veteran": [FootArtilleryBattery.get_name_of_battalion(),
                                HalfFootArtilleryBattery.get_name_of_battalion(),
                                HorseArtilleryBattery.get_name_of_battalion(),
                                HalfHorseArtilleryBattery.get_name_of_battalion(),
                                HeavyFootArtilleryBattery.get_name_of_battalion(),
                                HalfHeavyFootArtilleryBattery.get_name_of_battalion()]
         }

    def foot_battery_list(self):
        return [
            Unit(),
            FootArtilleryBattery(),
            HalfFootArtilleryBattery()
        ]


    def horse_battery_list(self):
        return [
            Unit(),
            HorseArtilleryBattery(),
            HalfHorseArtilleryBattery()
        ]

    def heavy_battery_list(self):
        return [
            Unit(),
            HeavyFootArtilleryBattery(),
            HalfHeavyFootArtilleryBattery()
        ]

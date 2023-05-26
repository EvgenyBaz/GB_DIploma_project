from model.army.brigade import Brigade

from model.army.unit import Unit
from model.army.ita.infantry.royal_guard_grenadier import RoyalGuardGrenadier
from model.army.ita.infantry.chasseurs import Chasseurs
from model.army.ita.infantry.italian_royal_velite_infantry import ItalianRoyalVeliteInfantry
from model.army.ita.infantry.italian_guard_conscripts import ItalianGuardsConscripts

from model.army.ita.cavalry.italian_guard_dragoons import ItalianGuardDragoons

from model.army.ita.artillery.regimental_artillery_section import RegimentalArtillerySection
from model.army.ita.artillery.regimental_artillery_battery import RegimentalArtilleryBattery
from model.army.ita.artillery.foot_artillery_battery import FootArtilleryBattery
from model.army.ita.artillery.half_foot_artillery_battery import HalfFootArtilleryBattery
from model.army.ita.artillery.horse_artillery_battery import HorseArtilleryBattery
from model.army.ita.artillery.half_horse_artillery_battery import HalfHorseArtilleryBattery


from model.army.basic_commander import BasicCommander
from model.army.ita.commanders.commander_skill7 import CommanderSkill7
from model.army.ita.commanders.commander_skill8 import CommanderSkill8

class ItalianGuardBrigade(Brigade):

    def __init__(self):
        # список командиров
        self.brigade_commanders_list = []
        self.brigade_commanders_list.append(BasicCommander())
        self.brigade_commanders_list.append(CommanderSkill7())
        self.brigade_commanders_list.append(CommanderSkill8())

        # список батальонов (обьектов) включенных в бригаду - по умолчанию unit - тоесть пустышка
        self.brigade_list = []
        # Guard Infantry
        self.brigade_list.append(Unit())  # первый батальон
        self.brigade_list.append(Unit())  # второй батальон
        # Royal Velite Infantry
        self.brigade_list.append(Unit())  # третий батальон
        self.brigade_list.append(Unit())  # четвертый батальон
        # Conscript Infantry
        self.brigade_list.append(Unit())  # пятый батальон
        self.brigade_list.append(Unit())  # шестой батальон
        # Artillery
        self.brigade_list.append(Unit())  # дополнительная рота полковой артиллерии
        self.brigade_list.append(Unit())  # дополнительная рота полковой артиллерии
        self.brigade_list.append(Unit())  # дополнительная рота полковой артиллерии
        # Dragoon
        self.brigade_list.append(Unit())  # дополнительная полк драгун
        self.brigade_list.append(Unit())  # дополнительная полк драгун
        # Artillery
        self.brigade_list.append(Unit())  # дополнительная рота легкой артиллерии
        self.brigade_list.append(Unit())  # дополнительная рота легкой артиллерии
        # Horse Artillery
        self.brigade_list.append(Unit())  # дополнительная рота конной артиллерии
        self.brigade_list.append(Unit())  # дополнительная рота конной артиллерии


        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list = []
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # второй батальон - варианты
        self.brigade_list_battalion_list.append(self.velite_battalion_list())  # третий батальон - варианты
        self.brigade_list_battalion_list.append(self.velite_battalion_list())  # четвертый батальон - варианты
        self.brigade_list_battalion_list.append(self.conscript_battalion_list())  # пятый батальон - варианты
        self.brigade_list_battalion_list.append(self.conscript_battalion_list())  # шестой батальон - варианты
        self.brigade_list_battalion_list.append(self.additional_regimental_artillery_list())  # дополнительная полковая арт рота - варианты
        self.brigade_list_battalion_list.append(self.additional_regimental_artillery_list())  # дополнительная полковая арт рота - варианты
        self.brigade_list_battalion_list.append(self.additional_regimental_artillery_list())  # дополнительная полковая арт рота - варианты
        self.brigade_list_battalion_list.append(self.additional_cavalry_list())  # дополнительный полк кавалерии - варианты
        self.brigade_list_battalion_list.append(self.additional_cavalry_list())  # дополнительный полк кавалерии
        self.brigade_list_battalion_list.append(self.additional_foot_artillery_list())  # дополнительная легкая арт рота - варианты
        self.brigade_list_battalion_list.append(self.additional_foot_artillery_list())  # дополнительная легкая арт рота - варианты
        self.brigade_list_battalion_list.append(self.additional_horse_artillery_list())  # дополнительная конная арт рота - варианты
        self.brigade_list_battalion_list.append(self.additional_horse_artillery_list())  # дополнительная конная арт рота - варианты



        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list = []
        self.brigade_bonus_list.append(["Tough Fighters", 1])
        self.brigade_bonus_list.append(["Small", -8])

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence = {}
        self.brigade_bonus_battalion_correspondence = \
            {"Tough Fighters": [RoyalGuardGrenadier.get_name_of_battalion(),
                                Chasseurs.get_name_of_battalion(),
                                ItalianRoyalVeliteInfantry.get_name_of_battalion(),
                                ItalianGuardsConscripts.get_name_of_battalion()],
             "Small": [RoyalGuardGrenadier.get_name_of_battalion(),
                       Chasseurs.get_name_of_battalion(),
                       ItalianRoyalVeliteInfantry.get_name_of_battalion(),
                       ItalianGuardsConscripts.get_name_of_battalion(),
                       ItalianGuardDragoons.get_name_of_battalion()]
             }

    def main_battalion_list(self):
        return [
            Unit(),
            RoyalGuardGrenadier(),
            Chasseurs()
        ]
    def velite_battalion_list(self):
        return [
            Unit(),
            ItalianRoyalVeliteInfantry()
        ]

    def conscript_battalion_list(self):
        return [
            Unit(),
            ItalianGuardsConscripts()
        ]
    def additional_cavalry_list(self):
        return [
            Unit(),
            ItalianGuardDragoons()
        ]

    def additional_regimental_artillery_list(self):
        return [
            Unit(),
            RegimentalArtillerySection(),
            RegimentalArtilleryBattery()
        ]

    def additional_foot_artillery_list(self):
        return [
            Unit(),
            FootArtilleryBattery(),
            HalfFootArtilleryBattery()
        ]

    def additional_horse_artillery_list(self):
        return [
            Unit(),
            HorseArtilleryBattery(),
            HalfHorseArtilleryBattery()
        ]
from model.army.brigade import Brigade

from model.army.unit import Unit
from model.army.ita.infantry.italian_line_Infantry import ItalianLineInfantry
from model.army.ita.infantry.italian_light_Infantry import ItalianLightInfantry
from model.army.ita.artillery.regimental_artillery_section import RegimentalArtillerySection
from model.army.ita.artillery.regimental_artillery_battery import RegimentalArtilleryBattery


from model.army.basic_commander import BasicCommander
from model.army.ita.commanders.commander_skill7 import CommanderSkill7
from model.army.ita.commanders.commander_skill8 import CommanderSkill8


class InfantryBrigade(Brigade):

    def __init__(self):
        # список командиров
        self.brigade_commanders_list = []
        self.brigade_commanders_list.append(BasicCommander())
        self.brigade_commanders_list.append(CommanderSkill7())
        self.brigade_commanders_list.append(CommanderSkill8())

        # список батальонов (обьектов) включенных в бригаду - по умолчанию unit - тоесть пустышка
        self.brigade_list = []
        # первый полк
        self.brigade_list.append(Unit())  # первый батальон
        self.brigade_list.append(Unit())  # второй батальон
        self.brigade_list.append(Unit())  # третий батальон
        self.brigade_list.append(Unit())  # четвертый батальон
        # второй полк
        self.brigade_list.append(Unit())  # первый батальон
        self.brigade_list.append(Unit())  # второй батальон
        self.brigade_list.append(Unit())  # третий батальон
        self.brigade_list.append(Unit())  # четвертый батальон

        self.brigade_list.append(Unit())  # дополнительный батальон 1 полка
        self.brigade_list.append(Unit())  # дополнительный батальон 2 полка

# первый полк
        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list = []
        self.brigade_list_battalion_list.append(self.line_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.line_battalion_list())  # второй батальон - варианты
        self.brigade_list_battalion_list.append(self.line_battalion_list())  # третий батальон - варианты
        self.brigade_list_battalion_list.append(self.line_battalion_list())  # четвертый батальон - варианты
        # второй полк
        self.brigade_list_battalion_list.append(self.line_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.line_battalion_list())  # второй батальон - варианты
        self.brigade_list_battalion_list.append(self.line_battalion_list())  # третий батальон - варианты
        self.brigade_list_battalion_list.append(self.line_battalion_list())  # четвертый батальон - варианты

        self.brigade_list_battalion_list.append(self.additional_battalion_list()) # дополнительная арт рота 1 полка
        self.brigade_list_battalion_list.append(self.additional_battalion_list()) # дополнительная арт рота 2 полка

# альтернатива # первый полк
        self.brigade_list_battalion_list.append(self.light_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.light_battalion_list())  # второй батальон - варианты
        self.brigade_list_battalion_list.append(self.light_battalion_list())  # третий батальон - варианты
        self.brigade_list_battalion_list.append(self.light_battalion_list())  # четвертый батальон - варианты
# альтернатива # второй полк
        self.brigade_list_battalion_list.append(self.light_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.light_battalion_list())  # второй батальон - варианты
        self.brigade_list_battalion_list.append(self.light_battalion_list())  # третий батальон - варианты
        self.brigade_list_battalion_list.append(self.light_battalion_list())  # четвертый батальон - варианты

        # self.brigade_list_battalion_list.append(self.additional_battalion_list())  # дополнительный батальон - варианты


        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list = []
        self.brigade_bonus_list.append(["Reliable, Elite 5+", 8])
        self.brigade_bonus_list.append(["Tough Fighters", 1])
        self.brigade_bonus_list.append(["Small", -8])
        self.brigade_bonus_list.append(["Wavering", -6])
        self.brigade_bonus_list.append(["Morale 5", -4])
        self.brigade_bonus_list.append(["Unreliable", -3])
        self.brigade_bonus_list.append(["remove Pas de Charge", -2])

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence = {}
        self.brigade_bonus_battalion_correspondence = \
            {"Reliable, Elite 5+": [ItalianLineInfantry.get_name_of_battalion(),
                         ItalianLightInfantry.get_name_of_battalion()],
             "Tough Fighters":  [ItalianLineInfantry.get_name_of_battalion(),
                         ItalianLightInfantry.get_name_of_battalion()],
             "Small": [ItalianLineInfantry.get_name_of_battalion(),
                         ItalianLightInfantry.get_name_of_battalion()],
             "Wavering": [ItalianLineInfantry.get_name_of_battalion(),
                         ItalianLightInfantry.get_name_of_battalion()],
             "Morale 5": [ItalianLineInfantry.get_name_of_battalion(),
                         ItalianLightInfantry.get_name_of_battalion()],
             "Unreliable": [ItalianLineInfantry.get_name_of_battalion(),
                         ItalianLightInfantry.get_name_of_battalion()],
             "remove Pas de Charge": [ItalianLineInfantry.get_name_of_battalion(),
                         ItalianLightInfantry.get_name_of_battalion()],

             }


    def line_battalion_list(self):
        return [
            Unit(),
            ItalianLineInfantry()
        ]

    def light_battalion_list(self):
        return [
            Unit(),
            ItalianLightInfantry()
        ]

    def additional_battalion_list(self):
        return [
            Unit(),
            RegimentalArtillerySection(),
            RegimentalArtilleryBattery()
        ]



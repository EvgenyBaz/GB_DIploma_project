from model.army.unit import Unit

from model.army.rus.rus_division import RusDivision
from model.army.ita.ita_division import ItaDivision


class Presenter:
    """ Class generating list of division in dependence of use choose 'country: str'.
    It serves to transfer requests from GUI to MODEL block and returns data from MODEL to GUI"""

    def __init__(self, country: str):
        # производим выбор структуры и наполнения дивизии в зависимости от выбранной страны
        match country:
            case "Rus":
                self.division = RusDivision()
            case "Ita":
                self.division = ItaDivision()

    # запрос на текущий состав бригады
    def BrigadeCurrentList(self, brigade_number: int) -> list[Unit]:
        """
        :param brigade_number: rigade number in th division list
        :return: brigade number in the list of the division and returns list of battalions (Units) for current brigade """

        return self.division.get_brigade(brigade_number).brigade_list

    # запрос на список имен батальонов доступных для выбора для данной позиции в бригаде
    def BrigadeBttlnList(self, order_number: int, brigade_number: int) -> list[str]:
        """
        :param order_number: battalion number in the brigade list
        :param brigade_number: brigade number in th division list
        and returns list of battalions names available for choose for current place it chosen brigade """

        return self.division.get_brigade(brigade_number).get_list_battalion_names(order_number)

    def FirstBttlnListChange(self, order_number: int, brigade_number: int):
        """
        :param order_number: battalion number in the brigade list
        :param brigade_number: brigade number in th division list
        set normal order of available for chose battalions for chosen place in the brigade battalion list (returns Unit
        object at first place in the list)
        """

        self.division.get_brigade(brigade_number).set_common_list_of_battalions(order_number)

    def FirstBttlnListChangeToShow(self, order_number: int, brigade_number: int):
        """
        :param order_number: battalion number in the brigade list
        :param brigade_number: brigade number in th division list

        exclude first object (Unit) from normal order of available for chose battalions for chosen place in the brigade
        battalion list
        # """

        self.division.get_brigade(brigade_number).set_list_of_battalions(order_number)

    # отправляет данные в модель для заполнения списка бригады
    def BrigadeBttlnChoosen(self, order_number: int, bttln_choosen_from_list: int, brigade_number: int, shift: int = 0):

        """
        :param order_number: battalion number in the brigade list
        :param bttln_choosen_from_list: battalion number taken from GUI
        :param brigade_number brigade number in the division list
        :param shift: number of shift battalion number in the brigade list (for brigades with ambiguous chose of battalions)
        :return: set battalion chosen in GUI ti its place in the brigade battalions list
        """
        self.division.get_brigade(brigade_number).set_battalion_to_list(order_number, bttln_choosen_from_list, shift)

    # запрос на стоимость текущего батальона
    def BrigadeBttlnCost(self, order_number: int, brigade_number: int) -> int:
        """

        :param order_number: battalion number in the brigade list
        :param brigade_number: brigade number in the division list
        :return: cost of chosen battalion together with selected bonuses
        """

        return self.division.get_brigade(brigade_number).get_cost_of_battalion(order_number)

    def BrigadeBttlnSpecials(self, order_number: int, brigade_number: int) -> str:
        """

        :param order_number: battalion number in the brigade list
        :param brigade_number: brigade number in the division list
        :return: string with current battalion bonuses
        """

        return self.division.get_brigade(brigade_number).get_bonus_of_battalion(order_number)

    # запрос имени текущего батальона
    def BrigadeBttlnName(self, order_number: int, brigade_number: int) -> str:
        """

        :param order_number: battalion number in the brigade list
        :param brigade_number: brigade number in the division list
        :return: chosen battalion name
        """

        return self.division.get_brigade(brigade_number).get_name_of_battalion(order_number)

    def BrigadeBttlnPresence(self, order_number: int, brigade_number: int) -> int:
        """

        :param order_number: battalion number in the brigade list
        :param brigade_number: brigade number in the division list
        :return: battalion presence flag (1 - yes, exist, 0 - no)
        """

        return self.division.get_brigade(brigade_number).get_presence_of_battalion(order_number)

    # запрос на присутствие или отсутствие командира бригады
    def BrigadeCmndrsPresence(self, order_number: int, brigade_number: int) -> int:
        """

        :param order_number: commander number in the brigade commander list
        :param brigade_number: brigade number in the division list
        :return: commander presence flag (1 - yes, exist, 0 - no)
        """

        return self.division.get_brigade(brigade_number).get_presence_of_commander(order_number)

    # запрос на список бонусов для бригады
    def BrigadeBonusNameList(self, brigade_number: int) -> list[str]:
        """

        :param brigade_number: brigade number in the division list
        :return: list of chosen battalion bonuses names
        """

        return self.division.get_brigade(brigade_number).get_brigade_bonus_list_names()

    # запрос на список стоимости бонусов для бригады
    def BrigadeBonusCostList(self, brigade_number: int) -> list[int]:
        """

        :param brigade_number: brigade number in the division list
        :return: list of chosen battalion bonus cost
        """

        return self.division.get_brigade(brigade_number).get_brigade_bonus_list_costs()

    # запрос стоимости бонуса для бригады
    def BrigadeBonusCost(self, brigade_number: int, bonus_name: str) -> int:
        """

        :param brigade_number: brigade number in the division list
        :param bonus_name: bonus name
        :return: corresponding bonus cost
        """

        return self.division.get_brigade(brigade_number).get_brigade_bonus_costs(bonus_name)

    def BrigadeBonusToBattalion(self, bonus_name: str, brigade_number: int) -> list[str]:
        """

        :param bonus_name: bonus name
        :param brigade_number: brigade number in the division list
        :return: corresponding to bonus list of battalions names
        """

        return self.division.get_brigade(brigade_number).get_brigade_bonus_to_battalion_list(bonus_name)

    # отправляем добавление бонуса к батальону
    def BrigadeBttlnBonusAdd(self, bonus: str, order_number: int, brigade_number: int):
        """

        :param bonus: bonus name
        :param order_number: battalion number in the brigade list
        :param brigade_number: brigade number in the division list
        :return: add chosen bonus to the battalion bonus list
        """
        self.division.get_brigade(brigade_number).set_battalion_bonus(bonus, order_number)

    def BrigadeBttlnListBonusAdd(self, bonus: str, place_number: int, order_number: int, brigade_number: int):
        """

        :param bonus: bonus name
        :param place_number: battalion number in the list of available battalions
        :param order_number: battalion number in the brigade list
        :param brigade_number: brigade number in the division list
        :return: add chosen bonus to list of current battalion bonuses. Using for load data process
        """

        self.division.get_brigade(brigade_number).set_battalion_bonus_in_br_lists(bonus, place_number, order_number)

    # отправляем удаление бонуса у батальона
    def BrigadeBttlnBonusDel(self, bonus: str, order_number: int, brigade_number: int):
        """

        :param bonus: bonus name
        :param order_number: battalion number in the brigade list
        :param brigade_number: brigade number in the division list
        :return: delete chosen bonus from list of battalion bonuses
        """

        self.division.get_brigade(brigade_number).del_battalion_bonus(bonus, order_number)

    # отправляем стоимость бонуса для батальона
    def BrigadeBttlnBonusCostAdd(self, bonus_cost: int, order_number: int, brigade_number: int):
        """

        :param bonus_cost: bonus cost
        :param order_number: battalion number in the brigade list
        :param brigade_number: brigade number in the division list
        :return: Add cost of added bonus to the battalion bonus cost
        """

        self.division.get_brigade(brigade_number).add_bonus_cost_to_battalion(bonus_cost, order_number)

    def BrigadeBttlnListBonusCostAdd(self, bonus_cost: int, place_number: int, order_number: int, brigade_number: int):
        """

        :param bonus_cost: bonus cost
        :param place_number: place_number: battalion number in the list of available battalions
        :param order_number: battalion number in the brigade list
        :param brigade_number: brigade number in the division list
        :return: Add cost of added bonus to the battalion bonus cost. Using for load data process
        """

        self.division.get_brigade(brigade_number).add_bonus_cost_to_battalionin_br_lists(bonus_cost, place_number,
                                                                                         order_number)

    # запрашиваем список бонусов батальона
    def BrigadeBttlnBonusList(self, order_number: int, brigade_number: int) -> dict:
        """

        :param order_number: battalion number in the brigade list
        :param brigade_number: brigade number in the division list
        :return: list of bonuses (Dict) for chosen battalion
        """

        return self.division.get_brigade(brigade_number).get_bonus_list(order_number)

    # запрашивает список имен командиров
    def BrigadeCmndrsNamesList(self, brigade_number: int) -> list[str]:
        """

        :param brigade_number: brigade number in the division list
        :return: brigade commanders names list
        """

        return self.division.get_brigade(brigade_number).get_list_commanders_names()

    # запрашивает стоимость выбранного командира бригады
    def BrigadeCmndrsName(self, index: int, brigade_number: int) -> str:
        """

        :param index: chosen commander index in the commanders list:
        :param brigade_number: brigade number in the division list
        :return: brigade commander name
        """

        return self.division.get_brigade(brigade_number).get_name_of_commander(index)

    # запрашивает стоимость выбранного командира бригады
    def BrigadeCmndrsCost(self, index: int, brigade_number: int) -> int:
        """

        :param index: chosen commander index in the commanders list:
        :param brigade_number: brigade number in the division list
        :return: brigade commander cost
        """

        return self.division.get_brigade(brigade_number).get_costs_of_commander(index)

    # запрашивает список имен командиров для дивизии
    def DivisionCmndrsNamesList(self) -> list[str]:
        """

        :return: list of division commanders names
        """

        return self.division.get_list_commanders_names()

    # запрашивает имя выбранного командира
    def DivisionCmndrName(self, index: int) -> str:
        """

        :param index: chosen commander index in the commanders list:
        :return: the division commander name
        """

        return self.division.get_name_of_commander(index)

    # запрашивает стоимость выбранного командира
    def DivisionCmndrCost(self, index: int) -> int:
        """

        :param index: chosen commander index in the commanders list:
        :return: the division commander cost
        """

        return self.division.get_cost_of_commander(index)

    # запрашивает навыки командира дивизии
    def DivisionCmndrSkills(self, index: int) -> str:
        """

        :param index: chosen commander index in the commanders list:
        :return: commander's skills as string
        """

        return self.division.get_skills_of_commander(index)

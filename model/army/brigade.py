from model.army.unit import Unit
from model.army.basic_commander import BasicCommander


class Brigade:
    """ Basic class for all brigades. It contains common methods for all brigades"""

    def __init__(self):
        # список командиров
        self.brigade_commanders_list: list[BasicCommander] = []

        # список батальонов (объектов) включенных в бригаду
        self.brigade_list: list[Unit] = []

        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list: list[list[Unit]] = []

        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list: list[list[str, int]] = []

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence: dict[str: list[str]] = {}

    def get_brigade_bonus_to_battalion_list(self, bonus_name: str) -> list[str]:
        """

        :param bonus_name: name of bonus
        :return: corresponding list of battalions names
        """

        return self.brigade_bonus_battalion_correspondence[bonus_name]

    def get_brigade_bonus_list_names(self) -> list[str]:
        """

        :return: list of battalions bonus names "
        """

        bonus_names_list: list[str] = []
        for i in range(len(self.brigade_bonus_list)):
            bonus_names_list.append(self.brigade_bonus_list[i][0])
        return bonus_names_list

    def get_brigade_bonus_list_costs(self) -> list[int]:
        """

        :return: list of battalions bonus costs
        """

        bonus_cost_list: list[int] = []
        for i in range(len(self.brigade_bonus_list)):
            # print("test:", self.brigade_bonus_list[i][1])
            bonus_cost_list.append(self.brigade_bonus_list[i][1])  # автопроверка дурит, второе значение в списке int
        return bonus_cost_list

    def get_brigade_bonus_costs(self, bonus_name: str) -> int:
        """

        :param bonus_name: bonus name
        :return: corresponding bonus cost
        """

        bonus_cost: int = 0
        for i in range(len(self.brigade_bonus_list)):
            if bonus_name == self.brigade_bonus_list[i][0]:
                bonus_cost = self.brigade_bonus_list[i][1]  # автопроверка дурит, второе значение в списке int

        return bonus_cost

    def get_list_commanders_names(self) -> list[str]:
        """

        :return: brigade commander names list
        """

        brigade_cmndrs_names: list[str] = []
        for cmndr in self.brigade_commanders_list:
            brigade_cmndrs_names.append(cmndr.get_name_of_commander())
        return brigade_cmndrs_names

    def get_name_of_commander(self, index: int) -> str:
        """

        :param index: commander list index:
        :return: brigade commander name
        """

        return self.brigade_commanders_list[index].get_name_of_commander()

    # по порядковому номеру в списке командиров возвращает его стоимость
    def get_costs_of_commander(self, index: int) -> int:
        """

        :param index: commander list index:
        :return: brigade commander cost
        """

        return self.brigade_commanders_list[index].get_cost_of_commander()

    def main_battalion_list(self) -> list[Unit]:
        """

        :return: list of core battalions in the brigade
        """

        return []

    def additional_battalion_list(self) -> list[Unit]:
        """

        :return: list of auxiliary battalions in the brigade
        """

        return []

    # создает список имен батальонов в зависимости от порядкового номера батальона в бригаде
    def get_list_battalion_names(self, order_number: int) -> list[str]:
        """

        :param order_number: battalion order number in the brigade
        :return: ist available for choosing battalion names for current order number
        """

        brigade_bttln_list_names: list[str] = []

        for bttln in self.brigade_list_battalion_list[order_number]:
            brigade_bttln_list_names.append(bttln.name)
        return brigade_bttln_list_names

    # помещает выбранный в интерфейсе батальон (объект) в список бригады на позицию соответствующую кнопке
    def set_battalion_to_list(self, order_number: int, bttln_choosen_from_list: int, shift: int):
        """

        :param order_number: battalion order number in the brigade
        :param bttln_choosen_from_list: number of chosen battalion from the list
        :param shift: parameter of shift battalion number in the list in the brigade battalion ( default = 0)
        :return:  Places chosen battalion in the current brigade battalion list for corresponding place
        """

        self.brigade_list[order_number] = self.brigade_list_battalion_list[order_number + shift][
            bttln_choosen_from_list]

    def get_cost_of_battalion(self, order_number: int) -> int:
        """

        :param order_number: battalion order number in the brigade
        :return: battalion total cost (basic + bonuses)
        """

        return self.brigade_list[order_number].cost + self.brigade_list[order_number].bonus_cost

    def get_name_of_battalion(self, order_number: int) -> str:
        """

        :param order_number: battalion order number in the brigade
        :return: battalion name
        """

        return self.brigade_list[order_number].name

    def get_bonus_of_battalion(self, order_number: int) -> str:
        """

        :param order_number: battalion order number in the brigade
        :return: string with current battalion bonuses
        """

        return self.brigade_list[order_number].get_bonus_of_battalion()

    def get_presence_of_battalion(self, order_number: int) -> int:
        """

        :param order_number: battalion order number in the brigade
        :return: battalion presence (1 - yes, chosen; 0 - no )
        """

        return self.brigade_list[order_number].presence

    def get_presence_of_commander(self, order_number: int) -> int:
        """

        :param order_number: commander order number in the brigade commanders list
        :return: commander presence (1 - yes, chosen; 0 - no )
        """

        return self.brigade_commanders_list[order_number].presence

    # добавляем свойство в список бонусов батальона
    def set_battalion_bonus(self, bonus: str, order_number: int):
        """

        :param bonus: bonus name
        :param order_number: battalion order number in the brigade
        :return:put this bonus to list of current battalion bonuses
        """


        self.brigade_list[order_number].bonus[bonus] = None

    # добавляем свойство в список бонусов батальона в общем списке бригады (используется при загрузке данных)
    def set_battalion_bonus_in_br_lists(self, bonus: str, place_number: int, order_number: int):
        """

        :param bonus: bonus name
        :param place_number: battalion number in the list of available battalions
        :param order_number: battalion order number in the brigade
        :return: put this bonus to list of current battalion bonuses. Using for load data process
        """

        self.brigade_list_battalion_list[place_number][order_number].bonus[bonus] = None

    def del_battalion_bonus(self, bonus: str, order_number: int):
        """

        :param bonus: bonus name
        :param order_number: battalion order number in the brigade
        :return: Delete this bonus from list of current battalion bonuses
        """

        del self.brigade_list[order_number].bonus[bonus]

    # добавляем стоимость бонуса к общей стоимости бонусов батальона
    def add_bonus_cost_to_battalion(self, new_bonus_cost: int, order_number: int):
        """

        :param new_bonus_cost: added bonus cost
        :param order_number: battalion order number in the brigade
        :return: Add cost of added bonus to the battalion bonus cost.
        """

        self.brigade_list[order_number].bonus_cost += new_bonus_cost

    # добавляем стоимость бонуса к общей стоимости бонусов батальона в общем списке бригады (используется при загрузке данных)
    def add_bonus_cost_to_battalionin_br_lists(self, new_bonus_cost: int, place_number: int, order_number: int):
        """

        :param new_bonus_cost: added bonus cost
        :param place_number: battalion number in the list of available battalions
        :param order_number: battalion order number in the brigade
        :return: Add cost of added bonus to the battalion bonus cost. Using for load data process
        """

        self.brigade_list_battalion_list[place_number][order_number].bonus_cost += new_bonus_cost

    # возвращаем по запросу список всех бонусов батальона
    def get_bonus_list(self, order_number: int) -> dict:
        """

        :param order_number: battalion order number in the brigade
        :return: list of battalion bonuses (Dict)
        """

        return self.brigade_list[order_number].bonus

    def set_common_list_of_battalions(self, order_number: int):
        """

        :param order_number: battalion order number in the brigade
        :return: put Unit() object for first place of the available battalions list. Using for first battalion in the
        brigade when commander is unchosen
        """

        self.brigade_list_battalion_list[order_number].insert(0, Unit())


    def set_list_of_battalions(self, order_number: int):
        """

        :param order_number: battalion order number in the brigade
        :return: delete object from first place of the available
        battalions list. Using for first battalion in the brigade when commander is choosing
        """

        self.brigade_list_battalion_list[order_number].pop(0)

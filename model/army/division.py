from model.army.brigade import Brigade
from model.army.basic_commander import BasicCommander


class Division:
    """ Basic class for all divisions. It contains common methods for all divisions"""

    def __init__(self):
        # список бригад в составе дивизии
        self.division_list: list[Brigade] = []
        # список командиров в составе дивизии
        self.division_commanders_list: list[BasicCommander] = []

    def get_list_commanders_names(self) -> list[str]:
        """

        :return: list of division commanders names
        """

        division_cmndrs_names: list[str] = []
        for cmndr in self.division_commanders_list:
            division_cmndrs_names.append(cmndr.get_name_of_commander())
        return division_cmndrs_names

    # по порядковому номеру в списке командиров возвращает имя
    def get_name_of_commander(self, index: int) -> str:
        """
        :param index: index of commander in the commanders list
        :return: the division commander name
        """

        return self.division_commanders_list[index].get_name_of_commander()

    # по порядковому номеру в списке командиров возвращает его стоимость
    def get_cost_of_commander(self, index: int) -> int:
        """

        :param index: index of commander in the commanders list
        :return: the division commander cost
        """

        return self.division_commanders_list[index].get_cost_of_commander()

    def get_skills_of_commander(self, index: int) -> str:
        """

        :param index: index of commander in the commanders list
        :return: commander's skills as string
        """

        return self.division_commanders_list[index].get_skills_of_commander()

    def get_list_of_division(self) -> list[Brigade]:
        """

        :return: division brigades list
        """

        return self.division_list

    def get_brigade(self, brigade_order: int) -> Brigade:
        """

        :param brigade_order: brigade order in the division list
        :return: corresponding brigade
        """

        return self.division_list[brigade_order]

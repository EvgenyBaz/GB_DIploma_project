class Division:
    def __init__(self):
        # список бригад в составе дивизии
        self.division_list = []
        # список командиров в составе дивизии
        self.division_commanders_list = []

    def get_list_commanders_names(self):
        division_cmndrs_names = []
        for cmndr in self.division_commanders_list:
            division_cmndrs_names.append(cmndr.get_name_of_commander())
        return division_cmndrs_names

    # по порядковому номеру в списке командиров возвращает имя
    def get_name_of_commander(self, index):
        return self.division_commanders_list[index].get_name_of_commander()
    # по порядковому номеру в списке командиров возвращает его стоимость
    def get_cost_of_commander(self, index):
        return self.division_commanders_list[index].get_cost_of_commander()

    def get_skills_of_commander(self, index):
        return self.division_commanders_list[index].get_skills_of_commander()
    def get_list_of_division(self):
        return self.division_list

    def get_brigade(self, brigade_order):
        return self.division_list[brigade_order]
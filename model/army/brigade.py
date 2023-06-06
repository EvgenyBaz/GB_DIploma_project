from model.army.unit import Unit
class Brigade:

    def __init__(self):
        # список командиров
        self.brigade_commanders_list = []

        # список батальонов (обьектов) включенных в бригаду - по умолчанию unit - тоесть пустышка
        self.brigade_list = []

        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list = []

        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list = []

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence = {}


    def get_brigade_bonus_to_battalion_list(self, bonus_name):
        return self.brigade_bonus_battalion_correspondence[bonus_name]

    def get_brigade_bonus_list_names(self):
        bonus_names_list = []
        for i in range(len(self.brigade_bonus_list)):
            bonus_names_list.append(self.brigade_bonus_list[i][0])
        return bonus_names_list

    def get_brigade_bonus_list_costs(self):
        bonus_cost_list = []
        for i in range(len(self.brigade_bonus_list)):
            bonus_cost_list.append(self.brigade_bonus_list[i][1])
        return bonus_cost_list

    def get_brigade_bonus_costs(self, bonus_name):
        bonus_cost = 0
        for i in range(len(self.brigade_bonus_list)):
            if bonus_name == self.brigade_bonus_list[i][0]:
                bonus_cost = self.brigade_bonus_list[i][1]

        return bonus_cost

    def get_list_commanders_names(self):
        brigade_cmndrs_names = []
        for cmndr in self.brigade_commanders_list:
            brigade_cmndrs_names.append(cmndr.get_name_of_commander())
        return brigade_cmndrs_names

    def get_name_of_commander(self, index):
        return self.brigade_commanders_list[index].get_name_of_commander()
    # по порядковому номеру в списке командиров возвращает его стоимость
    def get_costs_of_commander(self, index):
        return self.brigade_commanders_list[index].get_cost_of_commander()

    def main_battalion_list(self):
        return []

    def additional_battalion_list(self):
        return []

    # создает список имен батальонов в зависимости от порядкового номера батальона в бригаде
    def get_list_battalion_names(self, order_number):
        brigade_bttln_list_names = []

        for bttln in self.brigade_list_battalion_list[order_number]:
            brigade_bttln_list_names.append(bttln.name)
        return brigade_bttln_list_names

    # помещает выбраный в интерфейсе батальон (обьект) в список бригады на позицию соответствующую кнопке
    def set_battalion_to_list(self, order_number, bttln_choosen_from_list, shift):
        self.brigade_list[order_number] = self.brigade_list_battalion_list[order_number + shift][
            bttln_choosen_from_list]

    def get_cost_of_battalion(self, order_number):
        return self.brigade_list[order_number].cost + self.brigade_list[order_number].bonus_cost

    def get_name_of_battalion(self, order_number):
        return self.brigade_list[order_number].name

    def get_bonus_of_battalion(self, order_number):
        return self.brigade_list[order_number].get_bonus_of_battalion()

    def get_presence_of_battalion(self, order_number):
        return self.brigade_list[order_number].presence

    def get_presence_of_commander(self, order_number):
        return self.brigade_commanders_list[order_number].presence

    # добавляем свойство в список бонусов батальона
    def set_battalion_bonus(self, bonus, order_number):
        self.brigade_list[order_number].bonus[bonus] = None

    # добавляем свойство в список бонусов батальона в общем списке бригады (используется при загрузке данных)
    def set_battalion_bonus_in_br_lists(self, bonus, place_number, order_number):
        self.brigade_list_battalion_list[place_number][order_number].bonus[bonus] = None

    def del_battalion_bonus(self, bonus, order_number):
        del self.brigade_list[order_number].bonus[bonus]

    # добавляем стоимость бонуса к общей стоимости бонусов батальона
    def add_bonus_cost_to_battalion(self, new_bonus_cost, order_number):
        self.brigade_list[order_number].bonus_cost += new_bonus_cost

    # добавляем стоимость бонуса к общей стоимости бонусов батальона в общем списке бригады (используется при загрузке данных)
    def add_bonus_cost_to_battalionin_br_lists(self, new_bonus_cost, place_number, order_number):
        self.brigade_list_battalion_list[place_number][order_number].bonus_cost += new_bonus_cost
    # возвращаем по запросу список всех бонусов батальона
    def get_bonus_list(self, order_number):
        return self.brigade_list[order_number].bonus

    def set_common_list_of_battalions(self, order_number):
        self.brigade_list_battalion_list[order_number].insert(0, Unit())
    def set_list_of_battalions(self, order_number):
        self.brigade_list_battalion_list[order_number].pop(0)
import json

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog
from fpdf import FPDF, XPos, YPos, Align

from presenter.presenter import Presenter
from view.FraDivisionGuiWindow import Ui_FraDivisionWindow
from view.BonusWindow import BonusWindow
from view.E_message import MessageWindow

from view.brigades.brigade_view import brigade_bttln_Lists

class FraDivisionWindow(QtWidgets.QMainWindow, Ui_FraDivisionWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(FraDivisionWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.error_message = MessageWindow()

        self.actionSave.triggered.connect(self.saveFile)
        self.actionExport_army_list_to_PDF.triggered.connect(self.exportToPDF)

        self.country = "Fra"  # определяем страну
        self.presenter = Presenter(self.country)

        self.generalName.currentIndexChanged.connect(self.divisionCommanderCostView)
        # изменяемая переменная для прхождения проверки  - используется для кавполков с неоднозначным выбором первоко полка в списке, при изменении списка
        self.a_brigade_number = 0  # номер бригады попорядку
        self.a_battalion_index_add = 0

        self.aBrgdCmndr.currentIndexChanged.connect(self.aBrgdCommanderCostView)
        self.aBrgdFirstBattalion.currentIndexChanged.connect(self.aBrgd1stBttlnCostView)
        self.aBrgdSecondBattalion.currentIndexChanged.connect(self.aBrgd2ndBttlnCostView)
        self.aBrgdThirdBattalion.currentIndexChanged.connect(self.aBrgd3rdBttlnCostView)
        self.aBrgdFourthBattalion.currentIndexChanged.connect(self.aBrgd4thBttlnCostView)
        self.aBrgdFifthBattalion.currentIndexChanged.connect(self.aBrgd5thBttlnCostView)
        self.aBrgdSixthBattalion.currentIndexChanged.connect(self.aBrgd6thBttlnCostView)
        self.aBrgdSeventhBattalion.currentIndexChanged.connect(self.aBrgd7thBttlnCostView)
        self.aBrgdEighthBattalion.currentIndexChanged.connect(self.aBrgd8thBttlnCostView)
        self.aBrgdNinthBattalion.currentIndexChanged.connect(self.aBrgd9thBttlnCostView)
        self.aBrgdTenthBattalion.currentIndexChanged.connect(self.aBrgd10thBttlnCostView)

        self.aBrgd1AdditionalBattalion.currentIndexChanged.connect(self.aBrgd1AddBttlnCostView)
        self.aBrgd2AdditionalBattalion.currentIndexChanged.connect(self.aBrgd2AddBttlnCostView)
        self.aBrgd3AdditionalBattalion.currentIndexChanged.connect(self.aBrgd3AddBttlnCostView)
        self.aBrgd4AdditionalBattalion.currentIndexChanged.connect(self.aBrgd4AddBttlnCostView)
        self.aBrgd5AdditionalBattalion.currentIndexChanged.connect(self.aBrgd5AddBttlnCostView)

        self.aBrFirstBttlnModPushButton.clicked.connect(self.a_the_first_bttln_mod_button_was_clicked)
        self.aBrSecondBttlnModPushButton.clicked.connect(self.a_the_second_bttln_mod_button_was_clicked)
        self.aBrThirdBttlnModPushButton.clicked.connect(self.a_the_third_bttln_mod_button_was_clicked)
        self.aBrFourthBttlnModPushButton.clicked.connect(self.a_the_fourth_bttln_mod_button_was_clicked)
        self.aBrFifthBttlnModPushButton.clicked.connect(self.a_the_fifth_bttln_mod_button_was_clicked)
        self.aBrSixthBttlnModPushButton.clicked.connect(self.a_the_sixth_bttln_mod_button_was_clicked)
        self.aBrSeventhBttlnModPushButton.clicked.connect(self.a_the_seventh_bttln_mod_button_was_clicked)
        self.aBrEighthBttlnModPushButton.clicked.connect(self.a_the_eighth_bttln_mod_button_was_clicked)
        self.aBrNinthBttlnModPushButton.clicked.connect(self.a_the_ninth_bttln_mod_button_was_clicked)
        self.aBrTenthBttlnModPushButton.clicked.connect(self.a_the_tenth_bttln_mod_button_was_clicked)


    # заполняем список имен командиров дивизии
    def division_cmndrs_list(self):
        cmndrs_list = self.presenter.DivisionCmndrsNamesList()
        for cmndrName in cmndrs_list:
            self.generalName.addItem(cmndrName)

    def divisionCommanderCostView(self, index):
        value = self.presenter.DivisionCmndrCost(index)
        self.generalCost.setText(str(value))
        self.divisionTotalCostView()

    def divisionTotalCostView(self):
        army_part_of_ivision_total_cost = int(self.aBrgdTotalCost.text()) + \
                     int(self.bBrgdTotalCost.text()) + int(self.cBrgdTotalCost.text()) + \
                     int(self.JgrBrgdTotalCost.text()) + int(self.CombGrndrBrgdTotalCost.text()) + \
                     int(self.GrndrBrgdTotalCost.text()) + int(self.LCvlryBrgdTotalCost.text()) + \
                     int(self.HCvlryBrgdTotalCost.text()) + int(self.CossackBrgdTotalCost.text()) + \
                     self.artillery_total_cost

        guard_part_of_ivision_total_cost = int(self.ImpGrdInfBrgdTotalCost.text()) + \
                                           int(self.ImpGrdLCavBrgdTotalCost.text()) + \
                                           int(self.ImpGrdHCavBrgdTotalCost.text())

        self.division_total_cost = army_part_of_ivision_total_cost + guard_part_of_ivision_total_cost + int(self.generalCost.text())
        if self.division_total_cost > 1000:
            self.divisionTotalCost.setStyleSheet("background-color : yellow ")
        else:
            self.divisionTotalCost.setStyleSheet("background-color : white ")

        if self.division_total_cost*army_part_of_ivision_total_cost == 0:
            self.partOfDivisionTotalCost.setText("0 %")
        else:
            self.partOfDivisionTotalCost.setText(str(round(guard_part_of_ivision_total_cost/(army_part_of_ivision_total_cost+guard_part_of_ivision_total_cost)*100))+" %")
            if round(guard_part_of_ivision_total_cost/(army_part_of_ivision_total_cost+guard_part_of_ivision_total_cost)*100) > 25:
                self.partOfDivisionTotalCost.setStyleSheet("background-color : yellow ")
            else:
                self.partOfDivisionTotalCost.setStyleSheet("background-color : white ")

        total_cost = self.division_total_cost + self.earthworks_total_cost

        self.divisionTotalCost.setText(str(total_cost))
        self.artilleryBatteryVisible()
        self.earthworksVisible()
        self.imperialGuardBgigadesVisible()
    def artilleryBatteryVisible(self):

        number_of_infantry_battalions = self.a_brgd_nmbr_of_battalions + self.b_brgd_nmbr_of_battalions + \
                                        self.c_brgd_nmbr_of_battalions + self.jgr_brgd_nmbr_of_battalions + \
                                        self.comb_grndr_nmbr_of_battalions + self.grnd_brgd_nmbr_of_battalions

        number_of_cavalry_battalions = self.light_cvlry_nmbr_of_battalions + self.heavy_cvlry_nmbr_of_battalions + \
                                       self.cossack_nmbr_of_battalions

        if number_of_infantry_battalions > 5:
            self.LightArtilleryBattery1.setDisabled(False)
            self.UnicornBattery1.setDisabled(False)
        else:
            self.LightArtilleryBattery1.setCurrentIndex(0)
            self.LightArtilleryBattery1.setDisabled(True)
            self.UnicornBattery1.setCurrentIndex(0)
            self.UnicornBattery1.setDisabled(True)

        if number_of_infantry_battalions > 8:
            self.HeavyArtilleryBattery1.setDisabled(False)
        else:
            self.HeavyArtilleryBattery1.setCurrentIndex(0)
            self.HeavyArtilleryBattery1.setDisabled(True)

        if number_of_infantry_battalions > 11:
            self.LightArtilleryBattery2.setDisabled(False)
            self.UnicornBattery2.setDisabled(False)
        else:
            self.LightArtilleryBattery2.setCurrentIndex(0)
            self.LightArtilleryBattery2.setDisabled(True)
            self.UnicornBattery2.setCurrentIndex(0)
            self.UnicornBattery2.setDisabled(True)

        if number_of_infantry_battalions > 17:
            self.LightArtilleryBattery3.setDisabled(False)
            self.UnicornBattery3.setDisabled(False)
            self.HeavyArtilleryBattery2.setDisabled(False)
        else:
            self.LightArtilleryBattery3.setCurrentIndex(0)
            self.LightArtilleryBattery3.setDisabled(True)
            self.UnicornBattery3.setCurrentIndex(0)
            self.UnicornBattery3.setDisabled(True)
            self.HeavyArtilleryBattery2.setCurrentIndex(0)
            self.HeavyArtilleryBattery2.setDisabled(True)

        if number_of_infantry_battalions > 23:
            self.LightArtilleryBattery4.setDisabled(False)
            self.UnicornBattery4.setDisabled(False)
        else:
            self.LightArtilleryBattery4.setCurrentIndex(0)
            self.LightArtilleryBattery4.setDisabled(True)
            self.UnicornBattery4.setCurrentIndex(0)
            self.UnicornBattery4.setDisabled(True)

        if number_of_infantry_battalions > 26:
            self.HeavyArtilleryBattery3.setDisabled(False)
        else:
            self.HeavyArtilleryBattery3.setCurrentIndex(0)
            self.HeavyArtilleryBattery3.setDisabled(True)

        if number_of_infantry_battalions > 29:
            self.LightArtilleryBattery5.setDisabled(False)
            self.UnicornBattery5.setDisabled(False)
        else:
            self.LightArtilleryBattery5.setCurrentIndex(0)
            self.LightArtilleryBattery5.setDisabled(True)
            self.UnicornBattery5.setCurrentIndex(0)
            self.UnicornBattery5.setDisabled(True)

        if number_of_infantry_battalions > 35:
            self.LightArtilleryBattery6.setDisabled(False)
            self.UnicornBattery6.setDisabled(False)
            self.HeavyArtilleryBattery4.setDisabled(False)
        else:
            self.LightArtilleryBattery6.setCurrentIndex(0)
            self.LightArtilleryBattery6.setDisabled(True)
            self.UnicornBattery6.setCurrentIndex(0)
            self.UnicornBattery6.setDisabled(True)
            self.HeavyArtilleryBattery4.setCurrentIndex(0)
            self.HeavyArtilleryBattery4.setDisabled(True)

        if number_of_cavalry_battalions > 3:
            self.HorseArtilleryBattery1.setDisabled(False)
        else:
            self.HorseArtilleryBattery1.setCurrentIndex(0)
            self.HorseArtilleryBattery1.setDisabled(True)

        if number_of_cavalry_battalions > 7:
            self.HorseArtilleryBattery2.setDisabled(False)
        else:
            self.HorseArtilleryBattery2.setCurrentIndex(0)
            self.HorseArtilleryBattery2.setDisabled(True)

        if number_of_cavalry_battalions > 11:
            self.HorseArtilleryBattery3.setDisabled(False)
        else:
            self.HorseArtilleryBattery3.setCurrentIndex(0)
            self.HorseArtilleryBattery3.setDisabled(True)

    def earthworksVisible(self):

        if self.division_total_cost > 499:
            self.EarthWorks1.setDisabled(False)
        else:
            self.EarthWorks1.setCurrentIndex(0)
            self.EarthWorks1.setDisabled(True)

        if self.division_total_cost > 999:
            self.EarthWorks2.setDisabled(False)
        else:
            self.EarthWorks2.setCurrentIndex(0)
            self.EarthWorks2.setDisabled(True)

    def imperialGuardBgigadesVisible(self):
        commanders_list = [self.aBrgdCmndr, self.bBrgdCmndr, self.cBrgdCmndr,
                           self.JgrBrgdCmndr, self.CombGrndrBrgdCmndr, self.GrndrBrgdCmndr]

        nmbr_of_brigades = (sum(self.presenter.BrigadeCmndrsPresence(commanders_list[i].currentIndex(), i) for i in range(0, 6)))

        if nmbr_of_brigades >2:
            self.ImpGrdInfBrgdCmndr.setDisabled(False)
        else:
            self.ImpGrdInfBrgdCmndr.setCurrentIndex(0)
            self.ImpGrdInfBrgdCmndr.setDisabled(True)

        if nmbr_of_brigades >3:
            self.ImpGrdLCavBrgdCmndr.setDisabled(False)
            self.ImpGrdHCavBrgdCmndr.setDisabled(False)
        else:
            self.ImpGrdLCavBrgdCmndr.setCurrentIndex(0)
            self.ImpGrdLCavBrgdCmndr.setDisabled(True)
            self.ImpGrdHCavBrgdCmndr.setCurrentIndex(0)
            self.ImpGrdHCavBrgdCmndr.setDisabled(True)
    # ------------------------------------------------------------------------------------------------------------------
    def brgdCommanderCostView(self, index, brigade_number, brgdCmndrCost):
        value = self.presenter.BrigadeCmndrsCost(index, brigade_number)
        brgdCmndrCost.setText(str(value))

    def brgdBttlnCostView(self, bttln_choosen_from_list, brigade_number, brgdBattalionCost,
                          brgdTotalCostView, order_number, bttlnModPushButton):
        # отправляем индекс в презентер для передачи в модель чтобы поместить соотетствующий батальон на его место в бригаде
        # order_number =  порядковое место в бригаде
        # индекс выбранного баталльона из списка
        self.presenter.BrigadeBttlnChoosen(order_number, bttln_choosen_from_list, brigade_number)
        # отправляем запрос стоимости батальона стоящего на соответствующем месте в бригаде
        value = self.presenter.BrigadeBttlnCost(order_number, brigade_number)
        # записываем в соответствующее поле значение стоимости батальона
        brgdBattalionCost.setText(str(value))
        brgdTotalCostView()
        if bttlnModPushButton != None:
            self.check_bttln_bonus_for_button_color(order_number, brigade_number, bttlnModPushButton)


    # -------------------------------------------------------------------------------------------------------------------
    def a_brigade_bttln_Lists(self):
        a_brgd_bttlns_list =[self.aBrgdFirstBattalion,
                             self.aBrgdSecondBattalion,
                             self.aBrgdThirdBattalion,
                             self.aBrgdFourthBattalion,
                             self.aBrgdAdditionalBattalion,
                             self.aBrgdJgrAdditionalBattalion]

        brigade_bttln_Lists(self.a_brigade_number, self.presenter, self.aBrgdCmndr, a_brgd_bttlns_list)

    def aBrgdCommanderCostView(self, index):
        self.brgdCommanderCostView(index, self.a_brigade_number, self.aBrgdCmndrCost)
        self.aBrgdTotalCostView()
        if self.aBrgdCmndr.currentIndex() < 1:

            if self.presenter.BrigadeBttlnName(0, self.a_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(0, self.a_brigade_number)

                self.aBrgdFirstBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(0, self.a_brigade_number)
                for bttlnName in bttln_list:
                    self.aBrgdFirstBattalion.addItem(bttlnName)

                self.a_battalion_index_add = 0

            self.aBrgdFirstBattalion.setCurrentIndex(0)
            self.aBrgdFirstBattalion.setDisabled(True)
            self.aBrgdSecondBattalion.setCurrentIndex(0)
            self.aBrgdSecondBattalion.setDisabled(True)
            self.aBrgdThirdBattalion.setCurrentIndex(0)
            self.aBrgdThirdBattalion.setDisabled(True)
            self.aBrgdFourthBattalion.setCurrentIndex(0)
            self.aBrgdFourthBattalion.setDisabled(True)
            self.aBrgdAdditionalBattalion.setCurrentIndex(0)
            self.aBrgdAdditionalBattalion.setDisabled(True)
            self.aBrgdJgrAdditionalBattalion.setCurrentIndex(0)
            self.aBrgdJgrAdditionalBattalion.setDisabled(True)

            self.aBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.aBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.aBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.aBrFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.aBrAddBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.aBrJgrAddBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

        else:
            if self.a_battalion_index_add == 0:
            # убираем обьект empty из списка выбора
                self.aBrgdFirstBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(0, self.a_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(0, self.a_brigade_number)
                for bttlnName in bttln_list:
                    self.aBrgdFirstBattalion.addItem(bttlnName)
                # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.a_battalion_index_add = 1

            self.aBrgdFirstBattalion.setDisabled(False)
            self.aBrgdSecondBattalion.setDisabled(False)
            self.aBrgdThirdBattalion.setDisabled(False)
            self.aBrgdFourthBattalion.setDisabled(False)
            self.aBrgdAdditionalBattalion.setDisabled(False)



    def aBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgdFirstBattalionCost, self.aBrgdTotalCostView, 0, self.aBrFirstBttlnModPushButton)

    def aBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgdSecondBattalionCost, self.aBrgdTotalCostView, 1, self.aBrSecondBttlnModPushButton)

    def aBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgdThirdBattalionCost, self.aBrgdTotalCostView, 2, self.aBrThirdBttlnModPushButton)

    def aBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgdFourthBattalionCost, self.aBrgdTotalCostView, 3, self.aBrFourthBttlnModPushButton)

    def aBrgd5thBttlnCostView(self, bttln_choosen_from_list):
        pass

    def aBrgd6thBttlnCostView(self, bttln_choosen_from_list):
        pass

    def aBrgd7thBttlnCostView(self, bttln_choosen_from_list):
        pass


    def aBrgd8thBttlnCostView(self, bttln_choosen_from_list):
        pass


    def aBrgd9thBttlnCostView(self, bttln_choosen_from_list):
        pass

    def aBrgd10thBttlnCostView(self, bttln_choosen_from_list):
        pass

    def aBrgd1AddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgd1AddBattalionCost, self.aBrgdTotalCostView, 4, None)

    def aBrgd2AddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgd1AddBattalionCost, self.aBrgdTotalCostView, 4, None)

    def aBrgd3AddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgd1AddBattalionCost, self.aBrgdTotalCostView, 4, None)

    def aBrgd4AddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgd1AddBattalionCost, self.aBrgdTotalCostView, 4, None)

    def aBrgd5AddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgd1AddBattalionCost, self.aBrgdTotalCostView, 4, None)




    def aBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.aBrgdCmndr.currentIndex(), self.a_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.a_brigade_number) for i in range(6))

        self.a_brgd_nmbr_of_battalions = (sum(self.presenter.BrigadeBttlnPresence(i, self.a_brigade_number) for i in range(6)))

        self.aBrgdTotalCost.setText(str(total_cost))
        self.divisionTotalCostView()

    def a_the_first_bttln_mod_button_was_clicked(self):
        if self.aBrgdFirstBattalion.currentIndex()+ self.a_battalion_index_add != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.brgdFirstBattalionCostSetText = self.aBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBrFirstBttlnModPushButton, self.aBrgdFirstBattalion.currentText(), self.order_number)

    def a_the_second_bttln_mod_button_was_clicked(self):
        if self.aBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.brgdSecondBattalionCostSetText = self.aBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBrSecondBttlnModPushButton, self.aBrgdSecondBattalion.currentText(), self.order_number)

    def a_the_third_bttln_mod_button_was_clicked(self):
        if self.aBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.brgdThirdBattalionCostSetText = self.aBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBrThirdBttlnModPushButton, self.aBrgdThirdBattalion.currentText(), self.order_number)

    def a_the_fourth_bttln_mod_button_was_clicked(self):
        if self.aBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.brgdFourthBattalionCostSetText = self.aBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBrFourthBttlnModPushButton, self.aBrgdFourthBattalion.currentText(), self.order_number)

    def a_the_fifth_bttln_mod_button_was_clicked(self):
        pass

    def a_the_sixth_bttln_mod_button_was_clicked(self):
        pass

    def a_the_seventh_bttln_mod_button_was_clicked(self):
        pass

    def a_the_eighth_bttln_mod_button_was_clicked(self):
        pass

    def a_the_ninth_bttln_mod_button_was_clicked(self):
        pass

    def a_the_tenth_bttln_mod_button_was_clicked(self):
        pass

    # -------------------------------------------------------------------------------------------------------------------












    #--------------------------------------------------------------------------------------------------------------------

    def bttln_mod_button_was_clicked(self, battalion_order, brigade_number, mod_button_name, battalion_choosen_name, battalion_choosen_order):

        self.current_bttln_name_choosen = battalion_choosen_name # имя батальона который был выбран при нажатии окна МОД
        self.current_bttln_order_choosen = battalion_choosen_order # порядновый номер батальона в бригаде, который был выбран при нажатии окна МОД
        self.brigade_number = brigade_number #порядковый номер бригады
        self.bonus_window = BonusWindow()
        self.bonus_window.setWindowTitle(battalion_order)
        self.mod_button_name = mod_button_name

        self.bonuses = [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]

        self.bonuses_list_in_window = [
            self.bonus_window.bonus1,
            self.bonus_window.bonus2,
            self.bonus_window.bonus3,
            self.bonus_window.bonus4,
            self.bonus_window.bonus5,
            self.bonus_window.bonus6,
            self.bonus_window.bonus7
        ]

        self.bonuses_checkboxes_in_window = [
            self.bonus_window.checkBox_1,
            self.bonus_window.checkBox_2,
            self.bonus_window.checkBox_3,
            self.bonus_window.checkBox_4,
            self.bonus_window.checkBox_5,
            self.bonus_window.checkBox_6,
            self.bonus_window.checkBox_7,
        ]

        checkbox_Action_list =[
            self.checkBox1_Action,
            self.checkBox2_Action,
            self.checkBox3_Action
        ]

        # создаем временную переменную стоимости батальона , для отображения в окне бонусов
        self.temporary_bonus_cost = self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)
        # создаем временный список бонусов батальона
        self.temporary_bonus_list = self.presenter.BrigadeBttlnBonusList(self.order_number, self.brigade_number).copy()

        self.bonus_window.name.setText(str(self.presenter.BrigadeBttlnName(self.order_number, self.brigade_number)))
        self.bonus_window.cost.setText(str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))

        self.btln_bonus_list =[]
        self.btln_bonus_cost_list = []

        apply_bonus_count = 0
        for bonus_count in range (0, len(self.presenter.BrigadeBonusNameList(self.brigade_number))):
            # проверяем Имя текущего батальона находится среди имен батальонов списка соответствия бонуса к батальонам
            if self.presenter.BrigadeBttlnName(self.order_number, self.brigade_number) in self.presenter.BrigadeBonusToBattalion(self.presenter.BrigadeBonusNameList(self.brigade_number)[bonus_count], self.brigade_number):

                self.bonuses_list_in_window[apply_bonus_count].setText(self.presenter.BrigadeBonusNameList(self.brigade_number)[bonus_count])
                #создаем локальтный список всех возможных бонусов батальона
                self.btln_bonus_list.append(self.presenter.BrigadeBonusNameList(self.brigade_number)[bonus_count])
                self.btln_bonus_cost_list.append(self.presenter.BrigadeBonusCostList(self.brigade_number)[bonus_count])

                apply_bonus_count +=1

        #закрываем оставшиеся ненужные строки
        for i in range (apply_bonus_count, len(self.bonuses_list_in_window)):
            self.bonuses_list_in_window[i].close()
            self.bonuses_checkboxes_in_window[i].close()

        # расставляем статус "нажато" если такой бонус был ранее добавлен
        for i in range (0, len(self.btln_bonus_list)):
            if self.btln_bonus_list[i] in self.presenter.BrigadeBttlnBonusList(
                    self.order_number, self.brigade_number):
                self.bonuses_checkboxes_in_window[i].setChecked(True)

                self.check_contradiction(self.btln_bonus_list[i] , self.btln_bonus_list)

            self.bonuses_checkboxes_in_window[i].stateChanged.connect(checkbox_Action_list[i])


        self.bonus_window.ok_button.clicked.connect(self.ok_button_was_clicked)
        self.bonus_window.cancel_button.clicked.connect(self.cancel_button_was_clicked)
        self.bonus_window.show()

    def ok_button_was_clicked(self):
# gпроверка условия , что текущий выбор батальона тот же , что и при нажатии на кнопку модификации
        if self.presenter.BrigadeBttlnName(self.current_bttln_order_choosen, self.brigade_number) == self.current_bttln_name_choosen:

            for i in range(0, len(self.btln_bonus_list)):
                # проверка если выбранный бонус не пуст то тогда применяются свойства бонууса.
                if self.bonuses[i] != "":
                    # проверяем если чекбокс был нажат то добавляем свойста, если отжат , то удаляем свойства и стоимость
                    if self.bonuses_checkboxes_in_window[i].isChecked():
                        # проверяем, если такой такого юонуса еще нет то добавляем
                        if self.btln_bonus_list[i] not in self.presenter.BrigadeBttlnBonusList(self.order_number,self.brigade_number):
                            self.presenter.BrigadeBttlnBonusAdd(self.bonuses[i], self.order_number, self.brigade_number)
                            self.presenter.BrigadeBttlnBonusCostAdd(self.btln_bonus_cost_list[i], self.order_number,self.brigade_number)
                    else:
                        # проверяем, если такой бонус есть то удаляем
                        if self.btln_bonus_list[i] in self.presenter.BrigadeBttlnBonusList(self.order_number,self.brigade_number):
                            self.presenter.BrigadeBttlnBonusDel(self.bonuses[i], self.order_number, self.brigade_number)
                            self.presenter.BrigadeBttlnBonusCostAdd(self.btln_bonus_cost_list[i] * (-1),self.order_number, self.brigade_number)

            match self.order_number:
                case 0:
                    self.brgdFirstBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))
                case 1:
                    self.brgdSecondBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))
                case 2:
                    self.brgdThirdBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))
                case 3:
                    self.brgdFourthBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))
                case 4:
                    self.brgdFifthBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))
                case 5:
                    self.brgdSixthBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))
                case 6:
                    self.brgdSeventhBattalionCostSetText(
                        str(self.presenter.BrigadeBttlnCost(self.order_number, self.brigade_number)))



            # и обновляем полную стоимость бригады
            self.brgdTotalCostView()
            # перекрашиваем кнупку если надо
            self.check_bttln_bonus_for_button_color(self.order_number, self.brigade_number, self.mod_button_name)
            self.bonus_window.close()
        else:
            self.cancel_button_was_clicked()

    def cancel_button_was_clicked(self):
        self.bonus_window.close()

    def check_bttln_bonus_for_button_color(self, order_number, brigade_number, mod_button_name):
        if len(self.presenter.BrigadeBttlnBonusList(order_number, brigade_number)) == 0:
            mod_button_name.setStyleSheet("background-color : rgb(225,225,225) ")
        else:
            mod_button_name.setStyleSheet("background-color : white")

    def checkBox1_Action(self):
        self.checkBox_Action(0)

    def checkBox2_Action(self):
        self.checkBox_Action(1)

    def checkBox3_Action(self):
        self.checkBox_Action(2)

    def checkBox_Action(self, order_number):
        self.bonuses[order_number] = self.btln_bonus_list[order_number]

        # проверка если чекбокс нажат и такого бонуса еще нет в списке бонусов батальона, то в окне отображения бонусов показывается стоимость с бонусом ()
        # предварительно, эта стоимость еще не применилась к батальону
        # если чекбокс нажат и такой бонус уже есть, то показывается стоимость взятая из обьекта батальон
        if self.bonuses_checkboxes_in_window[order_number].isChecked():
            if self.btln_bonus_list[order_number] not in self.temporary_bonus_list:
                self.temporary_bonus_cost += self.btln_bonus_cost_list[order_number]  # к временной стоимости прибавляем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                self.temporary_bonus_list[self.btln_bonus_list[order_number]] = None  # вносим бонус во временный список
            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))
            self.check_contradiction(self.btln_bonus_list[order_number], self.btln_bonus_list)
        # проверка если чекбокс отжат и такой бонус есть в списке бонусов батальона, то в окне отображения бонусов показывается стоимость за вычетом бонуса
        # предварительно, эта стоимость еще не применилась к батальону
        # если чекбокс отжат  и такого бонуса нет, то показывается стоимость взятая из обьекта батальон
        else:
            if self.btln_bonus_list[order_number] in self.temporary_bonus_list:
                self.temporary_bonus_cost -= self.btln_bonus_cost_list[order_number]  # от временной стоимости вычитаем стоимость бонуса
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))  # печатаем стоимость в окне бонусов
                del self.temporary_bonus_list[self.btln_bonus_list[order_number] ]  # удаляем бонус из временный список
            else:
                self.bonus_window.cost.setText(str(self.temporary_bonus_cost))
            self.check_contradiction(self.btln_bonus_list[order_number], self.btln_bonus_list)

    def check_contradiction(self, current_bonus, bonuses_list):
        if current_bonus == "Large":
            count = False
            position = 0
            for i in range (0, len(bonuses_list)):
                if bonuses_list[i] == "Small":
                    count = True
                    position = i
            if count:
                if self.bonuses_checkboxes_in_window[position].isEnabled():
                    self.bonuses_checkboxes_in_window[position].setDisabled(True)
                else:
                    self.bonuses_checkboxes_in_window[position].setDisabled(False)

        if current_bonus == "Small":
            count = False
            position = 0
            for i in range(0, len(bonuses_list)):
                if bonuses_list[i] == "Large":
                    count = True
                    position = i
            if count:
                if self.bonuses_checkboxes_in_window[position].isEnabled():
                    self.bonuses_checkboxes_in_window[position].setDisabled(True)
                else:
                    self.bonuses_checkboxes_in_window[position].setDisabled(False)

        if current_bonus == "Small free":
            count = False
            position = 0
            for i in range(0, len(bonuses_list)):
                if bonuses_list[i] == "Large free":
                    count = True
                    position = i
            if count:
                if self.bonuses_checkboxes_in_window[position].isEnabled():
                    self.bonuses_checkboxes_in_window[position].setDisabled(True)
                else:
                    self.bonuses_checkboxes_in_window[position].setDisabled(False)

        if current_bonus == "Large free":
            count = False
            position = 0
            for i in range(0, len(bonuses_list)):
                if bonuses_list[i] == "Small free":
                    count = True
                    position = i
            if count:
                if self.bonuses_checkboxes_in_window[position].isEnabled():
                    self.bonuses_checkboxes_in_window[position].setDisabled(True)
                else:
                    self.bonuses_checkboxes_in_window[position].setDisabled(False)

    def saveFile(self):

        fileName, _= QFileDialog.getSaveFileName(
            parent=self,
            caption='Select a data file',
            filter='Data File (*.dat)'
        )

        if fileName:
            try:
                with open(fileName, 'w') as fileToSave:
                    fileToSave.write(self.dataCollectToSave())
            except:
                self.error_message.show()
        else:
            pass

    def dataCollectToSave(self):
        dataSet= {"Side": self.country,
                  "Division general": self.generalName.currentIndex()}
        if self.aBrgdCmndr.currentIndex() != 0:
            dataSet["1st Inf Brigade Commander"] = self.aBrgdCmndr.currentIndex()
            dataSet["1st Inf Brigade 1st bttln"] = [self.aBrgdFirstBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(0, self.a_brigade_number)]
            dataSet["1st Inf Brigade 2nd bttln"] = [self.aBrgdSecondBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(1, self.a_brigade_number)]
            dataSet["1st Inf Brigade 3rd bttln"] = [self.aBrgdThirdBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(2, self.a_brigade_number)]
            dataSet["1st Inf Brigade 4th bttln"] = [self.aBrgdFourthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(3, self.a_brigade_number)]
            dataSet["1st Inf Brigade add bttln"] = [self.aBrgdAdditionalBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(4, self.a_brigade_number)]
            dataSet["1st Inf Brigade jgr add bttln"] = [self.aBrgdJgrAdditionalBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(5, self.a_brigade_number)]
        if self.bBrgdCmndr.currentIndex() != 0:
            dataSet["2nd Inf Brigade Commander"] = self.bBrgdCmndr.currentIndex()
            dataSet["2nd Inf Brigade 1st bttln"] = [self.bBrgdFirstBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(0, self.b_brigade_number)]
            dataSet["2nd Inf Brigade 2nd bttln"] = [self.bBrgdSecondBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(1, self.b_brigade_number)]
            dataSet["2nd Inf Brigade 3rd bttln"] = [self.bBrgdThirdBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(2, self.b_brigade_number)]
            dataSet["2nd Inf Brigade 4th bttln"] = [self.bBrgdFourthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(3, self.b_brigade_number)]
            dataSet["2nd Inf Brigade add bttln"] = [self.bBrgdAdditionalBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(4, self.b_brigade_number)]
            dataSet["2nd Inf Brigade jgr add bttln"] = [self.bBrgdJgrAdditionalBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(5, self.b_brigade_number)]
        if self.cBrgdCmndr.currentIndex() != 0:
            dataSet["3rd Inf Brigade Commander"] = self.cBrgdCmndr.currentIndex()
            dataSet["3rd Inf Brigade 1st bttln"] = [self.cBrgdFirstBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(0, self.c_brigade_number)]
            dataSet["3rd Inf Brigade 2nd bttln"] = [self.cBrgdSecondBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(1, self.c_brigade_number)]
            dataSet["3rd Inf Brigade 3rd bttln"] = [self.cBrgdThirdBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(2, self.c_brigade_number)]
            dataSet["3rd Inf Brigade 4th bttln"] = [self.cBrgdFourthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(3, self.c_brigade_number)]
            dataSet["3rd Inf Brigade add bttln"] = [self.cBrgdAdditionalBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(4, self.c_brigade_number)]
            dataSet["3rd Inf Brigade jgr add bttln"] = [self.cBrgdJgrAdditionalBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(5, self.c_brigade_number)]

        if self.JgrBrgdCmndr.currentIndex() != 0:
            dataSet["Jgr Brigade Commander"] = self.JgrBrgdCmndr.currentIndex()
            dataSet["Jgr Brigade 1st bttln"] = [self.JgrBrgdFirstBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(0, self.jgr_brigade_number)]
            dataSet["Jgr Brigade 2nd bttln"] = [self.JgrBrgdSecondBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(1, self.jgr_brigade_number)]
            dataSet["Jgr Brigade 3rd bttln"] = [self.JgrBrgdThirdBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(2, self.jgr_brigade_number)]
            dataSet["Jgr Brigade 4th bttln"] = [self.JgrBrgdFourthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(3, self.jgr_brigade_number)]
            dataSet["Jgr Brigade 5th bttln"] = [self.JgrBrgdFifthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(4, self.jgr_brigade_number)]
            dataSet["Jgr Brigade 6th bttln"] = [self.JgrBrgdSixthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(5, self.jgr_brigade_number)]
            dataSet["Jgr Brigade add1 bttln"] = [self.JgrBrgdAdditional1Battalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(6, self.jgr_brigade_number)]
            dataSet["Jgr Brigade add2 bttln"] = [self.JgrBrgdAdditional2Battalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(7, self.jgr_brigade_number)]

        if self.CombGrndrBrgdCmndr.currentIndex() != 0:
            dataSet["Comb Grndr Brigade Commander"] = self.CombGrndrBrgdCmndr.currentIndex()
            dataSet["Comb Grndr Brigade 1st bttln"] = [self.CombGrndrBrgdFirstBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(0, self.comb_grndr_brigade_number)]
            dataSet["Comb Grndr Brigade 2nd bttln"] = [self.CombGrndrBrgdSecondBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(1, self.comb_grndr_brigade_number)]
            dataSet["Comb Grndr Brigade 3rd bttln"] = [self.CombGrndrBrgdThirdBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(2, self.comb_grndr_brigade_number)]
            dataSet["Comb Grndr Brigade 4th bttln"] = [self.CombGrndrBrgdFourthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(3, self.comb_grndr_brigade_number)]
            dataSet["Comb Grndr Brigade 5th bttln"] = [self.CombGrndrBrgdFifthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(4, self.comb_grndr_brigade_number)]
            dataSet["Comb Grndr Brigade 6th bttln"] = [self.CombGrndrBrgdSixthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(5, self.comb_grndr_brigade_number)]
            dataSet["Comb Grndr Brigade 7th bttln"] = [self.CombGrndrBrgdSeventhBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(6, self.comb_grndr_brigade_number)]

        if self.GrndrBrgdCmndr.currentIndex() != 0:
            dataSet["Grndr Brigade Commander"] = self.GrndrBrgdCmndr.currentIndex()
            dataSet["Grndr Brigade 1st bttln"] = [self.GrndrBrgdFirstBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(0, self.grndr_brigade_number)]
            dataSet["Grndr Brigade 2nd bttln"] = [self.GrndrBrgdSecondBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(1, self.grndr_brigade_number)]
            dataSet["Grndr Brigade 3rd bttln"] = [self.GrndrBrgdThirdBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(2, self.grndr_brigade_number)]
            dataSet["Grndr Brigade 4th bttln"] = [self.GrndrBrgdFourthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(3, self.grndr_brigade_number)]

        if self.LCvlryBrgdCmndr.currentIndex() != 0:
            dataSet["L Cvlry Brigade Commander"] = self.LCvlryBrgdCmndr.currentIndex()
            dataSet["L Cvlry Brigade 1st rgmnt"] = [self.LCvlryBrgdFirstBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(0, self.light_cvlry_brigade_number)]
            dataSet["L Cvlry Brigade 2nd rgmnt"] = [self.LCvlryBrgdSecondBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(1, self.light_cvlry_brigade_number)]
            dataSet["L Cvlry Brigade 3rd rgmnt"] = [self.LCvlryBrgdThirdBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(2, self.light_cvlry_brigade_number)]

        if self.HCvlryBrgdCmndr.currentIndex() != 0:
            dataSet["H Cvlry Brigade Commander"] = self.HCvlryBrgdCmndr.currentIndex()
            dataSet["H Cvlry Brigade 1st rgmnt"] = [self.HCvlryBrgdFirstBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(0, self.heavy_cvlry_brigade_number)]
            dataSet["H Cvlry Brigade 2nd rgmnt"] = [self.HCvlryBrgdSecondBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(1, self.heavy_cvlry_brigade_number)]
            dataSet["H Cvlry Brigade 3rd rgmnt"] = [self.HCvlryBrgdThirdBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(2, self.heavy_cvlry_brigade_number)]

        if self.CossackBrgdCmndr.currentIndex() != 0:
            dataSet["Cossack Brigade Commander"] = self.CossackBrgdCmndr.currentIndex()
            dataSet["Cossack Brigade 1st rgmnt"] = [self.CossackBrgdFirstBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(0, self.cossack_brigade_number)]
            dataSet["Cossack Brigade 2nd rgmnt"] = [self.CossackBrgdSecondBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(1, self.cossack_brigade_number)]
            dataSet["Cossack Brigade 3rd rgmnt"] = [self.CossackBrgdThirdBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(2, self.cossack_brigade_number)]
            dataSet["Cossack Brigade 4th rgmnt"] = [self.CossackBrgdFourthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(3, self.cossack_brigade_number)]
            dataSet["Cossack Brigade 5th rgmnt"] = [self.CossackBrgdFifthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(4, self.cossack_brigade_number)]
            dataSet["Cossack Brigade 6th rgmnt"] = [self.CossackBrgdSixthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(5, self.cossack_brigade_number)]

        if self.ImpGrdInfBrgdCmndr.currentIndex() != 0:
            dataSet["Imp Grd Inf Brigade Commander"] = self.ImpGrdInfBrgdCmndr.currentIndex()
            dataSet["Imp Grd Inf Brigade 1st bttln"] = [self.ImpGrdInfBrgdFirstBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(0, self.imp_grd_inf_brigade_number)]
            dataSet["Imp Grd Inf Brigade 2nd bttln"] = [self.ImpGrdInfBrgdSecondBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(1, self.imp_grd_inf_brigade_number)]
            dataSet["Imp Grd Inf Brigade 3rd bttln"] = [self.ImpGrdInfBrgdThirdBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(2, self.imp_grd_inf_brigade_number)]
            dataSet["Imp Grd Inf Brigade 4th bttln"] = [self.ImpGrdInfBrgdFourthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(3, self.imp_grd_inf_brigade_number)]
            dataSet["Imp Grd Inf Brigade 5th bttln"] = [self.ImpGrdInfBrgdFifthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(4, self.imp_grd_inf_brigade_number)]
            dataSet["Imp Grd Inf Brigade 6th bttln"] = [self.ImpGrdInfBrgdSixthBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(5, self.imp_grd_inf_brigade_number)]
            dataSet["Imp Grd Inf Brigade add1 bttln"] = [self.ImpGrdInfBrgdAdditional1Battalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(6, self.imp_grd_inf_brigade_number)]
            dataSet["Imp Grd Inf Brigade add2 bttln"] = [self.ImpGrdInfBrgdAdditional2Battalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(7, self.imp_grd_inf_brigade_number)]

        if self.ImpGrdLCavBrgdCmndr.currentIndex() != 0:
            dataSet["Imp Grd L Cav Brigade Commander"] = self.ImpGrdLCavBrgdCmndr.currentIndex()
            dataSet["Imp Grd L Cav Brigade 1st rgmnt"] = [self.ImpGrdLCavBrgdFirstBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(0, self.imp_grd_l_cav_brigade_number)]
            dataSet["Imp Grd L Cav Brigade 2nd rgmnt"] = [self.ImpGrdLCavBrgdSecondBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(1, self.imp_grd_l_cav_brigade_number)]

        if self.ImpGrdHCavBrgdCmndr.currentIndex() != 0:
            dataSet["Imp Grd H Cav Brigade Commander"] = self.ImpGrdHCavBrgdCmndr.currentIndex()
            dataSet["Imp Grd H Cav Brigade 1st rgmnt"] = [self.ImpGrdHCavBrgdFirstBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(0, self.imp_grd_h_cav_brigade_number)]
            dataSet["Imp Grd H Cav Brigade 2nd rgmnt"] = [self.ImpGrdHCavBrgdSecondBattalion.currentIndex(),
                                                    self.presenter.BrigadeBttlnBonusList(1, self.imp_grd_h_cav_brigade_number)]

        dataSet["Light Artillery Battery 1"] = [self.LightArtilleryBattery1.currentIndex()]
        dataSet["Light Artillery Battery 2"] = [self.LightArtilleryBattery2.currentIndex()]
        dataSet["Light Artillery Battery 3"] = [self.LightArtilleryBattery3.currentIndex()]
        dataSet["Light Artillery Battery 4"] = [self.LightArtilleryBattery4.currentIndex()]
        dataSet["Light Artillery Battery 5"] = [self.LightArtilleryBattery5.currentIndex()]
        dataSet["Light Artillery Battery 6"] = [self.LightArtilleryBattery6.currentIndex()]

        dataSet["Heavy Artillery Battery 1"] = [self.HeavyArtilleryBattery1.currentIndex()]
        dataSet["Heavy Artillery Battery 2"] = [self.HeavyArtilleryBattery2.currentIndex()]
        dataSet["Heavy Artillery Battery 3"] = [self.HeavyArtilleryBattery3.currentIndex()]
        dataSet["Heavy Artillery Battery 4"] = [self.HeavyArtilleryBattery4.currentIndex()]

        dataSet["Unicorn Battery 1"] = [self.UnicornBattery1.currentIndex()]
        dataSet["Unicorn Battery 2"] = [self.UnicornBattery2.currentIndex()]
        dataSet["Unicorn Battery 3"] = [self.UnicornBattery3.currentIndex()]
        dataSet["Unicorn Battery 4"] = [self.UnicornBattery4.currentIndex()]
        dataSet["Unicorn Battery 5"] = [self.UnicornBattery5.currentIndex()]
        dataSet["Unicorn Battery 6"] = [self.UnicornBattery6.currentIndex()]

        dataSet["Horse Artillery Battery 1"] = [self.HorseArtilleryBattery1.currentIndex()]
        dataSet["Horse Artillery Battery 2"] = [self.HorseArtilleryBattery2.currentIndex()]
        dataSet["Horse Artillery Battery 3"] = [self.HorseArtilleryBattery3.currentIndex()]

        dataSet["EarthWorks 1"] = [self.EarthWorks1.currentIndex()]
        dataSet["EarthWorks 2"] = [self.EarthWorks2.currentIndex()]



        json_object = json.dumps(dataSet, indent=4)
        return json_object

    def loadData(self, data):

        self.generalName.setCurrentIndex(data["Division general"])

        if "1st Inf Brigade Commander" in data.keys():
            # проверяем и устанавливаем бонусы батальона
            self.load_procedure_set_bonuses(data, "1st Inf Brigade 1st bttln", 0, data["1st Inf Brigade 1st bttln"][0]+1, self.a_brigade_number)
            # устанавливаеем командитра бригады
            self.aBrgdCmndr.setCurrentIndex(data["1st Inf Brigade Commander"])
            # проверяем и устанавливаем бонусы батальона
            self.load_procedure_set_bonuses(data, "1st Inf Brigade 2nd bttln", 1, data["1st Inf Brigade 2nd bttln"][0], self.a_brigade_number)
            # устанавливаеем батальон
            self.aBrgdSecondBattalion.setCurrentIndex(data["1st Inf Brigade 2nd bttln"][0])

            self.load_procedure_set_bonuses(data, "1st Inf Brigade 3rd bttln", 2, data["1st Inf Brigade 3rd bttln"][0], self.a_brigade_number)
            self.aBrgdThirdBattalion.setCurrentIndex(data["1st Inf Brigade 3rd bttln"][0])

            self.load_procedure_set_bonuses(data, "1st Inf Brigade 4th bttln", 3, data["1st Inf Brigade 4th bttln"][0], self.a_brigade_number)
            self.aBrgdFourthBattalion.setCurrentIndex(data["1st Inf Brigade 4th bttln"][0])

            self.load_procedure_set_bonuses(data, "1st Inf Brigade add bttln", 4, data["1st Inf Brigade add bttln"][0], self.a_brigade_number)
            self.aBrgdAdditionalBattalion.setCurrentIndex(data["1st Inf Brigade add bttln"][0])

            self.load_procedure_set_bonuses(data, "1st Inf Brigade jgr add bttln", 5, data["1st Inf Brigade jgr add bttln"][0], self.a_brigade_number)
            self.aBrgdJgrAdditionalBattalion.setCurrentIndex(data["1st Inf Brigade jgr add bttln"][0])

        if "2nd Inf Brigade Commander" in data.keys():
            # проверяем и устанавливаем бонусы батальона
            self.load_procedure_set_bonuses(data, "2nd Inf Brigade 1st bttln", 0, data["2nd Inf Brigade 1st bttln"][0]+1, self.b_brigade_number)
            self.bBrgdCmndr.setCurrentIndex(data["2nd Inf Brigade Commander"])

            self.load_procedure_set_bonuses(data, "2nd Inf Brigade 2nd bttln", 1, data["2nd Inf Brigade 2nd bttln"][0], self.b_brigade_number)
            self.bBrgdSecondBattalion.setCurrentIndex(data["2nd Inf Brigade 2nd bttln"][0])

            self.load_procedure_set_bonuses(data, "2nd Inf Brigade 3rd bttln", 2, data["2nd Inf Brigade 3rd bttln"][0], self.b_brigade_number)
            self.bBrgdThirdBattalion.setCurrentIndex(data["2nd Inf Brigade 3rd bttln"][0])

            self.load_procedure_set_bonuses(data, "2nd Inf Brigade 4th bttln", 3, data["2nd Inf Brigade 4th bttln"][0], self.b_brigade_number)
            self.bBrgdFourthBattalion.setCurrentIndex(data["2nd Inf Brigade 4th bttln"][0])

            self.load_procedure_set_bonuses(data, "2nd Inf Brigade add bttln", 4, data["2nd Inf Brigade add bttln"][0], self.b_brigade_number)
            self.bBrgdAdditionalBattalion.setCurrentIndex(data["2nd Inf Brigade add bttln"][0])

            self.load_procedure_set_bonuses(data, "2nd Inf Brigade jgr add bttln", 5, data["2nd Inf Brigade jgr add bttln"][0], self.b_brigade_number)
            self.bBrgdJgrAdditionalBattalion.setCurrentIndex(data["2nd Inf Brigade jgr add bttln"][0])

        if "3rd Inf Brigade Commander" in data.keys():
            # проверяем и устанавливаем бонусы батальона
            self.load_procedure_set_bonuses(data, "3rd Inf Brigade 1st bttln", 0, data["3rd Inf Brigade 1st bttln"][0]+1, self.c_brigade_number)
            self.cBrgdCmndr.setCurrentIndex(data["3rd Inf Brigade Commander"])

            self.load_procedure_set_bonuses(data, "3rd Inf Brigade 2nd bttln", 1, data["3rd Inf Brigade 2nd bttln"][0], self.c_brigade_number)
            self.cBrgdSecondBattalion.setCurrentIndex(data["3rd Inf Brigade 2nd bttln"][0])

            self.load_procedure_set_bonuses(data, "3rd Inf Brigade 3rd bttln", 2, data["3rd Inf Brigade 3rd bttln"][0], self.c_brigade_number)
            self.cBrgdThirdBattalion.setCurrentIndex(data["3rd Inf Brigade 3rd bttln"][0])

            self.load_procedure_set_bonuses(data, "3rd Inf Brigade 4th bttln", 3, data["3rd Inf Brigade 4th bttln"][0], self.c_brigade_number)
            self.cBrgdFourthBattalion.setCurrentIndex(data["3rd Inf Brigade 4th bttln"][0])

            self.load_procedure_set_bonuses(data, "3rd Inf Brigade add bttln", 4, data["3rd Inf Brigade add bttln"][0], self.c_brigade_number)
            self.cBrgdAdditionalBattalion.setCurrentIndex(data["3rd Inf Brigade add bttln"][0])

            self.load_procedure_set_bonuses(data, "3rd Inf Brigade jgr add bttln", 5, data["3rd Inf Brigade jgr add bttln"][0], self.c_brigade_number)
            self.cBrgdJgrAdditionalBattalion.setCurrentIndex(data["3rd Inf Brigade jgr add bttln"][0])

        if "Jgr Brigade Commander" in data.keys():
            # проверяем и устанавливаем бонусы батальона
            self.load_procedure_set_bonuses(data, "Jgr Brigade 1st bttln", 0, data["Jgr Brigade 1st bttln"][0]+1, self.jgr_brigade_number)
            self.load_procedure_set_bonuses(data, "Jgr Brigade 2nd bttln", 1, data["Jgr Brigade 2nd bttln"][0]+1, self.jgr_brigade_number)

            self.JgrBrgdCmndr.setCurrentIndex(data["Jgr Brigade Commander"])

            self.load_procedure_set_bonuses(data, "Jgr Brigade 3rd bttln", 2, data["Jgr Brigade 3rd bttln"][0], self.jgr_brigade_number)
            self.JgrBrgdThirdBattalion.setCurrentIndex(data["Jgr Brigade 3rd bttln"][0])

            self.load_procedure_set_bonuses(data, "Jgr Brigade 4th bttln", 3, data["Jgr Brigade 4th bttln"][0], self.jgr_brigade_number)
            self.JgrBrgdFourthBattalion.setCurrentIndex(data["Jgr Brigade 4th bttln"][0])

            self.load_procedure_set_bonuses(data, "Jgr Brigade 5th bttln", 4, data["Jgr Brigade 5th bttln"][0], self.jgr_brigade_number)
            self.JgrBrgdFifthBattalion.setCurrentIndex(data["Jgr Brigade 5th bttln"][0])

            self.load_procedure_set_bonuses(data, "Jgr Brigade 6th bttln", 5, data["Jgr Brigade 6th bttln"][0], self.jgr_brigade_number)
            self.JgrBrgdSixthBattalion.setCurrentIndex(data["Jgr Brigade 6th bttln"][0])

            self.load_procedure_set_bonuses(data, "Jgr Brigade add1 bttln", 6, data["Jgr Brigade add1 bttln"][0], self.jgr_brigade_number)
            self.JgrBrgdAdditional1Battalion.setCurrentIndex(data["Jgr Brigade add1 bttln"][0])

            self.load_procedure_set_bonuses(data, "Jgr Brigade add2 bttln", 7, data["Jgr Brigade add2 bttln"][0], self.jgr_brigade_number)
            self.JgrBrgdAdditional2Battalion.setCurrentIndex(data["Jgr Brigade add2 bttln"][0])

        if "Comb Grndr Brigade Commander" in data.keys():
            # проверяем и устанавливаем бонусы батальона
            self.load_procedure_set_bonuses(data, "Comb Grndr Brigade 1st bttln", 0, data["Comb Grndr Brigade 1st bttln"][0]+1, self.comb_grndr_brigade_number)
            self.load_procedure_set_bonuses(data, "Comb Grndr Brigade 2nd bttln", 1, data["Comb Grndr Brigade 2nd bttln"][0]+1, self.comb_grndr_brigade_number)

            self.CombGrndrBrgdCmndr.setCurrentIndex(data["Comb Grndr Brigade Commander"])

            self.load_procedure_set_bonuses(data, "Comb Grndr Brigade 3rd bttln", 2, data["Comb Grndr Brigade 3rd bttln"][0], self.comb_grndr_brigade_number)
            self.CombGrndrBrgdThirdBattalion.setCurrentIndex(data["Comb Grndr Brigade 3rd bttln"][0])

            self.load_procedure_set_bonuses(data, "Comb Grndr Brigade 4th bttln", 3, data["Comb Grndr Brigade 4th bttln"][0], self.comb_grndr_brigade_number)
            self.CombGrndrBrgdFourthBattalion.setCurrentIndex(data["Comb Grndr Brigade 4th bttln"][0])

            self.load_procedure_set_bonuses(data, "Comb Grndr Brigade 5th bttln", 4, data["Comb Grndr Brigade 5th bttln"][0], self.comb_grndr_brigade_number)
            self.CombGrndrBrgdFifthBattalion.setCurrentIndex(data["Comb Grndr Brigade 5th bttln"][0])

            self.load_procedure_set_bonuses(data, "Comb Grndr Brigade 6th bttln", 5, data["Comb Grndr Brigade 6th bttln"][0], self.comb_grndr_brigade_number)
            self.CombGrndrBrgdSixthBattalion.setCurrentIndex(data["Comb Grndr Brigade 6th bttln"][0])

            self.load_procedure_set_bonuses(data, "Comb Grndr Brigade 7th bttln", 6, data["Comb Grndr Brigade 7th bttln"][0], self.comb_grndr_brigade_number)
            self.CombGrndrBrgdSeventhBattalion.setCurrentIndex(data["Comb Grndr Brigade 7th bttln"][0])

        if "Grndr Brigade Commander" in data.keys():
            # проверяем и устанавливаем бонусы батальона
            self.load_procedure_set_bonuses(data, "Grndr Brigade 1st bttln", 0, data["Grndr Brigade 1st bttln"][0]+1, self.grndr_brigade_number)
            self.GrndrBrgdCmndr.setCurrentIndex(data["Grndr Brigade Commander"])

            self.load_procedure_set_bonuses(data, "Grndr Brigade 2nd bttln", 1, data["Grndr Brigade 2nd bttln"][0], self.grndr_brigade_number)
            self.GrndrBrgdSecondBattalion.setCurrentIndex(data["Grndr Brigade 2nd bttln"][0])

            self.load_procedure_set_bonuses(data, "Grndr Brigade 3rd bttln", 2, data["Grndr Brigade 3rd bttln"][0], self.grndr_brigade_number)
            self.GrndrBrgdThirdBattalion.setCurrentIndex(data["Grndr Brigade 3rd bttln"][0])

            self.load_procedure_set_bonuses(data, "Grndr Brigade 4th bttln", 3, data["Grndr Brigade 4th bttln"][0], self.grndr_brigade_number)
            self.GrndrBrgdFourthBattalion.setCurrentIndex(data["Grndr Brigade 4th bttln"][0])

        if "L Cvlry Brigade Commander" in data.keys():
            # проверяем и устанавливаем бонусы батальона
            self.load_procedure_set_bonuses(data, "L Cvlry Brigade 1st rgmnt", 0, data["L Cvlry Brigade 1st rgmnt"][0]+1,self.light_cvlry_brigade_number)
            self.LCvlryBrgdCmndr.setCurrentIndex(data["L Cvlry Brigade Commander"])
            self.LCvlryBrgdFirstBattalion.setCurrentIndex(data["L Cvlry Brigade 1st rgmnt"][0])

            self.load_procedure_set_bonuses(data, "L Cvlry Brigade 2nd rgmnt", 1, data["L Cvlry Brigade 2nd rgmnt"][0], self.light_cvlry_brigade_number)
            self.LCvlryBrgdSecondBattalion.setCurrentIndex(data["L Cvlry Brigade 2nd rgmnt"][0])

            self.load_procedure_set_bonuses(data, "L Cvlry Brigade 3rd rgmnt", 2, data["L Cvlry Brigade 3rd rgmnt"][0], self.light_cvlry_brigade_number)
            self.LCvlryBrgdThirdBattalion.setCurrentIndex(data["L Cvlry Brigade 3rd rgmnt"][0])

        if "H Cvlry Brigade Commander" in data.keys():
            # проверяем и устанавливаем бонусы батальона
            self.load_procedure_set_bonuses(data, "H Cvlry Brigade 1st rgmnt", 0, data["H Cvlry Brigade 1st rgmnt"][0]+1, self.heavy_cvlry_brigade_number)
            self.HCvlryBrgdCmndr.setCurrentIndex(data["H Cvlry Brigade Commander"])
            self.HCvlryBrgdFirstBattalion.setCurrentIndex(data["H Cvlry Brigade 1st rgmnt"][0])

            self.load_procedure_set_bonuses(data, "H Cvlry Brigade 2nd rgmnt", 1, data["H Cvlry Brigade 2nd rgmnt"][0], self.heavy_cvlry_brigade_number)
            self.HCvlryBrgdSecondBattalion.setCurrentIndex(data["H Cvlry Brigade 2nd rgmnt"][0])

            self.load_procedure_set_bonuses(data, "H Cvlry Brigade 3rd rgmnt", 2, data["H Cvlry Brigade 3rd rgmnt"][0], self.heavy_cvlry_brigade_number)
            self.HCvlryBrgdThirdBattalion.setCurrentIndex(data["H Cvlry Brigade 3rd rgmnt"][0])

        if "Cossack Brigade Commander" in data.keys():
            # проверяем и устанавливаем бонусы батальона
            self.load_procedure_set_bonuses(data, "Cossack Brigade 1st rgmnt", 0, data["Cossack Brigade 1st rgmnt"][0]+1, self.cossack_brigade_number)
            self.load_procedure_set_bonuses(data, "Cossack Brigade 2nd rgmnt", 1, data["Cossack Brigade 2nd rgmnt"][0]+1, self.cossack_brigade_number)
            self.CossackBrgdCmndr.setCurrentIndex(data["Cossack Brigade Commander"])
            self.CossackBrgdFirstBattalion.setCurrentIndex(data["Cossack Brigade 1st rgmnt"][0])
            self.CossackBrgdSecondBattalion.setCurrentIndex(data["Cossack Brigade 2nd rgmnt"][0])

            self.load_procedure_set_bonuses(data, "Cossack Brigade 3rd rgmnt", 2, data["Cossack Brigade 3rd rgmnt"][0], self.cossack_brigade_number)
            self.CossackBrgdThirdBattalion.setCurrentIndex(data["Cossack Brigade 3rd rgmnt"][0])

            self.load_procedure_set_bonuses(data, "Cossack Brigade 4th rgmnt", 3, data["Cossack Brigade 4th rgmnt"][0], self.cossack_brigade_number)
            self.CossackBrgdFourthBattalion.setCurrentIndex(data["Cossack Brigade 4th rgmnt"][0])

            self.load_procedure_set_bonuses(data, "Cossack Brigade 5th rgmnt", 4, data["Cossack Brigade 5th rgmnt"][0], self.cossack_brigade_number)
            self.CossackBrgdFifthBattalion.setCurrentIndex(data["Cossack Brigade 5th rgmnt"][0])

            self.load_procedure_set_bonuses(data, "Cossack Brigade 6th rgmnt", 5, data["Cossack Brigade 6th rgmnt"][0], self.cossack_brigade_number)
            self.CossackBrgdSixthBattalion.setCurrentIndex(data["Cossack Brigade 6th rgmnt"][0])

        if "Imp Grd Inf Brigade Commander" in data.keys():
            # проверяем и устанавливаем бонусы батальона
            self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade 1st bttln", 0, data["Imp Grd Inf Brigade 1st bttln"][0]+1, self.imp_grd_inf_brigade_number)
            self.ImpGrdInfBrgdCmndr.setCurrentIndex(data["Imp Grd Inf Brigade Commander"])

            self.ImpGrdInfBrgdFirstBattalion.setCurrentIndex(data["Imp Grd Inf Brigade 1st bttln"][0])

            self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade 2nd bttln", 1, data["Imp Grd Inf Brigade 2nd bttln"][0], self.imp_grd_inf_brigade_number)
            self.ImpGrdInfBrgdSecondBattalion.setCurrentIndex(data["Imp Grd Inf Brigade 2nd bttln"][0])

            self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade 3rd bttln", 2, data["Imp Grd Inf Brigade 3rd bttln"][0], self.imp_grd_inf_brigade_number)
            self.ImpGrdInfBrgdThirdBattalion.setCurrentIndex(data["Imp Grd Inf Brigade 3rd bttln"][0])

            self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade 4th bttln", 3, data["Imp Grd Inf Brigade 4th bttln"][0], self.imp_grd_inf_brigade_number)
            self.ImpGrdInfBrgdFourthBattalion.setCurrentIndex(data["Imp Grd Inf Brigade 4th bttln"][0])

            self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade 5th bttln", 4, data["Imp Grd Inf Brigade 5th bttln"][0], self.imp_grd_inf_brigade_number)
            self.ImpGrdInfBrgdFifthBattalion.setCurrentIndex(data["Imp Grd Inf Brigade 5th bttln"][0])

            self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade 6th bttln", 5, data["Imp Grd Inf Brigade 6th bttln"][0], self.imp_grd_inf_brigade_number)
            self.ImpGrdInfBrgdSixthBattalion.setCurrentIndex(data["Imp Grd Inf Brigade 6th bttln"][0])

            self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade add1 bttln", 6, data["Imp Grd Inf Brigade add1 bttln"][0], self.imp_grd_inf_brigade_number)
            self.ImpGrdInfBrgdAdditional1Battalion.setCurrentIndex(data["Imp Grd Inf Brigade add1 bttln"][0])

            self.load_procedure_set_bonuses(data, "Imp Grd Inf Brigade add2 bttln", 7, data["Imp Grd Inf Brigade add2 bttln"][0], self.imp_grd_inf_brigade_number)
            self.ImpGrdInfBrgdAdditional2Battalion.setCurrentIndex(data["Imp Grd Inf Brigade add2 bttln"][0])

        if "Imp Grd L Cav Brigade Commander" in data.keys():
            # проверяем и устанавливаем бонусы батальона
            self.load_procedure_set_bonuses(data, "Imp Grd L Cav Brigade 1st rgmnt", 0, data["Imp Grd L Cav Brigade 1st rgmnt"][0]+1, self.imp_grd_l_cav_brigade_number)
            self.ImpGrdLCavBrgdCmndr.setCurrentIndex(data["Imp Grd L Cav Brigade Commander"])

            self.ImpGrdLCavBrgdFirstBattalion.setCurrentIndex(data["Imp Grd L Cav Brigade 1st rgmnt"][0])

            self.load_procedure_set_bonuses(data, "Imp Grd L Cav Brigade 2nd rgmnt", 1, data["Imp Grd L Cav Brigade 2nd rgmnt"][0], self.imp_grd_l_cav_brigade_number)
            self.ImpGrdLCavBrgdSecondBattalion.setCurrentIndex(data["Imp Grd L Cav Brigade 2nd rgmnt"][0])

        if "Imp Grd H Cav Brigade Commander" in data.keys():
            # проверяем и устанавливаем бонусы батальона
            self.load_procedure_set_bonuses(data, "Imp Grd H Cav Brigade 1st rgmnt", 0, data["Imp Grd H Cav Brigade 1st rgmnt"][0]+1, self.imp_grd_h_cav_brigade_number)
            self.ImpGrdHCavBrgdCmndr.setCurrentIndex(data["Imp Grd H Cav Brigade Commander"])

            self.ImpGrdHCavBrgdFirstBattalion.setCurrentIndex(data["Imp Grd H Cav Brigade 1st rgmnt"][0])

            self.load_procedure_set_bonuses(data, "Imp Grd H Cav Brigade 2nd rgmnt", 1, data["Imp Grd H Cav Brigade 2nd rgmnt"][0], self.imp_grd_h_cav_brigade_number)
            self.ImpGrdHCavBrgdSecondBattalion.setCurrentIndex(data["Imp Grd H Cav Brigade 2nd rgmnt"][0])

        self.LightArtilleryBattery1.setCurrentIndex(data["Light Artillery Battery 1"][0])
        self.LightArtilleryBattery2.setCurrentIndex(data["Light Artillery Battery 2"][0])
        self.LightArtilleryBattery3.setCurrentIndex(data["Light Artillery Battery 3"][0])
        self.LightArtilleryBattery4.setCurrentIndex(data["Light Artillery Battery 4"][0])
        self.LightArtilleryBattery5.setCurrentIndex(data["Light Artillery Battery 5"][0])
        self.LightArtilleryBattery6.setCurrentIndex(data["Light Artillery Battery 6"][0])

        self.HeavyArtilleryBattery1.setCurrentIndex(data["Heavy Artillery Battery 1"][0])
        self.HeavyArtilleryBattery2.setCurrentIndex(data["Heavy Artillery Battery 2"][0])
        self.HeavyArtilleryBattery3.setCurrentIndex(data["Heavy Artillery Battery 3"][0])
        self.HeavyArtilleryBattery4.setCurrentIndex(data["Heavy Artillery Battery 4"][0])

        self.UnicornBattery1.setCurrentIndex(data["Unicorn Battery 1"][0])
        self.UnicornBattery2.setCurrentIndex(data["Unicorn Battery 2"][0])
        self.UnicornBattery3.setCurrentIndex(data["Unicorn Battery 3"][0])
        self.UnicornBattery4.setCurrentIndex(data["Unicorn Battery 4"][0])
        self.UnicornBattery5.setCurrentIndex(data["Unicorn Battery 5"][0])
        self.UnicornBattery6.setCurrentIndex(data["Unicorn Battery 6"][0])

        self.HorseArtilleryBattery1.setCurrentIndex(data["Horse Artillery Battery 1"][0])
        self.HorseArtilleryBattery2.setCurrentIndex(data["Horse Artillery Battery 2"][0])
        self.HorseArtilleryBattery3.setCurrentIndex(data["Horse Artillery Battery 3"][0])

        self.EarthWorks1.setCurrentIndex(data["EarthWorks 1"][0])
        self.EarthWorks2.setCurrentIndex(data["EarthWorks 2"][0])


    def load_procedure_set_bonuses(self, data, bttln_name, place_in_br_list, order_in_bttln_list, brgd_number):
        for bonus_name, v in data[bttln_name][1].items():
            bonus_cost = 0
            for i in range(0, len(self.presenter.BrigadeBonusNameList(brgd_number))):
                if bonus_name == self.presenter.BrigadeBonusNameList(brgd_number)[i]:
                    bonus_cost = self.presenter.BrigadeBonusCostList(brgd_number)[i]
            self.presenter.BrigadeBttlnListBonusAdd(bonus_name, place_in_br_list, order_in_bttln_list, brgd_number)
            self.presenter.BrigadeBttlnListBonusCostAdd(bonus_cost, place_in_br_list, order_in_bttln_list, brgd_number)

    def exportToPDF(self):

        fileName, _= QFileDialog.getSaveFileName(
            parent=self,
            caption='Select a pdf file',
            filter='Pdf File (*.pdf)'
        )

        if fileName:
            try:
                self.dataToSavePdf(fileName)
            except:
                self.error_message.text("pdf export error")
                self.error_message.show()
        else:
            pass



    def dataToSavePdf(self, fileName):

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.add_font('FontNS', '', 'Fonts\\Noto Sans\\NotoSans-Regular.ttf')
        pdf.add_font('FontNS', 'B', 'Fonts\\Noto Sans\\NotoSans-Bold.ttf')
        pdf.add_font('FontNS', 'I', 'Fonts\\Noto Sans\\NotoSans-Italic.ttf')
        pdf.add_font('FontNS', 'BI', 'Fonts\\Noto Sans\\NotoSans-BoldItalic.ttf')

        pdf.set_font('FontNS', '', 8)
        pdf.cell(10, 8, "Black Powder 2.0 Army Builder", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font('FontNS', 'B', 14)
        pdf.cell(0, 8, "Imperial Russian Army Division list", align='C', new_x=XPos.LMARGIN)
        pdf.set_font('FontNS', 'B', 10)
        pdf.cell(0, 8, f'Total cost: {self.divisionTotalCost.text()}', align=Align.R, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.print_line(pdf)
# запрашиваем и печатаем имя, стоимость и умения дивизионного командира
        pdf.set_font('FontNS', 'I', 10)
        pdf.cell(0, 8, "Division commander", new_x=XPos.LMARGIN)
        pdf.cell(0, 8, "Cost", align=Align.R, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font('FontNS', 'B', 10)
        pdf.cell(0, 8, f'{self.presenter.DivisionCmndrName(self.generalName.currentIndex())}', new_x=XPos.LMARGIN)
        pdf.cell(0, 8, f'{self.presenter.DivisionCmndrCost(self.generalName.currentIndex())}', align=Align.R, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font('FontNS', '', 8)
        pdf.multi_cell(0, 4, f'Skills: {self.presenter.DivisionCmndrSkills(self.generalName.currentIndex())}', new_x=XPos.LMARGIN,  new_y=YPos.NEXT)
        self.print_line(pdf)
        pdf.set_font('FontNS', 'I', 10)
        pdf.cell(0, 8, "Cost", align=Align.R, new_x=XPos.LMARGIN, new_y=YPos.NEXT)


        brigades_and_battalions = []
        brigades_and_battalions.append(["Line Infantry Brigade", self.aBrgdCmndr, self.aBrgdTotalCost, self.a_brigade_number, 6])
        brigades_and_battalions.append(["Line Infantry Brigade", self.bBrgdCmndr, self.bBrgdTotalCost, self.b_brigade_number, 6])
        brigades_and_battalions.append(["Line Infantry Brigade", self.cBrgdCmndr, self.cBrgdTotalCost, self.c_brigade_number, 6])
        brigades_and_battalions.append(["Jager Brigade", self.JgrBrgdCmndr, self.JgrBrgdTotalCost, self.jgr_brigade_number, 8])
        brigades_and_battalions.append(["Combine Grenadier Brigade", self.CombGrndrBrgdCmndr, self.CombGrndrBrgdTotalCost, self.comb_grndr_brigade_number, 7])
        brigades_and_battalions.append(["Grenadier Brigade", self.GrndrBrgdCmndr, self.GrndrBrgdTotalCost, self.grndr_brigade_number, 4])
        brigades_and_battalions.append(["Light Cavalry Brigade", self.LCvlryBrgdCmndr, self.LCvlryBrgdTotalCost, self.light_cvlry_brigade_number, 3])
        brigades_and_battalions.append(["Heavy Cavalry Brigade", self.HCvlryBrgdCmndr, self.HCvlryBrgdTotalCost, self.heavy_cvlry_brigade_number, 3])
        brigades_and_battalions.append(["Cossack Brigade", self.CossackBrgdCmndr, self.CossackBrgdTotalCost, self.cossack_brigade_number, 6])
        brigades_and_battalions.append(["Imperial Guard Infantry Brigade", self.ImpGrdInfBrgdCmndr, self.ImpGrdInfBrgdTotalCost, self.imp_grd_inf_brigade_number, 8])
        brigades_and_battalions.append(["Imperial Guard Light Cavalry Brigade", self.ImpGrdLCavBrgdCmndr, self.ImpGrdLCavBrgdTotalCost, self.imp_grd_l_cav_brigade_number, 2])
        brigades_and_battalions.append(["Imperial Guard Heavy Cavalry Brigade", self.ImpGrdHCavBrgdCmndr, self.ImpGrdHCavBrgdTotalCost, self.imp_grd_h_cav_brigade_number, 2])

        for i in range (0, len(brigades_and_battalions)):
           self.brigade_title_print(pdf, brigades_and_battalions[i][0], brigades_and_battalions[i][1], brigades_and_battalions[i][2], brigades_and_battalions[i][3], brigades_and_battalions[i][4], "Battalion")


        artillery_presence = 0
        for i in range (0, 19):
            artillery_presence += self.presenter.BrigadeBttlnPresence(i, self.artillery_quasy_brigade_number)
        if artillery_presence > 0:
            self.print_line(pdf)
            pdf.set_font('FontNS', 'B', 10)
            pdf.cell(0, 8, 'Artillery', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

            for order_number in range(0, 19):
                if self.presenter.BrigadeBttlnName(order_number, self.artillery_quasy_brigade_number) != "empty":
                    self.battalion_print(pdf, order_number, self.artillery_quasy_brigade_number, "Battery")

        earthworks_presence = 0
        for i in range (0, 2):
            earthworks_presence += self.presenter.BrigadeBttlnPresence(i, self.earthworks_quasy_brigade_number)
        if earthworks_presence > 0:
            self.print_line(pdf)
            pdf.set_font('FontNS', 'B', 10)
            pdf.cell(0, 8, 'EarthWorks', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

            for order_number in range(0, 2):
                if self.presenter.BrigadeBttlnName(order_number, self.earthworks_quasy_brigade_number) != "empty":
                    self.battalion_print(pdf, order_number, self.earthworks_quasy_brigade_number, 'EarthWorks')
            self.print_line(pdf)

        pdf.output(fileName)
    def brigade_title_print(self, pdf, x_brigade_name, xBrgdCmndr, xBrgdTotalCost,x_brigade_number, number_of_battalions, flag):

        # запрашиваем и печатаем (если выбран) имя и стоимость бригадного командира
        if xBrgdCmndr.currentIndex() != 0:
            self.print_line(pdf)
            pdf.set_font('FontNS', 'B', 10)
            pdf.cell(0, 8, f'{x_brigade_name}', new_x=XPos.LMARGIN)
            pdf.cell(0, 8, f'{xBrgdTotalCost.text()}', align=Align.R, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.set_font('FontNS', 'I', 10)
            pdf.cell(0, 8, f'Brigade Commander: ', new_x=XPos.END)
            pdf.set_font('FontNS', '', 10)
            pdf.cell(0, 8, f'{self.presenter.BrigadeCmndrsName(xBrgdCmndr.currentIndex(), x_brigade_number)}',
                     new_x=XPos.LMARGIN)
            pdf.cell(0, 8, f'{self.presenter.BrigadeCmndrsCost(xBrgdCmndr.currentIndex(), x_brigade_number)}',
                     align=Align.R, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

            for order_number in range(0, number_of_battalions):
                # запрашиваем и печатаем имя , стоимость и бонусы  батальона (если он есть)
                if self.presenter.BrigadeBttlnName(order_number, x_brigade_number) != "empty":
                    self.battalion_print(pdf, order_number, x_brigade_number, flag)
                    

    def print_line(self, pdf):
        pdf.set_font('FontNS', '', 8)
        line = "_" * 162
        pdf.cell(0, 0, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def battalion_print (self, pdf, order_number, brigade_number, flag):
        pdf.set_font('FontNS', 'I', 10)
        pdf.cell(0, 8, f'{flag}: ', new_x=XPos.END)
        pdf.set_font('FontNS', '', 10)
        pdf.cell(0, 8, f'{self.presenter.BrigadeBttlnName(order_number, brigade_number)}', new_x=XPos.LMARGIN)
        pdf.cell(0, 8, f'{self.presenter.BrigadeBttlnCost(order_number, brigade_number)}', align=Align.R,
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        if self.presenter.BrigadeBttlnBonusList(order_number, brigade_number):
            pdf.set_font('FontNS', '', 8)
            pdf.cell(0, 5, f'         Specials:  {self.presenter.BrigadeBttlnSpecials(order_number, brigade_number)}', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

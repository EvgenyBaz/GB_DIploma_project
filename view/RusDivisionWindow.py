import json

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog
from fpdf import FPDF, XPos, YPos, Align

from presenter.presenter import Presenter
from view.RusDivisionGuiWindow import Ui_RusDivisionWindow
from view.BonusWindow import BonusWindow
from view.E_message import MessageWindow

from view.brigades.brigade_view import brigade_bttln_Lists


class RusDivisionWindow(QtWidgets.QMainWindow, Ui_RusDivisionWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(RusDivisionWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.error_message = MessageWindow()

        self.actionSave.triggered.connect(self.saveFile)
        self.actionExport_army_list_to_PDF.triggered.connect(self.exportToPDF)

        self.country = "Rus"  # определяем страну
        self.presenter = Presenter(self.country)

        self.generalName.currentIndexChanged.connect(self.divisionCommanderCostView)
        # изменяемая переменная для прхождения проверки  - используется для кавполков с неоднозначным выбором первого полка в списке, при изменении списка
        self.a_brigade_number = 0  # номер бригады попорядку
        self.a_battalion_index_add = 0

        self.aBrgdCmndr.currentIndexChanged.connect(self.aBrgdCommanderCostView)
        self.aBrgdFirstBattalion.currentIndexChanged.connect(self.aBrgd1stBttlnCostView)
        self.aBrgdSecondBattalion.currentIndexChanged.connect(self.aBrgd2ndBttlnCostView)
        self.aBrgdThirdBattalion.currentIndexChanged.connect(self.aBrgd3rdBttlnCostView)
        self.aBrgdFourthBattalion.currentIndexChanged.connect(self.aBrgd4thBttlnCostView)
        self.aBrgdAdditionalBattalion.currentIndexChanged.connect(self.aBrgdAddBttlnCostView)
        self.aBrgdJgrAdditionalBattalion.currentIndexChanged.connect(self.aBrgdJgrAddBttlnCostView)

        self.aBrFirstBttlnModPushButton.clicked.connect(self.a_the_first_bttln_mod_button_was_clicked)
        self.aBrSecondBttlnModPushButton.clicked.connect(self.a_the_second_bttln_mod_button_was_clicked)
        self.aBrThirdBttlnModPushButton.clicked.connect(self.a_the_third_bttln_mod_button_was_clicked)
        self.aBrFourthBttlnModPushButton.clicked.connect(self.a_the_fourth_bttln_mod_button_was_clicked)
        self.aBrAddBttlnModPushButton.clicked.connect(self.a_the_add_bttln_mod_button_was_clicked)
        self.aBrJgrAddBttlnModPushButton.clicked.connect(self.a_the_jgr_add_bttln_mod_button_was_clicked)

        self.b_brigade_number = 1
        self.b_battalion_index_add = 0

        self.bBrgdCmndr.currentIndexChanged.connect(self.bBrgdCommanderCostView)
        self.bBrgdFirstBattalion.currentIndexChanged.connect(self.bBrgd1stBttlnCostView)
        self.bBrgdSecondBattalion.currentIndexChanged.connect(self.bBrgd2ndBttlnCostView)
        self.bBrgdThirdBattalion.currentIndexChanged.connect(self.bBrgd3rdBttlnCostView)
        self.bBrgdFourthBattalion.currentIndexChanged.connect(self.bBrgd4thBttlnCostView)
        self.bBrgdAdditionalBattalion.currentIndexChanged.connect(self.bBrgdAddBttlnCostView)
        self.bBrgdJgrAdditionalBattalion.currentIndexChanged.connect(self.bBrgdJgrAddBttlnCostView)

        self.bBrFirstBttlnModPushButton.clicked.connect(self.b_the_first_bttln_mod_button_was_clicked)
        self.bBrSecondBttlnModPushButton.clicked.connect(self.b_the_second_bttln_mod_button_was_clicked)
        self.bBrThirdBttlnModPushButton.clicked.connect(self.b_the_third_bttln_mod_button_was_clicked)
        self.bBrFourthBttlnModPushButton.clicked.connect(self.b_the_fourth_bttln_mod_button_was_clicked)
        self.bBrAddBttlnModPushButton.clicked.connect(self.b_the_add_bttln_mod_button_was_clicked)
        self.bBrJgrAddBttlnModPushButton.clicked.connect(self.b_the_jgr_add_bttln_mod_button_was_clicked)

        self.c_brigade_number = 2
        self.c_battalion_index_add = 0

        self.cBrgdCmndr.currentIndexChanged.connect(self.cBrgdCommanderCostView)
        self.cBrgdFirstBattalion.currentIndexChanged.connect(self.cBrgd1stBttlnCostView)
        self.cBrgdSecondBattalion.currentIndexChanged.connect(self.cBrgd2ndBttlnCostView)
        self.cBrgdThirdBattalion.currentIndexChanged.connect(self.cBrgd3rdBttlnCostView)
        self.cBrgdFourthBattalion.currentIndexChanged.connect(self.cBrgd4thBttlnCostView)
        self.cBrgdAdditionalBattalion.currentIndexChanged.connect(self.cBrgdAddBttlnCostView)
        self.cBrgdJgrAdditionalBattalion.currentIndexChanged.connect(self.cBrgdJgrAddBttlnCostView)

        self.cBrFirstBttlnModPushButton.clicked.connect(self.c_the_first_bttln_mod_button_was_clicked)
        self.cBrSecondBttlnModPushButton.clicked.connect(self.c_the_second_bttln_mod_button_was_clicked)
        self.cBrThirdBttlnModPushButton.clicked.connect(self.c_the_third_bttln_mod_button_was_clicked)
        self.cBrFourthBttlnModPushButton.clicked.connect(self.c_the_fourth_bttln_mod_button_was_clicked)
        self.cBrAddBttlnModPushButton.clicked.connect(self.c_the_add_bttln_mod_button_was_clicked)
        self.cBrJgrAddBttlnModPushButton.clicked.connect(self.c_the_jgr_add_bttln_mod_button_was_clicked)

        self.jgr_brigade_number = 3
        self.jgr_battalion1_index_add = 0
        self.jgr_battalion2_index_add = 0

        self.JgrBrgdCmndr.currentIndexChanged.connect(self.jgrBrgdCommanderCostView)
        self.JgrBrgdFirstBattalion.currentIndexChanged.connect(self.jgrBrgd1stBttlnCostView)
        self.JgrBrgdSecondBattalion.currentIndexChanged.connect(self.jgrBrgd2ndBttlnCostView)
        self.JgrBrgdThirdBattalion.currentIndexChanged.connect(self.jgrBrgd3rdBttlnCostView)
        self.JgrBrgdFourthBattalion.currentIndexChanged.connect(self.jgrBrgd4thBttlnCostView)
        self.JgrBrgdFifthBattalion.currentIndexChanged.connect(self.jgrBrgd5thBttlnCostView)
        self.JgrBrgdSixthBattalion.currentIndexChanged.connect(self.jgrBrgd6thBttlnCostView)
        self.JgrBrgdAdditional1Battalion.currentIndexChanged.connect(self.jgrBrgdAdd1BttlnCostView)
        self.JgrBrgdAdditional2Battalion.currentIndexChanged.connect(self.jgrBrgdAdd2BttlnCostView)

        self.JgrBrFirstBttlnModPushButton.clicked.connect(self.jgr_the_first_bttln_mod_button_was_clicked)
        self.JgrBrSecondBttlnModPushButton.clicked.connect(self.jgr_the_second_bttln_mod_button_was_clicked)
        self.JgrBrThirdBttlnModPushButton.clicked.connect(self.jgr_the_third_bttln_mod_button_was_clicked)
        self.JgrBrFourthBttlnModPushButton.clicked.connect(self.jgr_the_fourth_bttln_mod_button_was_clicked)
        self.JgrBrFifthBttlnModPushButton.clicked.connect(self.jgr_the_fifth_bttln_mod_button_was_clicked)
        self.JgrBrSixthBttlnModPushButton.clicked.connect(self.jgr_the_sixth_bttln_mod_button_was_clicked)

        self.comb_grndr_brigade_number = 4
        self.comb_grndr_battalion1_index_add = 0
        self.comb_grndr_battalion2_index_add = 0

        self.CombGrndrBrgdCmndr.currentIndexChanged.connect(self.combGrndrBrgdCommanderCostView)
        self.CombGrndrBrgdFirstBattalion.currentIndexChanged.connect(self.combGrndrBrgd1stBttlnCostView)
        self.CombGrndrBrgdSecondBattalion.currentIndexChanged.connect(self.combGrndrBrgd2ndBttlnCostView)
        self.CombGrndrBrgdThirdBattalion.currentIndexChanged.connect(self.combGrndrBrgd3rdBttlnCostView)
        self.CombGrndrBrgdFourthBattalion.currentIndexChanged.connect(self.combGrndrBrgd4thBttlnCostView)
        self.CombGrndrBrgdFifthBattalion.currentIndexChanged.connect(self.combGrndrBrgd5thBttlnCostView)
        self.CombGrndrBrgdSixthBattalion.currentIndexChanged.connect(self.combGrndrBrgd6thBttlnCostView)
        self.CombGrndrBrgdSeventhBattalion.currentIndexChanged.connect(self.combGrndrBrgd7thBttlnCostView)

        self.CombGrndrBrFirstBttlnModPushButton.clicked.connect(self.comb_grndr_the_first_bttln_mod_button_was_clicked)
        self.CombGrndrBrSecondBttlnModPushButton.clicked.connect(self.comb_grndr_the_second_bttln_mod_button_was_clicked)
        self.CombGrndrBrThirdBttlnModPushButton.clicked.connect(self.comb_grndr_the_third_bttln_mod_button_was_clicked)
        self.CombGrndrBrFourthBttlnModPushButton.clicked.connect(self.comb_grndr_the_fourth_bttln_mod_button_was_clicked)
        self.CombGrndrBrFifthBttlnModPushButton.clicked.connect(self.comb_grndr_the_fifth_bttln_mod_button_was_clicked)
        self.CombGrndrBrSixthBttlnModPushButton.clicked.connect(self.comb_grndr_the_sixth_bttln_mod_button_was_clicked)
        self.CombGrndrBrSeventhBttlnModPushButton.clicked.connect(self.comb_grndr_the_seventh_bttln_mod_button_was_clicked)

        self.grndr_brigade_number = 5
        self.grndr_battalion_index_add = 0

        self.GrndrBrgdCmndr.currentIndexChanged.connect(self.grndrBrgdCommanderCostView)
        self.GrndrBrgdFirstBattalion.currentIndexChanged.connect(self.grndrBrgd1stBttlnCostView)
        self.GrndrBrgdSecondBattalion.currentIndexChanged.connect(self.grndrBrgd2ndBttlnCostView)
        self.GrndrBrgdThirdBattalion.currentIndexChanged.connect(self.grndrBrgd3rdBttlnCostView)
        self.GrndrBrgdFourthBattalion.currentIndexChanged.connect(self.grndrBrgd4thBttlnCostView)

        self.GrndrBrFirstBttlnModPushButton.clicked.connect(self.grndr_the_first_bttln_mod_button_was_clicked)
        self.GrndrBrSecondBttlnModPushButton.clicked.connect(self.grndr_the_second_bttln_mod_button_was_clicked)
        self.GrndrBrThirdBttlnModPushButton.clicked.connect(self.grndr_the_third_bttln_mod_button_was_clicked)
        self.GrndrBrFourthBttlnModPushButton.clicked.connect(self.grndr_the_fourth_bttln_mod_button_was_clicked)

        self.light_cvlry_brigade_number = 6
        self.l_cvlry_battalion_index_add = 0

        self.LCvlryBrgdCmndr.currentIndexChanged.connect(self.lightCvlryBrgdCommanderCostView)
        self.LCvlryBrgdFirstBattalion.currentIndexChanged.connect(self.lightCvlryBrgd1stBttlnCostView)
        self.LCvlryBrgdSecondBattalion.currentIndexChanged.connect(self.lightCvlryBrgd2ndBttlnCostView)
        self.LCvlryBrgdThirdBattalion.currentIndexChanged.connect(self.lightCvlryBrgd3rdBttlnCostView)

        self.LCvlryBrFirstBttlnModPushButton.clicked.connect(self.lightCvlry_the_first_bttln_mod_button_was_clicked)
        self.LCvlryBrSecondBttlnModPushButton.clicked.connect(self.lightCvlry_the_second_bttln_mod_button_was_clicked)
        self.LCvlryBrThirdBttlnModPushButton.clicked.connect(self.lightCvlry_the_third_bttln_mod_button_was_clicked)

        self.heavy_cvlry_brigade_number = 7
        self.h_cvlry_battalion_index_add = 0

        self.HCvlryBrgdCmndr.currentIndexChanged.connect(self.heavyCvlryBrgdCommanderCostView)
        self.HCvlryBrgdFirstBattalion.currentIndexChanged.connect(self.heavyCvlryBrgd1stBttlnCostView)
        self.HCvlryBrgdSecondBattalion.currentIndexChanged.connect(self.heavyCvlryBrgd2ndBttlnCostView)
        self.HCvlryBrgdThirdBattalion.currentIndexChanged.connect(self.heavyCvlryBrgd3rdBttlnCostView)

        self.HCvlryBrFirstBttlnModPushButton.clicked.connect(self.heavyCvlry_the_first_bttln_mod_button_was_clicked)
        self.HCvlryBrSecondBttlnModPushButton.clicked.connect(self.heavyCvlry_the_second_bttln_mod_button_was_clicked)
        self.HCvlryBrThirdBttlnModPushButton.clicked.connect(self.heavyCvlry_the_third_bttln_mod_button_was_clicked)

        self.cossack_brigade_number = 8
        self.cossack_battalion1_index_add = 0
        self.cossack_battalion2_index_add = 0

        self.CossackBrgdCmndr.currentIndexChanged.connect(self.cossackBrgdCommanderCostView)
        self.CossackBrgdFirstBattalion.currentIndexChanged.connect(self.cossackBrgd1stBttlnCostView)
        self.CossackBrgdSecondBattalion.currentIndexChanged.connect(self.cossackBrgd2ndBttlnCostView)
        self.CossackBrgdThirdBattalion.currentIndexChanged.connect(self.cossackBrgd3rdBttlnCostView)
        self.CossackBrgdFourthBattalion.currentIndexChanged.connect(self.cossackBrgd4thBttlnCostView)
        self.CossackBrgdFifthBattalion.currentIndexChanged.connect(self.cossackBrgd5thBttlnCostView)
        self.CossackBrgdSixthBattalion.currentIndexChanged.connect(self.cossackBrgd6thBttlnCostView)

        self.CossackBrFirstBttlnModPushButton.clicked.connect(self.cossack_the_first_bttln_mod_button_was_clicked)
        self.CossackBrSecondBttlnModPushButton.clicked.connect(self.cossack_the_second_bttln_mod_button_was_clicked)
        self.CossackBrThirdBttlnModPushButton.clicked.connect(self.cossack_the_third_bttln_mod_button_was_clicked)
        self.CossackBrFourthBttlnModPushButton.clicked.connect(self.cossack_the_fourth_bttln_mod_button_was_clicked)
        self.CossackBrFifthBttlnModPushButton.clicked.connect(self.cossack_the_fifth_bttln_mod_button_was_clicked)
        self.CossackBrSixthBttlnModPushButton.clicked.connect(self.cossack_the_sixth_bttln_mod_button_was_clicked)

        self.imp_grd_inf_brigade_number = 9
        self.imp_grd_inf_battalion_index_add = 0

        self.ImpGrdInfBrgdCmndr.currentIndexChanged.connect(self.impGrdInfBrgdCommanderCostView)
        self.ImpGrdInfBrgdFirstBattalion.currentIndexChanged.connect(self.impGrdInfBrgd1stBttlnCostView)
        self.ImpGrdInfBrgdSecondBattalion.currentIndexChanged.connect(self.impGrdInfBrgd2ndBttlnCostView)
        self.ImpGrdInfBrgdThirdBattalion.currentIndexChanged.connect(self.impGrdInfBrgd3rdBttlnCostView)
        self.ImpGrdInfBrgdFourthBattalion.currentIndexChanged.connect(self.impGrdInfBrgd4thBttlnCostView)
        self.ImpGrdInfBrgdFifthBattalion.currentIndexChanged.connect(self.impGrdInfBrgd5thBttlnCostView)
        self.ImpGrdInfBrgdSixthBattalion.currentIndexChanged.connect(self.impGrdInfBrgd6thBttlnCostView)
        self.ImpGrdInfBrgdAdditional1Battalion.currentIndexChanged.connect(self.impGrdInfBrgdAdd1BttlnCostView)
        self.ImpGrdInfBrgdAdditional2Battalion.currentIndexChanged.connect(self.impGrdInfBrgdAdd2BttlnCostView)

        self.ImpGrdInfBrFirstBttlnModPushButton.clicked.connect(self.imp_grd_inf_the_first_bttln_mod_button_was_clicked)
        self.ImpGrdInfBrSecondBttlnModPushButton.clicked.connect(self.imp_grd_inf_the_second_bttln_mod_button_was_clicked)
        self.ImpGrdInfBrThirdBttlnModPushButton.clicked.connect(self.imp_grd_inf_the_third_bttln_mod_button_was_clicked)
        self.ImpGrdInfBrFourthBttlnModPushButton.clicked.connect(self.imp_grd_inf_the_fourth_bttln_mod_button_was_clicked)
        self.ImpGrdInfBrFifthBttlnModPushButton.clicked.connect(self.imp_grd_inf_the_fifth_bttln_mod_button_was_clicked)
        self.ImpGrdInfBrSixthBttlnModPushButton.clicked.connect(self.imp_grd_inf_the_sixth_bttln_mod_button_was_clicked)

        self.imp_grd_l_cav_brigade_number = 10
        self.imp_grd_l_cav_battalion_index_add = 0

        self.ImpGrdLCavBrgdCmndr.currentIndexChanged.connect(self.impGrdLCavBrgdCommanderCostView)
        self.ImpGrdLCavBrgdFirstBattalion.currentIndexChanged.connect(self.impGrdLCavBrgd1stBttlnCostView)
        self.ImpGrdLCavBrgdSecondBattalion.currentIndexChanged.connect(self.impGrdLCavBrgd2ndBttlnCostView)

        self.ImpGrdLCavBrFirstBttlnModPushButton.clicked.connect(self.imp_grd_l_cav_the_first_bttln_mod_button_was_clicked)
        self.ImpGrdLCavBrSecondBttlnModPushButton.clicked.connect(self.imp_grd_l_cav_the_second_bttln_mod_button_was_clicked)

        self.imp_grd_h_cav_brigade_number = 11
        self.imp_grd_h_cav_battalion_index_add = 0

        self.ImpGrdHCavBrgdCmndr.currentIndexChanged.connect(self.impGrdHCavBrgdCommanderCostView)
        self.ImpGrdHCavBrgdFirstBattalion.currentIndexChanged.connect(self.impGrdHCavBrgd1stBttlnCostView)
        self.ImpGrdHCavBrgdSecondBattalion.currentIndexChanged.connect(self.impGrdHCavBrgd2ndBttlnCostView)

        self.ImpGrdHCavBrFirstBttlnModPushButton.clicked.connect(self.imp_grd_h_cav_the_first_bttln_mod_button_was_clicked)
        self.ImpGrdHCavBrSecondBttlnModPushButton.clicked.connect(self.imp_grd_h_cav_the_second_bttln_mod_button_was_clicked)

        self.artillery_quasy_brigade_number = 12
        self.artillery_total_cost = 0

        self.a_brgd_nmbr_of_battalions = 0
        self.b_brgd_nmbr_of_battalions = 0
        self.c_brgd_nmbr_of_battalions = 0
        self.jgr_brgd_nmbr_of_battalions = 0
        self.comb_grndr_nmbr_of_battalions = 0
        self.grnd_brgd_nmbr_of_battalions = 0
        self.light_cvlry_nmbr_of_battalions = 0
        self.heavy_cvlry_nmbr_of_battalions = 0
        self.cossack_nmbr_of_battalions = 0

        self.LightArtilleryBattery1.currentIndexChanged.connect(self.artLightBattery1CostView)
        self.LightArtilleryBattery2.currentIndexChanged.connect(self.artLightBattery2CostView)
        self.LightArtilleryBattery3.currentIndexChanged.connect(self.artLightBattery3CostView)
        self.LightArtilleryBattery4.currentIndexChanged.connect(self.artLightBattery4CostView)
        self.LightArtilleryBattery5.currentIndexChanged.connect(self.artLightBattery5CostView)
        self.LightArtilleryBattery6.currentIndexChanged.connect(self.artLightBattery6CostView)
        self.HeavyArtilleryBattery1.currentIndexChanged.connect(self.artHeavyBattery1CostView)
        self.HeavyArtilleryBattery2.currentIndexChanged.connect(self.artHeavyBattery2CostView)
        self.HeavyArtilleryBattery3.currentIndexChanged.connect(self.artHeavyBattery3CostView)
        self.HeavyArtilleryBattery4.currentIndexChanged.connect(self.artHeavyBattery4CostView)
        self.UnicornBattery1.currentIndexChanged.connect(self.unicornBattery1CostView)
        self.UnicornBattery2.currentIndexChanged.connect(self.unicornBattery2CostView)
        self.UnicornBattery3.currentIndexChanged.connect(self.unicornBattery3CostView)
        self.UnicornBattery4.currentIndexChanged.connect(self.unicornBattery4CostView)
        self.UnicornBattery5.currentIndexChanged.connect(self.unicornBattery5CostView)
        self.UnicornBattery6.currentIndexChanged.connect(self.unicornBattery6CostView)
        self.HorseArtilleryBattery1.currentIndexChanged.connect(self.horseArtBattery1CostView)
        self.HorseArtilleryBattery2.currentIndexChanged.connect(self.horseArtBattery2CostView)
        self.HorseArtilleryBattery3.currentIndexChanged.connect(self.horseArtBattery3CostView)

        self.earthworks_quasy_brigade_number = 13
        self.earthworks_total_cost = 0

        self.EarthWorks1.currentIndexChanged.connect(self.earthworks1CostView)
        self.EarthWorks2.currentIndexChanged.connect(self.earthworks2CostView)

    # заполняем список имен командиров дивизии
    def division_cmndrs_list(self):
        """

        :return: GUI list with division commanders names
        """

        cmndrs_list: list[str] = self.presenter.DivisionCmndrsNamesList()
        for cmndrName in cmndrs_list:
            self.generalName.addItem(cmndrName)

    def divisionCommanderCostView(self, index: int):
        """

        :param index: chosen commander index in the commanders list:
        :return: the division commander cost
        """

        value: int = self.presenter.DivisionCmndrCost(index)
        self.generalCost.setText(str(value))
        self.divisionTotalCostView()

    def divisionTotalCostView(self):
        """

        :return: Division total cost to GUI. Calculates relation army unis and guard units and show this percentage
         relations in GUI. Send request for checking to visibility sealed brigades, artillery and earthworks
        """

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

        self.divisionTotalCost.setText(str(total_cost)) # <- value to GUI
        self.artilleryBatteryVisible()
        self.earthworksVisible()
        self.imperialGuardBgigadesVisible()

    def artilleryBatteryVisible(self):
        """

        :return: open or close possibility to add artillery units in the division list due to number of infantry ar
         cavalry units chosen
        """

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
        """

        :return: open or close possibility to add earthworks in the division list due to army point number chosen
        """

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
        """

        :return: open or close possibility to add Imperial Gueard brigades in the division list due to number of army's
         brigades chosen
        """

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

    def brgdCommanderCostView(self, index: int, brigade_number: int, brgdCmndrCost): # brgdCmndrCost текстовое поле в GUI соответствующее выбранной бригаде
        """

        :param index: chosen commander index in the commanders list:
        :param brigade_number: brigade number in the division list
        :param brgdCmndrCost: GUI text field name for chosen brigade
        :return: put brigade total cost to corresponding GUI text field
        """
        value = self.presenter.BrigadeCmndrsCost(index, brigade_number)
        brgdCmndrCost.setText(str(value))

    def brgdBttlnCostView(self, bttln_choosen_from_list, brigade_number, brgdBattalionCost,
                          brgdTotalCostView, order_number, bttlnModPushButton = None):
        # отправляем индекс в презентер для передачи в модель чтобы поместить соотетствующий батальон на его место в бригаде
        # order_number =  порядковое место в бригаде
        # индекс выбранного батальона из списка
        self.presenter.BrigadeBttlnChoosen(order_number, bttln_choosen_from_list, brigade_number)
        # отправляем запрос стоимости батальона стоящего на соответствующем месте в бригаде
        value = self.presenter.BrigadeBttlnCost(order_number, brigade_number)
        # записываем в соответствующее поле значение стоимости батальона
        brgdBattalionCost.setText(str(value))
        brgdTotalCostView()
        if bttlnModPushButton is not None:
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
                # сдвигаем на единицу номер выбираемого кав полка, чтобы пройти проверку при нажатии на кнопку модификаци
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

    def aBrgdAddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgdAddBattalionCost, self.aBrgdTotalCostView, 4, self.aBrAddBttlnModPushButton)
        if self.aBrgdAdditionalBattalion.currentText() == "Jager":
            self.aBrgdJgrAdditionalBattalion.setDisabled(False)
        else:
            self.aBrgdJgrAdditionalBattalion.setCurrentIndex(0)
            self.aBrgdJgrAdditionalBattalion.setDisabled(True)


    def aBrgdJgrAddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.a_brigade_number,
                               self.aBrgdJgrAddBattalionCost, self.aBrgdTotalCostView, 5, self.aBrJgrAddBttlnModPushButton)

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

    def a_the_add_bttln_mod_button_was_clicked(self):
        if self.aBrgdAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.brgdFifthBattalionCostSetText = self.aBrgdAddBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBrAddBttlnModPushButton, self.aBrgdAdditionalBattalion.currentText(), self.order_number)

    def a_the_jgr_add_bttln_mod_button_was_clicked(self):
        if self.aBrgdJgrAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 5  # шестой по порядку батальон
            self.brgdSixthBattalionCostSetText = self.aBrgdJgrAddBattalionCost.setText
            self.brgdTotalCostView = self.aBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.a_brigade_number, self.aBrJgrAddBttlnModPushButton, self.aBrgdJgrAdditionalBattalion.currentText(), self.order_number)

    # -------------------------------------------------------------------------------------------------------------------
    def b_brigade_bttln_Lists(self):
        b_brgd_bttlns_list =[self.bBrgdFirstBattalion,
                             self.bBrgdSecondBattalion,
                             self.bBrgdThirdBattalion,
                             self.bBrgdFourthBattalion,
                             self.bBrgdAdditionalBattalion,
                             self.bBrgdJgrAdditionalBattalion]

        brigade_bttln_Lists(self.b_brigade_number, self.presenter, self.bBrgdCmndr, b_brgd_bttlns_list)

    # описание кнопок второй бригады
    def bBrgdCommanderCostView(self, index):
        self.brgdCommanderCostView(index, self.b_brigade_number, self.bBrgdCmndrCost)
        self.bBrgdTotalCostView()
        if self.bBrgdCmndr.currentIndex() < 1:

            if self.presenter.BrigadeBttlnName(0, self.b_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(0, self.b_brigade_number)

                self.bBrgdFirstBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(0, self.b_brigade_number)
                for bttlnName in bttln_list:
                    self.bBrgdFirstBattalion.addItem(bttlnName)

                self.b_battalion_index_add = 0

            self.bBrgdFirstBattalion.setCurrentIndex(0)
            self.bBrgdFirstBattalion.setDisabled(True)
            self.bBrgdSecondBattalion.setCurrentIndex(0)
            self.bBrgdSecondBattalion.setDisabled(True)
            self.bBrgdThirdBattalion.setCurrentIndex(0)
            self.bBrgdThirdBattalion.setDisabled(True)
            self.bBrgdFourthBattalion.setCurrentIndex(0)
            self.bBrgdFourthBattalion.setDisabled(True)
            self.bBrgdAdditionalBattalion.setCurrentIndex(0)
            self.bBrgdAdditionalBattalion.setDisabled(True)
            self.bBrgdJgrAdditionalBattalion.setCurrentIndex(0)
            self.bBrgdJgrAdditionalBattalion.setDisabled(True)

            self.bBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.bBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.bBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.bBrFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.bBrAddBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.bBrJgrAddBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

        else:
            if self.b_battalion_index_add == 0:
            # убираем обьект empty из списка выбора
                self.bBrgdFirstBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(0, self.b_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(0, self.b_brigade_number)
                for bttlnName in bttln_list:
                    self.bBrgdFirstBattalion.addItem(bttlnName)
                # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.b_battalion_index_add = 1

            self.bBrgdFirstBattalion.setDisabled(False)
            self.bBrgdSecondBattalion.setDisabled(False)
            self.bBrgdThirdBattalion.setDisabled(False)
            self.bBrgdFourthBattalion.setDisabled(False)
            self.bBrgdAdditionalBattalion.setDisabled(False)

    def bBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                               self.bBrgdFirstBattalionCost, self.bBrgdTotalCostView, 0, self.bBrFirstBttlnModPushButton)

    def bBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                               self.bBrgdSecondBattalionCost, self.bBrgdTotalCostView, 1, self.bBrSecondBttlnModPushButton)

    def bBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                               self.bBrgdThirdBattalionCost, self.bBrgdTotalCostView, 2, self.bBrThirdBttlnModPushButton)

    def bBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                               self.bBrgdFourthBattalionCost, self.bBrgdTotalCostView, 3, self.bBrFourthBttlnModPushButton)

    def bBrgdAddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                               self.bBrgdAddBattalionCost, self.bBrgdTotalCostView, 4, self.bBrAddBttlnModPushButton)

        if self.bBrgdAdditionalBattalion.currentText() == "Jager":
            self.bBrgdJgrAdditionalBattalion.setDisabled(False)
        else:
            self.bBrgdJgrAdditionalBattalion.setCurrentIndex(0)
            self.bBrgdJgrAdditionalBattalion.setDisabled(True)

    def bBrgdJgrAddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.b_brigade_number,
                               self.bBrgdJgrAddBattalionCost, self.bBrgdTotalCostView, 5, self.bBrJgrAddBttlnModPushButton)

    def bBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.bBrgdCmndr.currentIndex(), self.b_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.b_brigade_number) for i in range(6))

        self.bBrgdTotalCost.setText(str(total_cost))
        self.b_brgd_nmbr_of_battalions = (
            sum(self.presenter.BrigadeBttlnPresence(i, self.b_brigade_number) for i in range(6)))

        self.divisionTotalCostView()

    def b_the_first_bttln_mod_button_was_clicked(self):

        if self.bBrgdFirstBattalion.currentIndex() +self.b_battalion_index_add != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.brgdFirstBattalionCostSetText = self.bBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number, self.bBrFirstBttlnModPushButton, self.bBrgdFirstBattalion.currentText(), self.order_number)

    def b_the_second_bttln_mod_button_was_clicked(self):

        if self.bBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.brgdSecondBattalionCostSetText = self.bBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number, self.bBrSecondBttlnModPushButton, self.bBrgdSecondBattalion.currentText(), self.order_number)

    def b_the_third_bttln_mod_button_was_clicked(self):

        if self.bBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.brgdThirdBattalionCostSetText = self.bBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number, self.bBrThirdBttlnModPushButton, self.bBrgdThirdBattalion.currentText(), self.order_number)

    def b_the_fourth_bttln_mod_button_was_clicked(self):

        if self.bBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.brgdFourthBattalionCostSetText = self.bBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number, self.bBrFourthBttlnModPushButton, self.bBrgdFourthBattalion.currentText(), self.order_number)

    def b_the_add_bttln_mod_button_was_clicked(self):

        if self.bBrgdAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.brgdFifthBattalionCostSetText = self.bBrgdAddBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number, self.bBrAddBttlnModPushButton, self.bBrgdAdditionalBattalion.currentText(), self.order_number)

    def b_the_jgr_add_bttln_mod_button_was_clicked(self):
        if self.bBrgdJgrAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 5  # шестой по порядку батальон
            self.brgdSixthBattalionCostSetText = self.bBrgdJgrAddBattalionCost.setText
            self.brgdTotalCostView = self.bBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.b_brigade_number, self.bBrJgrAddBttlnModPushButton, self.bBrgdJgrAdditionalBattalion.currentText(), self.order_number)

    # -------------------------------------------------------------------------------------------------------------------

    def c_brigade_bttln_Lists(self):
        c_brgd_bttlns_list =[self.cBrgdFirstBattalion,
                             self.cBrgdSecondBattalion,
                             self.cBrgdThirdBattalion,
                             self.cBrgdFourthBattalion,
                             self.cBrgdAdditionalBattalion,
                             self.cBrgdJgrAdditionalBattalion]

        brigade_bttln_Lists(self.c_brigade_number, self.presenter, self.cBrgdCmndr, c_brgd_bttlns_list)

    def cBrgdCommanderCostView(self, index):
        self.brgdCommanderCostView(index, self.c_brigade_number, self.cBrgdCmndrCost)
        self.cBrgdTotalCostView()
        if self.cBrgdCmndr.currentIndex() < 1:

            if self.presenter.BrigadeBttlnName(0, self.c_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(0, self.c_brigade_number)

                self.cBrgdFirstBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(0, self.c_brigade_number)
                for bttlnName in bttln_list:
                    self.cBrgdFirstBattalion.addItem(bttlnName)

                self.c_battalion_index_add = 0

            self.cBrgdFirstBattalion.setCurrentIndex(0)
            self.cBrgdFirstBattalion.setDisabled(True)
            self.cBrgdSecondBattalion.setCurrentIndex(0)
            self.cBrgdSecondBattalion.setDisabled(True)
            self.cBrgdThirdBattalion.setCurrentIndex(0)
            self.cBrgdThirdBattalion.setDisabled(True)
            self.cBrgdFourthBattalion.setCurrentIndex(0)
            self.cBrgdFourthBattalion.setDisabled(True)
            self.cBrgdAdditionalBattalion.setCurrentIndex(0)
            self.cBrgdAdditionalBattalion.setDisabled(True)
            self.cBrgdJgrAdditionalBattalion.setCurrentIndex(0)
            self.cBrgdJgrAdditionalBattalion.setDisabled(True)

            self.cBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.cBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.cBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.cBrFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.cBrAddBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.cBrJgrAddBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

        else:
            if self.c_battalion_index_add == 0:
            # убираем обьект empty из списка выбора
                self.cBrgdFirstBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(0, self.c_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(0, self.c_brigade_number)
                for bttlnName in bttln_list:
                    self.cBrgdFirstBattalion.addItem(bttlnName)
                # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.c_battalion_index_add = 1

            self.cBrgdFirstBattalion.setDisabled(False)
            self.cBrgdSecondBattalion.setDisabled(False)
            self.cBrgdThirdBattalion.setDisabled(False)
            self.cBrgdFourthBattalion.setDisabled(False)
            self.cBrgdAdditionalBattalion.setDisabled(False)

    def cBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                               self.cBrgdFirstBattalionCost, self.cBrgdTotalCostView, 0, self.cBrFirstBttlnModPushButton)

    def cBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                               self.cBrgdSecondBattalionCost, self.cBrgdTotalCostView, 1, self.cBrSecondBttlnModPushButton)

    def cBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                               self.cBrgdThirdBattalionCost, self.cBrgdTotalCostView, 2, self.cBrThirdBttlnModPushButton)

    def cBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                               self.cBrgdFourthBattalionCost, self.cBrgdTotalCostView, 3, self.cBrFourthBttlnModPushButton)

    def cBrgdAddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                               self.cBrgdAddBattalionCost, self.cBrgdTotalCostView, 4, self.cBrAddBttlnModPushButton)

        if self.cBrgdAdditionalBattalion.currentText() == "Jager":
            self.cBrgdJgrAdditionalBattalion.setDisabled(False)
        else:
            self.cBrgdJgrAdditionalBattalion.setCurrentIndex(0)
            self.cBrgdJgrAdditionalBattalion.setDisabled(True)

    def cBrgdJgrAddBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.c_brigade_number,
                               self.cBrgdJgrAddBattalionCost, self.cBrgdTotalCostView, 5, self.cBrJgrAddBttlnModPushButton)

    def cBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.cBrgdCmndr.currentIndex(), self.c_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.c_brigade_number) for i in range(6))

        self.cBrgdTotalCost.setText(str(total_cost))
        self.c_brgd_nmbr_of_battalions = (
            sum(self.presenter.BrigadeBttlnPresence(i, self.c_brigade_number) for i in range(6)))

        self.divisionTotalCostView()

    def c_the_first_bttln_mod_button_was_clicked(self):

        if self.cBrgdFirstBattalion.currentIndex() + self.c_battalion_index_add != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.brgdFirstBattalionCostSetText = self.cBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number, self.cBrFirstBttlnModPushButton, self.cBrgdFirstBattalion.currentText(), self.order_number)

    def c_the_second_bttln_mod_button_was_clicked(self):

        if self.cBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.brgdSecondBattalionCostSetText = self.cBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number, self.cBrSecondBttlnModPushButton, self.cBrgdSecondBattalion.currentText(), self.order_number)

    def c_the_third_bttln_mod_button_was_clicked(self):

        if self.cBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.brgdThirdBattalionCostSetText = self.cBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number, self.cBrThirdBttlnModPushButton, self.cBrgdThirdBattalion.currentText(), self.order_number)

    def c_the_fourth_bttln_mod_button_was_clicked(self):

        if self.cBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.brgdFourthBattalionCostSetText = self.cBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number, self.cBrFourthBttlnModPushButton, self.cBrgdFourthBattalion.currentText(), self.order_number)

    def c_the_add_bttln_mod_button_was_clicked(self):

        if self.cBrgdAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.brgdFifthBattalionCostSetText = self.cBrgdAddBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number, self.cBrAddBttlnModPushButton, self.cBrgdAdditionalBattalion.currentText(), self.order_number)

    def c_the_jgr_add_bttln_mod_button_was_clicked(self):
        if self.cBrgdJgrAdditionalBattalion.currentIndex() != 0:
            battalion_order = "Additional Battalion"
            self.order_number = 5  # шестой по порядку батальон
            self.brgdSixthBattalionCostSetText = self.cBrgdJgrAddBattalionCost.setText
            self.brgdTotalCostView = self.cBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.c_brigade_number, self.cBrJgrAddBttlnModPushButton, self.cBrgdJgrAdditionalBattalion.currentText(), self.order_number)

    # -------------------------------------------------------------------------------------------------------------------
    def jgr_brigade_bttln_Lists(self):
        jgr_brgd_bttlns_list = [self.JgrBrgdFirstBattalion,
                              self.JgrBrgdSecondBattalion,
                              self.JgrBrgdThirdBattalion,
                              self.JgrBrgdFourthBattalion,
                              self.JgrBrgdFifthBattalion,
                              self.JgrBrgdSixthBattalion,
                              self.JgrBrgdAdditional1Battalion,
                              self.JgrBrgdAdditional2Battalion]

        brigade_bttln_Lists(self.jgr_brigade_number, self.presenter, self.JgrBrgdCmndr, jgr_brgd_bttlns_list)

    def jgrBrgdCommanderCostView(self, index):
        value = self.presenter.BrigadeCmndrsCost(index, self.jgr_brigade_number)
        self.JgrBrgdCmndrCost.setText(str(value))
        self.jgrBrgdTotalCostView()

        if self.JgrBrgdCmndr.currentIndex() < 1:

            if self.presenter.BrigadeBttlnName(0, self.jgr_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(0, self.jgr_brigade_number)

                self.JgrBrgdFirstBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(0, self.jgr_brigade_number)
                for bttlnName in bttln_list:
                    self.JgrBrgdFirstBattalion.addItem(bttlnName)
                self.jgr_battalion1_index_add = 0
            if self.presenter.BrigadeBttlnName(1, self.jgr_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(1, self.jgr_brigade_number)

                self.JgrBrgdSecondBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(1, self.jgr_brigade_number)
                for bttlnName in bttln_list:
                    self.JgrBrgdSecondBattalion.addItem(bttlnName)

                self.jgr_battalion2_index_add = 0

            self.JgrBrgdFirstBattalion.setCurrentIndex(0)
            self.JgrBrgdFirstBattalion.setDisabled(True)
            self.JgrBrgdSecondBattalion.setCurrentIndex(0)
            self.JgrBrgdSecondBattalion.setDisabled(True)
            self.JgrBrgdThirdBattalion.setCurrentIndex(0)
            self.JgrBrgdThirdBattalion.setDisabled(True)
            self.JgrBrgdFourthBattalion.setCurrentIndex(0)
            self.JgrBrgdFourthBattalion.setDisabled(True)
            self.JgrBrgdFifthBattalion.setCurrentIndex(0)
            self.JgrBrgdFifthBattalion.setDisabled(True)
            self.JgrBrgdSixthBattalion.setCurrentIndex(0)
            self.JgrBrgdSixthBattalion.setDisabled(True)
            self.JgrBrgdAdditional1Battalion.setCurrentIndex(0)
            self.JgrBrgdAdditional1Battalion.setDisabled(True)
            self.JgrBrgdAdditional2Battalion.setCurrentIndex(0)
            self.JgrBrgdAdditional2Battalion.setDisabled(True)

            self.JgrBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.JgrBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.JgrBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.JgrBrFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.JgrBrFifthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.JgrBrSixthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

        else:
            if self.jgr_battalion1_index_add == 0:
            # убираем обьект empty из списка выбора
                self.JgrBrgdFirstBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(0, self.jgr_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(0, self.jgr_brigade_number)
                for bttlnName in bttln_list:
                    self.JgrBrgdFirstBattalion.addItem(bttlnName)
                # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.jgr_battalion1_index_add = 1
            if self.jgr_battalion2_index_add == 0:
            # убираем обьект empty из списка выбора
                self.JgrBrgdSecondBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(1, self.jgr_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(1, self.jgr_brigade_number)
                for bttlnName in bttln_list:
                    self.JgrBrgdSecondBattalion.addItem(bttlnName)
                # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.jgr_battalion2_index_add = 1

            self.JgrBrgdFirstBattalion.setDisabled(False)
            self.JgrBrgdSecondBattalion.setDisabled(False)
            self.JgrBrgdThirdBattalion.setDisabled(False)
            self.JgrBrgdFourthBattalion.setDisabled(False)
            self.JgrBrgdFifthBattalion.setDisabled(False)
            self.JgrBrgdSixthBattalion.setDisabled(False)
            self.JgrBrgdAdditional1Battalion.setDisabled(False)
            self.JgrBrgdAdditional2Battalion.setDisabled(False)

    def jgrBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdFirstBattalionCost, self.jgrBrgdTotalCostView, 0, self.JgrBrFirstBttlnModPushButton)

    def jgrBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdSecondBattalionCost, self.jgrBrgdTotalCostView, 1, self.JgrBrSecondBttlnModPushButton)

    def jgrBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdThirdBattalionCost, self.jgrBrgdTotalCostView, 2, self.JgrBrThirdBttlnModPushButton)

    def jgrBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdFourthBattalionCost, self.jgrBrgdTotalCostView, 3, self.JgrBrFourthBttlnModPushButton)

    def jgrBrgd5thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdFifthBattalionCost, self.jgrBrgdTotalCostView, 4, self.JgrBrFifthBttlnModPushButton)

    def jgrBrgd6thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdSixthBattalionCost, self.jgrBrgdTotalCostView, 5, self.JgrBrSixthBttlnModPushButton)

    def jgrBrgdAdd1BttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdAdd1BattalionCost, self.jgrBrgdTotalCostView, 6)

    def jgrBrgdAdd2BttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.jgr_brigade_number,
                               self.JgrBrgdAdd2BattalionCost, self.jgrBrgdTotalCostView, 7)

    def jgrBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.JgrBrgdCmndr.currentIndex(),
                                                      self.jgr_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.jgr_brigade_number) for i in range(8))

        self.JgrBrgdTotalCost.setText(str(total_cost))

        self.jgr_brgd_nmbr_of_battalions = (
            sum(self.presenter.BrigadeBttlnPresence(i, self.jgr_brigade_number) for i in range(8)))


        self.divisionTotalCostView()

    def jgr_the_first_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdFirstBattalion.currentIndex() + self.jgr_battalion1_index_add != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.brgdFirstBattalionCostSetText = self.JgrBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number, self.JgrBrFirstBttlnModPushButton, self.JgrBrgdFirstBattalion.currentText(), self.order_number)
    def jgr_the_second_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdSecondBattalion.currentIndex() + self.jgr_battalion2_index_add != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.brgdSecondBattalionCostSetText = self.JgrBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number, self.JgrBrSecondBttlnModPushButton, self.JgrBrgdSecondBattalion.currentText(), self.order_number)

    def jgr_the_third_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.brgdThirdBattalionCostSetText = self.JgrBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number, self.JgrBrThirdBttlnModPushButton, self.JgrBrgdThirdBattalion.currentText(), self.order_number)

    def jgr_the_fourth_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.brgdFourthBattalionCostSetText = self.JgrBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number, self.JgrBrFourthBttlnModPushButton, self.JgrBrgdFourthBattalion.currentText(), self.order_number)

    def jgr_the_fifth_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdFifthBattalion.currentIndex() != 0:
            battalion_order = "Fifth Battalion"
            self.order_number = 4  # четвертый по порядку батальон
            self.brgdFifthBattalionCostSetText = self.JgrBrgdFifthBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number, self.JgrBrFifthBttlnModPushButton, self.JgrBrgdFifthBattalion.currentText(), self.order_number)

    def jgr_the_sixth_bttln_mod_button_was_clicked(self):

        if self.JgrBrgdSixthBattalion.currentIndex() != 0:
            battalion_order = "Sixth Battalion"
            self.order_number = 5  # четвертый по порядку батальон
            self.brgdSixthBattalionCostSetText = self.JgrBrgdSixthBattalionCost.setText
            self.brgdTotalCostView = self.jgrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.jgr_brigade_number, self.JgrBrSixthBttlnModPushButton, self.JgrBrgdSixthBattalion.currentText(), self.order_number)

    # -------------------------------------------------------------------------------------------------------------------
    def comb_grndr_brigade_bttln_Lists(self):
        comb_grndr_brgd_bttlns_list = [self.CombGrndrBrgdFirstBattalion,
                                      self.CombGrndrBrgdSecondBattalion,
                                      self.CombGrndrBrgdThirdBattalion,
                                      self.CombGrndrBrgdFourthBattalion,
                                      self.CombGrndrBrgdFifthBattalion,
                                      self.CombGrndrBrgdSixthBattalion,
                                      self.CombGrndrBrgdSeventhBattalion]

        brigade_bttln_Lists(self.comb_grndr_brigade_number, self.presenter, self.CombGrndrBrgdCmndr, comb_grndr_brgd_bttlns_list)


    def combGrndrBrgdCommanderCostView(self, index):
        value = self.presenter.BrigadeCmndrsCost(index, self.comb_grndr_brigade_number)
        self.CombGrndrBrgdCmndrCost.setText(str(value))
        self.combGrndrBrgdTotalCostView()

        if self.CombGrndrBrgdCmndr.currentIndex() < 1:

            if self.presenter.BrigadeBttlnName(0, self.comb_grndr_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(0, self.comb_grndr_brigade_number)

                self.CombGrndrBrgdFirstBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(0, self.comb_grndr_brigade_number)
                for bttlnName in bttln_list:
                    self.CombGrndrBrgdFirstBattalion.addItem(bttlnName)

                self.comb_grndr_battalion1_index_add = 0
            if self.presenter.BrigadeBttlnName(1, self.comb_grndr_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(1, self.comb_grndr_brigade_number)

                self.CombGrndrBrgdSecondBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(1, self.comb_grndr_brigade_number)
                for bttlnName in bttln_list:
                    self.CombGrndrBrgdSecondBattalion.addItem(bttlnName)

                self.comb_grndr_battalion2_index_add = 0

            self.CombGrndrBrgdFirstBattalion.setCurrentIndex(0)
            self.CombGrndrBrgdFirstBattalion.setDisabled(True)
            self.CombGrndrBrgdSecondBattalion.setCurrentIndex(0)
            self.CombGrndrBrgdSecondBattalion.setDisabled(True)
            self.CombGrndrBrgdThirdBattalion.setCurrentIndex(0)
            self.CombGrndrBrgdThirdBattalion.setDisabled(True)
            self.CombGrndrBrgdFourthBattalion.setCurrentIndex(0)
            self.CombGrndrBrgdFourthBattalion.setDisabled(True)
            self.CombGrndrBrgdFifthBattalion.setCurrentIndex(0)
            self.CombGrndrBrgdFifthBattalion.setDisabled(True)
            self.CombGrndrBrgdSixthBattalion.setCurrentIndex(0)
            self.CombGrndrBrgdSixthBattalion.setDisabled(True)
            self.CombGrndrBrgdSeventhBattalion.setCurrentIndex(0)
            self.CombGrndrBrgdSeventhBattalion.setDisabled(True)

            self.CombGrndrBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CombGrndrBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CombGrndrBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CombGrndrBrFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CombGrndrBrFifthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CombGrndrBrSixthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CombGrndrBrSeventhBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

        else:
            if self.comb_grndr_battalion1_index_add == 0:
            # убираем обьект empty из списка выбора
                self.CombGrndrBrgdFirstBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(0, self.comb_grndr_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(0, self.comb_grndr_brigade_number)
                for bttlnName in bttln_list:
                    self.CombGrndrBrgdFirstBattalion.addItem(bttlnName)
                # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.comb_grndr_battalion1_index_add = 1
            if self.comb_grndr_battalion2_index_add == 0:
            # убираем обьект empty из списка выбора
                self.CombGrndrBrgdSecondBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(1, self.comb_grndr_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(1, self.comb_grndr_brigade_number)
                for bttlnName in bttln_list:
                    self.CombGrndrBrgdSecondBattalion.addItem(bttlnName)
                # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.comb_grndr_battalion2_index_add = 1

            self.CombGrndrBrgdFirstBattalion.setDisabled(False)
            self.CombGrndrBrgdSecondBattalion.setDisabled(False)
            self.CombGrndrBrgdThirdBattalion.setDisabled(False)
            self.CombGrndrBrgdFourthBattalion.setDisabled(False)
            self.CombGrndrBrgdFifthBattalion.setDisabled(False)
            self.CombGrndrBrgdSixthBattalion.setDisabled(False)
            self.CombGrndrBrgdSeventhBattalion.setDisabled(False)

    def combGrndrBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.comb_grndr_brigade_number,
                               self.CombGrndrBrgdFirstBattalionCost, self.combGrndrBrgdTotalCostView, 0, self.CombGrndrBrFirstBttlnModPushButton)

    def combGrndrBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.comb_grndr_brigade_number,
                               self.CombGrndrBrgdSecondBattalionCost, self.combGrndrBrgdTotalCostView, 1, self.CombGrndrBrSecondBttlnModPushButton)

    def combGrndrBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.comb_grndr_brigade_number,
                               self.CombGrndrBrgdThirdBattalionCost, self.combGrndrBrgdTotalCostView, 2, self.CombGrndrBrThirdBttlnModPushButton)

    def combGrndrBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.comb_grndr_brigade_number,
                               self.CombGrndrBrgdFourthBattalionCost, self.combGrndrBrgdTotalCostView, 3, self.CombGrndrBrFourthBttlnModPushButton)

    def combGrndrBrgd5thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.comb_grndr_brigade_number,
                               self.CombGrndrBrgdFifthBattalionCost, self.combGrndrBrgdTotalCostView, 4, self.CombGrndrBrFifthBttlnModPushButton)

    def combGrndrBrgd6thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.comb_grndr_brigade_number,
                               self.CombGrndrBrgdSixthBattalionCost, self.combGrndrBrgdTotalCostView, 5, self.CombGrndrBrSixthBttlnModPushButton)

    def combGrndrBrgd7thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.comb_grndr_brigade_number,
                               self.CombGrndrBrgdSeventhBattalionCost, self.combGrndrBrgdTotalCostView, 6, self.CombGrndrBrSeventhBttlnModPushButton)

    def combGrndrBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.CombGrndrBrgdCmndr.currentIndex(),self.comb_grndr_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.comb_grndr_brigade_number) for i in range(7))

        self.CombGrndrBrgdTotalCost.setText(str(total_cost))

        self.comb_grndr_nmbr_of_battalions = (
            sum(self.presenter.BrigadeBttlnPresence(i, self.comb_grndr_brigade_number) for i in range(7)))

        self.divisionTotalCostView()


    def comb_grndr_the_first_bttln_mod_button_was_clicked(self):

        if self.CombGrndrBrgdFirstBattalion.currentIndex() + self.comb_grndr_battalion1_index_add != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.brgdFirstBattalionCostSetText = self.CombGrndrBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.combGrndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.comb_grndr_brigade_number, self.CombGrndrBrFirstBttlnModPushButton, self.CombGrndrBrgdFirstBattalion.currentText(), self.order_number)

    def comb_grndr_the_second_bttln_mod_button_was_clicked(self):

        if self.CombGrndrBrgdSecondBattalion.currentIndex() + self.comb_grndr_battalion2_index_add!= 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.brgdSecondBattalionCostSetText = self.CombGrndrBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.combGrndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.comb_grndr_brigade_number, self.CombGrndrBrSecondBttlnModPushButton, self.CombGrndrBrgdSecondBattalion.currentText(), self.order_number)

    def comb_grndr_the_third_bttln_mod_button_was_clicked(self):

        if self.CombGrndrBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.brgdThirdBattalionCostSetText = self.CombGrndrBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.combGrndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.comb_grndr_brigade_number, self.CombGrndrBrThirdBttlnModPushButton, self.CombGrndrBrgdThirdBattalion.currentText(), self.order_number)

    def comb_grndr_the_fourth_bttln_mod_button_was_clicked(self):

        if self.CombGrndrBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.brgdFourthBattalionCostSetText = self.CombGrndrBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.combGrndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.comb_grndr_brigade_number, self.CombGrndrBrFourthBttlnModPushButton, self.CombGrndrBrgdFourthBattalion.currentText(), self.order_number)

    def comb_grndr_the_fifth_bttln_mod_button_was_clicked(self):

        if self.CombGrndrBrgdFifthBattalion.currentIndex() != 0:
            battalion_order = "Fifth Battalion"
            self.order_number = 4  # пятый по порядку батальон
            self.brgdFifthBattalionCostSetText = self.CombGrndrBrgdFifthBattalionCost.setText
            self.brgdTotalCostView = self.combGrndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.comb_grndr_brigade_number, self.CombGrndrBrFifthBttlnModPushButton, self.CombGrndrBrgdFifthBattalion.currentText(), self.order_number)

    def comb_grndr_the_sixth_bttln_mod_button_was_clicked(self):

        if self.CombGrndrBrgdSixthBattalion.currentIndex() != 0:
            battalion_order = "Sixth Battalion"
            self.order_number = 5  # шестой по порядку батальон
            self.brgdSixthBattalionCostSetText = self.CombGrndrBrgdSixthBattalionCost.setText
            self.brgdTotalCostView = self.combGrndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.comb_grndr_brigade_number, self.CombGrndrBrSixthBttlnModPushButton, self.CombGrndrBrgdSixthBattalion.currentText(), self.order_number)

    def comb_grndr_the_seventh_bttln_mod_button_was_clicked(self):

        if self.CombGrndrBrgdSeventhBattalion.currentIndex() != 0:
            battalion_order = "Seventh Battalion"
            self.order_number = 6  # седьмой по порядку батальон
            self.brgdSeventhBattalionCostSetText = self.CombGrndrBrgdSeventhBattalionCost.setText
            self.brgdTotalCostView = self.combGrndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.comb_grndr_brigade_number, self.CombGrndrBrSeventhBttlnModPushButton, self.CombGrndrBrgdSeventhBattalion.currentText(), self.order_number)

    # -------------------------------------------------------------------------------------------------------------------
    def grndr_brigade_bttln_Lists(self):
        grndr_brgd_bttlns_list = [self.GrndrBrgdFirstBattalion,
                                      self.GrndrBrgdSecondBattalion,
                                      self.GrndrBrgdThirdBattalion,
                                      self.GrndrBrgdFourthBattalion]

        brigade_bttln_Lists(self.grndr_brigade_number, self.presenter, self.GrndrBrgdCmndr, grndr_brgd_bttlns_list)

    def grndrBrgdCommanderCostView(self, index):
        value = self.presenter.BrigadeCmndrsCost(index, self.grndr_brigade_number)
        self.GrndrBrgdCmndrCost.setText(str(value))
        self.grndrBrgdTotalCostView()

        if self.GrndrBrgdCmndr.currentIndex() < 1:

            if self.presenter.BrigadeBttlnName(0, self.grndr_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(0, self.grndr_brigade_number)

                self.GrndrBrgdFirstBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(0, self.grndr_brigade_number)
                for bttlnName in bttln_list:
                    self.GrndrBrgdFirstBattalion.addItem(bttlnName)

                self.grndr_battalion_index_add = 0

            self.GrndrBrgdFirstBattalion.setCurrentIndex(0)
            self.GrndrBrgdFirstBattalion.setDisabled(True)
            self.GrndrBrgdSecondBattalion.setCurrentIndex(0)
            self.GrndrBrgdSecondBattalion.setDisabled(True)
            self.GrndrBrgdThirdBattalion.setCurrentIndex(0)
            self.GrndrBrgdThirdBattalion.setDisabled(True)
            self.GrndrBrgdFourthBattalion.setCurrentIndex(0)
            self.GrndrBrgdFourthBattalion.setDisabled(True)

            self.GrndrBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.GrndrBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.GrndrBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.GrndrBrFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

        else:
            if self.grndr_battalion_index_add == 0:
            # убираем обьект empty из списка выбора
                self.GrndrBrgdFirstBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(0, self.grndr_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(0, self.grndr_brigade_number)
                for bttlnName in bttln_list:
                    self.GrndrBrgdFirstBattalion.addItem(bttlnName)
                # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.grndr_battalion_index_add = 1

            self.GrndrBrgdFirstBattalion.setDisabled(False)
            self.GrndrBrgdSecondBattalion.setDisabled(False)
            self.GrndrBrgdThirdBattalion.setDisabled(False)
            self.GrndrBrgdFourthBattalion.setDisabled(False)

    def grndrBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.grndr_brigade_number,
                               self.GrndrBrgdFirstBattalionCost, self.grndrBrgdTotalCostView, 0, self.GrndrBrFirstBttlnModPushButton)

    def grndrBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.grndr_brigade_number,
                               self.GrndrBrgdSecondBattalionCost, self.grndrBrgdTotalCostView, 1, self.GrndrBrSecondBttlnModPushButton)

    def grndrBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.grndr_brigade_number,
                               self.GrndrBrgdThirdBattalionCost, self.grndrBrgdTotalCostView, 2, self.GrndrBrThirdBttlnModPushButton)

    def grndrBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.grndr_brigade_number,
                               self.GrndrBrgdFourthBattalionCost, self.grndrBrgdTotalCostView, 3, self.GrndrBrFourthBttlnModPushButton)


    def grndrBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.GrndrBrgdCmndr.currentIndex(),self.grndr_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.grndr_brigade_number) for i in range(4))

        self.GrndrBrgdTotalCost.setText(str(total_cost))
        self.grnd_brgd_nmbr_of_battalions = (
            sum(self.presenter.BrigadeBttlnPresence(i, self.grndr_brigade_number) for i in range(4)))

        self.divisionTotalCostView()


    def grndr_the_first_bttln_mod_button_was_clicked(self):

        if self.GrndrBrgdFirstBattalion.currentIndex() + self.grndr_battalion_index_add != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку батальон
            self.brgdFirstBattalionCostSetText = self.GrndrBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.grndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.grndr_brigade_number, self.GrndrBrFirstBttlnModPushButton, self.GrndrBrgdFirstBattalion.currentText(), self.order_number)

    def grndr_the_second_bttln_mod_button_was_clicked(self):

        if self.GrndrBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку батальон
            self.brgdSecondBattalionCostSetText = self.GrndrBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.grndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.grndr_brigade_number, self.GrndrBrSecondBttlnModPushButton, self.GrndrBrgdSecondBattalion.currentText(), self.order_number)

    def grndr_the_third_bttln_mod_button_was_clicked(self):

        if self.GrndrBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку батальон
            self.brgdThirdBattalionCostSetText = self.GrndrBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.grndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.grndr_brigade_number, self.GrndrBrThirdBttlnModPushButton, self.GrndrBrgdThirdBattalion.currentText(), self.order_number)

    def grndr_the_fourth_bttln_mod_button_was_clicked(self):

        if self.GrndrBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку батальон
            self.brgdFourthBattalionCostSetText = self.GrndrBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.grndrBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.grndr_brigade_number, self.GrndrBrFourthBttlnModPushButton, self.GrndrBrgdFourthBattalion.currentText(), self.order_number)

    #--------------------------------------------------------------------------------------------------------------------
    def light_cvlry_brigade_bttln_Lists(self):
        l_cvlry_brgd_bttlns_list = [self.LCvlryBrgdFirstBattalion,
                                    self.LCvlryBrgdSecondBattalion,
                                    self.LCvlryBrgdThirdBattalion]

        brigade_bttln_Lists(self.light_cvlry_brigade_number, self.presenter, self.LCvlryBrgdCmndr, l_cvlry_brgd_bttlns_list)

    def lightCvlryBrgdCommanderCostView(self, index):
        value = self.presenter.BrigadeCmndrsCost(index, self.light_cvlry_brigade_number)
        self.LCvlryBrgdCmndrCost.setText(str(value))
        self.lightCvlryBrgdTotalCostView()

        if self.LCvlryBrgdCmndr.currentIndex() < 1:

            if self.presenter.BrigadeBttlnName(0, self.light_cvlry_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(0, self.light_cvlry_brigade_number)

                self.LCvlryBrgdFirstBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(0, self.light_cvlry_brigade_number)
                for bttlnName in bttln_list:
                    self.LCvlryBrgdFirstBattalion.addItem(bttlnName)

                self.l_cvlry_battalion_index_add = 0

            self.LCvlryBrgdFirstBattalion.setCurrentIndex(0)
            self.LCvlryBrgdFirstBattalion.setDisabled(True)
            self.LCvlryBrgdSecondBattalion.setCurrentIndex(0)
            self.LCvlryBrgdSecondBattalion.setDisabled(True)
            self.LCvlryBrgdThirdBattalion.setCurrentIndex(0)
            self.LCvlryBrgdThirdBattalion.setDisabled(True)

            self.LCvlryBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.LCvlryBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.LCvlryBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

        else:

            if self.l_cvlry_battalion_index_add == 0:
            # убираем обьект empty из списка выбора
                self.LCvlryBrgdFirstBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(0, self.light_cvlry_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(0, self.light_cvlry_brigade_number)
                for bttlnName in bttln_list:
                    self.LCvlryBrgdFirstBattalion.addItem(bttlnName)
  # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.l_cvlry_battalion_index_add = 1

            self.LCvlryBrgdFirstBattalion.setDisabled(False)
            self.LCvlryBrgdSecondBattalion.setDisabled(False)
            self.LCvlryBrgdThirdBattalion.setDisabled(False)

    def lightCvlryBrgd1stBttlnCostView(self, bttln_choosen_from_list):

        self.brgdBttlnCostView(bttln_choosen_from_list, self.light_cvlry_brigade_number,
                               self.LCvlryBrgdFirstBattalionCost, self.lightCvlryBrgdTotalCostView, 0,
                               self.LCvlryBrFirstBttlnModPushButton)

        if self.LCvlryBrgdFirstBattalion.currentText() == "Ulan":
            if self.LCvlryBrgdSecondBattalion.currentText() == "Ulan" or self.LCvlryBrgdThirdBattalion.currentText() == "Ulan":
                self.LCvlryBrgdFirstBattalion.setCurrentIndex(0)

        if self.LCvlryBrgdFirstBattalion.currentText() == "Dragoon":
            if self.LCvlryBrgdSecondBattalion.currentText() == "Dragoon" and self.LCvlryBrgdThirdBattalion.currentText() == "Dragoon":
                self.LCvlryBrgdFirstBattalion.setCurrentIndex(1)

        if self.LCvlryBrgdFirstBattalion.currentText() == "Hussars":
            if self.LCvlryBrgdSecondBattalion.currentText() == "Hussars" and self.LCvlryBrgdThirdBattalion.currentText()  == "Hussars":
                self.LCvlryBrgdFirstBattalion.setCurrentIndex(0)

        if self.LCvlryBrgdFirstBattalion.currentText() == "Free Cossack regiment":
            if self.LCvlryBrgdSecondBattalion.currentText() == "Free Cossack regiment" or self.LCvlryBrgdThirdBattalion.currentText() == "Free Cossack regiment" or self.CossackBrgdFirstBattalion.currentText() == "Free Cossack regiment":
                self.LCvlryBrgdFirstBattalion.setCurrentIndex(0)

        if self.LCvlryBrgdFirstBattalion.currentText() == "Mounted Cossack" or self.LCvlryBrgdFirstBattalion.currentText() == "Irregular Mounted Cossack" or self.CossackBrgdFirstBattalion.currentText() == "Free Cossack regiment":
            if (self.LCvlryBrgdSecondBattalion.currentText() == "Mounted Cossack" or self.LCvlryBrgdSecondBattalion.currentText() == "Irregular Mounted Cossack" or self.LCvlryBrgdSecondBattalion.currentText() == "Free Cossack regiment") and \
                    (self.LCvlryBrgdThirdBattalion.currentText() == "Mounted Cossack" or self.LCvlryBrgdThirdBattalion.currentText() == "Irregular Mounted Cossack" or self.LCvlryBrgdThirdBattalion.currentText() == "Free Cossack regiment"):
                self.LCvlryBrgdFirstBattalion.setCurrentIndex(0)



    def lightCvlryBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.light_cvlry_brigade_number,
                               self.LCvlryBrgdSecondBattalionCost, self.lightCvlryBrgdTotalCostView, 1, self.LCvlryBrSecondBttlnModPushButton)

        if self.LCvlryBrgdSecondBattalion.currentText() == "Ulan":
            if self.LCvlryBrgdFirstBattalion.currentText() == "Ulan" or self.LCvlryBrgdThirdBattalion.currentText() == "Ulan":
                self.LCvlryBrgdSecondBattalion.setCurrentIndex(0)

        if self.LCvlryBrgdSecondBattalion.currentText() == "Dragoon":
            if self.LCvlryBrgdFirstBattalion.currentText() == "Dragoon" and self.LCvlryBrgdThirdBattalion.currentText() == "Dragoon" :
                self.LCvlryBrgdSecondBattalion.setCurrentIndex(0)

        if self.LCvlryBrgdSecondBattalion.currentText() == "Hussars":
            if self.LCvlryBrgdFirstBattalion.currentText() == "Hussars" and self.LCvlryBrgdThirdBattalion.currentText() == "Hussars" :
                self.LCvlryBrgdSecondBattalion.setCurrentIndex(0)

        if self.LCvlryBrgdSecondBattalion.currentText() == "Free Cossack regiment":
            if self.LCvlryBrgdFirstBattalion.currentText() == "Free Cossack regiment" or self.LCvlryBrgdThirdBattalion.currentText() == "Free Cossack regiment" or self.CossackBrgdFirstBattalion.currentText() == "Free Cossack regiment":
                self.LCvlryBrgdSecondBattalion.setCurrentIndex(0)

        if self.LCvlryBrgdSecondBattalion.currentText() == "Mounted Cossack" or self.LCvlryBrgdSecondBattalion.currentText() == "Irregular Mounted Cossack" or self.LCvlryBrgdSecondBattalion.currentText() == "Free Cossack regiment":
            if (self.LCvlryBrgdFirstBattalion.currentText() == "Mounted Cossack" or self.LCvlryBrgdFirstBattalion.currentText() == "Irregular Mounted Cossack" or self.LCvlryBrgdFirstBattalion.currentText() == "Free Cossack regiment") and \
                    (self.LCvlryBrgdThirdBattalion.currentText() == "Mounted Cossack" or self.LCvlryBrgdThirdBattalion.currentText() == "Irregular Mounted Cossack" or self.LCvlryBrgdThirdBattalion.currentText() == "Free Cossack regiment"):
                self.LCvlryBrgdSecondBattalion.setCurrentIndex(0)

    def lightCvlryBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.light_cvlry_brigade_number,
                               self.LCvlryBrgdThirdBattalionCost, self.lightCvlryBrgdTotalCostView, 2, self.LCvlryBrThirdBttlnModPushButton)

        if self.LCvlryBrgdThirdBattalion.currentText() == "Ulan":
            if self.LCvlryBrgdFirstBattalion.currentText() == "Ulan" or self.LCvlryBrgdSecondBattalion.currentText() == "Ulan":
                self.LCvlryBrgdThirdBattalion.setCurrentIndex(0)

        if self.LCvlryBrgdThirdBattalion.currentText() == "Dragoon":
            if self.LCvlryBrgdFirstBattalion.currentText() == "Dragoon" and self.LCvlryBrgdSecondBattalion.currentText() == "Dragoon":
                self.LCvlryBrgdThirdBattalion.setCurrentIndex(0)

        if self.LCvlryBrgdThirdBattalion.currentText() == "Hussars":
            if self.LCvlryBrgdFirstBattalion.currentText() == "Hussars" and self.LCvlryBrgdSecondBattalion.currentText() == "Hussars":
                self.LCvlryBrgdThirdBattalion.setCurrentIndex(0)

        if self.LCvlryBrgdThirdBattalion.currentText() == "Free Cossack regiment":
            if self.LCvlryBrgdFirstBattalion.currentText() == "Free Cossack regiment" or self.LCvlryBrgdSecondBattalion.currentText() == "Free Cossack regiment" or self.CossackBrgdFirstBattalion.currentText() == "Free Cossack regiment":
                self.LCvlryBrgdThirdBattalion.setCurrentIndex(0)

        if self.LCvlryBrgdThirdBattalion.currentText() == "Mounted Cossack" or self.LCvlryBrgdThirdBattalion.currentText() == "Irregular Mounted Cossack" or self.LCvlryBrgdThirdBattalion.currentText() == "Free Cossack regiment":
            if (self.LCvlryBrgdFirstBattalion.currentText() == "Mounted Cossack" or self.LCvlryBrgdFirstBattalion.currentText() == "Irregular Mounted Cossack" or self.LCvlryBrgdFirstBattalion.currentText() == "Free Cossack regiment") and \
                    (self.LCvlryBrgdSecondBattalion.currentText() == "Mounted Cossack" or self.LCvlryBrgdSecondBattalion.currentText() == "Irregular Mounted Cossack" or self.LCvlryBrgdSecondBattalion.currentText() == "Free Cossack regiment"):
                self.LCvlryBrgdThirdBattalion.setCurrentIndex(0)

    def lightCvlryBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.LCvlryBrgdCmndr.currentIndex(),self.light_cvlry_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.light_cvlry_brigade_number) for i in range(3))

        self.LCvlryBrgdTotalCost.setText(str(total_cost))
        self.light_cvlry_nmbr_of_battalions = (
            sum(self.presenter.BrigadeBttlnPresence(i, self.light_cvlry_brigade_number) for i in range(3)))

        self.divisionTotalCostView()

    def lightCvlry_the_first_bttln_mod_button_was_clicked(self):

        if self.LCvlryBrgdFirstBattalion.currentIndex() +self.l_cvlry_battalion_index_add != 0:
            battalion_order = "First Regiment"
            self.order_number = 0  # первый по порядку кав полк
            self.brgdFirstBattalionCostSetText = self.LCvlryBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.lightCvlryBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.light_cvlry_brigade_number, self.LCvlryBrFirstBttlnModPushButton, self.LCvlryBrgdFirstBattalion.currentText(), self.order_number)

    def lightCvlry_the_second_bttln_mod_button_was_clicked(self):

        if self.LCvlryBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Regiment"
            self.order_number = 1  # второй по порядку кав полк
            self.brgdSecondBattalionCostSetText = self.LCvlryBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.lightCvlryBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.light_cvlry_brigade_number, self.LCvlryBrSecondBttlnModPushButton, self.LCvlryBrgdSecondBattalion.currentText(), self.order_number)

    def lightCvlry_the_third_bttln_mod_button_was_clicked(self):

        if self.LCvlryBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Regiment"
            self.order_number = 2  # третий по порядку кав полк
            self.brgdThirdBattalionCostSetText = self.LCvlryBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.lightCvlryBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.light_cvlry_brigade_number, self.LCvlryBrThirdBttlnModPushButton, self.LCvlryBrgdThirdBattalion.currentText(), self.order_number)
    #--------------------------------------------------------------------------------------------------------------------

    def heavy_cvlry_brigade_bttln_Lists(self):
        h_cvlry_brgd_bttlns_list = [self.HCvlryBrgdFirstBattalion,
                                    self.HCvlryBrgdSecondBattalion,
                                    self.HCvlryBrgdThirdBattalion]

        brigade_bttln_Lists(self.heavy_cvlry_brigade_number, self.presenter, self.HCvlryBrgdCmndr, h_cvlry_brgd_bttlns_list)


    def heavyCvlryBrgdCommanderCostView(self, index):
        value = self.presenter.BrigadeCmndrsCost(index, self.heavy_cvlry_brigade_number)
        self.HCvlryBrgdCmndrCost.setText(str(value))
        self.heavyCvlryBrgdTotalCostView()

        if self.HCvlryBrgdCmndr.currentIndex() < 1:

            if self.presenter.BrigadeBttlnName(0, self.heavy_cvlry_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(0, self.heavy_cvlry_brigade_number)

                self.HCvlryBrgdFirstBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(0, self.heavy_cvlry_brigade_number)
                for bttlnName in bttln_list:
                    self.HCvlryBrgdFirstBattalion.addItem(bttlnName)

                self.h_cvlry_battalion_index_add = 0

            self.HCvlryBrgdFirstBattalion.setCurrentIndex(0)
            self.HCvlryBrgdFirstBattalion.setDisabled(True)
            self.HCvlryBrgdSecondBattalion.setCurrentIndex(0)
            self.HCvlryBrgdSecondBattalion.setDisabled(True)
            self.HCvlryBrgdThirdBattalion.setCurrentIndex(0)
            self.HCvlryBrgdThirdBattalion.setDisabled(True)

            self.HCvlryBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.HCvlryBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.HCvlryBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

        else:
            if self.h_cvlry_battalion_index_add == 0:
            # убираем обьект empty из списка выбора
                self.HCvlryBrgdFirstBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(0, self.heavy_cvlry_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(0, self.heavy_cvlry_brigade_number)
                for bttlnName in bttln_list:
                    self.HCvlryBrgdFirstBattalion.addItem(bttlnName)
                # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.h_cvlry_battalion_index_add = 1

            self.HCvlryBrgdFirstBattalion.setDisabled(False)
            self.HCvlryBrgdSecondBattalion.setDisabled(False)
            if self.HCvlryBrgdFirstBattalion.currentText() != "Cuirassier":
                self.HCvlryBrgdThirdBattalion.setDisabled(False)


    def heavyCvlryBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.HCvlryBrgdCmndr.currentIndex(),self.heavy_cvlry_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.heavy_cvlry_brigade_number) for i in range(3))

        self.HCvlryBrgdTotalCost.setText(str(total_cost))
        self.heavy_cvlry_nmbr_of_battalions = (
            sum(self.presenter.BrigadeBttlnPresence(i, self.heavy_cvlry_brigade_number) for i in range(3)))

        self.divisionTotalCostView()

    def heavyCvlryBrgd1stBttlnCostView(self, bttln_choosen_from_list):

        self.brgdBttlnCostView(bttln_choosen_from_list, self.heavy_cvlry_brigade_number,
                               self.HCvlryBrgdFirstBattalionCost, self.heavyCvlryBrgdTotalCostView, 0,
                               self.HCvlryBrFirstBttlnModPushButton)

        match self.HCvlryBrgdFirstBattalion.currentText():
            case "empty":
                self.HCvlryBrgdThirdBattalion.setCurrentIndex(0)
                self.HCvlryBrgdThirdBattalion.setDisabled(True)
            case "Cuirassier":
                self.HCvlryBrgdThirdBattalion.setCurrentIndex(0)
                self.HCvlryBrgdThirdBattalion.setDisabled(True)
                if self.HCvlryBrgdSecondBattalion.currentText() != "Cuirassier":
                    self.HCvlryBrgdSecondBattalion.setCurrentIndex(0)
            case "Dragoon":
                self.HCvlryBrgdThirdBattalion.setDisabled(False)
                if self.HCvlryBrgdSecondBattalion.currentText() != "Dragoon":
                    self.HCvlryBrgdSecondBattalion.setCurrentIndex(0)
                if self.HCvlryBrgdThirdBattalion.currentText() != "Dragoon":
                    self.HCvlryBrgdThirdBattalion.setCurrentIndex(0)
            case "Dragoon on foot":
                self.HCvlryBrgdThirdBattalion.setDisabled(False)
                if self.HCvlryBrgdSecondBattalion.currentText() != "Dragoon on foot":
                    self.HCvlryBrgdSecondBattalion.setCurrentIndex(0)
                if self.HCvlryBrgdThirdBattalion.currentText() != "Dragoon on foot":
                    self.HCvlryBrgdThirdBattalion.setCurrentIndex(0)

    def heavyCvlryBrgd2ndBttlnCostView(self, bttln_choosen_from_list):

        self.brgdBttlnCostView(bttln_choosen_from_list, self.heavy_cvlry_brigade_number,
                               self.HCvlryBrgdSecondBattalionCost, self.heavyCvlryBrgdTotalCostView, 1,
                               self.HCvlryBrSecondBttlnModPushButton)

        if self.HCvlryBrgdFirstBattalion.currentText() == "Dragoon":
            if self.HCvlryBrgdSecondBattalion.currentText() == "Cuirassier" or self.HCvlryBrgdSecondBattalion.currentText() == "Dragoon on foot":
                self.HCvlryBrgdSecondBattalion.setCurrentIndex(0)
        elif self.HCvlryBrgdFirstBattalion.currentText() == "Dragoon on foot":
            if self.HCvlryBrgdSecondBattalion.currentText() == "Cuirassier" or self.HCvlryBrgdSecondBattalion.currentText() == "Dragoon":
                self.HCvlryBrgdSecondBattalion.setCurrentIndex(0)
        elif self.HCvlryBrgdFirstBattalion.currentText() == "Cuirassier":
            if self.HCvlryBrgdSecondBattalion.currentText() == "Dragoon" or self.HCvlryBrgdSecondBattalion.currentText() == "Dragoon on foot":
                self.HCvlryBrgdSecondBattalion.setCurrentIndex(0)

    def heavyCvlryBrgd3rdBttlnCostView(self, bttln_choosen_from_list):

        self.brgdBttlnCostView(bttln_choosen_from_list, self.heavy_cvlry_brigade_number,
                               self.HCvlryBrgdThirdBattalionCost, self.heavyCvlryBrgdTotalCostView, 2,
                               self.HCvlryBrThirdBttlnModPushButton)

        if self.HCvlryBrgdFirstBattalion.currentText() == "Dragoon":
            if self.HCvlryBrgdThirdBattalion.currentText() == "Cuirassier" or self.HCvlryBrgdThirdBattalion.currentText() == "Dragoon on foot":
                self.HCvlryBrgdThirdBattalion.setCurrentIndex(0)
        elif self.HCvlryBrgdFirstBattalion.currentText() == "Dragoon on foot":
            if self.HCvlryBrgdThirdBattalion.currentText() == "Cuirassier" or self.HCvlryBrgdThirdBattalion.currentText() == "Dragoon":
                self.HCvlryBrgdThirdBattalion.setCurrentIndex(0)

    def heavyCvlry_the_first_bttln_mod_button_was_clicked(self):

        if self.HCvlryBrgdFirstBattalion.currentIndex() +self.h_cvlry_battalion_index_add != 0:
            battalion_order = "First Regiment"
            self.order_number = 0  # первый по порядку кав полк
            self.brgdFirstBattalionCostSetText = self.HCvlryBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.heavyCvlryBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.heavy_cvlry_brigade_number, self.HCvlryBrFirstBttlnModPushButton, self.HCvlryBrgdFirstBattalion.currentText(), self.order_number)

    def heavyCvlry_the_second_bttln_mod_button_was_clicked(self):

        if self.HCvlryBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Regiment"
            self.order_number = 1  # второй по порядку кав полк
            self.brgdSecondBattalionCostSetText = self.HCvlryBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.heavyCvlryBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.heavy_cvlry_brigade_number, self.HCvlryBrSecondBttlnModPushButton, self.HCvlryBrgdSecondBattalion.currentText(), self.order_number)

    def heavyCvlry_the_third_bttln_mod_button_was_clicked(self):

        if self.HCvlryBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Regiment"
            self.order_number = 2  # третий по порядку кав полк
            self.brgdThirdBattalionCostSetText = self.HCvlryBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.heavyCvlryBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.heavy_cvlry_brigade_number, self.HCvlryBrThirdBttlnModPushButton, self.HCvlryBrgdThirdBattalion.currentText(), self.order_number)

    #--------------------------------------------------------------------------------------------------------------------
    def cossack_brigade_bttln_Lists(self):
        cossack_brgd_bttlns_list = [self.CossackBrgdFirstBattalion,
                                    self.CossackBrgdSecondBattalion,
                                    self.CossackBrgdThirdBattalion,
                                    self.CossackBrgdFourthBattalion,
                                    self.CossackBrgdFifthBattalion,
                                    self.CossackBrgdSixthBattalion]

        brigade_bttln_Lists(self.cossack_brigade_number, self.presenter, self.CossackBrgdCmndr, cossack_brgd_bttlns_list)

    def cossackBrgdCommanderCostView(self, index):
        value = self.presenter.BrigadeCmndrsCost(index, self.cossack_brigade_number)
        self.CossackBrgdCmndrCost.setText(str(value))
        self.cossackBrgdTotalCostView()

        if self.CossackBrgdCmndr.currentIndex() < 1:

            if self.presenter.BrigadeBttlnName(0, self.cossack_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(0, self.cossack_brigade_number)

                self.CossackBrgdFirstBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(0, self.cossack_brigade_number)
                for bttlnName in bttln_list:
                    self.CossackBrgdFirstBattalion.addItem(bttlnName)

                self.cossack_battalion1_index_add = 0

            if self.presenter.BrigadeBttlnName(1, self.cossack_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(1, self.cossack_brigade_number)

                self.CossackBrgdSecondBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(1, self.cossack_brigade_number)
                for bttlnName in bttln_list:
                    self.CossackBrgdSecondBattalion.addItem(bttlnName)

                self.cossack_battalion2_index_add = 0

            self.CossackBrgdFirstBattalion.setCurrentIndex(0)
            self.CossackBrgdFirstBattalion.setDisabled(True)
            self.CossackBrgdSecondBattalion.setCurrentIndex(0)
            self.CossackBrgdSecondBattalion.setDisabled(True)
            self.CossackBrgdThirdBattalion.setCurrentIndex(0)
            self.CossackBrgdThirdBattalion.setDisabled(True)
            self.CossackBrgdFourthBattalion.setCurrentIndex(0)
            self.CossackBrgdFourthBattalion.setDisabled(True)
            self.CossackBrgdFifthBattalion.setCurrentIndex(0)
            self.CossackBrgdFifthBattalion.setDisabled(True)
            self.CossackBrgdSixthBattalion.setCurrentIndex(0)
            self.CossackBrgdSixthBattalion.setDisabled(True)

            self.CossackBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CossackBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CossackBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CossackBrFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CossackBrFifthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.CossackBrSixthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

        else:
            if self.cossack_battalion1_index_add == 0:
            # убираем обьект empty из списка выбора
                self.CossackBrgdFirstBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(0, self.cossack_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(0, self.cossack_brigade_number)
                for bttlnName in bttln_list:
                    self.CossackBrgdFirstBattalion.addItem(bttlnName)
                # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.cossack_battalion1_index_add = 1
            if self.cossack_battalion2_index_add == 0:
            # убираем обьект empty из списка выбора
                self.CossackBrgdSecondBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(1, self.cossack_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(1, self.cossack_brigade_number)
                for bttlnName in bttln_list:
                    self.CossackBrgdSecondBattalion.addItem(bttlnName)
                # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.cossack_battalion2_index_add = 1


            self.CossackBrgdFirstBattalion.setDisabled(False)
            self.CossackBrgdSecondBattalion.setDisabled(False)
            self.CossackBrgdThirdBattalion.setDisabled(False)
            self.CossackBrgdFourthBattalion.setDisabled(False)
            self.CossackBrgdFifthBattalion.setDisabled(False)
            self.CossackBrgdSixthBattalion.setDisabled(False)

    def cossackBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.cossack_brigade_number,
                               self.CossackBrgdFirstBattalionCost, self.cossackBrgdTotalCostView, 0, self.CossackBrFirstBttlnModPushButton)

        if self.CossackBrgdFirstBattalion.currentText() == "Free Cossack regiment":
            if self.LCvlryBrgdFirstBattalion.currentText() == "Free Cossack regiment" or self.LCvlryBrgdSecondBattalion.currentText() == "Free Cossack regiment" or self.LCvlryBrgdThirdBattalion.currentText() == "Free Cossack regiment":
                self.CossackBrgdFirstBattalion.setCurrentIndex(0)


    def cossackBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.cossack_brigade_number,
                               self.CossackBrgdSecondBattalionCost, self.cossackBrgdTotalCostView, 1, self.CossackBrSecondBttlnModPushButton)

    def cossackBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.cossack_brigade_number,
                               self.CossackBrgdThirdBattalionCost, self.cossackBrgdTotalCostView, 2, self.CossackBrThirdBttlnModPushButton)

    def cossackBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.cossack_brigade_number,
                               self.CossackBrgdFourthBattalionCost, self.cossackBrgdTotalCostView, 3, self.CossackBrFourthBttlnModPushButton)

    def cossackBrgd5thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.cossack_brigade_number,
                               self.CossackBrgdFifthBattalionCost, self.cossackBrgdTotalCostView, 4, self.CossackBrFifthBttlnModPushButton)

    def cossackBrgd6thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.cossack_brigade_number,
                               self.CossackBrgdSixthBattalionCost, self.cossackBrgdTotalCostView, 5, self.CossackBrSixthBttlnModPushButton)

    def cossackBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.CossackBrgdCmndr.currentIndex(), self.cossack_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.cossack_brigade_number) for i in range(6))

        self.CossackBrgdTotalCost.setText(str(total_cost))
        self.cossack_nmbr_of_battalions = (
            sum(self.presenter.BrigadeBttlnPresence(i, self.cossack_brigade_number) for i in range(6)))

        self.divisionTotalCostView()

    def cossack_the_first_bttln_mod_button_was_clicked(self):

        if self.CossackBrgdFirstBattalion.currentIndex() +self.cossack_battalion1_index_add != 0:
            battalion_order = "First Regiment"
            self.order_number = 0  # первый по порядку кав полк
            self.brgdFirstBattalionCostSetText = self.CossackBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.cossackBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.cossack_brigade_number, self.CossackBrFirstBttlnModPushButton, self.CossackBrgdFirstBattalion.currentText(), self.order_number)

    def cossack_the_second_bttln_mod_button_was_clicked(self):

        if self.CossackBrgdSecondBattalion.currentIndex() +self.cossack_battalion2_index_add != 0:
            battalion_order = "Second Regiment"
            self.order_number = 1  # второй по порядку кав полк
            self.brgdSecondBattalionCostSetText = self.CossackBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.cossackBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.cossack_brigade_number, self.CossackBrSecondBttlnModPushButton, self.CossackBrgdSecondBattalion.currentText(), self.order_number)
    def cossack_the_third_bttln_mod_button_was_clicked(self):

        if self.CossackBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Regiment"
            self.order_number = 2  # третий по порядку кав полк
            self.brgdThirdBattalionCostSetText = self.CossackBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.cossackBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.cossack_brigade_number, self.CossackBrThirdBttlnModPushButton, self.CossackBrgdThirdBattalion.currentText(), self.order_number)

    def cossack_the_fourth_bttln_mod_button_was_clicked(self):

        if self.CossackBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Regiment"
            self.order_number = 3  # четвертый по порядку кав полк
            self.brgdFourthBattalionCostSetText = self.CossackBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.cossackBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.cossack_brigade_number, self.CossackBrFourthBttlnModPushButton, self.CossackBrgdFourthBattalion.currentText(), self.order_number)

    def cossack_the_fifth_bttln_mod_button_was_clicked(self):

        if self.CossackBrgdFifthBattalion.currentIndex() != 0:
            battalion_order = "Fifth Regiment"
            self.order_number = 4  # пятый по порядку кав полк
            self.brgdFifthBattalionCostSetText = self.CossackBrgdFifthBattalionCost.setText
            self.brgdTotalCostView = self.cossackBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.cossack_brigade_number, self.CossackBrFifthBttlnModPushButton, self.CossackBrgdFifthBattalion.currentText(), self.order_number)

    def cossack_the_sixth_bttln_mod_button_was_clicked(self):

        if self.CossackBrgdSixthBattalion.currentIndex() != 0:
            battalion_order = "Sixth Regiment"
            self.order_number = 5  # шестой по порядку кав полк
            self.brgdSixthBattalionCostSetText = self.CossackBrgdSixthBattalionCost.setText
            self.brgdTotalCostView = self.cossackBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.cossack_brigade_number, self.CossackBrSixthBttlnModPushButton, self.CossackBrgdSixthBattalion.currentText(), self.order_number)
    #--------------------------------------------------------------------------------------------------------------------
    def imp_grd_inf_brigade_bttln_Lists(self):
        imp_grd_inf_brgd_bttlns_list = [self.ImpGrdInfBrgdFirstBattalion,
                                        self.ImpGrdInfBrgdSecondBattalion,
                                        self.ImpGrdInfBrgdThirdBattalion,
                                        self.ImpGrdInfBrgdFourthBattalion,
                                        self.ImpGrdInfBrgdFifthBattalion,
                                        self.ImpGrdInfBrgdSixthBattalion,
                                        self.ImpGrdInfBrgdAdditional1Battalion,
                                        self.ImpGrdInfBrgdAdditional2Battalion]

        brigade_bttln_Lists(self.imp_grd_inf_brigade_number, self.presenter, self.ImpGrdInfBrgdCmndr, imp_grd_inf_brgd_bttlns_list)

    def impGrdInfBrgdCommanderCostView(self, index):
        value = self.presenter.BrigadeCmndrsCost(index, self.imp_grd_inf_brigade_number)
        self.ImpGrdInfBrgdCmndrCost.setText(str(value))
        self.impGrdInfBrgdTotalCostView()

        if self.ImpGrdInfBrgdCmndr.currentIndex() < 1:

            if self.presenter.BrigadeBttlnName(0, self.imp_grd_inf_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(0, self.imp_grd_inf_brigade_number)

                self.ImpGrdInfBrgdFirstBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(0, self.imp_grd_inf_brigade_number)
                for bttlnName in bttln_list:
                    self.ImpGrdInfBrgdFirstBattalion.addItem(bttlnName)

                self.imp_grd_inf_battalion_index_add = 0

            self.ImpGrdInfBrgdFirstBattalion.setCurrentIndex(0)
            self.ImpGrdInfBrgdFirstBattalion.setDisabled(True)
            self.ImpGrdInfBrgdSecondBattalion.setCurrentIndex(0)
            self.ImpGrdInfBrgdSecondBattalion.setDisabled(True)
            self.ImpGrdInfBrgdThirdBattalion.setCurrentIndex(0)
            self.ImpGrdInfBrgdThirdBattalion.setDisabled(True)
            self.ImpGrdInfBrgdFourthBattalion.setCurrentIndex(0)
            self.ImpGrdInfBrgdFourthBattalion.setDisabled(True)
            self.ImpGrdInfBrgdFifthBattalion.setCurrentIndex(0)
            self.ImpGrdInfBrgdFifthBattalion.setDisabled(True)
            self.ImpGrdInfBrgdSixthBattalion.setCurrentIndex(0)
            self.ImpGrdInfBrgdSixthBattalion.setDisabled(True)
            self.ImpGrdInfBrgdAdditional1Battalion.setCurrentIndex(0)
            self.ImpGrdInfBrgdAdditional1Battalion.setDisabled(True)
            self.ImpGrdInfBrgdAdditional2Battalion.setCurrentIndex(0)
            self.ImpGrdInfBrgdAdditional2Battalion.setDisabled(True)

            self.ImpGrdInfBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.ImpGrdInfBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.ImpGrdInfBrThirdBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.ImpGrdInfBrFourthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.ImpGrdInfBrFifthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.ImpGrdInfBrSixthBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

        else:
            if self.imp_grd_inf_battalion_index_add == 0:
            # убираем обьект empty из списка выбора
                self.ImpGrdInfBrgdFirstBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(0, self.imp_grd_inf_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(0, self.imp_grd_inf_brigade_number)
                for bttlnName in bttln_list:
                    self.ImpGrdInfBrgdFirstBattalion.addItem(bttlnName)
                # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.imp_grd_inf_battalion_index_add = 1

            self.ImpGrdInfBrgdFirstBattalion.setDisabled(False)
            self.ImpGrdInfBrgdSecondBattalion.setDisabled(False)
            self.ImpGrdInfBrgdThirdBattalion.setDisabled(False)
            self.ImpGrdInfBrgdFourthBattalion.setDisabled(False)
            self.ImpGrdInfBrgdFifthBattalion.setDisabled(False)
            self.ImpGrdInfBrgdSixthBattalion.setDisabled(False)
            self.ImpGrdInfBrgdAdditional1Battalion.setDisabled(False)
            self.ImpGrdInfBrgdAdditional2Battalion.setDisabled(False)

    def impGrdInfBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.imp_grd_inf_brigade_number,
                               self.ImpGrdInfBrgdFirstBattalionCost, self.impGrdInfBrgdTotalCostView, 0, self.ImpGrdInfBrFirstBttlnModPushButton)

    def impGrdInfBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.imp_grd_inf_brigade_number,
                               self.ImpGrdInfBrgdSecondBattalionCost, self.impGrdInfBrgdTotalCostView, 1, self.ImpGrdInfBrSecondBttlnModPushButton)

    def impGrdInfBrgd3rdBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.imp_grd_inf_brigade_number,
                               self.ImpGrdInfBrgdThirdBattalionCost, self.impGrdInfBrgdTotalCostView, 2, self.ImpGrdInfBrThirdBttlnModPushButton)

    def impGrdInfBrgd4thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.imp_grd_inf_brigade_number,
                               self.ImpGrdInfBrgdFourthBattalionCost, self.impGrdInfBrgdTotalCostView, 3, self.ImpGrdInfBrFourthBttlnModPushButton)

    def impGrdInfBrgd5thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.imp_grd_inf_brigade_number,
                               self.ImpGrdInfBrgdFifthBattalionCost, self.impGrdInfBrgdTotalCostView, 4, self.ImpGrdInfBrFifthBttlnModPushButton)

    def impGrdInfBrgd6thBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.imp_grd_inf_brigade_number,
                               self.ImpGrdInfBrgdSixthBattalionCost, self.impGrdInfBrgdTotalCostView, 5, self.ImpGrdInfBrSixthBttlnModPushButton)

    def impGrdInfBrgdAdd1BttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.imp_grd_inf_brigade_number,
                               self.ImpGrdInfBrgdAdd1BattalionCost, self.impGrdInfBrgdTotalCostView, 6)

    def impGrdInfBrgdAdd2BttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.imp_grd_inf_brigade_number,
                               self.ImpGrdInfBrgdAdd2BattalionCost, self.impGrdInfBrgdTotalCostView, 7)


    def impGrdInfBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.ImpGrdInfBrgdCmndr.currentIndex(), self.imp_grd_inf_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.imp_grd_inf_brigade_number) for i in range(8))

        self.ImpGrdInfBrgdTotalCost.setText(str(total_cost))
        self.divisionTotalCostView()

    def imp_grd_inf_the_first_bttln_mod_button_was_clicked(self):

        if self.ImpGrdInfBrgdFirstBattalion.currentIndex() + self.imp_grd_inf_battalion_index_add != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку battalion
            self.brgdFirstBattalionCostSetText = self.ImpGrdInfBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.impGrdInfBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.imp_grd_inf_brigade_number, self.ImpGrdInfBrFirstBttlnModPushButton, self.ImpGrdInfBrgdFirstBattalion.currentText(), self.order_number)

    def imp_grd_inf_the_second_bttln_mod_button_was_clicked(self):

        if self.ImpGrdInfBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку battalion
            self.brgdSecondBattalionCostSetText = self.ImpGrdInfBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.impGrdInfBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.imp_grd_inf_brigade_number, self.ImpGrdInfBrSecondBttlnModPushButton, self.ImpGrdInfBrgdSecondBattalion.currentText(), self.order_number)
    def imp_grd_inf_the_third_bttln_mod_button_was_clicked(self):

        if self.ImpGrdInfBrgdThirdBattalion.currentIndex() != 0:
            battalion_order = "Third Battalion"
            self.order_number = 2  # третий по порядку battalion
            self.brgdThirdBattalionCostSetText = self.ImpGrdInfBrgdThirdBattalionCost.setText
            self.brgdTotalCostView = self.impGrdInfBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.imp_grd_inf_brigade_number, self.ImpGrdInfBrThirdBttlnModPushButton, self.ImpGrdInfBrgdThirdBattalion.currentText(), self.order_number)

    def imp_grd_inf_the_fourth_bttln_mod_button_was_clicked(self):

        if self.ImpGrdInfBrgdFourthBattalion.currentIndex() != 0:
            battalion_order = "Fourth Battalion"
            self.order_number = 3  # четвертый по порядку battalion
            self.brgdFourthBattalionCostSetText = self.ImpGrdInfBrgdFourthBattalionCost.setText
            self.brgdTotalCostView = self.impGrdInfBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.imp_grd_inf_brigade_number, self.ImpGrdInfBrFourthBttlnModPushButton, self.ImpGrdInfBrgdFourthBattalion.currentText(), self.order_number)

    def imp_grd_inf_the_fifth_bttln_mod_button_was_clicked(self):

        if self.ImpGrdInfBrgdFifthBattalion.currentIndex() != 0:
            battalion_order = "Fifth Battalion"
            self.order_number = 4  # пятый по порядку battalion
            self.brgdFifthBattalionCostSetText = self.ImpGrdInfBrgdFifthBattalionCost.setText
            self.brgdTotalCostView = self.impGrdInfBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.imp_grd_inf_brigade_number, self.ImpGrdInfBrFifthBttlnModPushButton, self.ImpGrdInfBrgdFifthBattalion.currentText(), self.order_number)

    def imp_grd_inf_the_sixth_bttln_mod_button_was_clicked(self):

        if self.ImpGrdInfBrgdSixthBattalion.currentIndex() != 0:
            battalion_order = "Sixth Battalion"
            self.order_number = 5  # шестой по порядку battalion
            self.brgdSixthBattalionCostSetText = self.ImpGrdInfBrgdSixthBattalionCost.setText
            self.brgdTotalCostView = self.impGrdInfBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.imp_grd_inf_brigade_number, self.ImpGrdInfBrSixthBttlnModPushButton, self.ImpGrdInfBrgdSixthBattalion.currentText(), self.order_number)
    #--------------------------------------------------------------------------------------------------------------------
    def imp_grd_l_cav_brigade_bttln_Lists(self):
        imp_grd_l_cav_brgd_bttlns_list = [self.ImpGrdLCavBrgdFirstBattalion,
                                          self.ImpGrdLCavBrgdSecondBattalion]
        brigade_bttln_Lists(self.imp_grd_l_cav_brigade_number, self.presenter, self.ImpGrdLCavBrgdCmndr, imp_grd_l_cav_brgd_bttlns_list)

    def impGrdLCavBrgdCommanderCostView(self, index):
        value = self.presenter.BrigadeCmndrsCost(index, self.imp_grd_l_cav_brigade_number)
        self.ImpGrdLCavBrgdCmndrCost.setText(str(value))
        self.impGrdLCavBrgdTotalCostView()

        if self.ImpGrdLCavBrgdCmndr.currentIndex() < 1:

            if self.presenter.BrigadeBttlnName(0, self.imp_grd_l_cav_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(0, self.imp_grd_l_cav_brigade_number)

                self.ImpGrdLCavBrgdFirstBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(0, self.imp_grd_l_cav_brigade_number)
                for bttlnName in bttln_list:
                    self.ImpGrdLCavBrgdFirstBattalion.addItem(bttlnName)

                self.imp_grd_l_cav_battalion_index_add = 0

            self.ImpGrdLCavBrgdFirstBattalion.setCurrentIndex(0)
            self.ImpGrdLCavBrgdFirstBattalion.setDisabled(True)
            self.ImpGrdLCavBrgdSecondBattalion.setCurrentIndex(0)
            self.ImpGrdLCavBrgdSecondBattalion.setDisabled(True)

            self.ImpGrdLCavBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.ImpGrdLCavBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

        else:
            if self.imp_grd_l_cav_battalion_index_add == 0:
            # убираем обьект empty из списка выбора
                self.ImpGrdLCavBrgdFirstBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(0, self.imp_grd_l_cav_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(0, self.imp_grd_l_cav_brigade_number)
                for bttlnName in bttln_list:
                    self.ImpGrdLCavBrgdFirstBattalion.addItem(bttlnName)
                # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.imp_grd_l_cav_battalion_index_add = 1

            self.ImpGrdLCavBrgdFirstBattalion.setDisabled(False)
            self.ImpGrdLCavBrgdSecondBattalion.setDisabled(False)

    def impGrdLCavBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.imp_grd_l_cav_brigade_number,
                               self.ImpGrdLCavBrgdFirstBattalionCost, self.impGrdLCavBrgdTotalCostView, 0, self.ImpGrdLCavBrFirstBttlnModPushButton)

    def impGrdLCavBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.imp_grd_l_cav_brigade_number,
                               self.ImpGrdLCavBrgdSecondBattalionCost, self.impGrdLCavBrgdTotalCostView, 1, self.ImpGrdLCavBrSecondBttlnModPushButton)

    def impGrdLCavBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.ImpGrdLCavBrgdCmndr.currentIndex(), self.imp_grd_l_cav_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.imp_grd_l_cav_brigade_number) for i in range(2))

        self.ImpGrdLCavBrgdTotalCost.setText(str(total_cost))
        self.divisionTotalCostView()

    def imp_grd_l_cav_the_first_bttln_mod_button_was_clicked(self):

        if self.ImpGrdLCavBrgdFirstBattalion.currentIndex() + self.imp_grd_l_cav_battalion_index_add != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку battalion
            self.brgdFirstBattalionCostSetText = self.ImpGrdLCavBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.impGrdLCavBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.imp_grd_l_cav_brigade_number,
                                              self.ImpGrdLCavBrFirstBttlnModPushButton,
                                              self.ImpGrdLCavBrgdFirstBattalion.currentText(), self.order_number)

    def imp_grd_l_cav_the_second_bttln_mod_button_was_clicked(self):

        if self.ImpGrdLCavBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку battalion
            self.brgdSecondBattalionCostSetText = self.ImpGrdLCavBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.impGrdLCavBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.imp_grd_l_cav_brigade_number,
                                              self.ImpGrdLCavBrSecondBttlnModPushButton,
                                              self.ImpGrdLCavBrgdSecondBattalion.currentText(), self.order_number)
    #--------------------------------------------------------------------------------------------------------------------
    def imp_grd_h_cav_brigade_bttln_Lists(self):
        imp_grd_h_cav_brgd_bttlns_list = [self.ImpGrdHCavBrgdFirstBattalion,
                                          self.ImpGrdHCavBrgdSecondBattalion]
        brigade_bttln_Lists(self.imp_grd_h_cav_brigade_number, self.presenter, self.ImpGrdHCavBrgdCmndr, imp_grd_h_cav_brgd_bttlns_list)

    def impGrdHCavBrgdCommanderCostView(self, index):
        value = self.presenter.BrigadeCmndrsCost(index, self.imp_grd_h_cav_brigade_number)
        self.ImpGrdHCavBrgdCmndrCost.setText(str(value))
        self.impGrdHCavBrgdTotalCostView()

        if self.ImpGrdHCavBrgdCmndr.currentIndex() < 1:

            if self.presenter.BrigadeBttlnName(0, self.imp_grd_h_cav_brigade_number) != "empty":
                self.presenter.FirstBttlnListChange(0, self.imp_grd_h_cav_brigade_number)

                self.ImpGrdHCavBrgdFirstBattalion.clear()
                bttln_list = self.presenter.BrigadeBttlnList(0, self.imp_grd_h_cav_brigade_number)
                for bttlnName in bttln_list:
                    self.ImpGrdHCavBrgdFirstBattalion.addItem(bttlnName)

                self.imp_grd_h_cav_battalion_index_add = 0

            self.ImpGrdHCavBrgdFirstBattalion.setCurrentIndex(0)
            self.ImpGrdHCavBrgdFirstBattalion.setDisabled(True)
            self.ImpGrdHCavBrgdSecondBattalion.setCurrentIndex(0)
            self.ImpGrdHCavBrgdSecondBattalion.setDisabled(True)

            self.ImpGrdHCavBrFirstBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")
            self.ImpGrdHCavBrSecondBttlnModPushButton.setStyleSheet("background-color : rgb(225,225,225) ")

        else:
            if self.imp_grd_h_cav_battalion_index_add == 0:
            # убираем обьект empty из списка выбора
                self.ImpGrdHCavBrgdFirstBattalion.clear()
                self.presenter.FirstBttlnListChangeToShow(0, self.imp_grd_h_cav_brigade_number)
                bttln_list = self.presenter.BrigadeBttlnList(0, self.imp_grd_h_cav_brigade_number)
                for bttlnName in bttln_list:
                    self.ImpGrdHCavBrgdFirstBattalion.addItem(bttlnName)
                # сдвигаем на единицу номер выбираемого кав полка чтобы пройти проверку при нажатии на кнопку модификаци
                self.imp_grd_h_cav_battalion_index_add = 1

            self.ImpGrdHCavBrgdFirstBattalion.setDisabled(False)
            self.ImpGrdHCavBrgdSecondBattalion.setDisabled(False)

    def impGrdHCavBrgd1stBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.imp_grd_h_cav_brigade_number,
                               self.ImpGrdHCavBrgdFirstBattalionCost, self.impGrdHCavBrgdTotalCostView, 0, self.ImpGrdHCavBrFirstBttlnModPushButton)

    def impGrdHCavBrgd2ndBttlnCostView(self, bttln_choosen_from_list):
        self.brgdBttlnCostView(bttln_choosen_from_list, self.imp_grd_h_cav_brigade_number,
                               self.ImpGrdHCavBrgdSecondBattalionCost, self.impGrdHCavBrgdTotalCostView, 1, self.ImpGrdHCavBrSecondBttlnModPushButton)

    def impGrdHCavBrgdTotalCostView(self):
        total_cost = self.presenter.BrigadeCmndrsCost(self.ImpGrdHCavBrgdCmndr.currentIndex(), self.imp_grd_h_cav_brigade_number) + \
                     sum(self.presenter.BrigadeBttlnCost(i, self.imp_grd_h_cav_brigade_number) for i in range(2))

        self.ImpGrdHCavBrgdTotalCost.setText(str(total_cost))
        self.divisionTotalCostView()

    def imp_grd_h_cav_the_first_bttln_mod_button_was_clicked(self):

        if self.ImpGrdHCavBrgdFirstBattalion.currentIndex() + self.imp_grd_h_cav_battalion_index_add != 0:
            battalion_order = "First Battalion"
            self.order_number = 0  # первый по порядку battalion
            self.brgdFirstBattalionCostSetText = self.ImpGrdHCavBrgdFirstBattalionCost.setText
            self.brgdTotalCostView = self.impGrdHCavBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.imp_grd_h_cav_brigade_number,
                                              self.ImpGrdHCavBrFirstBttlnModPushButton,
                                              self.ImpGrdHCavBrgdFirstBattalion.currentText(), self.order_number)

    def imp_grd_h_cav_the_second_bttln_mod_button_was_clicked(self):

        if self.ImpGrdHCavBrgdSecondBattalion.currentIndex() != 0:
            battalion_order = "Second Battalion"
            self.order_number = 1  # второй по порядку battalion
            self.brgdSecondBattalionCostSetText = self.ImpGrdHCavBrgdSecondBattalionCost.setText
            self.brgdTotalCostView = self.impGrdHCavBrgdTotalCostView
            self.bttln_mod_button_was_clicked(battalion_order, self.imp_grd_h_cav_brigade_number,
                                              self.ImpGrdHCavBrSecondBttlnModPushButton,
                                              self.ImpGrdHCavBrgdSecondBattalion.currentText(), self.order_number)
    #--------------------------------------------------------------------------------------------------------------------
    def all_artillery_batteries_Lists(self):
        artillery_battery_Lists1 = [self.LightArtilleryBattery1,
                                    self.LightArtilleryBattery2, self.LightArtilleryBattery3, self.LightArtilleryBattery4,
                                    self.LightArtilleryBattery5, self.LightArtilleryBattery6, self.HeavyArtilleryBattery1,
                                    self.HeavyArtilleryBattery2, self.HeavyArtilleryBattery3, self.HeavyArtilleryBattery4,
                                    self.UnicornBattery1, self.UnicornBattery2, self.UnicornBattery3, self.UnicornBattery4,
                                    self.UnicornBattery5, self.UnicornBattery6, self.HorseArtilleryBattery1,
                                    self.HorseArtilleryBattery2, self.HorseArtilleryBattery3]

        brigade_bttln_Lists(self.artillery_quasy_brigade_number, self.presenter, None,
                            artillery_battery_Lists1)

    def artLightBattery1CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.LightArtBttryCost1, self.ArtilleryTotalCost, 0)

    def artLightBattery2CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.LightArtBttryCost2, self.ArtilleryTotalCost, 1)

    def artLightBattery3CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.LightArtBttryCost3, self.ArtilleryTotalCost, 2)

    def artLightBattery4CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.LightArtBttryCost4, self.ArtilleryTotalCost, 3)

    def artLightBattery5CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.LightArtBttryCost5, self.ArtilleryTotalCost, 4)

    def artLightBattery6CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.LightArtBttryCost6, self.ArtilleryTotalCost, 5)

    def artHeavyBattery1CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.HvyArtBttryCost1, self.ArtilleryTotalCost, 6)

    def artHeavyBattery2CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.HvyArtBttryCost2, self.ArtilleryTotalCost, 7)

    def artHeavyBattery3CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.HvyArtBttryCost3, self.ArtilleryTotalCost, 8)

    def artHeavyBattery4CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.HvyArtBttryCost4, self.ArtilleryTotalCost, 9)

    def unicornBattery1CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.UnicornBttryCost1, self.ArtilleryTotalCost, 10)
    def unicornBattery2CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.UnicornBttryCost2, self.ArtilleryTotalCost, 11)

    def unicornBattery3CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.UnicornBttryCost3, self.ArtilleryTotalCost, 12)

    def unicornBattery4CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.UnicornBttryCost4, self.ArtilleryTotalCost, 13)

    def unicornBattery5CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.UnicornBttryCost5, self.ArtilleryTotalCost, 14)

    def unicornBattery6CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.UnicornBttryCost6, self.ArtilleryTotalCost, 15)

    def horseArtBattery1CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.HorseArtBttryCost1, self.ArtilleryTotalCost, 16)

    def horseArtBattery2CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.HorseArtBttryCost2, self.ArtilleryTotalCost, 17)

    def horseArtBattery3CostView(self, battery_choosen_from_list):
        self.brgdBttlnCostView(battery_choosen_from_list, self.artillery_quasy_brigade_number,
                               self.HorseArtBttryCost3, self.ArtilleryTotalCost, 18)


    def ArtilleryTotalCost(self):
        self.artillery_total_cost = sum(self.presenter.BrigadeBttlnCost(i, self.artillery_quasy_brigade_number) for i in range(19))
        self.divisionTotalCostView()

    #--------------------------------------------------------------------------------------------------------------------

    def earth_works_Lists(self):
        earthworks_list = [self.EarthWorks1, self.EarthWorks2]
        brigade_bttln_Lists(self.earthworks_quasy_brigade_number, self.presenter, None, earthworks_list)

    def earthworks1CostView(self, battery_choosen_from_list):

        self.brgdBttlnCostView(battery_choosen_from_list, self.earthworks_quasy_brigade_number,
                                   self.EarthWorks1Cost, self.EarthWorksTotalCost, 0)
    def earthworks2CostView(self, battery_choosen_from_list):

        self.brgdBttlnCostView(battery_choosen_from_list, self.earthworks_quasy_brigade_number,
                                   self.EarthWorks2Cost, self.EarthWorksTotalCost, 1)

    def EarthWorksTotalCost(self):
        self.earthworks_total_cost = sum(self.presenter.BrigadeBttlnCost(i, self.earthworks_quasy_brigade_number) for i in range(2))
        self.divisionTotalCostView()

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
        # если чекбокс нажат и такой бонус уже есть, то показывается стоимость взятая из объекта батальон
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

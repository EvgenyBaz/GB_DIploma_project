# pyuic6 StartGuiWindow.ui -o StartGuiWindow.py
# pyuic6 RusDivisionGuiWindow.ui -o RusDivisionGuiWindow.py
# pyuic6 BonusGuiWindow.ui -o BonusGuiWindow.py
import json

from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QFileDialog
import sys
from PyQt6 import QtWidgets, uic

from view.StartWindow import StartWindow
from view.RusDivisionWindow import RusDivisionWindow
from view.ItaDivisionWindow import ItaDivisionWindow
from view.E_message import MessageWindow


class MainWindow(QMainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # self.setupUi(self)
        self.error_message = MessageWindow()

        self.flagToLoad = False

    def show_StartWindow(self):
        self.startWindow = StartWindow()
        self.startWindow.setWindowTitle("Black Powder 2.0 Army Builder")

        self.startWindow.actionLoad.triggered.connect(self.loadFile)
        self.startWindow.actionAbout.triggered.connect(self.aboutMessage)

        self.startWindow.pushButton_Russia.clicked.connect(self.show_RusDivisionWindow) # по нажатию кнопки включаем окно с описанием корпуса русской армии
        self.startWindow.pushButton_Russia.clicked.connect(self.startWindow.close) # выключаем текущее окно
        self.startWindow.pushButton_France.clicked.connect(self.the_fra_button_was_clicked) # заглушка
        self.startWindow.pushButton_Italy.clicked.connect(self.show_ItaDivisionWindow)
        self.startWindow.pushButton_Italy.clicked.connect(self.startWindow.close)


        self.startWindow.show()

    def loadFile(self):

        fileName, _= QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            filter='Data File (*.dat)'
        )

        if fileName:
            try:
                with open(fileName, 'r') as fileToLoad:
                    self.data = json.load(fileToLoad)
                    self.dataToTableFill(self.data)
            except:
                self.error_message.text("load army list error")
                self.error_message.show()
        else:
            pass

    def dataToTableFill(self, data):
        match data["Side"]:
            case "Rus":
                self.flagToLoad = True
                self.startWindow.pushButton_Russia.click()
            case "Ita":
                self.flagToLoad = True
                self.startWindow.pushButton_Italy.click()
            case _:
                self.error_message.text("this country is not available")
                self.error_message.show()


    def show_RusDivisionWindow(self):
        self.rusDivisionWindow = RusDivisionWindow()

# добавляем прокрутку
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidget(self.rusDivisionWindow)
        self.scrollArea.show()
        self.scrollArea.resize(1600, 1000)
# помещаем окно в левый верхний угол
        qr=self.frameGeometry()
        cp=QtGui.QGuiApplication.primaryScreen().availableGeometry().topLeft()
        qr.moveTopLeft(cp)
        self.scrollArea.move(qr.topLeft())

        self.scrollArea.setWindowTitle("Black Powder 2.0 Army Builder")

        # self.rusDivisionWindow.setWindowTitle("Black Powder 2.0 Army Builder")
        # инициализация начальных значений полей
        self.rusDivisionWindow.generalCost.setText("0")
        self.rusDivisionWindow.aBrgdTotalCost.setText("0")
        self.rusDivisionWindow.bBrgdTotalCost.setText("0")
        self.rusDivisionWindow.cBrgdTotalCost.setText("0")
        self.rusDivisionWindow.JgrBrgdTotalCost.setText("0")
        self.rusDivisionWindow.CombGrndrBrgdTotalCost.setText("0")
        self.rusDivisionWindow.GrndrBrgdTotalCost.setText("0")
        self.rusDivisionWindow.LCvlryBrgdTotalCost.setText("0")
        self.rusDivisionWindow.HCvlryBrgdTotalCost.setText("0")
        self.rusDivisionWindow.CossackBrgdTotalCost.setText("0")
        self.rusDivisionWindow.ImpGrdInfBrgdTotalCost.setText("0")
        self.rusDivisionWindow.ImpGrdLCavBrgdTotalCost.setText("0")
        self.rusDivisionWindow.ImpGrdHCavBrgdTotalCost.setText("0")

        # инициализация списков батальонов в бригадах
        self.rusDivisionWindow.division_cmndrs_list()
        self.rusDivisionWindow.a_brigade_bttln_Lists()
        self.rusDivisionWindow.b_brigade_bttln_Lists()
        self.rusDivisionWindow.c_brigade_bttln_Lists()
        self.rusDivisionWindow.jgr_brigade_bttln_Lists()
        self.rusDivisionWindow.comb_grndr_brigade_bttln_Lists()
        self.rusDivisionWindow.grndr_brigade_bttln_Lists()
        self.rusDivisionWindow.light_cvlry_brigade_bttln_Lists()
        self.rusDivisionWindow.heavy_cvlry_brigade_bttln_Lists()
        self.rusDivisionWindow.cossack_brigade_bttln_Lists()
        self.rusDivisionWindow.imp_grd_inf_brigade_bttln_Lists()
        self.rusDivisionWindow.imp_grd_l_cav_brigade_bttln_Lists()
        self.rusDivisionWindow.imp_grd_h_cav_brigade_bttln_Lists()

        self.rusDivisionWindow.all_artillery_batteries_Lists()
        self.rusDivisionWindow.earth_works_Lists()

        if self.flagToLoad:
            try:
                self.rusDivisionWindow.loadData(self.data)
            except:
                self.error_message.text("load army list error")
                self.error_message.show()

        self.rusDivisionWindow.show()


    def the_fra_button_was_clicked(self): # заглушка
        self.error_message.text("France will be available in further updates")
        self.error_message.show()

    def show_ItaDivisionWindow(self):
        self.itaDivisionWindow = ItaDivisionWindow()

        # добавляем прокрутку
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidget(self.itaDivisionWindow)
        self.scrollArea.show()
        self.scrollArea.resize(1600, 1020)
        # поещаем окно в левый верхний угол
        qr = self.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().topLeft()
        qr.moveTopLeft(cp)
        self.scrollArea.move(qr.topLeft())

        self.scrollArea.setWindowTitle("Black Powder 2.0 Army Builder")

        # инициализация начальных значений полей
        self.itaDivisionWindow.generalCost.setText("0")
        self.itaDivisionWindow.aBrgdTotalCost.setText("0")
        self.itaDivisionWindow.bBrgdTotalCost.setText("0")
        self.itaDivisionWindow.cBrgdTotalCost.setText("0")
        self.itaDivisionWindow.CvlryBrgdTotalCost.setText("0")
        self.itaDivisionWindow.GrdBrgdTotalCost.setText("0")



        # инициализация списков батальонов в бригадах
        self.itaDivisionWindow.division_cmndrs_list()
        self.itaDivisionWindow.a_brigade_1stReg_choice()
        self.itaDivisionWindow.a_brigade_2ndReg_choice()
        self.itaDivisionWindow.a_brigade_bttln_Lists()
        self.itaDivisionWindow.b_brigade_1stReg_choice()
        self.itaDivisionWindow.b_brigade_2ndReg_choice()
        self.itaDivisionWindow.b_brigade_bttln_Lists()
        self.itaDivisionWindow.c_brigade_1stReg_choice()
        self.itaDivisionWindow.c_brigade_2ndReg_choice()
        self.itaDivisionWindow.c_brigade_bttln_Lists()
        self.itaDivisionWindow.cvlry_brigade_bttln_Lists()
        self.itaDivisionWindow.guard_brigade_bttln_Lists()
        self.itaDivisionWindow.all_artillery_batteries_Lists()

        if self.flagToLoad:
            try:
                self.itaDivisionWindow.loadData(self.data)
            except:
                self.error_message.text("load army list error")
                self.error_message.show()

        self.itaDivisionWindow.show()








    def aboutMessage(self):
        self.error_message.text("Black Powder 2.0 army builder v 0.9<br>created by Evgeny Bazarov<br>This program is \
free for use<br>Source code <a href='https://github.com/EvgenyBaz/GB_DIploma_project'> on Github </a>")
        self.error_message.show()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show_StartWindow()
app.exec()

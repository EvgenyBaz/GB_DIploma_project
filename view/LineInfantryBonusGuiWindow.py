# Form implementation generated from reading ui file 'LineInfantryBonusGuiWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LineInfanntryBonusWindow(object):
    def setupUi(self, LineInfanntryBonusWindow):
        LineInfanntryBonusWindow.setObjectName("LineInfanntryBonusWindow")
        LineInfanntryBonusWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=LineInfanntryBonusWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(parent=self.centralwidget)
        self.name.setGeometry(QtCore.QRect(70, 100, 131, 16))
        self.name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name.setObjectName("name")
        self.cost = QtWidgets.QLabel(parent=self.centralwidget)
        self.cost.setGeometry(QtCore.QRect(250, 100, 71, 16))
        self.cost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cost.setObjectName("cost")
        self.checkBox_1 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(230, 190, 81, 20))
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(230, 220, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(230, 250, 81, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.bonus1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.bonus1.setGeometry(QtCore.QRect(140, 190, 55, 16))
        self.bonus1.setObjectName("bonus1")
        self.bonus2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.bonus2.setGeometry(QtCore.QRect(140, 220, 55, 16))
        self.bonus2.setObjectName("bonus2")
        self.bonus3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.bonus3.setGeometry(QtCore.QRect(140, 250, 55, 16))
        self.bonus3.setObjectName("bonus3")
        self.ok_button = QtWidgets.QToolButton(parent=self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(150, 350, 91, 22))
        self.ok_button.setObjectName("ok_button")
        self.cancel_button = QtWidgets.QToolButton(parent=self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(310, 350, 91, 22))
        self.cancel_button.setObjectName("cancel_button")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 70, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 70, 55, 16))
        self.label_2.setObjectName("label_2")
        LineInfanntryBonusWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=LineInfanntryBonusWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        LineInfanntryBonusWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=LineInfanntryBonusWindow)
        self.statusbar.setObjectName("statusbar")
        LineInfanntryBonusWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LineInfanntryBonusWindow)
        QtCore.QMetaObject.connectSlotsByName(LineInfanntryBonusWindow)

    def retranslateUi(self, LineInfanntryBonusWindow):
        _translate = QtCore.QCoreApplication.translate
        LineInfanntryBonusWindow.setWindowTitle(_translate("LineInfanntryBonusWindow", "MainWindow"))
        self.name.setText(_translate("LineInfanntryBonusWindow", "name"))
        self.cost.setText(_translate("LineInfanntryBonusWindow", "cost"))
        self.checkBox_1.setText(_translate("LineInfanntryBonusWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("LineInfanntryBonusWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("LineInfanntryBonusWindow", "CheckBox"))
        self.bonus1.setText(_translate("LineInfanntryBonusWindow", "bonus1"))
        self.bonus2.setText(_translate("LineInfanntryBonusWindow", "bonus2"))
        self.bonus3.setText(_translate("LineInfanntryBonusWindow", "bonus3"))
        self.ok_button.setText(_translate("LineInfanntryBonusWindow", "OK"))
        self.cancel_button.setText(_translate("LineInfanntryBonusWindow", "CANCEL"))
        self.label.setText(_translate("LineInfanntryBonusWindow", "Name"))
        self.label_2.setText(_translate("LineInfanntryBonusWindow", "Cost"))

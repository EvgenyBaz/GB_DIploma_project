# Form implementation generated from reading ui file 'RusCorpsGuiWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RusCorpsWindow(object):
    def setupUi(self, RusCorpsWindow):
        RusCorpsWindow.setObjectName("RusCorpsWindow")
        RusCorpsWindow.resize(1780, 1066)
        RusCorpsWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(parent=RusCorpsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 130, 191, 41))
        self.label.setObjectName("label")
        self.aBrgdFirstBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.aBrgdFirstBattalion.setGeometry(QtCore.QRect(90, 240, 191, 22))
        self.aBrgdFirstBattalion.setObjectName("aBrgdFirstBattalion")
        self.aBrgdSecondBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.aBrgdSecondBattalion.setGeometry(QtCore.QRect(90, 260, 191, 22))
        self.aBrgdSecondBattalion.setObjectName("aBrgdSecondBattalion")
        self.aBrgdThirdBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.aBrgdThirdBattalion.setGeometry(QtCore.QRect(90, 280, 191, 22))
        self.aBrgdThirdBattalion.setObjectName("aBrgdThirdBattalion")
        self.aBrgdFourthBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.aBrgdFourthBattalion.setGeometry(QtCore.QRect(90, 300, 191, 22))
        self.aBrgdFourthBattalion.setObjectName("aBrgdFourthBattalion")
        self.aBrgdAdditionalBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.aBrgdAdditionalBattalion.setGeometry(QtCore.QRect(90, 350, 191, 22))
        self.aBrgdAdditionalBattalion.setObjectName("aBrgdAdditionalBattalion")
        self.mainTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.mainTitle.setGeometry(QtCore.QRect(670, 0, 341, 41))
        self.mainTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainTitle.setObjectName("mainTitle")
        self.aBrgdAddBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.aBrgdAddBattalionCost.setGeometry(QtCore.QRect(20, 350, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aBrgdAddBattalionCost.setFont(font)
        self.aBrgdAddBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aBrgdAddBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.aBrgdAddBattalionCost.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.aBrgdAddBattalionCost.setText("")
        self.aBrgdAddBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.aBrgdAddBattalionCost.setObjectName("aBrgdAddBattalionCost")
        self.aBrgdFourthBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.aBrgdFourthBattalionCost.setGeometry(QtCore.QRect(20, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aBrgdFourthBattalionCost.setFont(font)
        self.aBrgdFourthBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aBrgdFourthBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.aBrgdFourthBattalionCost.setText("")
        self.aBrgdFourthBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.aBrgdFourthBattalionCost.setObjectName("aBrgdFourthBattalionCost")
        self.aBrgdThirdBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.aBrgdThirdBattalionCost.setGeometry(QtCore.QRect(20, 280, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aBrgdThirdBattalionCost.setFont(font)
        self.aBrgdThirdBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aBrgdThirdBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.aBrgdThirdBattalionCost.setText("")
        self.aBrgdThirdBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.aBrgdThirdBattalionCost.setObjectName("aBrgdThirdBattalionCost")
        self.aBrgdSecondBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.aBrgdSecondBattalionCost.setGeometry(QtCore.QRect(20, 260, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aBrgdSecondBattalionCost.setFont(font)
        self.aBrgdSecondBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aBrgdSecondBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.aBrgdSecondBattalionCost.setText("")
        self.aBrgdSecondBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.aBrgdSecondBattalionCost.setObjectName("aBrgdSecondBattalionCost")
        self.aBrgdFirstBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.aBrgdFirstBattalionCost.setGeometry(QtCore.QRect(20, 240, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aBrgdFirstBattalionCost.setFont(font)
        self.aBrgdFirstBattalionCost.setAutoFillBackground(False)
        self.aBrgdFirstBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aBrgdFirstBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.aBrgdFirstBattalionCost.setText("")
        self.aBrgdFirstBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.aBrgdFirstBattalionCost.setObjectName("aBrgdFirstBattalionCost")
        self.aBrgdTotalCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.aBrgdTotalCost.setGeometry(QtCore.QRect(20, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aBrgdTotalCost.setFont(font)
        self.aBrgdTotalCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aBrgdTotalCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.aBrgdTotalCost.setText("")
        self.aBrgdTotalCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.aBrgdTotalCost.setObjectName("aBrgdTotalCost")
        self.Cost = QtWidgets.QLabel(parent=self.centralwidget)
        self.Cost.setGeometry(QtCore.QRect(20, 120, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cost.setFont(font)
        self.Cost.setStyleSheet("")
        self.Cost.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Cost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Cost.setObjectName("Cost")
        self.aBrFirstBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.aBrFirstBttlnModPushButton.setGeometry(QtCore.QRect(300, 240, 71, 21))
        self.aBrFirstBttlnModPushButton.setObjectName("aBrFirstBttlnModPushButton")
        self.aBrSecondBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.aBrSecondBttlnModPushButton.setGeometry(QtCore.QRect(300, 260, 71, 21))
        self.aBrSecondBttlnModPushButton.setObjectName("aBrSecondBttlnModPushButton")
        self.aBrThirdBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.aBrThirdBttlnModPushButton.setGeometry(QtCore.QRect(300, 280, 71, 21))
        self.aBrThirdBttlnModPushButton.setObjectName("aBrThirdBttlnModPushButton")
        self.aBrFourthBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.aBrFourthBttlnModPushButton.setGeometry(QtCore.QRect(300, 300, 71, 21))
        self.aBrFourthBttlnModPushButton.setObjectName("aBrFourthBttlnModPushButton")
        self.aBrAddBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.aBrAddBttlnModPushButton.setGeometry(QtCore.QRect(300, 350, 71, 21))
        self.aBrAddBttlnModPushButton.setObjectName("aBrAddBttlnModPushButton")
        self.aBrgdCmndr = QtWidgets.QComboBox(parent=self.centralwidget)
        self.aBrgdCmndr.setGeometry(QtCore.QRect(90, 190, 191, 22))
        self.aBrgdCmndr.setObjectName("aBrgdCmndr")
        self.aBrgdCmndrCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.aBrgdCmndrCost.setGeometry(QtCore.QRect(20, 190, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aBrgdCmndrCost.setFont(font)
        self.aBrgdCmndrCost.setAutoFillBackground(False)
        self.aBrgdCmndrCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aBrgdCmndrCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.aBrgdCmndrCost.setText("")
        self.aBrgdCmndrCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.aBrgdCmndrCost.setObjectName("aBrgdCmndrCost")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 170, 191, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 220, 191, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 330, 191, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.bBrSecondBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bBrSecondBttlnModPushButton.setGeometry(QtCore.QRect(700, 260, 71, 21))
        self.bBrSecondBttlnModPushButton.setObjectName("bBrSecondBttlnModPushButton")
        self.bBrgdThirdBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.bBrgdThirdBattalionCost.setGeometry(QtCore.QRect(420, 280, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bBrgdThirdBattalionCost.setFont(font)
        self.bBrgdThirdBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bBrgdThirdBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.bBrgdThirdBattalionCost.setText("")
        self.bBrgdThirdBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bBrgdThirdBattalionCost.setObjectName("bBrgdThirdBattalionCost")
        self.bBrgdFirstBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.bBrgdFirstBattalionCost.setGeometry(QtCore.QRect(420, 240, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bBrgdFirstBattalionCost.setFont(font)
        self.bBrgdFirstBattalionCost.setAutoFillBackground(False)
        self.bBrgdFirstBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bBrgdFirstBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.bBrgdFirstBattalionCost.setText("")
        self.bBrgdFirstBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bBrgdFirstBattalionCost.setObjectName("bBrgdFirstBattalionCost")
        self.bBrgdFourthBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.bBrgdFourthBattalionCost.setGeometry(QtCore.QRect(420, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bBrgdFourthBattalionCost.setFont(font)
        self.bBrgdFourthBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bBrgdFourthBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.bBrgdFourthBattalionCost.setText("")
        self.bBrgdFourthBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bBrgdFourthBattalionCost.setObjectName("bBrgdFourthBattalionCost")
        self.bBrgdCmndrCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.bBrgdCmndrCost.setGeometry(QtCore.QRect(420, 190, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bBrgdCmndrCost.setFont(font)
        self.bBrgdCmndrCost.setAutoFillBackground(False)
        self.bBrgdCmndrCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bBrgdCmndrCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.bBrgdCmndrCost.setText("")
        self.bBrgdCmndrCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bBrgdCmndrCost.setObjectName("bBrgdCmndrCost")
        self.bBrgdThirdBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.bBrgdThirdBattalion.setGeometry(QtCore.QRect(490, 280, 191, 22))
        self.bBrgdThirdBattalion.setObjectName("bBrgdThirdBattalion")
        self.bBrAddBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bBrAddBttlnModPushButton.setGeometry(QtCore.QRect(700, 350, 71, 21))
        self.bBrAddBttlnModPushButton.setObjectName("bBrAddBttlnModPushButton")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 220, 191, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.bBrgdSecondBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.bBrgdSecondBattalionCost.setGeometry(QtCore.QRect(420, 260, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bBrgdSecondBattalionCost.setFont(font)
        self.bBrgdSecondBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bBrgdSecondBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.bBrgdSecondBattalionCost.setText("")
        self.bBrgdSecondBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bBrgdSecondBattalionCost.setObjectName("bBrgdSecondBattalionCost")
        self.bBrFourthBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bBrFourthBttlnModPushButton.setGeometry(QtCore.QRect(700, 300, 71, 21))
        self.bBrFourthBttlnModPushButton.setObjectName("bBrFourthBttlnModPushButton")
        self.bBrThirdBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bBrThirdBttlnModPushButton.setGeometry(QtCore.QRect(700, 280, 71, 21))
        self.bBrThirdBttlnModPushButton.setObjectName("bBrThirdBttlnModPushButton")
        self.bBrgdTotalCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.bBrgdTotalCost.setGeometry(QtCore.QRect(420, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bBrgdTotalCost.setFont(font)
        self.bBrgdTotalCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bBrgdTotalCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.bBrgdTotalCost.setText("")
        self.bBrgdTotalCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bBrgdTotalCost.setObjectName("bBrgdTotalCost")
        self.bBrFirstBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bBrFirstBttlnModPushButton.setGeometry(QtCore.QRect(700, 240, 71, 21))
        self.bBrFirstBttlnModPushButton.setObjectName("bBrFirstBttlnModPushButton")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 170, 191, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.bBrgdFirstBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.bBrgdFirstBattalion.setGeometry(QtCore.QRect(490, 240, 191, 22))
        self.bBrgdFirstBattalion.setObjectName("bBrgdFirstBattalion")
        self.bBrgdFourthBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.bBrgdFourthBattalion.setGeometry(QtCore.QRect(490, 300, 191, 22))
        self.bBrgdFourthBattalion.setObjectName("bBrgdFourthBattalion")
        self.bBrgdSecondBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.bBrgdSecondBattalion.setGeometry(QtCore.QRect(490, 260, 191, 22))
        self.bBrgdSecondBattalion.setObjectName("bBrgdSecondBattalion")
        self.bBrgdAddBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.bBrgdAddBattalionCost.setGeometry(QtCore.QRect(420, 350, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bBrgdAddBattalionCost.setFont(font)
        self.bBrgdAddBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bBrgdAddBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.bBrgdAddBattalionCost.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.bBrgdAddBattalionCost.setText("")
        self.bBrgdAddBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bBrgdAddBattalionCost.setObjectName("bBrgdAddBattalionCost")
        self.Cost_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Cost_2.setGeometry(QtCore.QRect(420, 120, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cost_2.setFont(font)
        self.Cost_2.setStyleSheet("")
        self.Cost_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Cost_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Cost_2.setObjectName("Cost_2")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(490, 330, 191, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(490, 130, 191, 41))
        self.label_8.setObjectName("label_8")
        self.bBrgdCmndr = QtWidgets.QComboBox(parent=self.centralwidget)
        self.bBrgdCmndr.setGeometry(QtCore.QRect(490, 190, 191, 22))
        self.bBrgdCmndr.setObjectName("bBrgdCmndr")
        self.bBrgdAdditionalBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.bBrgdAdditionalBattalion.setGeometry(QtCore.QRect(490, 350, 191, 22))
        self.bBrgdAdditionalBattalion.setObjectName("bBrgdAdditionalBattalion")
        self.cBrFirstBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cBrFirstBttlnModPushButton.setGeometry(QtCore.QRect(1100, 240, 71, 21))
        self.cBrFirstBttlnModPushButton.setObjectName("cBrFirstBttlnModPushButton")
        self.cBrgdSecondBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.cBrgdSecondBattalionCost.setGeometry(QtCore.QRect(820, 260, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cBrgdSecondBattalionCost.setFont(font)
        self.cBrgdSecondBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cBrgdSecondBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.cBrgdSecondBattalionCost.setText("")
        self.cBrgdSecondBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cBrgdSecondBattalionCost.setObjectName("cBrgdSecondBattalionCost")
        self.cBrgdAdditionalBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cBrgdAdditionalBattalion.setGeometry(QtCore.QRect(890, 350, 191, 22))
        self.cBrgdAdditionalBattalion.setObjectName("cBrgdAdditionalBattalion")
        self.cBrgdSecondBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cBrgdSecondBattalion.setGeometry(QtCore.QRect(890, 260, 191, 22))
        self.cBrgdSecondBattalion.setObjectName("cBrgdSecondBattalion")
        self.cBrFourthBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cBrFourthBttlnModPushButton.setGeometry(QtCore.QRect(1100, 300, 71, 21))
        self.cBrFourthBttlnModPushButton.setObjectName("cBrFourthBttlnModPushButton")
        self.Cost_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Cost_3.setGeometry(QtCore.QRect(820, 120, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cost_3.setFont(font)
        self.Cost_3.setStyleSheet("")
        self.Cost_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Cost_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Cost_3.setObjectName("Cost_3")
        self.cBrgdFourthBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.cBrgdFourthBattalionCost.setGeometry(QtCore.QRect(820, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cBrgdFourthBattalionCost.setFont(font)
        self.cBrgdFourthBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cBrgdFourthBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.cBrgdFourthBattalionCost.setText("")
        self.cBrgdFourthBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cBrgdFourthBattalionCost.setObjectName("cBrgdFourthBattalionCost")
        self.cBrgdFirstBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cBrgdFirstBattalion.setGeometry(QtCore.QRect(890, 240, 191, 22))
        self.cBrgdFirstBattalion.setObjectName("cBrgdFirstBattalion")
        self.cBrgdAddBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.cBrgdAddBattalionCost.setGeometry(QtCore.QRect(820, 350, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cBrgdAddBattalionCost.setFont(font)
        self.cBrgdAddBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cBrgdAddBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.cBrgdAddBattalionCost.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.cBrgdAddBattalionCost.setText("")
        self.cBrgdAddBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cBrgdAddBattalionCost.setObjectName("cBrgdAddBattalionCost")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(890, 130, 191, 41))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(890, 330, 191, 16))
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.cBrAddBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cBrAddBttlnModPushButton.setGeometry(QtCore.QRect(1100, 350, 71, 21))
        self.cBrAddBttlnModPushButton.setObjectName("cBrAddBttlnModPushButton")
        self.cBrgdTotalCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.cBrgdTotalCost.setGeometry(QtCore.QRect(820, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cBrgdTotalCost.setFont(font)
        self.cBrgdTotalCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cBrgdTotalCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.cBrgdTotalCost.setText("")
        self.cBrgdTotalCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cBrgdTotalCost.setObjectName("cBrgdTotalCost")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(890, 220, 191, 16))
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.cBrgdFirstBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.cBrgdFirstBattalionCost.setGeometry(QtCore.QRect(820, 240, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cBrgdFirstBattalionCost.setFont(font)
        self.cBrgdFirstBattalionCost.setAutoFillBackground(False)
        self.cBrgdFirstBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cBrgdFirstBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.cBrgdFirstBattalionCost.setText("")
        self.cBrgdFirstBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cBrgdFirstBattalionCost.setObjectName("cBrgdFirstBattalionCost")
        self.cBrgdCmndr = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cBrgdCmndr.setGeometry(QtCore.QRect(890, 190, 191, 22))
        self.cBrgdCmndr.setObjectName("cBrgdCmndr")
        self.cBrgdFourthBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cBrgdFourthBattalion.setGeometry(QtCore.QRect(890, 300, 191, 22))
        self.cBrgdFourthBattalion.setObjectName("cBrgdFourthBattalion")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(890, 170, 191, 16))
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.cBrgdCmndrCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.cBrgdCmndrCost.setGeometry(QtCore.QRect(820, 190, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cBrgdCmndrCost.setFont(font)
        self.cBrgdCmndrCost.setAutoFillBackground(False)
        self.cBrgdCmndrCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cBrgdCmndrCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.cBrgdCmndrCost.setText("")
        self.cBrgdCmndrCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cBrgdCmndrCost.setObjectName("cBrgdCmndrCost")
        self.cBrThirdBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cBrThirdBttlnModPushButton.setGeometry(QtCore.QRect(1100, 280, 71, 21))
        self.cBrThirdBttlnModPushButton.setObjectName("cBrThirdBttlnModPushButton")
        self.cBrgdThirdBattalionCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.cBrgdThirdBattalionCost.setGeometry(QtCore.QRect(820, 280, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cBrgdThirdBattalionCost.setFont(font)
        self.cBrgdThirdBattalionCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cBrgdThirdBattalionCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.cBrgdThirdBattalionCost.setText("")
        self.cBrgdThirdBattalionCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cBrgdThirdBattalionCost.setObjectName("cBrgdThirdBattalionCost")
        self.cBrgdThirdBattalion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cBrgdThirdBattalion.setGeometry(QtCore.QRect(890, 280, 191, 22))
        self.cBrgdThirdBattalion.setObjectName("cBrgdThirdBattalion")
        self.cBrSecondBttlnModPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cBrSecondBttlnModPushButton.setGeometry(QtCore.QRect(1100, 260, 71, 21))
        self.cBrSecondBttlnModPushButton.setObjectName("cBrSecondBttlnModPushButton")
        self.generalCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.generalCost.setGeometry(QtCore.QRect(680, 60, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.generalCost.setFont(font)
        self.generalCost.setAutoFillBackground(False)
        self.generalCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.generalCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.generalCost.setText("")
        self.generalCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.generalCost.setObjectName("generalCost")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(760, 40, 191, 16))
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.generalName = QtWidgets.QComboBox(parent=self.centralwidget)
        self.generalName.setGeometry(QtCore.QRect(760, 60, 191, 22))
        self.generalName.setObjectName("generalName")
        self.Cost_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Cost_4.setGeometry(QtCore.QRect(680, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cost_4.setFont(font)
        self.Cost_4.setStyleSheet("")
        self.Cost_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Cost_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Cost_4.setObjectName("Cost_4")
        self.Cost_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Cost_5.setGeometry(QtCore.QRect(990, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cost_5.setFont(font)
        self.Cost_5.setStyleSheet("")
        self.Cost_5.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Cost_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Cost_5.setObjectName("Cost_5")
        self.corpsTotalCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.corpsTotalCost.setGeometry(QtCore.QRect(1100, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.corpsTotalCost.setFont(font)
        self.corpsTotalCost.setAutoFillBackground(False)
        self.corpsTotalCost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.corpsTotalCost.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.corpsTotalCost.setText("")
        self.corpsTotalCost.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.corpsTotalCost.setObjectName("corpsTotalCost")
        RusCorpsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=RusCorpsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1780, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        RusCorpsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=RusCorpsWindow)
        self.statusbar.setObjectName("statusbar")
        RusCorpsWindow.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(parent=RusCorpsWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(RusCorpsWindow)
        QtCore.QMetaObject.connectSlotsByName(RusCorpsWindow)

    def retranslateUi(self, RusCorpsWindow):
        _translate = QtCore.QCoreApplication.translate
        RusCorpsWindow.setWindowTitle(_translate("RusCorpsWindow", "MainWindow"))
        self.label.setText(_translate("RusCorpsWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Line Infantry brigade</span></p></body></html>"))
        self.mainTitle.setText(_translate("RusCorpsWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Imperial Russian Army Corps</span></p></body></html>"))
        self.Cost.setText(_translate("RusCorpsWindow", "Cost"))
        self.aBrFirstBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.aBrSecondBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.aBrThirdBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.aBrFourthBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.aBrAddBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.label_2.setText(_translate("RusCorpsWindow", "Brigade Commander"))
        self.label_3.setText(_translate("RusCorpsWindow", "Core Battalions"))
        self.label_4.setText(_translate("RusCorpsWindow", "Additional Battalion"))
        self.bBrSecondBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.bBrAddBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.label_5.setText(_translate("RusCorpsWindow", "Core Battalions"))
        self.bBrFourthBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.bBrThirdBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.bBrFirstBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.label_6.setText(_translate("RusCorpsWindow", "Brigade Commander"))
        self.Cost_2.setText(_translate("RusCorpsWindow", "Cost"))
        self.label_7.setText(_translate("RusCorpsWindow", "Additional Battalion"))
        self.label_8.setText(_translate("RusCorpsWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Line Infantry brigade</span></p></body></html>"))
        self.cBrFirstBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.cBrFourthBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.Cost_3.setText(_translate("RusCorpsWindow", "Cost"))
        self.label_9.setText(_translate("RusCorpsWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Line Infantry brigade</span></p></body></html>"))
        self.label_10.setText(_translate("RusCorpsWindow", "Additional Battalion"))
        self.cBrAddBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.label_11.setText(_translate("RusCorpsWindow", "Core Battalions"))
        self.label_12.setText(_translate("RusCorpsWindow", "Brigade Commander"))
        self.cBrThirdBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.cBrSecondBttlnModPushButton.setText(_translate("RusCorpsWindow", "modify"))
        self.label_13.setText(_translate("RusCorpsWindow", "General"))
        self.Cost_4.setText(_translate("RusCorpsWindow", "Cost"))
        self.Cost_5.setText(_translate("RusCorpsWindow", "Total cost"))
        self.menuFile.setTitle(_translate("RusCorpsWindow", "File"))
        self.menuHelp.setTitle(_translate("RusCorpsWindow", "Help"))
        self.actionSave.setText(_translate("RusCorpsWindow", "Save"))

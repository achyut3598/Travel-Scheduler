# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Achyut\Project\Modify.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from travelSchedulerBackend import database
import keyring
from dateutil import parser
import os


class Ui_MainWindow(object):
    def add(self):
        USERNAME_KEY = 'Username_key'
        myDatabase = database('travelschedulerserver.database.windows.net','TravelScheduler','TravelSchedulerServer','G00dGrad3s')
        myUserName = keyring.get_password("TravelSchedulerUsername", USERNAME_KEY)
        myEventName = self.lineEdit.text()
        myStartTime = self.dateTimeEdit.text()
        myEndTime = self.dateTimeEdit_2.text()
        myCurrAddress = self.lineEdit_4.text()
        myDestAddress = self.lineEdit_5.text()
        myDatabase.addEvent(myEventName, myUserName, myDestAddress, myCurrAddress, parser.parse(myStartTime), parser.parse(myEndTime))

    def Redirect(self):
        os.system('python EventList.py')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 40, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 240, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 290, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 350, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 400, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(410, 179, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(410, 340, 191, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(410, 400, 191, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 90, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 460, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(410, 230, 194, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(410, 290, 194, 31))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Travel Scheduler"))
        self.label_2.setText(_translate("MainWindow", "Event Name"))
        self.label_3.setText(_translate("MainWindow", "Start Date/Time"))
        self.label_4.setText(_translate("MainWindow", "End Date/Time"))
        self.label_5.setText(_translate("MainWindow", "From"))
        self.label_6.setText(_translate("MainWindow", "To"))
        self.label_7.setText(_translate("MainWindow", "Add an event"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton.clicked.connect(self.add)
        self.pushButton.clicked.connect(self.Redirect)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Achyut\Project\EventList.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from travelSchedulerBackend import database
import keyring
from dateutil import parser
import Add
import os

class Ui_MainWindow(object):
    def Table(self):
        USERNAME_KEY = 'Username_key'
        myDatabase = database('travelschedulerserver.database.windows.net','TravelScheduler','TravelSchedulerServer','G00dGrad3s')
        myUserName = keyring.get_password("TravelSchedulerUsername", USERNAME_KEY)
        rows = myDatabase.getEventList(myUserName)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        #print (rows)
        for row_number, row_data in enumerate(rows):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def Save(self):
        USERNAME_KEY = 'Username_key'
        myDatabase = database('travelschedulerserver.database.windows.net','TravelScheduler','TravelSchedulerServer','G00dGrad3s')
        myUserName = keyring.get_password("TravelSchedulerUsername", USERNAME_KEY)
        myEventName = self.tableWidget.item(0,0).text()
        myStartTime = self.tableWidget.item(0,4).text()
        myEndTime = self.tableWidget.item(0,5).text()
        myCurrAddress = self.tableWidget.item(0,3).text()
        myDestAddress = self.tableWidget.item(0,2).text()
        myDatabase.modifyEvent(myEventName, myUserName, myDestAddress, myCurrAddress, myStartTime, myEndTime)
        myEventName = self.tableWidget.item(1,0).text()
        myStartTime = self.tableWidget.item(1,4).text()
        myEndTime = self.tableWidget.item(1,5).text()
        myCurrAddress = self.tableWidget.item(1,3).text()
        myDestAddress = self.tableWidget.item(1,2).text()
        myDatabase.modifyEvent(myEventName, myUserName, myDestAddress, myCurrAddress, myStartTime, myEndTime)
        myEventName = self.tableWidget.item(2,0).text()
        myStartTime = self.tableWidget.item(2,4).text()
        myEndTime = self.tableWidget.item(2,5).text()
        myCurrAddress = self.tableWidget.item(2,3).text()
        myDestAddress = self.tableWidget.item(2,2).text()
        myDatabase.modifyEvent(myEventName, myUserName, myDestAddress, myCurrAddress, myStartTime, myEndTime)

    def Add(self):
        os.system('python Add.py')

    def Redirect(self):
        os.system('python Dashboard.py')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(320, 60, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 120, 631, 361))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 500, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 500, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 500, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 500, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
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
        self.label_7.setText(_translate("MainWindow", "Event List"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Event Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "To"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "From"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Start Time"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "End Time"))
        self.pushButton.setText(_translate("MainWindow", "Refresh List"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.pushButton_3.setText(_translate("MainWindow", "Back"))
        self.pushButton_4.setText(_translate("MainWindow", "Add an Event"))
        self.pushButton.clicked.connect(self.Table)
        self.pushButton_2.clicked.connect(self.Save)
        self.pushButton_4.clicked.connect(self.Add)
        self.pushButton_3.clicked.connect(self.Redirect)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

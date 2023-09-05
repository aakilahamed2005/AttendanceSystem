
from PyQt5 import QtCore, QtGui, QtWidgets
from main import my_class

class Ui_AttendanceSystem(my_class):
    def setupUi(self, AttendanceSystem):
        AttendanceSystem.setObjectName("AttendanceSystem")
        AttendanceSystem.resize(650, 244)
        AttendanceSystem.setMinimumSize(QtCore.QSize(650, 244))
        AttendanceSystem.setMaximumSize(QtCore.QSize(650, 244))
        icon = QtGui.QIcon.fromTheme("attendance.ico")
        AttendanceSystem.setWindowIcon(icon)
        AttendanceSystem.setLayoutDirection(QtCore.Qt.LeftToRight)
        AttendanceSystem.setAutoFillBackground(False)
        AttendanceSystem.setStyleSheet("background-color:#222222;")
        self.centralwidget = QtWidgets.QWidget(AttendanceSystem)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 301, 41))
        self.label.setStyleSheet("font-family:Calibri;\n"
"font-size:20px;\n"
"color:#eeeeee;")
        self.label.setObjectName("label")
        self.numberOfSchoolDays = QtWidgets.QSpinBox(self.centralwidget)
        self.numberOfSchoolDays.setGeometry(QtCore.QRect(60, 70, 111, 41))
        self.numberOfSchoolDays.setStyleSheet("font-size:20px;\n"
"color:white;\n"
"\n"
"background-color:#333333;")
        self.numberOfSchoolDays.setObjectName("numberOfSchoolDays")
        self.numberOfSchoolDays.setMinimum(1)
        self.numberOfSchoolDays.setMaximum(300)
        self.numberOfPresentDays = QtWidgets.QSpinBox(self.centralwidget)
        self.numberOfPresentDays.setMinimum(0)
        self.numberOfPresentDays.setMaximum(300)
        self.numberOfPresentDays.setGeometry(QtCore.QRect(60, 150, 111, 41))
        self.numberOfPresentDays.setStyleSheet("font-size:20px;\n"
"color:white;\n"
"background-color:#333333;")
        self.numberOfPresentDays.setObjectName("numberOfPresentDays")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(411, 60, 221, 81))
        self.frame.setStyleSheet("background-color:#333333;\n"
"border-radius:5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(70, 10, 81, 21))
        self.label_5.setStyleSheet("color:#29fff8;\n"
"font-size:15px;")
        self.label_5.setObjectName("label_5")
        self.percentageValue = QtWidgets.QLabel(self.frame)
        self.percentageValue.setGeometry(QtCore.QRect(66, 30, 81, 41))
        self.percentageValue.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.percentageValue.setStyleSheet("color:#ff0000;\n"
"font-size:20px;")
        self.percentageValue.setAlignment(QtCore.Qt.AlignCenter)
        self.percentageValue.setObjectName("percentageValue")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 91, 16))
        self.label_2.setStyleSheet("color:#dddddd;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 91, 16))
        self.label_3.setStyleSheet("color:#dddddd;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 200, 141, 16))
        self.label_4.setStyleSheet("color:#444444;")
        self.label_4.setObjectName("label_4")
        self.studentIndexNo = QtWidgets.QSpinBox(self.centralwidget)
        self.studentIndexNo.setGeometry(QtCore.QRect(240, 70, 111, 41))
        self.studentIndexNo.setStyleSheet("font-size:20px;\n"
"color:white;\n"
"\n"
"background-color:#333333;")
        self.studentIndexNo.setMinimum(1)
        self.studentIndexNo.setMaximum(48)
        self.studentIndexNo.setObjectName("studentIndexNo")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 50, 91, 16))
        self.label_6.setStyleSheet("color:#dddddd;")
        self.label_6.setObjectName("label_6")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(220, 130, 75, 23))
        self.searchButton.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color:#007bff;\n"
"color:white;\n"
"font-family:Calibri;\n"
"font-size:13px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#0079bf;\n"
"}\n"
"\n"
"\n"
"")
        self.searchButton.setObjectName("searchButton")
        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(300, 130, 75, 23))
        self.updateButton.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color:#007bff;\n"
"color:white;\n"
"font-family:Calibri;\n"
"font-size:13px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#0079bf;\n"
"}\n"
"\n"
"\n"
"")
        self.updateButton.setObjectName("updateButton")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(530, 10, 141, 16))
        self.label_7.setStyleSheet("color:#444444;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(380, 170, 31, 16))
        self.label_8.setStyleSheet("color:#dddddd;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(420, 170, 221, 16))
        self.label_9.setStyleSheet("color:#ffffff;")
        self.label_9.setObjectName("label_9")
        AttendanceSystem.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AttendanceSystem)
        self.statusbar.setObjectName("statusbar")
        AttendanceSystem.setStatusBar(self.statusbar)

        self.retranslateUi(AttendanceSystem)
        QtCore.QMetaObject.connectSlotsByName(AttendanceSystem)


        #Connect
        self.searchButton.clicked.connect(self.search_student)
        self.updateButton.clicked.connect(self.update_data)

    def retranslateUi(self, AttendanceSystem):
        _translate = QtCore.QCoreApplication.translate
        AttendanceSystem.setWindowTitle(_translate("AttendanceSystem", "Attendance System - 1.0.1"))
        self.label.setText(_translate("AttendanceSystem", "ATTENDANCE CALCULATION SYSTEM "))
        self.label_5.setText(_translate("AttendanceSystem", "Percentage"))
        self.percentageValue.setText(_translate("AttendanceSystem", "0%"))
        self.label_2.setText(_translate("AttendanceSystem", "No of School Days"))
        self.label_3.setText(_translate("AttendanceSystem", "No Present Days"))
        self.label_4.setText(_translate("AttendanceSystem", "Developed By Aakil Ahamed"))
        self.label_6.setText(_translate("AttendanceSystem", "Student Index no"))
        self.searchButton.setText(_translate("AttendanceSystem", "Search"))
        self.updateButton.setText(_translate("AttendanceSystem", "Update"))
        self.label_7.setText(_translate("AttendanceSystem", "Created for 12/13 M1"))
        self.label_8.setText(_translate("AttendanceSystem", "Name:"))
        self.label_9.setText(_translate("AttendanceSystem", "__"))

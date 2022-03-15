# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    styleLineEditOk = ("QLineEdit{\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color:rgb(30, 30, 30);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(36, 36, 100);\n"
"    color:rgb(200,200,200);\n"
"}")

    styleLineEditError = ("QLineEdit{\n"
"    border: 2px solid rgb(255, 85, 127);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color:rgb(30, 30, 30);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(36, 36, 100);\n"
"    color:rgb(200,200,200);\n"
"}")


    def showMessage(self, message):
            self.frame_error.show()
            self.label_error.setText(message)

    def checkFields(self):
            textUser = ""
            textPassWord = ""

            if not self.lineEdit_user.text():
                    textUser = "User empty."
                    self.lineEdit_user.setStyleSheet(self.styleLineEditError)
            else:
                    textUser = ""
                    self.lineEdit_user.setStyleSheet(self.styleLineEditOk)

            if not self.lineEdit_password.text():
                    textPassWord = " Password empty."
                    self.lineEdit_password.setStyleSheet(self.styleLineEditError)
            else:
                    textPassWord = ""
                    self.lineEdit_password.setStyleSheet(self.styleLineEditOk)
            
            if textUser + textPassWord != "":
                    text = textUser + textPassWord
            else:
                    text = "Login OK!"
                    if self.checkBox_save_user.isChecked():
                            text = text + " | Save user OK!"

            self.showMessage(text) 

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Login LAPROSOLDA")
        MainWindow.resize(862, 767)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("color:rgb(200, 200, 200);\n"
"background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_error = QtWidgets.QFrame(self.top_bar)
        self.frame_error.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_error.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"border-radius:5px;")
        self.frame_error.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setStyleSheet("color:rgb(35, 35, 35);")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_3.addWidget(self.label_error)
        self.close_popup = QtWidgets.QPushButton(self.frame_error)
        self.close_popup.setMaximumSize(QtCore.QSize(20, 20))
        self.close_popup.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    background-image: url(:/closeImage/cil-x.png);\n"
"    background-position: center;\n"
"    background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(40, 40, 40);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 20, 20);\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.close_popup.setText("")
        self.close_popup.setObjectName("close_popup")
        self.horizontalLayout_3.addWidget(self.close_popup)
        self.horizontalLayout_2.addWidget(self.frame_error)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMaximumSize(QtCore.QSize(450, 550))
        self.login_area.setStyleSheet("")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.logo = QtWidgets.QFrame(self.login_area)
        self.logo.setGeometry(QtCore.QRect(180, 40, 90, 90))
        self.logo.setMinimumSize(QtCore.QSize(0, 0))
        self.logo.setStyleSheet("background-repeat: no-repeat;\n"
"background-image: url(:/logo-resized/logo.png);\n"
"background-position: center;")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.avatar = QtWidgets.QFrame(self.login_area)
        self.avatar.setGeometry(QtCore.QRect(165, 150, 120, 120))
        self.avatar.setStyleSheet("QFrame{\n"
"    background-image: url(:/avatar/avatar.png);\n"
"    background-position: center;\n"
"    border-radius: 60px;\n"
"    border: 10px solid rgb(36, 36, 100);\n"
"}")
        self.avatar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.avatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.avatar.setObjectName("avatar")
        self.lineEdit_user = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_user.setGeometry(QtCore.QRect(85, 288, 280, 50))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        font.setPointSize(10)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setStyleSheet(self.styleLineEditOk)
        self.lineEdit_user.setMaxLength(32)
        self.lineEdit_user.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_password = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_password.setGeometry(QtCore.QRect(85, 342, 280, 50))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet(self.styleLineEditOk)

        self.lineEdit_password.setMaxLength(16)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.checkBox_save_user = QtWidgets.QCheckBox(self.login_area)
        self.checkBox_save_user.setGeometry(QtCore.QRect(85, 395, 281, 24))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        font.setPointSize(10)
        self.checkBox_save_user.setFont(font)
        self.checkBox_save_user.setStyleSheet("QCheckBox::indicator{\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    border: 3px solid rgb(36, 36, 100);\n"
"    background-color: rgb(60,60,147);\n"
"}")
        self.checkBox_save_user.setObjectName("checkBox_save_user")
        self.pushButton_login = QtWidgets.QPushButton(self.login_area)
        self.pushButton_login.setGeometry(QtCore.QRect(85, 425, 280, 50))
        self.pushButton_login.setStyleSheet("QPushButton{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(52,60,148);\n"
"    border: 2px solid rgb(44,44,120);\n"
"    border-radius: 5px;\n"
"    color:rgb(35, 35, 35);\n"
"}")
        self.pushButton_login.setText("CONNECT TO LAPROSOLDA")
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        self.bottom.setFont(font)
        self.bottom.setStyleSheet("background-color:rgb(15,15,15);")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.bottom)
        font = QtGui.QFont()
        font.setFamily("System-ui")
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(75,75,75);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)

        #
        #FUNCTIONS
        #
        self.close_popup.clicked.connect(lambda: self.frame_error.hide())
        
        self.frame_error.hide()

        self.pushButton_login.clicked.connect(self.checkFields)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_error.setText(_translate("MainWindow", "Error"))
        self.lineEdit_user.setPlaceholderText(_translate("MainWindow", "USER"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.checkBox_save_user.setText(_translate("MainWindow", "SAVE USER"))
        self.label.setText(_translate("MainWindow", "Created by: Luis Felipe Costa"))
import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

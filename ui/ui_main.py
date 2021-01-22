# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/duan/git/12306/12306-V1.0.3/ui_login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)


        image = QtGui.QImage("./images/loginbackground.jpeg")
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(image))

        Form.setPalette(palette)
        self.LoginBtn = QtWidgets.QPushButton(Form)
        self.LoginBtn.setGeometry(QtCore.QRect(130, 160, 89, 25))
        self.LoginBtn.setObjectName("LoginBtn")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(75, 70, 210, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.usernameLabel = QtWidgets.QLabel(self.widget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.horizontalLayout.addWidget(self.usernameLabel)
        self.userName = QtWidgets.QLineEdit(self.widget)
        self.userName.setObjectName("userName")
        self.userName.setPlaceholderText("请输入用户名")
        self.userName.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.userName)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(90, 100, 195, 27))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.passwdLabel = QtWidgets.QLabel(self.widget1)
        self.passwdLabel.setObjectName("passwdLabel")
        self.horizontalLayout_2.addWidget(self.passwdLabel)
        self.passWd = QtWidgets.QLineEdit(self.widget1)
        self.passWd.setObjectName("passWd")
        self.horizontalLayout_2.addWidget(self.passWd)

        self.passWd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passWd.setClearButtonEnabled(True)
        self.passWd.setPlaceholderText("请输入密码")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.LoginBtn.setText(_translate("Form", "登录"))
        self.usernameLabel.setText(_translate("Form", "用户名："))
        #self.userName.setText(_translate("Form","请输入用户名"))
        self.passwdLabel.setText(_translate("Form", "密码："))
        #self.passWd.setText(_translate("Form", "请输入密码"))

if __name__ == '__main__':
    import sys
    ui = Ui_Form()
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/duan/git/12306/12306-V1.0.3/ui_verify.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verifyLabel = QtWidgets.QLabel(Form)
        self.verifyLabel.setGeometry(QtCore.QRect(20, 30, 351, 171))
        self.verifyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.verifyLabel.setObjectName("verifyLabel")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(46, 240, 301, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.okBtn = QtWidgets.QPushButton(self.widget)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout.addWidget(self.okBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "验证码"))
        self.verifyLabel.setText(_translate("Form", "验证码"))
        self.label.setText(_translate("Form", "请输入位置(0~7):"))
        self.okBtn.setText(_translate("Form", "确定"))


if __name__ == '__main__':
    import sys
    ui = Ui_Form()
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
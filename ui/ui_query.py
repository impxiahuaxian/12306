# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(434, 327)

        image = QtGui.QImage("./images/mainbackground.jpeg")
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(image))

        Form.setPalette(palette)

        self.qureyBtn = QtWidgets.QPushButton(Form)
        self.qureyBtn.setGeometry(QtCore.QRect(130, 220, 97, 32))
        self.qureyBtn.setObjectName("qureyBtn")

        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 330, 34))
        self.layoutWidget.setObjectName("layoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.startCityLine = QtWidgets.QLineEdit(self.layoutWidget)
        self.startCityLine.setObjectName("startCityLine")
        self.horizontalLayout.addWidget(self.startCityLine)

        self.symbol = QtWidgets.QLabel(self.layoutWidget)
        self.symbol.setAlignment(QtCore.Qt.AlignCenter)
        self.symbol.setObjectName("symbol")
        self.horizontalLayout.addWidget(self.symbol)

        self.endCityLine = QtWidgets.QLineEdit(self.layoutWidget)
        self.endCityLine.setObjectName("endCityLine")
        self.horizontalLayout.addWidget(self.endCityLine)

        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 100, 330, 34))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.selectDateLbl = QtWidgets.QLabel(self.layoutWidget1)
        self.selectDateLbl.setObjectName("selectDataLbl")
        self.horizontalLayout_2.addWidget(self.selectDateLbl)

        self.dataTBtn = QtWidgets.QToolButton(self.layoutWidget1)
        self.dataTBtn.setObjectName("dataTBtn")
        self.horizontalLayout_2.addWidget(self.dataTBtn)

        self.passengersLbl = QtWidgets.QLabel(self.layoutWidget1)
        self.passengersLbl.setObjectName("passengers")
        self.horizontalLayout_2.addWidget(self.passengersLbl)

        self.passengersLine = QtWidgets.QLineEdit(self.layoutWidget1)
        self.passengersLine.setObjectName("passengersLine")
        self.horizontalLayout_2.addWidget(self.passengersLine)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 150, 330, 34))
        self.layoutWidget2.setObjectName("layoutWidget2")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.phoneNumLbl = QtWidgets.QLabel(self.layoutWidget2)
        self.phoneNumLbl.setObjectName("phoneNumLbl")
        self.horizontalLayout_3.addWidget(self.phoneNumLbl)

        self.phoneNumLine = QtWidgets.QLineEdit(self.layoutWidget2)
        self.phoneNumLine.setObjectName("phoneNumLine")
        self.horizontalLayout_3.addWidget(self.phoneNumLine)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "查询"))
        self.qureyBtn.setText(_translate("Form", "查询"))
        self.symbol.setText(_translate("Form", "开往"))
        self.selectDateLbl.setText(_translate("Form", "选择日期"))
        self.dataTBtn.setText(_translate("Form", "1月1日"))
        self.passengersLbl.setText(_translate("Form", "乘车人"))
        self.phoneNumLbl.setText(_translate("Form", "乘车人号码"))
if __name__ == '__main__':
    import sys
    ui = Ui_Form()
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
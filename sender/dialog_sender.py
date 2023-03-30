# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog_sender.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 180)
        Dialog.setMinimumSize(QtCore.QSize(360, 180))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        Dialog.setFont(font)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_1 = QtWidgets.QPushButton(self.groupBox)
        self.button_1.setObjectName("button_1")
        self.verticalLayout.addWidget(self.button_1)
        self.button_2 = QtWidgets.QPushButton(self.groupBox)
        self.button_2.setObjectName("button_2")
        self.verticalLayout.addWidget(self.button_2)
        self.button_3 = QtWidgets.QPushButton(self.groupBox)
        self.button_3.setObjectName("button_3")
        self.verticalLayout.addWidget(self.button_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "button group"))
        self.button_1.setText(_translate("Dialog", "Button1"))
        self.button_2.setText(_translate("Dialog", "Button2"))
        self.button_3.setText(_translate("Dialog", "Button3"))
        self.label.setText(_translate("Dialog", "PUSH BUTTON"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


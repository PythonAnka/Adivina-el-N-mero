from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogDos(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 240)
        Dialog.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 66, 280, 41))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 200, 89, 25))
        self.pushButton.setStyleSheet("background-color: rgb(224, 27, 36);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(18, 190, 131, 25))
        self.pushButton_2.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.pushButton_2.setObjectName("pushButton_2")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Acierto"))
        self.label.setText(_translate("Dialog", "¡Acertaste!"))
        self.pushButton.setText(_translate("Dialog", "Salir"))
        self.pushButton_2.setText(_translate("Dialog", "Volver a jugar"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DialogDos()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
'''


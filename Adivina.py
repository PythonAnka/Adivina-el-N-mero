
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 240)
        Dialog.setStyleSheet("background-color: rgb(143, 240, 164);")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(9)
        font.setItalic(True)

        
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(80, 100, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 10, 67, 17))
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 200, 89, 25))
        self.pushButton.setStyleSheet("background-color: rgb(224, 27, 36);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(18, 190, 90, 25))
        self.pushButton_2.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Adivina"))
        self.label.setText(_translate("Dialog", "Adivina el numero secreto entre 1 y 500"))
        self.pushButton.setText(_translate("Dialog", "Acertar"))
        self.pushButton_2.setText(_translate("Dialog", "Volver"))
        
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
'''

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 406)
        MainWindow.setStyleSheet("background-color: rgb(87, 227, 137);\n""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(0, -10, 641, 441))
        self.label4.setText("")
        self.label4.setPixmap(QtGui.QPixmap("FondoPrincipal.jpg"))
        self.label4.setObjectName("label4")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 581, 61))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(14)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
    
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 260, 131, 51))
        self.pushButton.setStyleSheet("background-color: rgb(237, 51, 59);")
        self.pushButton.setObjectName("pushButton")
        #imagen a los botones
        self.pushButton.setStyleSheet("background-image : url(Magia);")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 150, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(153, 193, 241);")
        #cambiar por asteriscos lo introducido por teclado

        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 330, 61, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("anka.ico"))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
    
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Principal"))
        self.label.setText(_translate("MainWindow", "Introduce un número secreto entre 1 y 500"))
        self.pushButton.setText(_translate("MainWindow", "Jugar"))
     
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaPrincipalEngloba = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(VentanaPrincipalEngloba)
    VentanaPrincipalEngloba.show()
    sys.exit(app.exec_())



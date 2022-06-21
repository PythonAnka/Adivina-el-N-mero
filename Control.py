from cProfile import label
from PyQt5 import QtCore, QtGui, QtWidgets

from Principal import Ui_MainWindow
from Adivina import Ui_Dialog
from Acierto import Ui_DialogDos

from playsound import playsound


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        

        self.dialgoAdivina = QtWidgets.QDialog()
        self.uiDialog = Ui_Dialog()
        self.uiDialog.setupUi(self.dialgoAdivina)

        self.dialogoAcierta = QtWidgets.QDialog()
        self.uiDialogDos = Ui_DialogDos()
        self.uiDialogDos.setupUi(self.dialogoAcierta)

        self.cont = 0


        def mostrarTexto():
            
            try:
                valor = int(self.textEdit.toPlainText())
                if valor >= 1 and  valor <= 500:
                    #Manipulación de valor
                    print(valor)
                    
                    self.dialgoAdivina.show()
                    mainWindow.close()

                else:
                    self.label.setText("¡¡¡¡¡¡¡¡¡¡¡¡ Entre 1 y 500 cojoncit@ !!!!!!!!!!!")
            except:
                self.label.setText("¡No vale poner texto o dejarlo sin nada!")

        self.pushButton.clicked.connect(mostrarTexto)
        

        
        def compValores():
            
            try:
                valor = int(self.textEdit.toPlainText())
                segunValor = int(self.uiDialog.textEdit.toPlainText())
                
                
                if segunValor >= 1 and segunValor <= 500:
                #Manipulación del segundo numero
                    print(segunValor)
                    print(valor)
                    self.cont += 1

                    if segunValor > valor:
                            print("El número secreto es menor")
                            self.uiDialog.label.setText("El número secreto es menor")
                            
                    elif segunValor < valor:
                            print("El número secreto es mayor")
                            self.uiDialog.label.setText("El número secreto es mayor")
                    else:
                        
                        valor = int(self.textEdit.toPlainText())
                        if self.cont == 1:
                            self.uiDialogDos.label.setText("Has acertado a la primera, vaya suerte")
                            print("has acertado, en %d veces "% self.cont )
                            self.dialogoAcierta.show()
                            self.dialgoAdivina.close()
                            playsound("AplausosCortos.mp3")
                        else:
                            self.uiDialogDos.label.setText("Has acertado, en %d veces"% self.cont)
                            self.dialogoAcierta.show()
                            self.dialgoAdivina.close()
                else:
                    self.uiDialog.label.setText("¡¡¡¡¡¡¡¡¡¡¡¡ Entre 1 y 500 cojoncit@ !!!!!!!!!!!")
            except:
                self.uiDialog.label.setText("¡No vale poner texto o dejarlo sin nada!")

        
        self.uiDialog.pushButton.clicked.connect(compValores)
        
        def cerrarAbrirVentana():
            self.dialgoAdivina.close()
            self.show()
            
        self.uiDialog.pushButton_2.clicked.connect(cerrarAbrirVentana)

        def  cerrarJuego():
            self.dialogoAcierta.close()
        def cerrarJuegoAbreNuevo():
            self.dialogoAcierta.close()
            self.show()
            
        self.uiDialogDos.pushButton.clicked.connect(cerrarJuego)
        self.uiDialogDos.pushButton_2.clicked.connect(cerrarJuegoAbreNuevo)

          
        

    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())





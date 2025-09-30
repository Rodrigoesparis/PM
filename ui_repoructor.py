import sys #Imports que hacer
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt

#Se crea la clase reproductor
class Reproductor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Título de la ventana
        self.setWindowTitle("Reproductor de Música Básico")

        #Aqui se crea el menu archivo y su submenu Salir
        menuArchivo = self.menuBar().addMenu("Archivo")
        accionSalir = menuArchivo.addAction("Salir")
        accionSalir.triggered.connect(self.close)  #Se vincula el boton salir para que se cierre la ventana

        #Se crea la barra de herramientas
        toolbar = self.addToolBar("Principal")
        botonPlay = toolbar.addAction("▶")  #Se crea el boton play
        botonPlay.triggered.connect(self.reproducir) #Se crea la accion para iniciar

        #Mensaje que sale de forma inicial
        self.statusBar().showMessage("Listo")

        #Texto central de reproductor de música
        self.labelCentral = QLabel("Reproductor de música")
        self.labelCentral.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.labelCentral)

    #Funcion al pulsar el boton cambia el mensaje de listo
    def reproducir(self):
        self.statusBar().showMessage("Reproduciendo música", 2000)  # 2 segundos

#Main para que inicie la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Reproductor()
    ventana.show()
    app.exec()

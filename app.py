import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_repoructor import Ui_MainWindow

class Ventana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.StopBtn.clicked.connect(self.on_stop)
        self.PuaseBtn.clicked.connect(self.on_pause)
        self.PlayBtn.clicked.connect(self.on_play)

        self.lblTitle.setObjectName("lbl_1")

    def on_play(self):
        self.lblTitle.setText("Play")
        self.statusBar().showMessage("Has pulsado play", 2000)

    def on_pause(self):
        self.lblTitle.setText("Pause")
        self.statusBar().showMessage("Has pulsado pausa", 2000)

    def on_stop(self):
        self.lblTitle.setText("Stop")
        self.statusBar().showMessage("Has pulsado stop", 2000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Ventana()
    w.show()
    sys.exit(app.exec())
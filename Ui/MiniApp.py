import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class MiniApp(QWidget):
    def __init__(self):
        super().__init__()


        self.label = QLabel("Buenas buenas", self)


        self.button = QPushButton("No me toques", self)
        self.button.clicked.connect(self.cambiar_texto)


        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)


        self.setWindowTitle("Mi app")
        self.resize(300, 150)


        print("Aplicacion abierta")

    def cambiar_texto(self):
        self.label.setText("Que no me toques")
        print("Que pesao")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiniApp()
    ventana.show()
    sys.exit(app.exec())

import calculator

from PySide6.QtWidgets import QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Classic Calculator")
        self.resize(500, 300)

        label = QLabel("Hello!")
        self.setCentralWidget(label)

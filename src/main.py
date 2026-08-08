import sys

from gui import MainWindow

from PySide6.QtWidgets import QApplication


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())

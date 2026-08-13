import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication
from gui import MainWindow


app = QApplication(sys.argv)

window = MainWindow()

style_path = Path(__file__).parent / "style.qss"

with open(style_path, "r", encoding="utf-8") as f:
    app.setStyleSheet(f.read())

window.show()

sys.exit(app.exec())

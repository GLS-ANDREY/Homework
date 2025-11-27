from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from owner_window import Ui_MainWindow


def add():
    widget.append(QWidget())
    widget[-1].show()

widget = []
creator = QApplication()
window = QMainWindow()
window.show()
mainwindow = Ui_MainWindow()
mainwindow.setupUi(window)
mainwindow.pushButton.clicked.connect(add)

creator.exec()

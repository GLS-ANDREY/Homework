from PySide6.QtWidgets import QMainWindow, QApplication, QHeaderView
from main_window import Ui_MainWindow
import main2
from PySide6.QtGui import QStandardItemModel

creator = QApplication()
model = QStandardItemModel(0, 3)
model.setHorizontalHeaderLabels(["Адрес", "Цена", "Тип недвижимости"])


def maker(address, price, type):
    model.appendRow([])
    row_count = model.rowCount()
    model.setData(model.index(row_count - 1, 0), address)
    model.setData(model.index(row_count - 1, 1), price)
    model.setData(model.index(row_count - 1, 2), type)


window = QMainWindow()
window.show()

mainwindow = Ui_MainWindow()
mainwindow.setupUi(window)

mainwindow.tableView.setModel(model)
title = mainwindow.tableView.horizontalHeader()
maker("Улица Пушкина дом Колотушкина", "G64", "Жило-коммерческо")
maker("Там где черт ногу сломит", "G64eG64", "Коммерческо-жило")

mainwindow.pushButton.clicked.connect(main2.add)
for a in range(0, 3):
    title.setSectionResizeMode(a, QHeaderView.ResizeMode.ResizeToContents)
creator.exec()

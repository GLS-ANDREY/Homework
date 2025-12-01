from PySide6.QtWidgets import QWidget
from form_window import Ui_Form

def cancel():
    widget_variable:QWidget = widget[-1]
    widget_variable.close()

def save():
    print(1)


def add():
    widget.append(QWidget())
    formwindow.setupUi(widget[-1])
    widget[-1].show()
    formwindow.cancelButton.clicked.connect(cancel)
    formwindow.saveButton.clicked.connect(save)

formwindow = Ui_Form()
widget = []
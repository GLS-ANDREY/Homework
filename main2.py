from PySide6.QtWidgets import QWidget, QButtonGroup
from form_window import Ui_Form

def cancel():
    widget_variable:QWidget = widget[-1]
    widget_variable.close()
#анекдот спор, звонят мне
def add(save):
    def prosloika2():
        save(formwindow.name.text(),formwindow.price.text(),str(group.checkedId()))
    widget.append(QWidget())
    formwindow.setupUi(widget[-1])
    group = QButtonGroup()
    group.addButton(formwindow.residentButton,1)
    group.addButton(formwindow.commercialButton,2)
    widget[-1].show()

    formwindow.cancelButton.clicked.connect(cancel)
    formwindow.saveButton.clicked.connect(prosloika2)





formwindow = Ui_Form()
widget = []
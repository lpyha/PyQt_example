import sys

from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QDialog, QApplication
from validatorDialog import Ui_Dialog

class validator(QDialog, Ui_Dialog):
    def __init__(self) -> None:
        super(validator, self).__init__()
        self.setupUi(self)
        
        self.lineEdit.setValidator(QIntValidator())
        self.lineEdit_2.setValidator(QDoubleValidator())
        
def window():
    app = QApplication(sys.argv)
    win = validator()
    win.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    window()
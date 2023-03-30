import sys

from PyQt5 import QtWidgets
from dialog_sender import Ui_Dialog

class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self) -> None:
        super(Dialog, self).__init__()
        self.setupUi(self)
        
        self.button_1.index = 1
        self.button_2.index = 2
        self.button_3.index = 3
        
        self.button_1.released.connect(self.released_buttons)
        self.button_2.released.connect(self.released_buttons)
        self.button_3.released.connect(self.released_buttons)
        
    def released_buttons(self):
        button = self.sender()
        self.label.setText(f"index{button.index}")

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    window()
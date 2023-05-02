from PyQt5 import QtCore, QtGui, QtWidgets
from dialog import Ui_Dialog
import sys

class Dialog(QtWidgets.QDialog, Ui_Dialog):
    
    def __init__(self):
        super(Dialog, self).__init__()
        self.setupUi(self)
        
        self.pushButton.released.connect(self.reset_value)

    def reset_value(self):
        self.label.setText("clicked")
        self.horizontalSlider.setValue(0)

def show_window():
    app = QtWidgets.QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    show_window()
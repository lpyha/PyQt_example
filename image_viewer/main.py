from PyQt5 import QtCore, QtGui, QtWidgets
from dialog import Ui_Dialog
import sys

class ImageDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(ImageDialog, self).__init__()
        self.setupUi(self)
        self.width = 800
        self.height = 600
        self.pushButton.released.connect(self.open_image)
        
    def open_image(self):
        path = QtWidgets.QFileDialog.getOpenFileName()[0]
        pixmap = QtGui.QPixmap(path)
        pixmap = pixmap.scaled(self.width,
                               self.height,
                               QtCore.Qt.KeepAspectRatio,
                               QtCore.Qt.FastTransformation)
        self.label.setPixmap(pixmap)
        
        
def show_window():
    app = QtWidgets.QApplication(sys.argv)
    win = ImageDialog()
    win.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    show_window()
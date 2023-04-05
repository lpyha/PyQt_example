from PyQt5.QtWidgets import QApplication, QDialog

from buttondialog import Ui_Dialog

button_on_css = '''
QPushButton{
    background-color: red
}
'''

button_off_css = '''
QPushButton{
    background-color: blue
}
'''

class BuutonDialog(QDialog, Ui_Dialog):
    def __init__(self) -> None:
        super(BuutonDialog, self).__init__()
        self.setupUi(self)
        self.set_css(2)
        
        self.pushButton.clicked.connect(lambda: self.set_css(1))
        self.pushButton_2.clicked.connect(lambda: self.set_css(2))
        self.pushButton_3.clicked.connect(lambda: self.set_css(3))
        self.pushButton_4.clicked.connect(lambda: self.set_css(4))
        
        
    def set_css(self, index):
        self.pushButton.setStyleSheet(button_off_css)
        self.pushButton_2.setStyleSheet(button_off_css)
        self.pushButton_3.setStyleSheet(button_off_css)
        self.pushButton_4.setStyleSheet(button_off_css)
        match index:
            case 1:
                self.pushButton.setStyleSheet(button_on_css)
            case 2:
                self.pushButton_2.setStyleSheet(button_on_css)
            case 3:
                self.pushButton_3.setStyleSheet(button_on_css)
            case 4:
                self.pushButton_4.setStyleSheet(button_on_css)


def show_window():
    import sys
    app = QApplication(sys.argv)
    win = BuutonDialog()
    win.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    show_window()
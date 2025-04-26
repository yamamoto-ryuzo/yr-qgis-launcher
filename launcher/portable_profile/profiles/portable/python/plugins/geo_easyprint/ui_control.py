from PyQt4.QtCore import *
from PyQt4.QtGui import *

# from test import Ui_Dialog
from ui_test import Ui_Dialog

class ui_Control(QDialog, Ui_Dialog):
    def __init__(self, parent, fl):
        QDialog.__init__(self, parent, fl)
        self.setupUi(self)

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_test3.ui'
#
# Created: Tue Nov 26 09:42:42 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("AddLabel"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(400, 350)

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(220, 310, 170, 30))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        # self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 380, 300))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))

        # self.label_3 = QtGui.QLabel(self.tab)
        # self.label_3.setGeometry(QtCore.QRect(120, 190, 50, 12))
        # self.label_3.setObjectName(_fromUtf8("label_3"))

        self.checkBox_2 = QtGui.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 170, 75, 16))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))

        self.pushButton_4 = QtGui.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 190, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.checkBox = QtGui.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(10, 110, 100, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 130, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 270, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(110, 130, 60, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        # self.horizontalSlider = QtGui.QSlider(self.tab)
        # self.horizontalSlider.setGeometry(QtCore.QRect(190, 190, 180, 20))
        # self.horizontalSlider.setSliderPosition(99)
        # self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        # self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))

        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 50, 12))
        self.label.setObjectName(_fromUtf8("label"))

        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.tab)
        self.doubleSpinBox.setGeometry(QtCore.QRect(180, 130, 95, 22))
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMinimum(0.1)
        self.doubleSpinBox.setMaximum(50.0)
        self.doubleSpinBox.setProperty("value", 0.3)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))

        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 270, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.pushButton_7 = QtGui.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(290, 247, 75, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))

        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 50, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.lineEdit_2 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 40, 270, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.pushButton_5 = QtGui.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 40, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 270, 200))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 140, 140))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.pushButton_6 = QtGui.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 247, 75, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.doubleSpinBox.setEnabled(False)

        # QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "ラベル追加", None))
        # self.label_3.setText(_translate("Dialog", "透過率", None))
        self.checkBox_2.setText(_translate("Dialog", "塗りつぶし", None))
        self.pushButton_4.setText(_translate("Dialog", "塗りつぶし色", None))
        self.checkBox.setText(_translate("Dialog", "フレームを表示", None))
        self.pushButton_3.setText(_translate("Dialog", "フレーム色", None))
        self.pushButton.setText(_translate("Dialog", "フォント", None))
        self.label_2.setText(_translate("Dialog", "フレーム太さ", None))
        self.label.setText(_translate("Dialog", "テキスト", None))
        self.pushButton_2.setText(_translate("Dialog", "フォント色", None))
        self.label_4.setText(_translate("Dialog", "AaBbYyZz", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "ラベル", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "ピクチャー", None))
        self.label_5.setText(_translate("Dialog", "ファイル", None))
        self.pushButton_5.setText(_translate("Dialog", "参照", None))
        self.groupBox.setTitle(_translate("Dialog", "プレビュー", None))
        self.pushButton_6.setText(_translate("Dialog", "適用", None))
        self.pushButton_7.setText(_translate("Dialog", "適用", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

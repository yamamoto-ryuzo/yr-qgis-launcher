#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_test2.ui'
#
# Created: Tue Nov 12 11:50:34 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import qgis.utils

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text,
                                            disambig,
                                            _encoding)


except AttributeError:

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
# class Ui_Dialog(object, EasyPrint):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8('EditTool'))
        Dialog.setFixedSize(400, 395)

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 360, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8('buttonBox'))

        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 381, 351))
        self.tabWidget.setObjectName(_fromUtf8('tabWidget'))
        self.label_tab = QtGui.QWidget()
        self.label_tab.setObjectName(_fromUtf8('tab'))

        self.label = QtGui.QLabel(self.label_tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 50, 12))
        self.label.setObjectName(_fromUtf8('label'))

        self.lineEdit = QtGui.QLineEdit(self.label_tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 351, 20))
        self.lineEdit.setObjectName(_fromUtf8('lineEdit'))

        self.label_font_button = QtGui.QPushButton(self.label_tab)
        self.label_font_button.setGeometry(QtCore.QRect(10, 60, 80, 23))
        self.label_font_button.setObjectName(_fromUtf8('label_font_button'))

        self.label_font_color_button = QtGui.QPushButton(self.label_tab)
        self.label_font_color_button.setGeometry(QtCore.QRect(100, 60, 80, 23))
        self.label_font_color_button.setObjectName(_fromUtf8('label_font_color_button'))

        self.checkBox = QtGui.QCheckBox(self.label_tab)
        self.checkBox.setGeometry(QtCore.QRect(10, 100, 150, 16))
        self.checkBox.setObjectName(_fromUtf8('checkBox'))

        self.label_frame_color_button = QtGui.QPushButton(self.label_tab)
        self.label_frame_color_button.setGeometry(QtCore.QRect(10, 120, 80, 23))
        self.label_frame_color_button.setObjectName(_fromUtf8('label_frame_color_button'))

        self.checkBox_2 = QtGui.QCheckBox(self.label_tab)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 160, 150, 16))
        self.checkBox_2.setObjectName(_fromUtf8('checkBox_2'))

        self.label_background_color_button = QtGui.QPushButton(self.label_tab)
        self.label_background_color_button.setGeometry(QtCore.QRect(10, 180, 80, 23))
        self.label_background_color_button.setObjectName(_fromUtf8('label_background_color_button'))


        self.label_2 = QtGui.QLabel(self.label_tab)
        self.label_2.setGeometry(QtCore.QRect(105, 120, 80, 16))
        self.label_2.setObjectName(_fromUtf8('label_2'))

        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.label_tab)
        self.doubleSpinBox.setGeometry(QtCore.QRect(180, 120, 50, 22))
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMinimum(0.1)
        self.doubleSpinBox.setMaximum(50.00)
        self.doubleSpinBox.setProperty('value', 0.3)
        self.doubleSpinBox.setObjectName(_fromUtf8('doubleSpinBox'))


        self.checkBox_3 = QtGui.QCheckBox(self.label_tab)
        self.checkBox_3.setGeometry(QtCore.QRect(240, 120, 131, 16))
        self.checkBox_3.setObjectName(_fromUtf8('checkBox_3'))

        self.line = QtGui.QFrame(self.label_tab)
        self.line.setGeometry(QtCore.QRect(10, 85, 351, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8('line'))

        self.line_2 = QtGui.QFrame(self.label_tab)
        self.line_2.setGeometry(QtCore.QRect(10, 145, 351, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8('line_2'))

        self.pushButton_7 = QtGui.QPushButton(self.label_tab)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 280, 80, 23))
        self.pushButton_7.setObjectName(_fromUtf8('pushButton_7'))

#        self.label_3 = QtGui.QLabel(self.label_tab)
#        self.label_3.setGeometry(QtCore.QRect(110, 180, 50, 12))
#        self.label_3.setObjectName(_fromUtf8("label_3"))

#        self.horizontalSlider = QtGui.QSlider(self.label_tab)
#        self.horizontalSlider.setGeometry(QtCore.QRect(180, 180, 181, 22))
#        self.horizontalSlider.setSliderPosition(99)
#        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
#        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))

#        self.groupBox_3 = QtGui.QGroupBox(self.label_tab)
#        self.groupBox_3.setGeometry(QtCore.QRect(10, 220, 171, 41))
#        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))

#        self.radioButton = QtGui.QRadioButton(self.groupBox_3)
#        self.radioButton.setGeometry(QtCore.QRect(10, 20, 41, 16))
#        self.radioButton.setChecked(True)
#        self.radioButton.setObjectName(_fromUtf8("radioButton"))

#        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_3)
#        self.radioButton_2.setGeometry(QtCore.QRect(70, 20, 51, 16))
#        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))

#        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_3)
#        self.radioButton_3.setGeometry(QtCore.QRect(130, 20, 41, 16))
#        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))

#        self.groupBox_2 = QtGui.QGroupBox(self.label_tab)
#        self.groupBox_2.setGeometry(QtCore.QRect(190, 220, 171, 41))
#        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

#        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_2)
#        self.radioButton_4.setGeometry(QtCore.QRect(10, 20, 41, 16))
#        self.radioButton_4.setChecked(True)
#        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))

#        self.radioButton_5 = QtGui.QRadioButton(self.groupBox_2)
#        self.radioButton_5.setGeometry(QtCore.QRect(70, 20, 51, 16))
#        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))

#        self.radioButton_6 = QtGui.QRadioButton(self.groupBox_2)
#        self.radioButton_6.setGeometry(QtCore.QRect(130, 20, 41, 16))
#        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))

        self.tabWidget.addTab(self.label_tab, _fromUtf8(''))

        self.picture_tab = QtGui.QWidget()
        self.picture_tab.setObjectName(_fromUtf8('picture_tab'))

        self.pushButton_5 = QtGui.QPushButton(self.picture_tab)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 30, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8('pushButton_5'))

#        self.graphicsView = QtGui.QGraphicsView(self.picture_tab)
#        self.graphicsView.setGeometry(QtCore.QRect(10, 211, 256, 81))
#        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        self.label_4 = QtGui.QLabel(self.picture_tab)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 50, 12))
        self.label_4.setObjectName(_fromUtf8('label_4'))

        self.picture_file_line = QtGui.QLineEdit(self.picture_tab)
        self.picture_file_line.setGeometry(QtCore.QRect(10, 30, 270, 20))
        self.picture_file_line.setObjectName(_fromUtf8('picture_file_line'))

        self.groupBox = QtGui.QGroupBox(self.picture_tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 55, 355, 240))
        self.groupBox.setObjectName(_fromUtf8('groupBox'))

        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)

        # self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 140, 140))

        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 250, 225))
        self.gridLayoutWidget.setObjectName(_fromUtf8('gridLayoutWidget'))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8('gridLayout'))

        # QListWidget

        self.listWidget = QtGui.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(3, 15, 351, 220))
        self.listWidget.setObjectName(_fromUtf8('listWidget'))
        self.listWidget.setMinimumSize(QtCore.QSize(230, 200))
        self.listWidget.viewport().setProperty(
            'cursor', QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.listWidget.setMouseTracking(False)
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)

        # self.listWidget.setAutoFillBackground(False)

        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.listWidget.setIconSize(QtCore.QSize(50, 50))
        self.listWidget.setProperty('isWrapping', True)
        self.listWidget.setViewMode(QtGui.QListView.IconMode)
        self.listWidget.setSelectionMode(
            QtGui.QAbstractItemView.SingleSelection)
        self.listWidget.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectItems)

        # self.listWidget.setSelectionRectVisible(False)

        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setDragEnabled(False)

        self.lineEdit_3 = QtGui.QLineEdit(self.picture_tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 300, 270, 20))
        self.lineEdit_3.setObjectName(_fromUtf8('lineEdit_3'))

        self.pushButton_6 = QtGui.QPushButton(self.picture_tab)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 300, 75, 23))

        # self.pushButton_6.setGeometry(QtCore.QRect(290, 277, 75, 23))

        self.pushButton_6.setObjectName(_fromUtf8('pushButton_6'))

        self.label_5 = QtGui.QLabel(self.picture_tab)
        self.label_5.setGeometry(QtCore.QRect(10, 305, 30, 12))
        self.label_5.setObjectName(_fromUtf8('label_5'))

        self.phot_rotation_spinbox = QtGui.QDoubleSpinBox(self.picture_tab)
        self.phot_rotation_spinbox.setGeometry(QtCore.QRect(40, 300, 150, 22))
        self.phot_rotation_spinbox.setDecimals(2)
        self.phot_rotation_spinbox.setMinimum(0.00)
        self.phot_rotation_spinbox.setMaximum(360.0)
        self.phot_rotation_spinbox.setProperty('value', 0.00)
        self.phot_rotation_spinbox.setObjectName(_fromUtf8('phot_rotation_spinbox'))

        # self.phot_rotation_spinbox.setEnabled(False)

        # self.scrollArea = QtGui.QScrollArea(self.groupBox)
        # self.scrollArea.setGeometry(QtCore.QRect(5, 15, 260, 220))
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        # self.scrollAreaWidgetContents = QtGui.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 250, 200))
        # self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))

        # self.widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        # self.widget.setGeometry(QtCore.QRect(10, 10, 231, 191))
        # self.widget.setObjectName(_fromUtf8("widget"))

        # self.gridLayoutWidget_2 = QtGui.QWidget(self.widget)
        # self.gridLayoutWidget_2.setGeometry(QtCore.QRect(5, 5, 220, 180))
        # self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        # self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        # self.gridLayout_2.setMargin(0)
        # self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))

        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # self.graphicsView = QtGui.QGraphicsView(self.groupBox)
        # self.graphicsView.setGeometry(QtCore.QRect(10, 20, 251, 61))
        # self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        self.tabWidget.addTab(self.picture_tab, _fromUtf8(''))

        # 基本図形
        # タブ「基本図形」

        self.shape_tab = QtGui.QWidget()
        self.shape_tab.setObjectName(_fromUtf8('shape_tab'))

        # ラベル「図形」

        self.shape_label = QtGui.QLabel(self.shape_tab)
        self.shape_label.setGeometry(QtCore.QRect(10, 20, 50, 12))
        self.shape_label.setObjectName(_fromUtf8('shape_label'))

        # コンボ「図形」

        self.shape_type_combobox = QtGui.QComboBox(self.shape_tab)
        self.shape_type_combobox.setGeometry(QtCore.QRect(60, 20, 301, 22))
        self.shape_type_combobox.setObjectName(_fromUtf8('shape_type_combobox'))

        # ボタン「ｱｳﾄﾗｲﾝ色」

        self.shape_outline_color_button = QtGui.QPushButton(self.shape_tab)
        self.shape_outline_color_button.setGeometry(QtCore.QRect(60, 50, 101, 23))
        self.shape_outline_color_button.setObjectName(_fromUtf8('shape_outline_color_button'))

        # ラベル「ｱｳﾄﾗｲﾝ幅」

        self.shape_outline_width_label = QtGui.QLabel(self.shape_tab)
        self.shape_outline_width_label.setGeometry(QtCore.QRect(200, 50, 61, 16))
        self.shape_outline_width_label.setObjectName(_fromUtf8('shape_outline_width_label'))

        # スピン「ｱｳﾄﾗｲﾝ幅」

        self.shape_outline_width_spinbox = QtGui.QDoubleSpinBox(self.shape_tab)
        self.shape_outline_width_spinbox.setGeometry(QtCore.QRect(270, 50, 91, 22))
        self.shape_outline_width_spinbox.setDecimals(2)
        self.shape_outline_width_spinbox.setMinimum(0.00)
        self.shape_outline_width_spinbox.setMaximum(50.00)
        self.shape_outline_width_spinbox.setProperty('value', 1.00)
        self.shape_outline_width_spinbox.setObjectName(_fromUtf8('shape_outline_width_spinbox'))

        # チェック「透過塗りつぶし」

        self.shape_symbol_checkbox = QtGui.QCheckBox(self.shape_tab)
        self.shape_symbol_checkbox.setGeometry(QtCore.QRect(200, 105, 100, 16))
        self.shape_symbol_checkbox.setObjectName(_fromUtf8('shape_symbol_checkbox'))
        self.shape_symbol_checkbox.setVisible(False)

        # ボタン「図形塗りつぶし色」

        self.shape_fill_color_button = QtGui.QPushButton(self.shape_tab)
        self.shape_fill_color_button.setGeometry(QtCore.QRect(60, 80, 101, 23))
        self.shape_fill_color_button.setObjectName(_fromUtf8('shape_fill_color_button'))
        # self.shape_fill_color_button.setVisible(False)
        # self.shape_fill_color_button.setEnabled(False)

        # ボタン：既存設定画面

        self.shape_show_settings_button = QtGui.QPushButton(self.shape_tab)
        self.shape_show_settings_button.setGeometry(QtCore.QRect(60, 105, 40, 40))
        self.shape_show_settings_button.setObjectName(_fromUtf8('shape_show_settings_button'))

        self.shape_apply_button = QtGui.QPushButton(self.shape_tab)
        self.shape_apply_button.setGeometry(QtCore.QRect(270, 105, 69, 22))
        self.shape_apply_button.setObjectName(_fromUtf8('shape_apply_button'))

        self.shape_release_button = QtGui.QPushButton(self.shape_tab)
        self.shape_release_button.setGeometry(QtCore.QRect(197, 105, 69, 22))
        self.shape_release_button.setObjectName(_fromUtf8('shape_release_button'))
        # ラベル「ヘッドの幅」

        self.label_17 = QtGui.QLabel(self.shape_tab)
        self.label_17.setGeometry(QtCore.QRect(60, 145, 150, 16))
        self.label_17.setObjectName(_fromUtf8('label_17'))

        # ラベル「回転」

        self.shape_rotation_label = QtGui.QLabel(self.shape_tab)
        self.shape_rotation_label.setGeometry(QtCore.QRect(200, 80, 61, 16))
        self.shape_rotation_label.setObjectName(_fromUtf8('shape_rotation_label'))

        # スピン「回転」

        self.shape_rotation_spinbox = QtGui.QDoubleSpinBox(self.shape_tab)
        self.shape_rotation_spinbox.setGeometry(QtCore.QRect(270, 80, 91, 22))
        self.shape_rotation_spinbox.setDecimals(0)
        self.shape_rotation_spinbox.setMinimum(0)
        self.shape_rotation_spinbox.setMaximum(359)
        self.shape_rotation_spinbox.setProperty('value', 0)
        self.shape_rotation_spinbox.setObjectName(_fromUtf8('shape_rotation_spinbox'))

        # separator

        self.line = QtGui.QFrame(self.shape_tab)
        self.line.setGeometry(QtCore.QRect(10, 167, 351, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8('line'))
        self.line.setVisible(False)

        # チェック「フレーム表示」

        self.shape_frame_checkbox = QtGui.QCheckBox(self.shape_tab)
        self.shape_frame_checkbox.setGeometry(QtCore.QRect(10, 184, 101, 16))
        self.shape_frame_checkbox.setObjectName(_fromUtf8('shape_frame_checkbox'))
        self.shape_frame_checkbox.setVisible(False)

        # ボタン「フレーム色」

        self.shape_frame_color_button = QtGui.QPushButton(self.shape_tab)
        self.shape_frame_color_button.setGeometry(QtCore.QRect(60, 205, 101, 23))
        self.shape_frame_color_button.setObjectName(_fromUtf8('shape_frame_color_button'))
        self.shape_frame_color_button.setVisible(False)

        # ラベル「ﾌﾚｰﾑ幅」

        self.shape_frame_width_label = QtGui.QLabel(self.shape_tab)
        self.shape_frame_width_label.setGeometry(QtCore.QRect(200, 205, 61, 16))
        self.shape_frame_width_label.setObjectName(_fromUtf8('shape_frame_width_label'))
        self.shape_frame_width_label.setVisible(False)

        # スピン「ﾌﾚｰﾑ幅」

        self.shape_frame_width_spinbox = QtGui.QDoubleSpinBox(self.shape_tab)
        self.shape_frame_width_spinbox.setGeometry(QtCore.QRect(270, 205, 91, 22))
        self.shape_frame_width_spinbox.setDecimals(2)
        self.shape_frame_width_spinbox.setMinimum(0.00)
        self.shape_frame_width_spinbox.setMaximum(50.00)
        self.shape_frame_width_spinbox.setProperty('value', 0.00)
        self.shape_frame_width_spinbox.setObjectName(_fromUtf8('shape_frame_width_spinbox'))
        self.shape_frame_width_spinbox.setVisible(False)

        # ボタン「背景色」

        self.shape_background_color_button = QtGui.QPushButton(self.shape_tab)
        self.shape_background_color_button.setGeometry(QtCore.QRect(60, 235, 101, 23))
        self.shape_background_color_button.setObjectName(_fromUtf8('shape_background_color_button'))
        self.shape_background_color_button.setVisible(False)

        # ラベル「透過率」

        self.shape_alpha_label = QtGui.QLabel(self.shape_tab)
        self.shape_alpha_label.setGeometry(QtCore.QRect(60, 270, 50, 12))
        self.shape_alpha_label.setObjectName(_fromUtf8('shape_alpha_label'))
        self.shape_alpha_label.setVisible(False)

        # スライダ「透過率」

        self.shape_alpha_slider = QtGui.QSlider(self.shape_tab)
        self.shape_alpha_slider.setGeometry(
            QtCore.QRect(60, 285, 301, 22))
        self.shape_alpha_slider.setMinimum(0)
        self.shape_alpha_slider.setMaximum(255)
        self.shape_alpha_slider.setSliderPosition(255)
        self.shape_alpha_slider.setOrientation(QtCore.Qt.Horizontal)
        self.shape_alpha_slider.setObjectName(
            _fromUtf8('shape_alpha_slider'))
        self.shape_alpha_slider.setVisible(False)

        self.tabWidget.addTab(self.shape_tab, _fromUtf8(''))

        # 矢印
        # タブ「矢印」

        self.arrow_tab = QtGui.QWidget()
        self.arrow_tab.setObjectName(_fromUtf8('arrow_tab'))
        self.tabWidget.addTab(self.arrow_tab, _fromUtf8(''))

        # ラベル「矢印」

        self.arrow_label = QtGui.QLabel(self.arrow_tab)
        self.arrow_label.setGeometry(QtCore.QRect(10, 20, 50, 12))
        self.arrow_label.setObjectName(_fromUtf8('arrow_label'))

        # ボタン「矢印の色」

        self.arrow_color_button = QtGui.QPushButton(self.arrow_tab)
        self.arrow_color_button.setGeometry(QtCore.QRect(60, 20, 101, 23))
        self.arrow_color_button.setObjectName(_fromUtf8('arrow_color_button'))
        self.arrow_color_button.setVisible(False)
        self.arrow_color_button.setEnabled(False)

        # ラベル「線幅」

        self.arrow_line_width_label = QtGui.QLabel(self.arrow_tab)
        self.arrow_line_width_label.setGeometry(QtCore.QRect(200, 20, 61, 16))
        self.arrow_line_width_label.setObjectName(_fromUtf8('arrow_line_width_label'))
        self.arrow_line_width_label.setVisible(False)
        self.arrow_line_width_label.setEnabled(False)

        # スピン「線幅」

        self.arrow_line_width_spinbox = QtGui.QDoubleSpinBox(self.arrow_tab)
        self.arrow_line_width_spinbox.setGeometry(QtCore.QRect(270, 20, 91, 22))
        self.arrow_line_width_spinbox.setDecimals(2)
        self.arrow_line_width_spinbox.setMinimum(0.00)
        self.arrow_line_width_spinbox.setMaximum(50.00)
        self.arrow_line_width_spinbox.setProperty('value', 1.00)
        self.arrow_line_width_spinbox.setObjectName(_fromUtf8('arrow_line_width_spinbox'))
        self.arrow_line_width_spinbox.setVisible(False)
        self.arrow_line_width_spinbox.setEnabled(False)

        # ラベル「ヘッドの幅」

        self.arrow_head_width = QtGui.QLabel(self.arrow_tab)
        self.arrow_head_width.setGeometry(QtCore.QRect(200, 70, 61, 16))
        self.arrow_head_width.setObjectName(_fromUtf8('arrow_head_width'))
        self.arrow_head_width.setVisible(False)
        self.arrow_head_width.setEnabled(False)

        # スピン「ヘッドの幅」

        self.arrow_head_width_spinbox = QtGui.QDoubleSpinBox(self.arrow_tab)
        self.arrow_head_width_spinbox.setGeometry(QtCore.QRect(270, 70, 91, 22))
        self.arrow_head_width_spinbox.setDecimals(2)
        self.arrow_head_width_spinbox.setMinimum(0.00)
        self.arrow_head_width_spinbox.setMaximum(50.00)
        self.arrow_head_width_spinbox.setProperty('value', 4.00)
        self.arrow_head_width_spinbox.setObjectName(_fromUtf8('arrow_head_width_spinbox'))
        self.arrow_head_width_spinbox.setVisible(False)
        self.arrow_head_width_spinbox.setEnabled(False)

        # ボタン：既存設定画面

        self.arrow_settings_button = QtGui.QPushButton(self.arrow_tab)
        self.arrow_settings_button.setGeometry(QtCore.QRect(60, 20, 40, 40))
        self.arrow_settings_button.setObjectName(_fromUtf8('arrow_settings_button'))

        # ラベル「矢印の設定画面」

        self.arrow_settings_label = QtGui.QLabel(self.arrow_tab)
        self.arrow_settings_label.setGeometry(QtCore.QRect(60, 65, 150, 16))
        self.arrow_settings_label.setObjectName(_fromUtf8('arrow_settings_label'))

        # separator

        self.line = QtGui.QFrame(self.arrow_tab)
        self.line.setGeometry(QtCore.QRect(10, 167, 351, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8('line'))
        self.line.setVisible(False)

        # チェック「フレーム表示」

        self.arrow_frame_checkbox = QtGui.QCheckBox(self.arrow_tab)
        self.arrow_frame_checkbox.setGeometry(QtCore.QRect(10, 184, 101, 16))
        self.arrow_frame_checkbox.setObjectName(_fromUtf8('arrow_frame_checkbox'))
        self.arrow_frame_checkbox.setVisible(False)

        # ボタン「フレーム色」

        self.arrow_frame_color_button = QtGui.QPushButton(self.arrow_tab)
        self.arrow_frame_color_button.setGeometry(QtCore.QRect(60, 205, 101, 23))
        self.arrow_frame_color_button.setObjectName(_fromUtf8('arrow_frame_color_button'))
        self.arrow_frame_color_button.setVisible(False)

        # ラベル「フレーム幅」
        self.arrow_frame_width_label = QtGui.QLabel(self.arrow_tab)
        self.arrow_frame_width_label.setGeometry(QtCore.QRect(200, 205, 61, 16))
        self.arrow_frame_width_label.setObjectName(_fromUtf8('arrow_frame_width_label'))
        self.arrow_frame_width_label.setVisible(False)

        # スピン「フレーム幅」

        self.arrow_frame_width_spinbox = QtGui.QDoubleSpinBox(self.arrow_tab)
        self.arrow_frame_width_spinbox.setGeometry(QtCore.QRect(270, 205, 91, 22))
        self.arrow_frame_width_spinbox.setDecimals(2)
        self.arrow_frame_width_spinbox.setMinimum(0.00)
        self.arrow_frame_width_spinbox.setMaximum(50.00)
        self.arrow_frame_width_spinbox.setProperty('value', 0.00)
        self.arrow_frame_width_spinbox.setObjectName(_fromUtf8('arrow_frame_width_spinbox'))
        self.arrow_frame_width_spinbox.setVisible(False)

        # ボタン「背景色」

        self.arrow_background_color_button = QtGui.QPushButton(self.arrow_tab)
        self.arrow_background_color_button.setGeometry(QtCore.QRect(60, 235, 101, 23))
        self.arrow_background_color_button.setObjectName(_fromUtf8('arrow_background_color_button'))
        self.arrow_background_color_button.setVisible(False)

        # ラベル「透過率」

        self.arrow_alpha_label = QtGui.QLabel(self.arrow_tab)
        self.arrow_alpha_label.setGeometry(QtCore.QRect(60, 270, 50, 12))
        self.arrow_alpha_label.setObjectName(_fromUtf8('arrow_alpha_label'))
        self.arrow_alpha_label.setVisible(False)

        # スライダ「透過率」

        self.arrow_alpha_slider = QtGui.QSlider(self.arrow_tab)
        self.arrow_alpha_slider.setGeometry(
            QtCore.QRect(60, 285, 301, 22))
        self.arrow_alpha_slider.setMinimum(0)
        self.arrow_alpha_slider.setMaximum(255)
        self.arrow_alpha_slider.setSliderPosition(255)
        self.arrow_alpha_slider.setOrientation(QtCore.Qt.Horizontal)
        self.arrow_alpha_slider.setObjectName(
            _fromUtf8('arrow_alpha_slider' ))
        self.arrow_alpha_slider.setVisible(False)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox,
                               QtCore.SIGNAL(_fromUtf8('accepted()')),
                               Dialog.accept)
        QtCore.QObject.connect(self.buttonBox,
                               QtCore.SIGNAL(_fromUtf8('rejected()')),
                               Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate('Dialog', "アイテム編集", None))
        self.label.setText(_translate('Dialog', "テキスト", None))
        self.label_font_button.setText(_translate('Dialog', "フォント", None))
        self.label_font_color_button.setText(_translate('Dialog', "フォント色", None))
        self.checkBox.setText(_translate('Dialog', "フレームを表示", None))
        self.label_frame_color_button.setText(_translate('Dialog', "フレーム色", None))
        self.checkBox_3.setText(_translate('Dialog', "テキスト幅に合わせる", None))
        self.checkBox_2.setText(_translate('Dialog', "塗りつぶし", None))
        self.label_background_color_button.setText(_translate('Dialog', "塗りつぶし色", None))
        self.label_2.setText(_translate('Dialog', "フレーム太さ", None))
        self.pushButton_7.setText(_translate('Dialog', "詳細設定", None))

        # self.label_3.setText(_translate("Dialog", "透過率", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.label_tab),
                                  _translate('Dialog', "ラベル", None))
        self.pushButton_5.setText(_translate('Dialog', "参照", None))
        self.label_4.setText(_translate('Dialog', "フォルダ", None))
        self.groupBox.setTitle(_translate('Dialog', "プレビュー", None))
        self.pushButton_6.setText(_translate('Dialog', "適用", None))
        self.label_5.setText(_translate('Dialog', "回転", None))

        # self.groupBox_3.setTitle(_translate("Dialog", "水平方向配置", None))
        # self.radioButton.setText(_translate("Dialog", "左", None))
        # self.radioButton_2.setText(_translate("Dialog", "中央", None))
        # self.radioButton_3.setText(_translate("Dialog", "右", None))
        # self.groupBox_2.setTitle(_translate("Dialog", "垂直方向配置", None))
        # self.radioButton_4.setText(_translate("Dialog", "上", None))
        # self.radioButton_5.setText(_translate("Dialog", "中央", None))
        # self.radioButton_6.setText(_translate("Dialog", "下", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.picture_tab),
                                  _translate('Dialog', "ピクチャー", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shape_tab),
                                  _translate('Dialog', "基本図形", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.arrow_tab),
                                  _translate('Dialog', "矢印", None))

        # 基本図形

        self.shape_label.setText(_translate('Dialog', "図形", None))
        self.shape_outline_color_button.setText(_translate('Dialog', "ｱｳﾄﾗｲﾝ色", None))
        self.shape_outline_width_label.setText(_translate('Dialog', "ｱｳﾄﾗｲﾝ幅", None))
        self.shape_symbol_checkbox.setText(_translate('Dialog', "デフォルト", None))
        self.shape_fill_color_button.setText(_translate('Dialog', "図形塗りつぶし色", None))
        self.shape_rotation_label.setText(_translate('Dialog', "回転", None))
        self.shape_frame_checkbox.setText(_translate('Dialog', "フレーム表示", None))
        self.shape_frame_color_button.setText(_translate('Dialog', "フレーム色", None))
        self.shape_background_color_button.setText(_translate('Dialog', "背景色", None))
        self.shape_release_button.setText(_translate('Dialog', "デフォルト", None))
        self.shape_apply_button.setText(_translate('Dialog', "適用", None))
        self.shape_frame_width_label.setText(_translate('Dialog', "フレーム幅", None))
        self.shape_alpha_label.setText(_translate('Dialog', "透過率", None))
        self.label_17.setText(_translate('Dialog', "図形の設定画面", None))

        # 矢印

        self.arrow_label.setText(_translate('Dialog', "矢印", None))
        self.arrow_color_button.setText(_translate('Dialog', "矢印の色", None))
        self.arrow_line_width_label.setText(_translate('Dialog', "線幅", None))
        self.arrow_head_width.setText(_translate('Dialog', "ヘッドの幅", None))
        self.arrow_frame_checkbox.setText(_translate('Dialog', "フレーム表示", None))
        self.arrow_frame_color_button.setText(_translate('Dialog', "フレーム色", None))
        self.arrow_frame_width_label.setText(_translate('Dialog', "フレーム幅", None))
        self.arrow_background_color_button.setText(_translate('Dialog', "背景色", None))
        self.arrow_alpha_label.setText(_translate('Dialog', "透過率", None))
        self.arrow_settings_button.setText(_fromUtf8(''))
        self.arrow_settings_label.setText(_translate('Dialog', "矢印の設定画面", None))


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

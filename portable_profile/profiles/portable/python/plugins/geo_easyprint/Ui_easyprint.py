# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_easyprint.ui'
#
# Created: Fri Oct  7 17:45:37 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_EasyPrint(object):
    def setupUi(self, EasyPrint):
        EasyPrint.setObjectName("EasyPrint")
        EasyPrint.resize(396, 287)
        self.gridLayout_4 = QtGui.QGridLayout(EasyPrint)
        self.gridLayout_4.setObjectName("gridLayout_4")

        # tab widget
        self.tabWidget = QtGui.QTabWidget(EasyPrint)
        self.tabWidget.setObjectName("tabWidget")
        # シンプル地図
        self.tabSimpleMap = QtGui.QWidget()
        self.tabSimpleMap.setObjectName("tabSimpleMap")
        self.gridLayout_16 = QtGui.QGridLayout(self.tabSimpleMap)
        self.gridLayout_16.setObjectName("gridLayout_16")
        # 地図
        self.groupBox_7 = QtGui.QGroupBox(self.tabSimpleMap)
        self.groupBox_7.setObjectName("groupBox_7")

        # grid layout
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setMargin(4)
        self.gridLayout.setHorizontalSpacing(50)
        self.gridLayout.setObjectName("gridLayout")

        # 縮尺 label
        self.label = QtGui.QLabel(self.groupBox_7)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        # 縮尺 combobox
        self.printScale = QtGui.QComboBox(self.groupBox_7)
        self.printScale.setObjectName("printScale")
        self.gridLayout.addWidget(self.printScale, 0, 1, 1, 1)

        # ユーザー定義縮尺 label
        self.label_7 = QtGui.QLabel(self.groupBox_7)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        # ユーザー定義縮尺 spinbox
        self.userScale = QtGui.QSpinBox(self.groupBox_7)
        self.userScale.setEnabled(False)
        self.userScale.setObjectName("userScale")
        self.gridLayout.addWidget(self.userScale, 1, 1, 1, 1)

        # サイズ label
        self.label_2 = QtGui.QLabel(self.groupBox_7)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        # サイズ combobox
        self.printFormat = QtGui.QComboBox(self.groupBox_7)
        self.printFormat.setObjectName("printFormat")
        self.gridLayout.addWidget(self.printFormat, 2, 1, 1, 1)

        # Muki label
        self.label_orientation = QtGui.QLabel(self.groupBox_7)
        self.label_orientation.setObjectName("label_orientation")
        self.gridLayout.addWidget(self.label_orientation, 3, 0, 1, 1)
        self.label_orientation.setVisible(False)

        # muki  combobox
        self.print_orientation = QtGui.QComboBox(self.groupBox_7)
        self.print_orientation.setObjectName("print_orientation")
        self.gridLayout.addWidget(self.print_orientation, 3, 1, 1, 1)
        self.print_orientation.setVisible(False)

        # レイアウト label(未使用)
        self.label_5 = QtGui.QLabel(self.groupBox_7)
        self.label_5.setVisible(False)
        self.label_5.setObjectName("label_5")
        # self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        # レイアウト combobox(未使用)
        self.layout = QtGui.QComboBox(self.groupBox_7)
        self.layout.setVisible(False)
        self.layout.setObjectName("layout")
        # self.gridLayout.addWidget(self.layout, 3, 1, 1, 1)
        # タイトル label
        self.label_3 = QtGui.QLabel(self.groupBox_7)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        # タイトル lineedit
        self.title = QtGui.QLineEdit(self.groupBox_7)
        self.title.setText("")
        self.title.setReadOnly(False)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 4, 1, 1, 1)
        # サブタイトル label
        self.label_4 = QtGui.QLabel(self.groupBox_7)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        # サブタイトル lineedit
        self.subtitle = QtGui.QLineEdit(self.groupBox_7)
        self.subtitle.setEnabled(True)
        self.subtitle.setText("")
        self.subtitle.setObjectName("subtitle")
        self.gridLayout.addWidget(self.subtitle, 5, 1, 1, 1)
        # パーソン label(未使用)
        self.label_6 = QtGui.QLabel(self.groupBox_7)
        self.label_6.setVisible(False)
        self.label_6.setObjectName("label_6")
        # self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        # パーソン lineedit(未使用)
        self.person = QtGui.QLineEdit(self.groupBox_7)
        self.person.setVisible(False)
        self.person.setObjectName("person")
        # self.gridLayout.addWidget(self.person, 6, 1, 1, 1)

        # 背景
        self.map_background = QtGui.QLabel(self.groupBox_7)
        self.map_background.setObjectName("map_background")
        self.gridLayout.addWidget(self.map_background, 7, 0, 1, 1)
        self.map_background.setVisible(True)

        # colorbutton
        self.map_background_button = QtGui.QToolButton(self.groupBox_7)
        self.map_background.setObjectName("map_background_button")
        self.gridLayout.addWidget(self.map_background_button, 7, 1, 1, 1)
        self.map_background_button.setVisible(True)

        # 凡例 label
        self.label_26 = QtGui.QLabel(self.groupBox_7)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 8, 0, 1, 1)
        # 凡例 checkbox
        self.legend = QtGui.QCheckBox(self.groupBox_7)
        # self.legend.setMinimumSize(QtCore.QSize(0, 23))
        self.legend.setText("")
        # self.legend.setText(u"蜃｡萓九�ｮ逕ｻ蜒上ヵ繧｡繧､繝ｫ縺ｯ\n莉･荳九�ｮ繝輔か繝ｫ繝�縺ｫ菫晏ｭ倥＠縺ｦ縺上□縺輔＞縲�\nC:\\nishi_dodai\\legends\\")
        self.legend.setFixedSize(210, 40)
        self.legend.setObjectName("legend")
        self.gridLayout.addWidget(self.legend, 8, 1, 1, 1)
        # 凡例 label:注意書き
        # self.label_36 = QtGui.QLabel(self.groupBox_7)
        # self.label_36.setObjectName("label_36")
        # self.gridLayout.addWidget(self.label_36, 7, 3, 1, 1)
        # copyright label(未使用)
        self.label_27 = QtGui.QLabel(self.groupBox_7)
        self.label_27.setVisible(False)
        self.label_27.setObjectName("label_27")
        # self.gridLayout.addWidget(self.label_27, 8, 0, 1, 1)

        # copyright checkbox(未使用)
        self.copyright = QtGui.QCheckBox(self.groupBox_7)
        self.copyright.setVisible(False)
        self.copyright.setMinimumSize(QtCore.QSize(0, 23))
        self.copyright.setText("")
        self.copyright.setObjectName("copyright")
        # self.gridLayout.addWidget(self.copyright, 8, 1, 1, 1)

        # グリッド label
        self.label_28 = QtGui.QLabel(self.groupBox_7)
        self.label_28.setObjectName("label_28")
        self.label_28.setVisible(True)
        self.gridLayout.addWidget(self.label_28, 11, 0, 1, 1)

        # グリッド checkbox
        self.grids = QtGui.QCheckBox(self.groupBox_7)
        self.grids.setVisible(True)
        self.grids.setEnabled(True)
        self.grids.setMinimumSize(QtCore.QSize(0, 23))
        self.grids.setText("")
        self.grids.setChecked(True)
        self.grids.setTristate(False)
        self.grids.setObjectName("grids")
        self.gridLayout.addWidget(self.grids, 11, 1, 1, 1)

        # cutting lines label(未使用)
        self.label_29 = QtGui.QLabel(self.groupBox_7)
        self.label_29.setVisible(False)
        self.label_29.setObjectName("label_29")
        # self.gridLayout.addWidget(self.label_29, 11, 0, 1, 1)

        # cutting lines checkbox(未使用)
        self.cuttinglines = QtGui.QCheckBox(self.groupBox_7)
        self.cuttinglines.setVisible(False)
        self.cuttinglines.setMinimumSize(QtCore.QSize(0, 23))
        self.cuttinglines.setText("")
        self.cuttinglines.setObjectName("cuttinglines")
        # self.gridLayout.addWidget(self.cuttinglines, 11, 1, 1, 1)

        # folding marks label(未使用)
        self.label_30 = QtGui.QLabel(self.groupBox_7)
        self.label_30.setVisible(False)
        self.label_30.setObjectName("label_30")
        # self.gridLayout.addWidget(self.label_30, 12, 0, 1, 1)

        # folding marks checkbox(未使用)
        self.foldingmarks = QtGui.QCheckBox(self.groupBox_7)
        self.foldingmarks.setVisible(False)
        self.foldingmarks.setMinimumSize(QtCore.QSize(0, 23))
        self.foldingmarks.setText("")
        self.foldingmarks.setObjectName("foldingmarks")
        # self.gridLayout.addWidget(self.foldingmarks, 12, 1, 1, 1)
        # スケールバー label

        self.label_35 = QtGui.QLabel(self.groupBox_7)
        self.label_35.setObjectName("label_35")
        self.label_35.setText(u"スケールバー")
        self.gridLayout.addWidget(self.label_35, 9, 0, 1, 1)
        # スケールバー checkbox

        self.scalebar = QtGui.QCheckBox(self.groupBox_7)
        self.scalebar.setMinimumSize(QtCore.QSize(0, 23))
        self.scalebar.setText("")
        self.scalebar.setFixedSize(23, 23)
        self.scalebar.setObjectName("scalebar")
        self.gridLayout.addWidget(self.scalebar, 9, 1, 1, 1)
        # 方位 label

        self.label_34 = QtGui.QLabel(self.groupBox_7)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 10, 0, 1, 1)
        # 方位 checkbox

        self.crsdesc = QtGui.QCheckBox(self.groupBox_7)
        self.crsdesc.setMinimumSize(QtCore.QSize(0, 23))
        self.crsdesc.setText("")
        self.crsdesc.setFixedSize(23, 23)
        self.crsdesc.setObjectName("crsdesc")
        self.gridLayout.addWidget(self.crsdesc, 10, 1, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.groupBox_7, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding
        )
        self.gridLayout_16.addItem(spacerItem, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabSimpleMap, "")
        # 以下 未使用

        self.tabMapbook = QtGui.QWidget()
        self.tabMapbook.setObjectName("tabMapbook")
        self.gridLayout_6 = QtGui.QGridLayout(self.tabMapbook)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox = QtGui.QGroupBox(self.tabMapbook)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setMargin(4)
        self.gridLayout_5.setHorizontalSpacing(34)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.mbgridtype = QtGui.QComboBox(self.groupBox)
        self.mbgridtype.setObjectName("mbgridtype")
        self.gridLayout_5.addWidget(self.mbgridtype, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 1, 0, 1, 1)
        self.mbmaplayer = QtGui.QComboBox(self.groupBox)
        self.mbmaplayer.setObjectName("mbmaplayer")
        self.gridLayout_5.addWidget(self.mbmaplayer, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)
        self.mboverlap = QtGui.QDoubleSpinBox(self.groupBox)
        self.mboverlap.setDecimals(1)
        self.mboverlap.setSingleStep(5.0)
        self.mboverlap.setProperty("value", 10.0)
        self.mboverlap.setObjectName("mboverlap")
        self.gridLayout_5.addWidget(self.mboverlap, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.btnMbGrid = QtGui.QPushButton(self.groupBox)
        self.btnMbGrid.setObjectName("btnMbGrid")
        self.horizontalLayout.addWidget(self.btnMbGrid)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.tabMapbook)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setMargin(4)
        self.gridLayout_7.setHorizontalSpacing(34)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_7.addWidget(self.label_11, 1, 0, 1, 1)
        self.mboverviewmap = QtGui.QCheckBox(self.groupBox_2)
        self.mboverviewmap.setMinimumSize(QtCore.QSize(0, 23))
        self.mboverviewmap.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mboverviewmap.setText("")
        self.mboverviewmap.setObjectName("mboverviewmap")
        self.gridLayout_7.addWidget(self.mboverviewmap, 1, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 2, 0, 1, 1)
        self.mbtileindicator = QtGui.QCheckBox(self.groupBox_2)
        self.mbtileindicator.setMinimumSize(QtCore.QSize(0, 23))
        self.mbtileindicator.setText("")
        self.mbtileindicator.setObjectName("mbtileindicator")
        self.gridLayout_7.addWidget(self.mbtileindicator, 2, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setEnabled(True)
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 4, 0, 1, 1)
        self.mbprintasraster = QtGui.QCheckBox(self.groupBox_2)
        self.mbprintasraster.setEnabled(True)
        self.mbprintasraster.setMinimumSize(QtCore.QSize(0, 23))
        self.mbprintasraster.setText("")
        self.mbprintasraster.setObjectName("mbprintasraster")
        self.gridLayout_7.addWidget(self.mbprintasraster, 4, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setEnabled(True)
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 3, 0, 1, 1)
        self.mbshadedcells = QtGui.QCheckBox(self.groupBox_2)
        self.mbshadedcells.setMinimumSize(QtCore.QSize(0, 23))
        self.mbshadedcells.setText("")
        self.mbshadedcells.setObjectName("mbshadedcells")
        self.gridLayout_7.addWidget(self.mbshadedcells, 3, 1, 1, 1)
        self.mbprintsinglefile = QtGui.QCheckBox(self.groupBox_2)
        self.mbprintsinglefile.setMinimumSize(QtCore.QSize(0, 23))
        self.mbprintsinglefile.setText("")
        self.mbprintsinglefile.setObjectName("mbprintsinglefile")
        self.gridLayout_7.addWidget(self.mbprintsinglefile, 5, 1, 1, 1)
        self.label_32 = QtGui.QLabel(self.groupBox_2)
        self.label_32.setMinimumSize(QtCore.QSize(0, 23))
        self.label_32.setObjectName("label_32")
        self.gridLayout_7.addWidget(self.label_32, 5, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.tabMapbook)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.mbExport = QtGui.QHBoxLayout()
        self.mbExport.setObjectName("mbExport")
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.mbExport.addWidget(self.label_13)
        self.mbexportpath = QtGui.QLineEdit(self.groupBox_3)
        self.mbexportpath.setObjectName("mbexportpath")
        self.mbExport.addWidget(self.mbexportpath)
        self.btnBrowseExport = QtGui.QPushButton(self.groupBox_3)
        self.btnBrowseExport.setObjectName("btnBrowseExport")
        self.mbExport.addWidget(self.btnBrowseExport)
        self.gridLayout_9.addLayout(self.mbExport, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding
        )
        self.gridLayout_6.addItem(spacerItem2, 3, 0, 1, 1)
        # self.tabWidget.addTab(self.tabMapbook, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_15 = QtGui.QGridLayout(self.tab)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_12 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.mbfmaplayer = QtGui.QComboBox(self.groupBox_4)
        self.mbfmaplayer.setObjectName("mbfmaplayer")
        self.gridLayout_10.addWidget(self.mbfmaplayer, 0, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_4)
        self.label_16.setObjectName("label_16")
        self.gridLayout_10.addWidget(self.label_16, 0, 0, 1, 1)
        self.mbftitle = QtGui.QComboBox(self.groupBox_4)
        self.mbftitle.setObjectName("mbftitle")
        self.gridLayout_10.addWidget(self.mbftitle, 1, 1, 1, 1)
        self.mbfsubtitle = QtGui.QComboBox(self.groupBox_4)
        self.mbfsubtitle.setObjectName("mbfsubtitle")
        self.gridLayout_10.addWidget(self.mbfsubtitle, 2, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.groupBox_4)
        self.label_17.setObjectName("label_17")
        self.gridLayout_10.addWidget(self.label_17, 1, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.groupBox_4)
        self.label_18.setObjectName("label_18")
        self.gridLayout_10.addWidget(self.label_18, 2, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.groupBox_4)
        self.label_19.setObjectName("label_19")
        self.gridLayout_10.addWidget(self.label_19, 3, 0, 1, 1)
        self.label_20 = QtGui.QLabel(self.groupBox_4)
        self.label_20.setObjectName("label_20")
        self.gridLayout_10.addWidget(self.label_20, 4, 0, 1, 1)
        self.mbfscale = QtGui.QComboBox(self.groupBox_4)
        self.mbfscale.setObjectName("mbfscale")
        self.gridLayout_10.addWidget(self.mbfscale, 3, 1, 1, 1)
        self.mbfrotation = QtGui.QComboBox(self.groupBox_4)
        self.mbfrotation.setObjectName("mbfrotation")
        self.gridLayout_10.addWidget(self.mbfrotation, 4, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.tab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_14 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_21 = QtGui.QLabel(self.groupBox_5)
        self.label_21.setObjectName("label_21")
        self.gridLayout_11.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_22 = QtGui.QLabel(self.groupBox_5)
        self.label_22.setObjectName("label_22")
        self.gridLayout_11.addWidget(self.label_22, 1, 0, 1, 1)
        self.label_23 = QtGui.QLabel(self.groupBox_5)
        self.label_23.setObjectName("label_23")
        self.gridLayout_11.addWidget(self.label_23, 2, 0, 1, 1)
        self.mbfextraspace = QtGui.QDoubleSpinBox(self.groupBox_5)
        self.mbfextraspace.setDecimals(0)
        self.mbfextraspace.setSingleStep(5.0)
        self.mbfextraspace.setProperty("value", 10.0)
        self.mbfextraspace.setObjectName("mbfextraspace")
        self.gridLayout_11.addWidget(self.mbfextraspace, 0, 1, 1, 1)
        self.mbfdefaultscale = QtGui.QDoubleSpinBox(self.groupBox_5)
        self.mbfdefaultscale.setMaximum(100000000.0)
        self.mbfdefaultscale.setProperty("value", 1000.0)
        self.mbfdefaultscale.setObjectName("mbfdefaultscale")
        self.gridLayout_11.addWidget(self.mbfdefaultscale, 1, 1, 1, 1)
        self.mbfdefaultrotation = QtGui.QDoubleSpinBox(self.groupBox_5)
        self.mbfdefaultrotation.setMaximum(260.0)
        self.mbfdefaultrotation.setObjectName("mbfdefaultrotation")
        self.gridLayout_11.addWidget(self.mbfdefaultrotation, 2, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.groupBox_5)
        self.label_24.setObjectName("label_24")
        self.gridLayout_11.addWidget(self.label_24, 4, 0, 1, 1)
        self.mbfprintasraster = QtGui.QCheckBox(self.groupBox_5)
        self.mbfprintasraster.setMinimumSize(QtCore.QSize(0, 23))
        self.mbfprintasraster.setText("")
        self.mbfprintasraster.setObjectName("mbfprintasraster")
        self.gridLayout_11.addWidget(self.mbfprintasraster, 4, 1, 1, 1)
        self.label_31 = QtGui.QLabel(self.groupBox_5)
        self.label_31.setMinimumSize(QtCore.QSize(0, 23))
        self.label_31.setObjectName("label_31")
        self.gridLayout_11.addWidget(self.label_31, 3, 0, 1, 1)
        self.mbfoverviewmap = QtGui.QCheckBox(self.groupBox_5)
        self.mbfoverviewmap.setText("")
        self.mbfoverviewmap.setObjectName("mbfoverviewmap")
        self.gridLayout_11.addWidget(self.mbfoverviewmap, 3, 1, 1, 1)
        self.mbfprintsinglefile = QtGui.QCheckBox(self.groupBox_5)
        self.mbfprintsinglefile.setMinimumSize(QtCore.QSize(0, 23))
        self.mbfprintsinglefile.setText("")
        self.mbfprintsinglefile.setObjectName("mbfprintsinglefile")
        self.gridLayout_11.addWidget(self.mbfprintsinglefile, 5, 1, 1, 1)
        self.label_33 = QtGui.QLabel(self.groupBox_5)
        self.label_33.setObjectName("label_33")
        self.gridLayout_11.addWidget(self.label_33, 5, 0, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.tab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_13 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_25 = QtGui.QLabel(self.groupBox_6)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_2.addWidget(self.label_25)
        self.mbfexportpath = QtGui.QLineEdit(self.groupBox_6)
        self.mbfexportpath.setObjectName("mbfexportpath")
        self.horizontalLayout_2.addWidget(self.mbfexportpath)
        self.btnBrowseExportFeature = QtGui.QPushButton(self.groupBox_6)
        self.btnBrowseExportFeature.setObjectName("btnBrowseExportFeature")
        self.horizontalLayout_2.addWidget(self.btnBrowseExportFeature)
        self.gridLayout_13.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_6, 2, 0, 1, 1)
        # self.tabWidget.addTab(self.tab, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(EasyPrint)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_4.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(EasyPrint)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(
            self.buttonBox, QtCore.SIGNAL("accepted()"), EasyPrint.accept
        )
        QtCore.QObject.connect(
            self.buttonBox, QtCore.SIGNAL("rejected()"), EasyPrint.reject
        )
        QtCore.QMetaObject.connectSlotsByName(EasyPrint)

    def retranslateUi(self, EasyPrint):
        EasyPrint.setWindowTitle(
            QtGui.QApplication.translate(
                "EasyPrint", "EasyPrint", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.groupBox_7.setTitle(
            QtGui.QApplication.translate(
                "EasyPrint", "Map ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Scale: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_7.setText(
            QtGui.QApplication.translate(
                "EasyPrint",
                "User defined scale: ",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.label_2.setText(
            QtGui.QApplication.translate(
                "EasyPrint", u"用紙サイズと向き: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_orientation.setText(
            QtGui.QApplication.translate(
                "EasyPrint", u"向き: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )

        self.label_5.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Layout: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_3.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Title: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_4.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Subtitle: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_6.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Person: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_26.setText(
            QtGui.QApplication.translate(
                "EasyPrint", u"画像: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.map_background.setText(
            QtGui.QApplication.translate(
                "EasyPrint", u"背景色: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.map_background_button.setText(
            QtGui.QApplication.translate(
                "EasyPrint", u"背景色の変更", None, QtGui.QApplication.UnicodeUTF8
            )
        )

        # 20140129 add
        # self.label_36.setText(u"凡例の画像ファイルは以下のフォルダに保存してください。\nC:\\nishi_dodai\\plugins\\pictures\\")
        self.label_27.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Copyright: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_28.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Grid: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_29.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Cutting lines: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_30.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Folding marks: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        #        self.label_34.setText(QtGui.QApplication.translate("EasyPrint", "Crs description:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(u"方位: ")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabSimpleMap),
            QtGui.QApplication.translate(
                "EasyPrint", "SimpleMap", None, QtGui.QApplication.UnicodeUTF8
            ),
        )

        # 以下 未使用？？
        self.groupBox.setTitle(
            QtGui.QApplication.translate(
                "EasyPrint", "Grid ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_8.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Grid type: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_9.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Map layer: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_10.setText(
            QtGui.QApplication.translate(
                "EasyPrint",
                "Overlap percentage: ",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.mboverlap.setSuffix(
            QtGui.QApplication.translate(
                "EasyPrint", " %", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.btnMbGrid.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Create", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.groupBox_2.setTitle(
            QtGui.QApplication.translate(
                "EasyPrint", "Parameter ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_11.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Overview map: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_12.setText(
            QtGui.QApplication.translate(
                "EasyPrint",
                "Adjacent tile indicator: ",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.label_14.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Print as raster: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_15.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Shaded cells: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_32.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Print single file: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.groupBox_3.setTitle(
            QtGui.QApplication.translate(
                "EasyPrint", "Export ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_13.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Export to: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.btnBrowseExport.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Browse", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabMapbook),
            QtGui.QApplication.translate(
                "EasyPrint", "Mapbook by grid", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.groupBox_4.setTitle(
            QtGui.QApplication.translate(
                "EasyPrint", "Map ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_16.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Map layer: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_17.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Title: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_18.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Subtitle: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_19.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Scale: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_20.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Rotation: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.groupBox_5.setTitle(
            QtGui.QApplication.translate(
                "EasyPrint", "Parameter ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_21.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Extra space: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_22.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Default scale: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_23.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Default rotation: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.mbfextraspace.setSuffix(
            QtGui.QApplication.translate(
                "EasyPrint", " %", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.mbfdefaultscale.setPrefix(
            QtGui.QApplication.translate(
                "EasyPrint", "1 : ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.mbfdefaultrotation.setSuffix(
            QtGui.QApplication.translate(
                "EasyPrint", " Degrees", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_24.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Print as raster: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_31.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Overview map: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_33.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Print single file: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.groupBox_6.setTitle(
            QtGui.QApplication.translate(
                "EasyPrint", "Export ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.label_25.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Export to: ", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.btnBrowseExportFeature.setText(
            QtGui.QApplication.translate(
                "EasyPrint", "Browse", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QtGui.QApplication.translate(
                "EasyPrint", "Mapbook by feature", None, QtGui.QApplication.UnicodeUTF8
            ),
        )


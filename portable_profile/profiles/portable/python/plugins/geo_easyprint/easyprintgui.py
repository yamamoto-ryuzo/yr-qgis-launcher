# -*- coding: utf-8 -*-
from pathlib import Path
import sys

from qgis.PyQt import uic
from qgis.PyQt.QtCore import pyqtSignal, Qt, QSettings
from qgis.PyQt.QtGui import QColor, QPixmap
from qgis.PyQt.QtWidgets import QDialog, QDialogButtonBox, QColorDialog
from qgis.core import QgsProject


from .tools import utils
from . import settings

UI_FILE = "Ui_easyprint.ui"


class EasyPrintGui(QDialog):
    okClickedSimpleMap = pyqtSignal(
        str, str, str, str, str, bool, bool, bool, bool, bool, bool, bool, int, QColor
    )

    def __init__(self, parent, iface):
        super(EasyPrintGui, self).__init__(parent=parent)
        self.iface = iface
        self.newest_composer = None

        directory = Path(__file__).parent
        ui_file = directory / UI_FILE
        uic.loadUi(ui_file, self)

    def initGui(
        self, scales, paperformats, layouts, maplayers, vectorlayers, newest_composer
    ):

        # hidden GUI
        self.label_5.setVisible(False)
        self.layout.setVisible(False)
        self.label_6.setVisible(False)
        self.person.setVisible(False)
        self.label_27.setVisible(False)
        self.copyright.setVisible(False)
        self.label_29.setVisible(False)
        self.cuttinglines.setVisible(False)
        self.label_30.setVisible(False)
        self.foldingmarks.setVisible(False)

        self.button_show_composer = self.buttonBox.addButton(
            u"最後に閉じた(作成した)プレビュー画面を開く", QDialogButtonBox.ActionRole
        )
        self.button_show_composer.setEnabled(False)
        self.buttonBox.layout().insertWidget(
            0, self.button_show_composer, 0, Qt.AlignLeft
        )

        self.settings = QSettings()

        # SimpleMap #
        # Set some stuff for the user scale spin box.
        self.userScale.setMinimum(1)
        self.userScale.setMaximum(100000000)
        self.userScale.setPrefix("1 : ")
        try:
            self.userScale.setValue(int(scales[0]))
        except TypeError:
            self.userScale.setValue(100000000)

        # Fill the combobox with available scales.
        for scale in scales:
            self.printScale.addItem("1 : " + scale)
        self.printScale.currentIndexChanged.connect(
            self.on_printScale_currentIndexChanged
        )

        # Fill the combobox with available paperformats.
        self.printFormat.addItems(paperformats)

        # Fill the combobox with available layouts.
        for l in layouts:
            self.layout.addItem(l.getID())

        self.person.setText(self.settings.value("easyprint/gui/person"))
        self.grids.setChecked(self.get_registry("easyprint/gui/grids", True))
        self.legend.setChecked(self.get_registry("easyprint/gui/legend", True))
        self.scalebar.setChecked(self.get_registry("easyprint/gui/scalebar", True))
        self.copyright.setChecked(self.get_registry("easyprint/gui/copyright", False))
        self.cuttinglines.setChecked(
            self.get_registry("easyprint/gui/cuttinglines", False)
        )
        self.foldingmarks.setChecked(
            self.get_registry("easyprint/gui/foldingmarks", False)
        )
        self.crsdesc.setChecked(
            self.get_registry("easyprint/gui/crsdescription", False)
        )

        self.background_color = Qt.white
        self.change_color_pix()
        self.map_background_button.clicked.connect(self.change_background_color)

        project = QgsProject.instance()
        manager = project.layoutManager()
        composers = manager.printLayouts()

        if newest_composer and newest_composer in composers:
            self.newest_composer = newest_composer
        elif newest_composer is None and composers:
            self.newest_composer = composers[-1]
        if self.newest_composer:
            self.button_show_composer.setEnabled(True)

        self.button_show_composer.clicked.connect(self.show_composer)

    def set_newest_composer(self, composer):
        self.newest_composer = composer
        self.button_show_composer.setEnabled(True)

    def hidden_view(self, view):
        composerView.composerViewHide.connect(self.hidden_view)
        window = view.composerWindow()
        reply = QMessageBox.question(
            window,
            u"保存しますか？",
            u"印刷(コンポーザー)の設定を保存しますか？",
            QMessageBox.Yes,
            QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            window.close()
            self.iface.deleteComposer(view)

    def set_newestbutton_enabled(self, composer):
        project = QgsProject.instance()
        manager = project.layoutManager()
        composers = manager.printLayouts()
        if composer in composers:
            composers.remove(composer)
        if self.newest_composer == composer and not composers:
            self.newest_composer = None
            self.button_show_composer.setEnabled(False)
        elif self.newest_composer == composer and composers:
            # print('current composer remove')
            self.newest_composer = composers[-1]
        elif self.newest_composer is None and composers:
            self.newest_composer = composers[-1]
            self.button_show_composer.setEnabled(True)
        else:
            self.newest_composer = None
            self.button_show_composer.setEnabled(False)

    def show_composer(self):
        composer = self.newest_composer
        if not composer:
            return
        self.close()
        self.iface.openLayoutDesigner(composer)

    def change_background_color(self):
        color = QColorDialog.getColor(self.background_color)
        if not color.isValid():
            # カラーが選択されたかの判定
            return
        self.background_color = color
        self.change_color_pix()

    def change_color_pix(self):
        color_pix = QPixmap(24, 24)
        color_pix.fill(self.background_color)
        self.map_background.setPixmap(color_pix)

    def on_printScale_currentIndexChanged(self):
        currentIndex = self.printScale.currentIndex()
        if currentIndex == 1:
            self.userScale.setEnabled(True)
        else:
            self.userScale.setEnabled(False)

    def accept(self):
        super(EasyPrintGui, self).accept()
        self.set_registry("easyprint/gui/person", self.person.text())
        self.set_registry("easyprint/gui/grids", self.grids.isChecked())
        self.set_registry("easyprint/gui/legend", self.legend.isChecked())
        self.set_registry("easyprint/gui/scalebar", self.scalebar.isChecked())
        self.set_registry("easyprint/gui/copyright", self.copyright.isChecked())
        self.set_registry("easyprint/gui/cuttinglines", self.cuttinglines.isChecked())
        self.set_registry("easyprint/gui/foldingmarks", self.foldingmarks.isChecked())
        self.set_registry("easyprint/gui/crsdescription", self.crsdesc.isChecked())

        currentIndex = self.printScale.currentIndex()
        if currentIndex == 1:
            self.scale = "1 : " + str(self.userScale.value())
        else:
            self.scale = self.printScale.currentText()

        tabIndex = self.tabWidget.currentIndex()

        if tabIndex == 0:
            self.okClickedSimpleMap.emit(
                self.scale,
                self.printFormat.currentText(),
                self.title.text(),
                self.subtitle.text(),
                self.person.text(),
                self.crsdesc.isChecked(),
                self.grids.isChecked(),
                self.legend.isChecked(),
                self.scalebar.isChecked(),
                self.copyright.isChecked(),
                self.cuttinglines.isChecked(),
                self.foldingmarks.isChecked(),
                int(self.layout.currentIndex()),
                self.background_color,
            )

    def set_registry(self, key, value):
        if not self.settings:
            return -1
        # value = {True: 1, False: 0}.get(value, value)
        return self.settings.setValue(key, value)

    def get_registry(self, key, default=None):
        if not self.settings:
            return -1
        value = self.settings.value(key, default)
        return {"true": True, "false": False}.get(value, value)

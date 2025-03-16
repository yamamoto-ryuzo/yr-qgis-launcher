#!/usr/bin/python
# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
#
# EasyPrint - A QGIS plugin to create maps.
#
# Copyright (C) 2010 Stefan Ziegler
#
# EMAIL: stefan.ziegler (at) bd.so.ch
# WEB  : www.catais.org
#
# ---------------------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# ---------------------------------------------------------------------

from pathlib import Path

from qgis.PyQt.QtCore import QSettings
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.PyQt import QtXml
from qgis.core import QgsProject
from qgis.gui import QgsLayoutView

# from .myToolBar import MyToolBar
from .tools import utils
from . import resources
from .easyprintgui import EasyPrintGui

from .layout import Layout
from .decoration import Decoration


class EasyPrint:
    def __init__(self, iface):
        # Save reference to the QGIS interface.
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.scales = []
        self.paperformats = []
        self.dlg = None
        self.composers = []
        self.toolbars = []
        self.remove_composer = None

        self.plugin_dir = Path(__file__).parent

    def initGui(self):
        # Create action that will start plugin configuration.
        icon_path = self.plugin_dir / "images" / "mActionFilePrint.png"
        self.action = QAction(QIcon(str(icon_path)), "簡易印刷", self.iface.mainWindow())
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item.
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&EasyPrint", self.action)
        project = QgsProject.instance()
        manager = project.layoutManager()
        # project.layoutAdded.connect(self.add_toolbar)
        self.set_composers()
        manager.layoutAdded.connect(self.set_composers)

    def unload(self):
        # Remove the plugin menu item and icon.
        self.iface.removePluginMenu("&EasyPrint", self.action)
        self.iface.removeToolBarIcon(self.action)
        project = QgsProject.instance()
        manager = project.layoutManager()
        manager.layoutAdded.disconnect(self.set_composers)
        # project.layoutAdded.disconnect(self.add_toolbar)

        if self.dlg:
            self.dlg.close()

    def run(self):
        layouts = self.layouts()
        scales = self.preferences("scale", False)
        canvas_scale = round(self.canvas.scale())
        if canvas_scale == 0:
            canvas_scale = 1
        scales.insert(0, str(canvas_scale))
        scales.insert(1, "ユーザー定義")
        paperformats = self.preferences("format", True)

        maplayers = utils.getLayerNames("all")
        vectorlayers = utils.getLayerNames([0, 1, 2])

        self.set_composers()
        newest_composer = None
        if self.composers:
            newest_composer = self.composers[-1]
        self.dlg = EasyPrintGui(self.iface.mainWindow(), self.iface)
        self.dlg.initGui(
            scales, paperformats, layouts, maplayers, vectorlayers, newest_composer
        )

        # Connect to the signals.
        self.dlg.okClickedSimpleMap.connect(self.doSimpleMap)
        self.dlg.exec_()

    def doSimpleMap(
        self,
        printScale,
        printFormat,
        titleString,
        subtitleString,
        personString,
        crsdesc,
        grid,
        legend,
        scalebar,
        copyright,
        cuttinglines,
        foldingmarks,
        layoutIndex,
        background_color,
    ):

        from .tools.doCreateSimpleMap import CreateSimpleMap

        self.d = CreateSimpleMap(
            self.iface,
            float(printScale[3:]),
            printFormat,
            layoutIndex,
            titleString,
            subtitleString,
            personString,
            crsdesc,
            grid,
            legend,
            scalebar,
            copyright,
            cuttinglines,
            foldingmarks,
            background_color=background_color,
        )
        composer = self.d.run()
        """
        composition = self.d.composerView.composition()
        maps = composition.composerMapItems()
        if maps:
            maps[0].setSelected(True)
        """
        self.iface.openLayoutDesigner(composer)

    def hidden_view(self, view):
        """
        非表示になった場合、削除するかを確認する。
        Args:
            view: 非表示にされたコンポーザー
        Returns:

        """
        window = view.composerWindow()
        reply = QMessageBox.question(
            window, "保存しますか？", "印刷(コンポーザー)の設定を保存しますか？", QMessageBox.Yes, QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            # QGIS起動時は問題がないが、終了時にエラーを吐く
            # window.setAttribute(Qt.WA_DeleteOnClose)
            view.composerViewHide.disconnect()
            # 非表示シグナルからのコンポーザー削除の場合、コンポーザー終了時にエラーを吐く
            # self.iface.deleteComposer(view)

    def papersize(self, paper_format):
        height = 297
        width = 210
        preffilename = self.plugin_dir / "preferences/preferences.xml"

        preffile = open(preffilename, "r")
        prefxml = preffile.read()

        doc = QtXml.QDomDocument()
        doc.setContent(prefxml, True)

        root = doc.documentElement()
        if root.tagName() != "preferences":
            return

        n = root.firstChild()
        while not n.isNull():
            e = n.toElement()
            sube = e.firstChild()
            while not sube.isNull():
                if sube.toElement().tagName() == "format":
                    if sube.toElement().text() == paper_format:
                        height = sube.toElement().attribute("height", "")
                        width = sube.toElement().attribute("width", "")
                        try:
                            float(height)
                            float(width)
                            return (height, width)
                        except ValueError:
                            print("height/width float error")
                sube = sube.nextSibling()
            n = n.nextSibling()
        return (height, width)

    def preferences(self, pref, text):
        prefs = []
        preffilename = self.plugin_dir / "preferences/preferences.xml"

        try:
            preffile = open(preffilename, "r")
            prefxml = preffile.read()

            doc = QtXml.QDomDocument()
            doc.setContent(prefxml, True)

            root = doc.documentElement()
            if root.tagName() != "preferences":
                return

            n = root.firstChild()
            while not n.isNull():
                e = n.toElement()
                sube = e.firstChild()
                while not sube.isNull():
                    if sube.toElement().tagName() == pref:
                        try:
                            if not text:
                                float(sube.toElement().text())
                            prefs.append(sube.toElement().text())
                        except ValueError:
                            print("float error: reading scales")
                    sube = sube.nextSibling()
                n = n.nextSibling()
        except IOError:

            print("error opening preferences.xml")

        return prefs

    def layouts(self):
        layouts = []

        layoutsfilename = self.plugin_dir / "layouts/layouts.xml"

        try:
            layoutsfile = open(layoutsfilename, "r")
            layoutsxml = layoutsfile.read()

            doc = QtXml.QDomDocument()
            doc.setContent(layoutsxml, True)

            root = doc.documentElement()
            if root.tagName() != "layouts":
                return

            node = root.firstChild()
            while not node.isNull():
                if node.toElement() and node.nodeName() == "layout":
                    margins = []
                    node_id = node.toElement().attribute("id", "")
                    layout = Layout(node_id)
                    ori = node.toElement().attribute("orientation", "")
                    layout.setOrientation(ori)

                    #  Read a single layout.

                    layoutnode = node.toElement().firstChild()
                    while not layoutnode.isNull():
                        if (
                            layoutnode.toElement()
                            and layoutnode.nodeName() == "margins"
                        ):
                            #  Read margins.
                            marginnode = layoutnode.toElement().firstChild()
                            while not marginnode.isNull():
                                try:
                                    margins.append(float(marginnode.toElement().text()))
                                    print(marginnode.toElement().text())
                                except ValueError:
                                    margins.append(float(0.0))
                                marginnode = marginnode.nextSibling()
                            print(margins)
                            layout.setMargins(margins)
                        elif (
                            layoutnode.toElement()
                            and layoutnode.nodeName() == "decorations"
                        ):
                            #  Read decorations.
                            deconode = layoutnode.toElement().firstChild()
                            while not deconode.isNull():
                                element_type = deconode.toElement().attribute(
                                    "type", ""
                                )
                                decoration = Decoration(element_type)

                                affinity = deconode.toElement().attribute(
                                    "affinity", ""
                                )
                                offset_x = deconode.toElement().attribute(
                                    "offset_x", ""
                                )
                                offset_y = deconode.toElement().attribute(
                                    "offset_y", ""
                                )
                                height = deconode.toElement().attribute("height", "")
                                width = deconode.toElement().attribute("width", "")
                                fontsize = deconode.toElement().attribute(
                                    "font-size", ""
                                )
                                fontfamily = deconode.toElement().attribute(
                                    "font-family", ""
                                )
                                rotation = deconode.toElement().attribute(
                                    "rotation", ""
                                )

                                if str.find(str(affinity), ",") >= 0:
                                    affx = str(str.split(str(affinity), ",")[1]).strip()
                                    affy = str(str.split(str(affinity), ",")[0]).strip()

                                    if (
                                        affx == "left"
                                        or affx == "right"
                                        or affx == "center"
                                    ):
                                        decoration.setAffinityX(affx)

                                    if affy == "top" or affy == "bottom":
                                        decoration.setAffinityY(affy)

                                if fontfamily is not None:
                                    decoration.setFontFamily(fontfamily)

                                try:
                                    decoration.setOffsetX(float(offset_x))
                                except ValueError:
                                    print("float offset_x error")

                                try:
                                    decoration.setOffsetY(float(offset_y))
                                except ValueError:
                                    print("float offset_y error")

                                try:
                                    decoration.setHeight(float(height))
                                except ValueError:
                                    decoration.setHeight(float(0.0))
                                    print("float height error or not found.")

                                try:
                                    decoration.setWidth(float(width))
                                except ValueError:
                                    decoration.setWidth(float(0.0))
                                    print("float width error or not found.")

                                try:
                                    decoration.setFontSize(float(fontsize))
                                except ValueError:
                                    print("float fontsize error or not found.")

                                try:
                                    decoration.setRotation(float(rotation))
                                except ValueError:
                                    print("float rotation error or not found.")

                                if element_type in [
                                    "text",
                                    "date",
                                    "scaletext",
                                    "legend",
                                    "copyright",
                                    "person",
                                ]:
                                    text = deconode.toElement().text()
                                    decoration.setText(text)

                                if element_type in [
                                    "picture",
                                    "northarrow",
                                    "legendpic",
                                ]:
                                    pic = deconode.toElement().text()
                                    decoration.setPicture(pic)

                                layout.addDecoration(decoration)

                                deconode = deconode.nextSibling()

                        layoutnode = layoutnode.nextSibling()
                    print(layout.getMargins())
                    layouts.append(layout)

                node = node.nextSibling()
        except IOError:
            print("error opening preferences.xml")
        return layouts

    def set_composers(self, composer=None):
        project = QgsProject.instance()
        manager = project.layoutManager()
        composers = [com for com in self.composers if com in manager.printLayouts()]
        if composer is not None:
            composers.append(composer)
        self.composers = composers

    def add_toolbar(self, composer):
        composer_window = composer.composerWindow()
        toolbar = MyToolBar(composer_window, self.iface, composer)
        toolbar.run()
        composer_window.addToolBar(Qt.RightToolBarArea, toolbar)
        self.toolbars.append(toolbar)

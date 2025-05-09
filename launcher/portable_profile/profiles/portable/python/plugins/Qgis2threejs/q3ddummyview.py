# -*- coding: utf-8 -*-
# (C) 2023 Minoru Akagi
# SPDX-License-Identifier: GPL-2.0-or-later
# begin: 2023-11-10

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QGraphicsColorizeEffect, QGraphicsPixmapItem, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QColorConstants, QPixmap

from .conf import DEBUG_MODE
from .utils import logMessage, pluginDir


class Q3DDummyView(QGraphicsView):

    def __init__(self, parent=None):
        QGraphicsView.__init__(self, parent)
        self._page = Q3DDummyPage()
        self.setEnabled(False)

        item = QGraphicsPixmapItem(QPixmap(pluginDir("Qgis2threejs.png")))

        effect = QGraphicsColorizeEffect()
        effect.setColor(QColorConstants.Gray)
        item.setGraphicsEffect(effect)

        scene = QGraphicsScene()
        scene.addItem(item)

        self.setScene(scene)

    def teardown(self):
        pass

    def page(self):
        return self._page

    def showDevTools(self):
        pass

    def disableWidgetsAndMenus(self, ui):
        objs = [ui.checkBoxPreview, ui.menuSaveAs, ui.actionReload,
                ui.actionResetCameraPosition, ui.actionDevTools, ui.actionUsage]

        for obj in objs:
            obj.setEnabled(False)

    def __bool__(self):
        return False


class Q3DDummyPage(QObject):

    def __bool__(self):
        return False

    def __getattr__(self, name):
        if DEBUG_MODE:
            logMessage("Q3DDummyPage.{} referenced".format(name))

        return self._func

    def _func(self, *args1, **args2):
        pass

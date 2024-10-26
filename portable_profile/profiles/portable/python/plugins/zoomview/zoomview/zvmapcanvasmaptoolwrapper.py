from PyQt5.QtCore import pyqtSignal, Qt
from qgis.gui import *
from qgis.core import QgsPointXY

from zoomview.zoomview import debug


class ZvMapCanvasMapToolWrapper(QgsMapTool):
    sigPointChanged = pyqtSignal(QgsPointXY)

    def __init__(self, mapTool, canvas):
        assert isinstance(mapTool, QgsMapTool)
        QgsMapTool.__init__(self, canvas=canvas)
        self.mapTool = mapTool

    def canvasReleaseEvent(self, event):
        if debug:
            print('ZvMapCanvasMapToolWrapper->canvasReleaseEvent')
        self.mapTool.canvasReleaseEvent(event)
        if not isinstance(self.mapTool, (QgsMapToolZoom)) or event.button() == Qt.RightButton:
            self.sigPointChanged.emit(event.originalMapPoint())

    def canvasPressEvent(self, event):
        if debug:
            print('ZvMapCanvasMapToolWrapper->canvasPressEvent')
        self.mapTool.canvasPressEvent(event)

    def canvasDoubleClickEvent(self, *args, **kwargs):
        if debug:
            print('ZvMapCanvasMapToolWrapper->canvasDoubleClickEvent')

        self.mapTool.canvasDoubleClickEvent(*args, **kwargs)

    def canvasMoveEvent(self, *args, **kwargs):
        if debug:
            print('ZvMapCanvasMapToolWrapper->canvasMoveEvent')
        self.mapTool.canvasMoveEvent(*args, **kwargs)

    def wheelEvent(self, *args, **kwargs):
        if debug:
            print('ZvMapCanvasMapToolWrapper->wheelEvent')
        return self.mapTool.wheelEvent(*args, **kwargs)

    def __getattr__(self, *args, **kwargs):
        return self.mapTool.__getattr__(*args, **kwargs)

    # def __init_subclass__(self, *args, **kwargs): return self.mapTool.__init_subclass__(*args, **kwargs)
    # def __new__(self, *args, **kwargs): return self.mapTool.__new__(*args, **kwargs)
    def __subclasshook__(self, *args, **kwargs):
        return self.mapTool.__subclasshook__(*args, **kwargs)

    def action(self, *args, **kwargs):
        return self.mapTool.action(*args, **kwargs)

    def activate(self, *args, **kwargs):
        return self.mapTool.activate(*args, **kwargs)

    def blockSignals(self, *args, **kwargs):
        return self.mapTool.blockSignals(*args, **kwargs)

    def button(self, *args, **kwargs):
        return self.mapTool.button(*args, **kwargs)

    def children(self, *args, **kwargs):
        return self.mapTool.children(*args, **kwargs)

    def clean(self, *args, **kwargs):
        return self.mapTool.clean(*args, **kwargs)

    def connectNotify(self, *args, **kwargs):
        return self.mapTool.connectNotify(*args, **kwargs)

    def customEvent(self, *args, **kwargs):
        if debug:
            print('ZvMapCanvasMapToolWrapper->customEvent')
        return self.mapTool.customEvent(*args, **kwargs)

    def deactivate(self, *args, **kwargs):
        return self.mapTool.deactivate(*args, **kwargs)

    def deleteLater(self, *args, **kwargs):
        return self.mapTool.deleteLater(*args, **kwargs)

    def disconnect(self, *args, **kwargs):
        return self.mapTool.disconnect(*args, **kwargs)

    def disconnectNotify(self, *args, **kwargs):
        return self.mapTool.disconnectNotify(*args, **kwargs)

    def dumpObjectInfo(self, *args, **kwargs):
        return self.mapTool.dumpObjectInfo(*args, **kwargs)

    def dumpObjectTree(self, *args, **kwargs):
        return self.mapTool.dumpObjectTree(*args, **kwargs)

    def dynamicPropertyNames(self, *args, **kwargs):
        return self.mapTool.dynamicPropertyNames(*args, **kwargs)

    def event(self, *args, **kwargs):
        return self.mapTool.event(*args, **kwargs)

    def eventFilter(self, *args, **kwargs):
        return self.mapTool.eventFilter(*args, **kwargs)

    def findChild(self, *args, **kwargs):
        return self.mapTool.findChild(*args, **kwargs)

    def findChildren(self, *args, **kwargs):
        return self.mapTool.findChildren(*args, **kwargs)

    def flags(self, *args, **kwargs):
        return self.mapTool.flags(*args, **kwargs)

    def gestureEvent(self, *args, **kwargs):
        if debug:
            print('ZvMapCanvasMapToolWrapper->gestureEvent')
        return self.mapTool.gestureEvent(*args, **kwargs)

    def inherits(self, *args, **kwargs):
        return self.mapTool.inherits(*args, **kwargs)

    def installEventFilter(self, *args, **kwargs):
        return self.mapTool.installEventFilter(*args, **kwargs)

    def isActive(self, *args, **kwargs):
        return self.mapTool.isActive(*args, **kwargs)

    def isSignalConnected(self, *args, **kwargs):
        return self.mapTool.isSignalConnected(*args, **kwargs)

    def isWidgetType(self, *args, **kwargs):
        return self.mapTool.isWidgetType(*args, **kwargs)

    def isWindowType(self, *args, **kwargs):
        return self.mapTool.isWindowType(*args, **kwargs)

    def keyPressEvent(self, *args, **kwargs):
        if debug:
            print('ZvMapCanvasMapToolWrapper->keyPressEvent')
        return self.mapTool.keyPressEvent(*args, **kwargs)

    def keyReleaseEvent(self, *args, **kwargs):
        if debug:
            print('ZvMapCanvasMapToolWrapper->keyReleaseEvent')
        return self.mapTool.keyReleaseEvent(*args, **kwargs)

    def killTimer(self, *args, **kwargs):
        return self.mapTool.killTimer(*args, **kwargs)

    def metaObject(self, *args, **kwargs):
        return self.mapTool.metaObject(*args, **kwargs)

    def moveToThread(self, *args, **kwargs):
        return self.mapTool.moveToThread(*args, **kwargs)

    def objectName(self, *args, **kwargs):
        return self.mapTool.objectName(*args, **kwargs)

    def parent(self, *args, **kwargs):
        return self.mapTool.parent(*args, **kwargs)

    def property(self, *args, **kwargs):
        return self.mapTool.property(*args, **kwargs)

    def pyqtConfigure(self, *args, **kwargs):
        return self.mapTool.pyqtConfigure(*args, **kwargs)

    def receivers(self, *args, **kwargs):
        return self.mapTool.receivers(*args, **kwargs)

    def removeEventFilter(self, *args, **kwargs):
        return self.mapTool.removeEventFilter(*args, **kwargs)

    def searchRadiusMM(self, *args, **kwargs):
        return self.mapTool.searchRadiusMM(*args, **kwargs)

    def searchRadiusMU(self, *args, **kwargs):
        return self.mapTool.searchRadiusMU(*args, **kwargs)

    def sender(self, *args, **kwargs):
        return self.mapTool.sender(*args, **kwargs)

    def senderSignalIndex(self, *args, **kwargs):
        return self.mapTool.senderSignalIndex(*args, **kwargs)

    def setAction(self, *args, **kwargs):
        return self.mapTool.setAction(*args, **kwargs)

    def setButton(self, *args, **kwargs):
        return self.mapTool.setButton(*args, **kwargs)

    def setCursor(self, *args, **kwargs):
        return self.mapTool.setCursor(*args, **kwargs)

    def setObjectName(self, *args, **kwargs):
        return self.mapTool.setObjectName(*args, **kwargs)

    def setParent(self, *args, **kwargs):
        return self.mapTool.setParent(*args, **kwargs)

    def setProperty(self, *args, **kwargs):
        return self.mapTool.setProperty(*args, **kwargs)

    def signalsBlocked(self, *args, **kwargs):
        return self.mapTool.signalsBlocked(*args, **kwargs)

    def startTimer(self, *args, **kwargs):
        return self.mapTool.startTimer(*args, **kwargs)

    def thread(self, *args, **kwargs):
        return self.mapTool.thread(*args, **kwargs)

    def timerEvent(self, *args, **kwargs):
        return self.mapTool.timerEvent(*args, **kwargs)

    def toCanvasCoordinates(self, *args, **kwargs):
        return self.mapTool.toCanvasCoordinates(*args, **kwargs)

    def toLayerCoordinates(self, *args, **kwargs):
        return self.mapTool.toLayerCoordinates(*args, **kwargs)

    def toMapCoordinates(self, *args, **kwargs):
        return self.mapTool.toMapCoordinates(*args, **kwargs)

    def toMapCoordinatesV2(self, *args, **kwargs):
        return self.mapTool.toMapCoordinatesV2(*args, **kwargs)

    def toolName(self, *args, **kwargs):
        return self.mapTool.toolName(*args, **kwargs)

    def tr(self, *args, **kwargs):
        return self.mapTool.tr(*args, **kwargs)

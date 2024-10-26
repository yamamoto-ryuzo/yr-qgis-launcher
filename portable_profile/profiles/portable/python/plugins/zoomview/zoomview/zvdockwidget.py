import types
from os.path import join
from qgis.gui import *
from qgis.core import *
from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtCore import *

from zoomview.zoomview import debug
from zoomview.zoomview.zvmapcanvasmaptoolwrapper import ZvMapCanvasMapToolWrapper
from . import ui
from .zvmaptool import ZvMapTool


class ZvDockWidget(QgsDockWidget):
    iface = None
    sigPointChanged = pyqtSignal(QgsPointXY)

    def __init__(self, parent=None):
        QgsDockWidget.__init__(self, parent)

        uic.loadUi(join(ui.path, 'dockwidget.ui'), self)
        self._initUi()

        self.mapToolZoom = ZvMapTool(zoomCanvas=self.ui.mapCanvas(), mapCanvas=self.mapCanvas(), iface=self.iface)
        self.ui.mapCanvas().setMapTool(self.mapToolZoom)
        try:  # QGIS
            self.iface.actionPan().trigger()
        except:  # Test
            # wait a moment until the event loop has startet
            QTimer.singleShot(1000, lambda: self.mapCanvas().setMapTool(QgsMapToolPan(self.mapCanvas())))

        self._oldZoomCenter = self._oldZoomScale = None
        self._connectSignals()

    def _initUi(self):
        self.ui = _Ui(self)

    def _connectSignals(self):
        self.visibilityChanged.connect(self.onVisibilityChanged)
        self.sigPointChanged.connect(self.onPointChanged)

        # layer tree
        # QgsProject.instance().layerTreeRoot().visibilityChanged.connect(self.onLayerTreeVisibilityChanged)

        # map canvases
        self.mapCanvas().scaleChanged.connect(self.onImageScaleChanged)
        self.mapCanvas().mapToolSet.connect(self.onMapCanvasMapToolSet)
        self.mapCanvas().layersChanged.connect(self.onMapCanvasLayersChanged)
        self.mapCanvas().canvasColorChanged.connect(self.onCanvasColorChanged)
        # self.mapCanvas().renderComplete.connect(self.ui.mapCanvas().refresh)
        self.ui.mapCanvas().scaleChanged.connect(self.onZoomScaleChanged)
        self.ui.mapCanvas().extentsChanged.connect(self.onZoomExtentsChanged)

        # widgets
        self.ui.showRectangle().toggled.connect(self.plotMapCanvasItems)
        self.ui.showCrosshair().toggled.connect(self.plotMapCanvasItems)
        self.ui.zoomFactor().valueChanged.connect(self.updateZoomExtent)

        # map tools
        self.mapToolZoom.sigPointChanged.connect(lambda p: self.sigPointChanged.emit(p))

    def onCanvasColorChanged(self):
        self.ui.mapCanvas().setCanvasColor(self.mapCanvas().canvasColor())

    def onVisibilityChanged(self, visible):
        mapTool = self.mapCanvas().mapTool()
        if visible:
            # wrap the current map tool
            self.mapCanvas().setMapTool(mapTool=mapTool)
        else:
            # unwrap the current map tool
            if isinstance(mapTool, ZvMapCanvasMapToolWrapper):
                mapTool = mapTool.mapTool
                self.mapCanvas().setMapTool(mapTool=mapTool)

    # def onLayerTreeVisibilityChanged(self, node):
    #    print('onLayerTreeVisibilityChanged')

    def onMapCanvasLayersChanged(self):
        if debug:
            print('onMapCanvasLayersChanged')
        self.syncMapCanvas()

    def onMapCanvasMapToolSet(self):
        if debug:
            print('onMapCanvasMapToolSet')
        self.plotMapCanvasItems()
        mapTool = self.mapCanvas().mapTool()

        if not self.isVisible():
            return
        if not isinstance(mapTool, QgsMapTool):
            return
        if isinstance(mapTool, ZvMapCanvasMapToolWrapper):
            return

        # set central map tool
        wrappedMapTool = ZvMapCanvasMapToolWrapper(mapTool=mapTool, canvas=self.mapCanvas())
        self.mapCanvas().setMapTool(wrappedMapTool)
        wrappedMapTool.sigPointChanged.connect(self.onPointChanged)

        # set zoom map tool cursor
        if isinstance(mapTool, (QgsMapToolPan, QgsMapToolZoom)):
            self.ui.mapCanvas().setCursor(self.mapToolZoom._cursor)
        else:
            self.ui.mapCanvas().setCursor(self.mapCanvas().cursor())

    def onImageScaleChanged(self):
        if debug:
            print('onImageScaleChanged')
        self.updateZoomExtent()

    def setZoomScale(self, zoomScale):
        if debug:
            print('setZoomScale', zoomScale)
        zoomFactor = self.mapCanvas().scale() / zoomScale
        self.setZoomFactor(zoomFactor=zoomFactor)
        self._oldZoomScale = zoomScale

    def onZoomScaleChanged(self, zoomScale):

        if self.mapToolZoom._synchronized:
            return  # do not change zoom factor while programmatically triggering a mouse click

        if debug:
            print('onZoomScaleChanged')
        if zoomScale == 1.:
            return  # edge case
        self.setZoomScale(zoomScale=zoomScale)

    def setZoomFactor(self, zoomFactor):
        if debug:
            print('setZoomFactor', zoomFactor)

        max = self.ui.zoomFactor().maximum()
        self.ui.mapCanvas().blockSignals(True)
        if zoomFactor >= 1 and zoomFactor <= max:
            self.ui.zoomFactor().setValue(int(round(zoomFactor)))
        else:
            self.ui.mapCanvas().setCenter(self.point())
            if zoomFactor < 1:
                self.ui.mapCanvas().zoomScale(scale=self.mapCanvas().scale())
            else:
                self.ui.mapCanvas().zoomScale(scale=self.mapCanvas().scale() / max)
                self.ui.zoomFactor().setValue(max)
        self.ui.mapCanvas().blockSignals(False)

    def onZoomExtentsChanged(self):
        if debug:
            print('onZoomExtentsChanged')

        zoomScale = self.ui.mapCanvas().scale()
        if zoomScale != self._oldZoomScale:
            self.onZoomScaleChanged(zoomScale=zoomScale)
            self.plotMapCanvasItems()
            return

        point = self.ui.mapCanvas().center()
        if point != self._oldZoomCenter:
            self._oldZoomCenter = point
            self.mapToolZoom.setPoint(point=point)

    def onPointChanged(self, point):
        if debug:
            print('onPointChanged')
        self.mapToolZoom.setPoint(point=point)
        self.plotMapCanvasItems()
        self.updateCoordinateWidget()
        self.ui.mapCanvas().refresh()

    def point(self):
        return self.mapToolZoom.point()

    def syncMapCanvas(self):
        if self.mapCanvas().layers() != self.ui.mapCanvas().layers():
            if debug:
                print('syncMapCanvas: layers')
            self.ui.mapCanvas().setLayers(self.mapCanvas().layers())

        if self.mapCanvas().mapSettings().destinationCrs() != self.ui.mapCanvas().mapSettings().destinationCrs():
            if debug:
                print('syncMapCanvas: crs')
            self.ui.mapCanvas().setDestinationCrs(self.mapCanvas().mapSettings().destinationCrs())
            self.ui.mapCanvas().setExtent(self.ui.mapCanvas().fullExtent())

    def updateZoomExtent(self):
        if debug:
            print('updateZoomExtent')

        point = self.point()
        self.syncMapCanvas()
        zoomFactor = self.ui.zoomFactor().value()
        scaleCentral = self.mapCanvas().scale()
        scale = scaleCentral / zoomFactor

        self.ui.mapCanvas().blockSignals(True)
        self.ui.mapCanvas().setCenter(point)
        self.ui.mapCanvas().zoomScale(scale)
        self.ui.mapCanvas().blockSignals(False)

        self.plotMapCanvasItems()

    def plotMapCanvasItems(self):
        self.mapToolZoom.plotMapCanvasItems(showCrosshair=self.ui.showCrosshair().isChecked() and self.isVisible(),
            showRectangle=self.ui.showRectangle().isChecked() and self.isVisible())

    def updateCoordinateWidget(self):
        text = '{}, {}'.format(round(self.point().x(), 4), round(self.point().y(), 4))
        self.ui.point().setPlainText(text)

    def mapCanvas(self):
        mapCanvas = self.iface.mapCanvas()
        assert isinstance(mapCanvas, QgsMapCanvas)
        return mapCanvas


class _Ui(object):

    def __init__(self, obj):
        self.obj = obj

    def mapCanvas(self):
        assert isinstance(self.obj._mapCanvas, QgsMapCanvas)
        return self.obj._mapCanvas

    def showCrosshair(self):
        assert isinstance(self.obj._showCrosshair, QToolButton)
        return self.obj._showCrosshair

    def showRectangle(self):
        assert isinstance(self.obj._showRectangle, QToolButton)
        return self.obj._showRectangle

    def zoomFactor(self):
        assert isinstance(self.obj._zoomFactor, QSpinBox)
        return self.obj._zoomFactor

    def point(self):
        assert isinstance(self.obj._point, QPlainTextEdit)
        return self.obj._point

from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.gui import *
from qgis.core import *

from zoomview.zoomview import debug


class ZvMapTool(QgsMapTool):
    sigPointChanged = pyqtSignal(QgsPointXY)

    def __init__(self, zoomCanvas, mapCanvas, iface):
        assert isinstance(zoomCanvas, QgsMapCanvas)
        assert isinstance(iface, QgisInterface)
        QgsMapTool.__init__(self, zoomCanvas)
        self.iface = iface
        self._mapCanvas = mapCanvas
        self._cursor = QCursor(Qt.CrossCursor)
        self._point = QgsPointXY(0, 0)
        self._synchronized = False
        self._oldCenter = None
        self._oldScale = None

        # init map canvas items
        self._crosshairItem = QgsVertexMarker(mapCanvas=zoomCanvas)
        self._crosshairItem.setColor(QColor(255, 0, 0))
        self._crosshairItem.setIconSize(31)
        self._crosshairItem.setIconType(QgsVertexMarker.ICON_CROSS)
        self._crosshairItem.setPenWidth(1)

        try:
            self._rectangleItem = QgsRubberBand(mapCanvas=mapCanvas, geometryType=3)  # QGIS < 3.30
        except Exception:
            self._rectangleItem = QgsRubberBand(mapCanvas=mapCanvas, geometryType=Qgis.GeometryType.Unknown)

        self._rectangleItem.setStrokeColor(QColor(255, 0, 0))
        self._rectangleItem.setColor(QColor(255, 0, 0))
        self._rectangleItem.setFillColor(QColor(0, 0, 0, 0))
        self._rectangleItem.setWidth(1)

        self._dotItem = QgsVertexMarker(mapCanvas=mapCanvas)
        self._dotItem.setColor(QColor(255, 0, 0))
        self._dotItem.setIconSize(2)
        self._dotItem.setIconType(QgsVertexMarker.ICON_CIRCLE)
        self._dotItem.setPenWidth(2)

    def mapCanvas(self):
        assert isinstance(self._mapCanvas, QgsMapCanvas)
        return self._mapCanvas

    def wrappedMapTool(self):
        mapTool = self.mapCanvas().mapTool().mapTool
        assert isinstance(mapTool, QgsMapTool)
        return mapTool

    def activate(self):
        QgsMapTool.activate(self)
        self.canvas().setCursor(self._cursor)
        self.plotMapCanvasItems()

    def deactivate(self):
        QgsMapTool.deactivate(self)
        self.plotMapCanvasItems(showRectangle=False, showCrosshair=False)

    def isZoomTool(self):
        return False

    def onPointChanged(self, point):
        self.plotMapCanvasItems()

    def setPoint(self, point):
        if self._point != point:
            if debug:
                print('setPointZoom')
            self._point = point
            self.canvas().setCenter(point)
            self.sigPointChanged.emit(point)

    def triggerPointClicked(self, point, type, button):
        assert isinstance(point, QgsPointXY)
        pixel = self.canvas().getCoordinateTransform().transform(point)
        event2 = QgsMapMouseEvent(mapCanvas=self.canvas(),
            type=type,
            pos=QPoint(round(pixel.x()), round(pixel.y())),
            button=button)
        event2.originalMapPoint = lambda: point
        event2.mapPoint = lambda: point
        event2.snapPoint = lambda: point
        self.canvasPressEvent(event2)
        self.canvasReleaseEvent(event2)

    def point(self):
        assert isinstance(self._point, QgsPointXY)
        return self._point

    def plotMapCanvasItems(self, showRectangle=True, showCrosshair=True):

        self._crosshairItem.setCenter(self._point)
        self._dotItem.setCenter(self._point)
        self._rectangleItem.setToGeometry(QgsGeometry.fromRect(self.canvas().extent()), None)

        self._crosshairItem.setVisible(showCrosshair)
        self._dotItem.setVisible(showRectangle)
        self._rectangleItem.setVisible(showRectangle)

    def keyReleaseEvent(self, event):
        assert isinstance(event, QKeyEvent)
        if debug:
            print('keyReleaseEvent')

        layer = self.iface.activeLayer()
        if isinstance(layer, QgsRasterLayer):
            pX, pY = self.point().x(), self.point().y()
            resX = layer.rasterUnitsPerPixelX()
            resY = layer.rasterUnitsPerPixelY()
            if event.key() == Qt.Key_A:
                pX -= resX
            if event.key() == Qt.Key_D:
                pX += resX
            if event.key() == Qt.Key_W:
                pY += resY
            if event.key() == Qt.Key_S:
                pY -= resY
            self.triggerPointClicked(point=QgsPointXY(pX, pY), type=5, button=Qt.LeftButton)

        self.mapCanvas().mapTool().keyReleaseEvent(event)

    # delegate all events to the map canvas map tool
    def _convertEvent(self, event):
        if isinstance(event, QgsMapMouseEvent):
            point = event.originalMapPoint()  # from map coordinates ...
            pixel = self._mapCanvas.getCoordinateTransform().transform(point)  # ... to device coordinates (inplace)
            event2 = QgsMapMouseEvent(mapCanvas=self._mapCanvas,
                type=event.type(),
                pos=QPoint(int(round(pixel.x())), int(round(pixel.y()))),
                button=event.button(),
                buttons=event.buttons(),
                modifiers=event.modifiers())
            event2.originalMapPoint = lambda: point
            event2.mapPoint = lambda: point
            event2.snapPoint = lambda: point
            return event2
        else:
            return event

    def _syncCanvas(self):
        # sync map view scale and center with zoom view
        self._synchronized = True
        self._oldScale = self.mapCanvas().scale()
        self._oldCenter = self.mapCanvas().center()
        self.mapCanvas().blockSignals(True)
        self.mapCanvas().zoomScale(self.canvas().scale())
        self.mapCanvas().setCenter(self.canvas().center())
        self.mapCanvas().blockSignals(False)

    def _restoreCanvas(self):
        self.mapCanvas().blockSignals(True)
        self.mapCanvas().zoomScale(self._oldScale)
        self.mapCanvas().setCenter(self._oldCenter)
        self.mapCanvas().blockSignals(False)
        self._synchronized = False
        self.canvas().refresh()
        self.plotMapCanvasItems()

    def canvasReleaseEvent(self, event):

        if isinstance(self.wrappedMapTool(), (QgsMapToolPan, QgsMapToolZoom)):
            return

        if self.mapCanvas().mapTool() is not None:
            self._syncCanvas()
            self.mapCanvas().mapTool().canvasReleaseEvent(self._convertEvent(event))
            self._restoreCanvas()

    # def canvasMoveEvent(self, event):
    #    if self.mapCanvas().mapTool() is not None:
    #        self._syncCanvas()
    #        self.mapCanvas().mapTool().canvasMoveEvent(self._convertEvent(event))
    #        self._restoreCanvas()

    def canvasPressEvent(self, event):

        if isinstance(self.wrappedMapTool(), (QgsMapToolPan, QgsMapToolZoom)):
            self.setPoint(point=event.originalMapPoint())
            return

        if self.mapCanvas().mapTool() is not None:
            self._syncCanvas()
            self.mapCanvas().mapTool().canvasPressEvent(self._convertEvent(event))
            self._restoreCanvas()

        # self.setPoint(point=event.originalMapPoint())

    def canvasDoubleClickEvent(self, event):
        if self.mapCanvas().mapTool() is not None:
            self._syncCanvas()
            self.mapCanvas().mapTool().canvasDoubleClickEvent(self._convertEvent(event))
            self._restoreCanvas()

    def customEvent(self, event):
        if self.mapCanvas().mapTool() is not None:
            self.mapCanvas().mapTool().customEvent(self._convertEvent(event))

    def gestureEvent(self, event):
        if self.mapCanvas().mapTool() is not None:
            self.mapCanvas().mapTool().gestureEvent(self._convertEvent(event))

    def keyPressEvent(self, event):
        if self.mapCanvas().mapTool() is not None:
            self.mapCanvas().mapTool().keyPressEvent(self._convertEvent(event))

    def timerEvent(self, event):
        if self.mapCanvas().mapTool() is not None:
            self.mapCanvas().mapTool().timerEvent(self._convertEvent(event))

    def wheelEvent(self, event):
        if self.mapCanvas().mapTool() is not None:
            self.mapCanvas().mapTool().wheelEvent(self._convertEvent(event))

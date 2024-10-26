from qgis.PyQt.QtCore import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtGui import *
from qgis.gui import *
from qgis.core import *

from enmapbox.testing import initQgisApplication
from enmapbox import EnMAPBox

#import qgisresources.images
#qgisresources.images.qInitResources()

# start application and open test dataset
qgsApp = initQgisApplication()
enmapBox = EnMAPBox(None)
enmapBox.run()
enmapBox.ui.hide()

testRaster = True
testTimeseries = not testRaster

layer = QgsRasterLayer(r'C:\Work\data\jan_knorn\Sitzung_7\Daten\LC81930232015276.bsq', baseName='LC81930232015276')
layers = [layer]

QgsProject.instance().addMapLayers(layers)

class TestInterface(QgisInterface):

    def __init__(self):
        QgisInterface.__init__(self)

        self.ui = QMainWindow()
        self.ui.setWindowTitle('QGIS')
        self.ui.setWindowIcon(QIcon(r'C:\source\QGIS3-master\images\icons\qgis_icon.svg'))
        self.ui.resize(QSize(1500, 750))
        self.ui.canvas = QgsMapCanvas()
        self.ui.setCentralWidget(self.ui.canvas)
        self.ui.show()
        self.ui.canvas.setLayers(layers)
        self.ui.canvas.setDestinationCrs(layer.crs())
        self.ui.canvas.setExtent(layer.extent())

    def addDockWidget(self, area, dockwidget):
        self.ui.addDockWidget(area, dockwidget)

    def mapCanvas(self):
        assert isinstance(self.ui.canvas, QgsMapCanvas)
        return self.ui.canvas

    def activeLayer(self):
        return layer

def test_ZvPlugin():
    from zoomview.zoomview.plugin import ZvPlugin

    iface = TestInterface()

    rdpPlugin = ZvPlugin(iface=iface)
    rdpPlugin.initGui()

    iface.mapCanvas().destinationCrsChanged.emit()
    iface.mapCanvas().layersChanged.emit()

    qgsApp.exec_()

if __name__ == '__main__':
    test_ZvPlugin()

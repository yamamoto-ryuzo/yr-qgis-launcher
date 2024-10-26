from os.path import join, dirname
from qgis.gui import *
from qgis.core import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from .zvdockwidget import ZvDockWidget


class ZvInterface(QObject):
    sigPointChanged = pyqtSignal(QgsPointXY)

    INSTANCE = None
    pluginName = 'ZoomView'
    pluginId = pluginName.replace(' ', '')

    def __init__(self, iface, parent=None):

        if self.INSTANCE is not None:
            raise Exception('{} already initialized.'.format(self.pluginName))
        else:
            ZvInterface.INSTANCE = self

        QObject.__init__(self, parent)
        assert isinstance(iface, QgisInterface)
        self.iface = iface
        self._initUi()
        self.integratePlugin()

    def _initUi(self):
        ZvDockWidget.iface = self.iface
        self.ui = ZvDockWidget(parent=self.parent())
        self.ui.setWindowIcon(self.icon())
        self._oldPoint = QgsPointXY()
        self.ui.sigPointChanged.connect(self.onDockPointChanged)

    def integratePlugin(self):
        if isinstance(self.iface, QgisInterface):
            self.action = QAction(self.icon(), self.pluginName.replace(' ', ''), self.iface.mainWindow())
            self.action.triggered.connect(self.toggleVisibility)
            self.iface.addToolBarIcon(self.action)

    def unloadPlugin(self):
        self.ui.close()
        self.iface.removeToolBarIcon(self.action)

    @classmethod
    def instance(cls):
        if cls.INSTANCE is None:
            raise Exception('{} not initialized.'.format(cls.pluginName))

        assert isinstance(cls.INSTANCE, ZvInterface)
        return cls.INSTANCE

    def pluginFolder(self):
        return join(dirname(__file__), '..')

    def icon(self):
        return QIcon(join(self.pluginFolder(), 'icon.svg'))

    def toggleVisibility(self):
        self.ui.setVisible(not self.ui.isVisible())
        self.ui.ui.zoomFactor().setValue(5)

    def show(self):
        self.ui.show()

    def onDockPointChanged(self, point):
        if point != self._oldPoint:
            self._oldPoint = point
            self.sigPointChanged.emit(point)

from __future__ import absolute_import
from qgis.gui import QgisInterface, QtCore
from .zvinterface import ZvInterface


class ZvPlugin(object):

    def __init__(self, iface):
        assert isinstance(iface, QgisInterface)
        self.iface = iface

    def initGui(self):
        self.zvInterface = ZvInterface(self.iface)
        self.zvInterface.show()
        self.iface.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.zvInterface.ui)

    def unload(self):
        self.zvInterface.unloadPlugin()
        self.iface.removeDockWidget(self.zvInterface.ui)

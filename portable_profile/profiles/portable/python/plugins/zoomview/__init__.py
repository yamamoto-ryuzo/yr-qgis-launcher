from .zoomview.plugin import ZvPlugin


def classFactory(iface):
    return ZvPlugin(iface)

def zvInterface():
    from zoomview.zoomview.zvinterface import ZvInterface
    return ZvInterface.instance()

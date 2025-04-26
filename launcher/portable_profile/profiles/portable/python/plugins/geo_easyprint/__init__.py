# -*- coding: utf-8 -*-


def name():
    return u"(GEO)EasyPrint"


def description():
    return u"デフォルトの印刷の操作が複雑なので、簡略化させた印刷プラグイン"


def version():
    return "Version 1.10"


def qgisMinimumVersion():
    return "1.7"


def icon():
    return "images/mActionFilePrint.png"


def classFactory(iface):
    from .easyprint import EasyPrint
    return EasyPrint(iface)

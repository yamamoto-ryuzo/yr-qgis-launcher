# -*- coding: utf-8 -*-
import math
import os

from qgis.PyQt import QtXml
from qgis.core import QgsMapLayer, QgsProject

from .layout import Layout
from .decoration import Decoration


def getPapersize(format):
    height = 297
    width = 210

    preffilename = (
        os.path.dirname(os.path.dirname(__file__)) + "/preferences/preferences.xml"
    )
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
                if sube.toElement().text() == format:
                    height = sube.toElement().attribute("height", "")
                    width = sube.toElement().attribute("width", "")
                    try:
                        float(height)
                        float(width)
                        return height, width
                    except ValueError:
                        pass
            #                        print("height/width float error")
            sube = sube.nextSibling()
        n = n.nextSibling()

    return height, width


def getLayouts():
    layouts = []

    layoutsfilename = (
        os.path.dirname(os.path.dirname(__file__)) + "/layouts/layouts.xml"
    )
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
                id = node.toElement().attribute("id", "")
                layout = Layout(id)
                ori = node.toElement().attribute("orientation", "")
                layout.setOrientation(ori)
                # # Read a single layout.
                layoutnode = node.toElement().firstChild()
                while not layoutnode.isNull():
                    if layoutnode.toElement() and layoutnode.nodeName() == "margins":
                        # # Read margins.
                        marginnode = layoutnode.toElement().firstChild()
                        while not marginnode.isNull():
                            try:
                                margins.append(float(marginnode.toElement().text()))
                            #                                print(marginnode.toElement().text())
                            except ValueError:
                                margins.append(float(0.0))
                            marginnode = marginnode.nextSibling()
                        #                        print(margins)
                        layout.setMargins(margins)

                    elif (
                        layoutnode.toElement()
                        and layoutnode.nodeName() == "decorations"
                    ):
                        # # Read decorations.
                        deconode = layoutnode.toElement().firstChild()
                        while not deconode.isNull():
                            type = deconode.toElement().attribute("type", "")
                            decoration = Decoration(type)

                            affinity = deconode.toElement().attribute("affinity", "")
                            offset_x = deconode.toElement().attribute("offset_x", "")
                            offset_y = deconode.toElement().attribute("offset_y", "")
                            height = deconode.toElement().attribute("height", "")
                            width = deconode.toElement().attribute("width", "")
                            fontsize = deconode.toElement().attribute("font-size", "")
                            fontfamily = deconode.toElement().attribute(
                                "font-family", ""
                            )
                            rotation = deconode.toElement().attribute("rotation", "")

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

                            if fontfamily != None:
                                decoration.setFontFamily(fontfamily)

                            try:
                                decoration.setOffsetX(float(offset_x))
                            except ValueError:
                                pass
                            #                                print("float offset_x error")

                            try:
                                decoration.setOffsetY(float(offset_y))
                            except ValueError:
                                pass
                            #                                print("float offset_y error")

                            try:
                                decoration.setHeight(float(height))
                            except ValueError:
                                decoration.setHeight(float(0.0))
                            #                                print("float height error or not found.")

                            try:
                                decoration.setWidth(float(width))
                            except ValueError:
                                decoration.setWidth(float(0.0))
                            #                                print("float width error or not found.")

                            try:
                                decoration.setFontSize(float(fontsize))
                            except ValueError:
                                pass
                            #                                print("float fontsize error or not found.")

                            try:
                                decoration.setRotation(float(rotation))
                            except ValueError:
                                pass
                            #                                print("float rotation error or not found.")

                            if (
                                type == "text"
                                or type == "date"
                                or type == "scaletext"
                                or type == "legend"
                                or type == "copyright"
                                or type == "person"
                                or type == "crsdescription"
                            ):
                                text = deconode.toElement().text()
                                decoration.setText(text)

                            if (
                                type == "picture"
                                or type == "northarrow"
                                or type == "legendpic"
                            ):
                                pic = deconode.toElement().text()
                                decoration.setPicture(pic)

                            layout.addDecoration(decoration)

                            deconode = deconode.nextSibling()

                    layoutnode = layoutnode.nextSibling()
                #                print(layout.getMargins())
                layouts.append(layout)

            node = node.nextSibling()

    except IOError:
        print("error opening preferences.xml")

    return layouts


# Rotates a geometry.
# (c) Stefan Ziegler
def rotate(geom, point, angle):

    if angle == 0 or angle == 2 * math.pi or angle == -2 * math.pi:
        return geom

    type = geom.wkbType()

    if type == 1:
        p0 = geom.asPoint()
        p1 = QgsPoint(p0.x() - point.x(), p0.y() - point.y())
        p2 = rotatePoint(p1, angle)
        p3 = QgsPoint(point.x() + p2.x(), point.y() + p2.y())
        return QgsGeometry().fromPoint(p3)

    elif type == 2:
        coords = []
        for i in geom.asPolyline():
            p1 = QgsPoint(i.x() - point.x(), i.y() - point.y())
            p2 = rotatePoint(p1, angle)
            p3 = QgsPoint(point.x() + p2.x(), point.y() + p2.y())
            coords.append(p3)
        return QgsGeometry().fromPolyline(coords)

    elif type == 3:
        coords = []
        ring = []
        for i in geom.asPolygon():
            for k in i:
                p1 = QgsPoint(k.x() - point.x(), k.y() - point.y())
                p2 = rotatePoint(p1, angle)
                p3 = QgsPoint(point.x() + p2.x(), point.y() + p2.y())
                ring.append(p3)
            coords.append(ring)
            ring = []
        return QgsGeometry().fromPolygon(coords)

    elif type == 4:
        coords = []
        for i in geom.asMultiPoint():
            p1 = QgsPoint(i.x() - point.x(), i.y() - point.y())
            p2 = rotatePoint(p1, angle)
            p3 = QgsPoint(point.x() + p2.x(), point.y() + p2.y())
            coords.append(p3)
        return QgsGeometry().fromMultiPoint(coords)

    elif type == 5:
        coords = []
        singleline = []
        for i in geom.asMultiPolyline():
            for j in i:
                p1 = QgsPoint(j.x() - point.x(), j.y() - point.y())
                p2 = rotatePoint(p1, angle)
                p3 = QgsPoint(point.x() + p2.x(), point.y() + p2.y())
                singleline.append(p3)
            coords.append(singleline)
            singleline = []
        return QgsGeometry().fromMultiPolyline(coords)

    elif type == 6:
        coords = []
        ring = []
        for i in geom.asMultiPolygon():
            for j in i:
                for k in j:
                    p1 = QgsPoint(k.x() - point.x(), k.y() - point.y())
                    p2 = rotatePoint(p1, angle)
                    p3 = QgsPoint(point.x() + p2.x(), point.y() + p2.y())
                    ring.append(p3)
                coords.append(ring)
                ring = []
        return QgsGeometry().fromMultiPolygon([coords])

    else:
        QMessageBox.information(
            None, "Information", str("Vector type is not supported.")
        )
        return None


# Rotates a single point (centre 0/0).
# (c) Stefan Ziegler
def rotatePoint(point, angle):
    x = math.cos(angle) * point.x() - math.sin(angle) * point.y()
    y = math.sin(angle) * point.x() + math.cos(angle) * point.y()
    return QgsPoint(x, y)


# Return list of names of all layers in QgsMapLayerRegistry
# (c) Carson Farmer / fTools
#
def getLayerNames(vTypes, providerException=None):
    layermap = QgsProject.instance().mapLayers()
    layerlist = []
    if vTypes == "all":
        for name, layer in layermap.items():
            provider = None
            if "dataProvider" in dir(layer):
                provider = layer.dataProvider()
            # # Is this a bug??? I only get "None" as provider for a TIFF....???
            if provider is None:
                layerlist.append(unicode(layer.name()))
                continue
            providerName = provider.name()
            if providerName == providerException:
                continue
            else:
                layerlist.append(unicode(layer.name()))
    else:
        for name, layer in layermap.items():
            if layer.type() == QgsMapLayer.VectorLayer:
                if layer.geometryType() in vTypes:
                    layerlist.append(unicode(layer.name()))
            elif layer.type() == QgsMapLayer.RasterLayer:
                if "Raster" in vTypes:
                    layerlist.append(unicode(layer.name()))
    return layerlist


# Return QgsMapLayer from a layer name ( as string )
def getLayerByName(myName):
    layermap = QgsProject.instance().mapLayers()
    for name, layer in layermap.items():
        if layer.name() == myName:
            if layer.isValid():
                return layer
            else:
                return None


# Return QgsVectorLayer from a layer name ( as string )
# (c) Carson Farmer / fTools
def getVectorLayerByName(myName):
    layermap = QgsProject.instance().mapLayers()
    for name, layer in layermap.items():
        if layer.type() == QgsMapLayer.VectorLayer and layer.name() == myName:
            if layer.isValid():
                return layer
            else:
                return None

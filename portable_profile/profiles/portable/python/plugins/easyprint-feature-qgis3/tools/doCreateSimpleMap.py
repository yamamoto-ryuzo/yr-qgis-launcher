# -*- coding: utf-8 -*-
import math
import time
import os

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QBrush, QColor, QFont, QPen

from qgis.PyQt.QtWidgets import QToolBar
from qgis.core import (
    QgsProject,
    QgsPrintLayout,
    QgsRectangle,
    QgsLayoutItemMap,
    QgsLayoutItemMapGrid,
    QgsLayoutItemLabel,
    QgsLayoutItemPicture,
    QgsLayoutItemScaleBar,
    QgsLayoutPoint,
    QgsLayoutSize,
    QgsUnitTypes,
)

from . import utils


# from myToolBar import MyToolBar
# TODO: ScaleBarとどうように他のアイテム追加部分を関数に分離する


class CreateSimpleMap:
    def __init__(
        self,
        iface,
        printScale,
        printFormat,
        layoutIndex,
        titleString,
        subtitleString,
        personString,
        crsdesc,
        grid,
        legend,
        scalebar,
        copyright,
        cuttinglines,
        foldingmarks,
        overlapPercentage=0,
        overviewMap=False,
        adjacentTiles=None,
        exportPath=None,
        tileName=None,
        printRotation=0,
        background_color=Qt.white,
    ):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.printScale = printScale
        self.printFormat = printFormat
        self.paperheight, self.paperwidth = utils.getPapersize(self.printFormat)
        self.layoutIndex = layoutIndex
        self.titleString = titleString
        self.subtitleString = subtitleString
        self.personString = personString
        self.crsdesc = crsdesc
        self.grid = grid
        self.legend = legend
        self.scalebar = scalebar
        self.copyright = copyright
        self.cuttinglines = cuttinglines
        self.foldingmarks = foldingmarks
        self.overlapPercentage = overlapPercentage
        self.overviewMap = overviewMap
        self.adjacentTiles = adjacentTiles
        self.exportPath = exportPath
        self.tileName = tileName
        self.printRotation = printRotation
        self.background_color = background_color
        self.newMapExtent = None
        self.printer = None
        self.painter = None
        self.fileName = None
        self.plugin_dir = os.path.dirname(os.path.dirname(__file__))

        self.composerView = None
        self.composerViewWindowTitle = None
        self.composerViewIndex = None

        layouts = utils.getLayouts()
        self.layout = layouts[0]
        # layout = layouts[self.layoutIndex]

        margins = self.layout.getMargins()
        self.margin_top = margins["margin-top"]
        self.margin_right = margins["margin-right"]
        self.margin_bottom = margins["margin-bottom"]
        self.margin_left = margins["margin-left"]

        self.orientation = self.layout.getOrientation()
        if self.orientation == "landscape":
            self.paperheight, self.paperwidth = self.paperwidth, self.paperheight

    def setOutputFileName(self, fileName):
        self.fileName = fileName

    def setPrinterPainter(self, printer, painter):
        self.printer = printer
        self.painter = painter

    def getMapExtent(self):
        return self.newMapExtent

    def self_hidenshowDock(self, composerView):
        cw = composerView.composerWindow()
        tb = cw.findChildren(QDockWidget)
        if tb:
            for t in tb:
                t.hide()

    def self_removeToolBar(self, composerView):
        # hide Qgis1.7.0 default toolbar
        cw = composerView.composerWindow()

        tbs = cw.findChildren(QToolBar)
        if tbs:
            for tb in tbs:
                tb.hide()

    def run(self):
        # QObject.connect(self, SIGNAL("selectedItemChanged(QgsComposerItem *)"), self.self_selectedItemChanged)
        headerHeight = 0
        footerHeight = 0

        project = QgsProject.instance()
        manager = project.layoutManager()
        composer_names = [com.name() for com in manager.printLayouts()]
        name = u"コンポーザー{number}"
        n = 1
        while True:
            composer_name = name.format(number=n)
            if not composer_name in composer_names:
                break
            n += 1
        composer = QgsPrintLayout(project)
        composer.initializeDefaults()
        composer.setName(composer_name)

        manager.addLayout(composer)
        # FIXME: LayoutDesignerの表示調整
        """
        self.self_hidenshowDock(composer)
        self.self_removeToolBar(composer)
        toolbar = composerView.composerWindow().findChild(QToolBar, "myToolBar")
        if toolbar:
            toolbar.setVisible(True)
            toolbar.show()
        """
        pages = composer.pageCollection()
        page = pages.page(0)
        size = QgsLayoutSize(float(self.paperwidth), float(self.paperheight))
        page.setPageSize(size)

        # Cutting lines.
        if self.cuttinglines:
            self.cuttingLines(composer)

        # Folding marks.
        if self.foldingmarks:
            self.foldingMarks(composer)

        decorations = self.layout.getDecorations()
        self.create_decoration_items(composer, decorations)
        return composer

    def create_decoration_items(self, composer, decorations):
        for decoration in decorations:
            self.create_decoration_item(composer, decoration)

    def create_title_item(self, composer, decoration, offset_x=0, offset_y=0):
        option = decoration.getType()
        titleFont = QFont(decoration.getFontFamily(), decoration.getFontSize())

        if option == "title":
            titleFont.setBold(True)
        item = QgsLayoutItemLabel(composer)
        item.setFont(titleFont)

        if option == "title":
            item.setText(self.titleString)
        elif option == "subtitle":
            item.setText(self.subtitleString)
        elif option == "person":
            item.setText(decoration.getText() + self.personString)

        item.setMargin(1.0)

        item.setZValue(30)
        if decoration.getAffinityX() == "center":
            offset_x = offset_x - item.boundingRect().width() * 0.5
        point = QgsLayoutPoint(self.margin_left + offset_x, self.margin_top + offset_y)
        item.adjustSizeToText()
        item.setReferencePoint(item.UpperMiddle)
        item.attemptMove(point)
        if item.text():
            return item

    def create_text_item(self, composer, decoration, offset_x=0, offset_y=0):
        option = decoration.getType()

        textFont = QFont(decoration.getFontFamily(), decoration.getFontSize())
        item = QgsLayoutItemLabel(composer)
        item.setFont(textFont)
        item.setText(decoration.getText())
        if decoration.getWidth() > 0:
            item.setRect(0, 0, decoration.getWidth(), decoration.getHeight())
        else:
            item.adjustSizeToText()

        item.setFrameEnabled(0)
        item.setMargin(0)
        brush = QBrush()
        brush.setStyle(Qt.NoBrush)
        brush.setColor(Qt.white)
        item.setBrush(brush)
        item.setZValue(20)
        item.setItemPosition(self.margin_left + offset_x, self.margin_top + offset_y)

        if decoration.getRotation() != 0:
            item.setRotation(decoration.getRotation())

        if option == "copyright" and not copyright:
            return
        return item

    def create_map_item(self, composer, decoration, offset_x=0, offset_y=0):
        composerMap = QgsLayoutItemMap(composer)
        composerMap.setRect(20, 20, 20, 20)
        composerMap.setExtent(self.canvas.extent())

        scale = float(self.printScale)
        mapWidth = float(self.paperwidth) - (
            self.margin_right + self.margin_left + (offset_x)
        )
        # mapWidth = float(self.paperwidth) - (headerWidth+margin_right+margin_left+(offset_x-headerWidth))
        mapHeight = float(self.paperheight) - self.margin_top - self.margin_bottom

        point = QgsLayoutPoint(
            self.margin_left + offset_x,
            self.margin_top + offset_y,
            QgsUnitTypes.LayoutMillimeters,
        )
        composerMap.attemptMove(point)
        size = QgsLayoutSize(mapWidth, mapHeight, QgsUnitTypes.LayoutMillimeters)
        composerMap.attemptResize(size)

        project = QgsProject.instance()
        crs = project.crs()
        projectEPSG = crs.toProj4()
        if str.find(str(projectEPSG), "+proj=longlat") >= 0:
            composerMap.setScale(scale)  # Does not center correctly?
        else:
            rect = self.getMapExtentFromMapCanvas(mapWidth, mapHeight, scale)
            composerMap.setExtent(rect)

        pen = QPen()
        pen.setWidthF(0.2)
        pen.setJoinStyle(Qt.MiterJoin)
        composerMap.setPen(pen)
        composerMap.setBackgroundColor(self.background_color)

        composerMap.setFrameEnabled(True)
        # FIXME: QGIS3
        # composerMap.updateCachedImage()
        # composerMap.setPreviewMode(1)
        # composerMap.setLocked(True)

        if self.grid:
            grid_item = QgsLayoutItemMapGrid("グリッド", composerMap)
            map_scale = composerMap.scale()
            if not math.isnan(map_scale):
                interval = self.getGridInterval(map_scale)

                grid_item.setIntervalX(interval)
                grid_item.setIntervalY(interval)
            grid_item.setEnabled(True)
            grid_item.setStyle(1)
            grid_item.setAnnotationEnabled(True)
            gridFont = QFont(decoration.getFontFamily(), 6)
            gridFont.setItalic(True)
            grid_item.setAnnotationFont(gridFont)
            grid_item.setAnnotationPrecision(0)
            grid_item.setAnnotationFrameDistance(2)
            grid_item.setGridLineWidth(0.1)

            grids = composerMap.grids()
            grids.addGrid(grid_item)
        return composerMap

    def create_legend_item(self, composer, decoration, offset_x=0, offset_y=0):
        legendFont = QFont(decoration.getFontFamily(), decoration.getFontSize())
        groupFont = QFont(decoration.getFontFamily(), decoration.getFontSize() - 1)
        layerFont = QFont(decoration.getFontFamily(), decoration.getFontSize() - 2)
        itemFont = QFont(decoration.getFontFamily(), decoration.getFontSize() - 2)
        item = QgsLayoutItemLegend(composer)
        item.setTitle(decoration.getText())
        item.adjustBoxSize()

        # item.setItemPosition(margin_left + offset_x, margin_top + offset_y)
        item.setItemFont(itemFont)
        item.setLayerFont(layerFont)
        try:
            item.setGroupFont(groupFont)
        except:
            print("EASYPRINT: old qgis version...")
        item.setTitleFont(legendFont)
        item.setSymbolWidth(6)
        item.setSymbolHeight(3)
        item.setLayerSpace(2)
        item.setSymbolSpace(1.5)
        item.setBoxSpace(0)
        item.setPositionLock(1)
        item.setFrameEnabled(0)
        item.setZValue(30)
        brush = QBrush()
        brush.setStyle(Qt.NoBrush)
        brush.setColor(Qt.white)
        item.setBrush(brush)
        return item

    def create_legendpic_item(self, composer, decoration, offset_x=0, offset_y=0):
        item = QgsLayoutItemPicture(composer)
        qgs_dir = os.path.dirname(QgsProject.instance().fileName())
        pic = qgs_dir + "/../pictures/" + decoration.getPicture()
        if not os.path.isfile(pic):
            pic = self.plugin_dir + "/pictures/" + decoration.getPicture()

        item.setPicturePath(pic)
        item.setFrameEnabled(0)
        item.setZValue(10)
        item.setObjectName("legendpic")

        brush = QBrush()
        brush.setStyle(Qt.SolidPattern)

        color = QColor(255, 255, 255, 0)
        brush.setColor(color)
        item.setBrush(brush)

        point = QgsLayoutPoint(
            self.margin_left + offset_x,
            self.margin_top + offset_y,
            QgsUnitTypes.LayoutMillimeters,
        )
        item.attemptMove(point)

        size = QgsLayoutSize(
            decoration.getWidth(),
            decoration.getHeight(),
            QgsUnitTypes.LayoutMillimeters,
        )
        item.attemptResize(size)
        return item

    def create_date_item(self, composer, decoration, offset_x=0, offset_y=0):
        dateFont = QFont(decoration.getFontFamily(), decoration.getFontSize())
        item = QgsLayoutItemLabel(composer)
        item.setFont(dateFont)
        d = time.localtime()
        item.setText(decoration.getText() + "%d.%d.%d" % (d[2], d[1], d[0]))
        item.adjustSizeToText()

        item.setFrameEnabled(0)
        item.setMargin(0)
        brush = QBrush()
        brush.setStyle(Qt.NoBrush)
        brush.setColor(Qt.white)
        item.setBrush(brush)
        item.setItemPosition(margin_left + offset_x, margin_top + offset_y)
        return item

    def create_picture_item(self, composer, decoration, offset_x=0, offset_y=0):
        item = QgsLayoutItemPicture(composer)
        qgs_dir = os.path.dirname(QgsProject.instance().fileName())
        pic = qgs_dir + decoration.getPicture()
        if not os.path.isfile(pic):
            pic = self.plugin_dir + "/pictures/" + decoration.getPicture()
        item.setPicturePath(pic)
        # FIXME: QGIS3
        """
        item.setSceneRect(
            QRectF(0, 0, decoration.getWidth(), decoration.getHeight())
        )
        item.setItemPosition(margin_left + offset_x, margin_top + offset_y)
        """
        item.setFrameEnabled(0)
        item.setZValue(10)

        brush = QBrush()
        brush.setStyle(Qt.NoBrush)
        brush.setColor(Qt.white)
        item.setBrush(brush)

        return item

    def create_arrow_item(self, composer, decoration, offset_x=0, offset_y=0):
        item = QgsLayoutItemPicture(composer)
        qgs_dir = os.path.dirname(QgsProject.instance().fileName())
        pic = qgs_dir + "/../pictures/" + decoration.getPicture()
        if not os.path.isfile(pic):
            pic = self.plugin_dir + "/pictures/" + decoration.getPicture()
        item.setPicturePath(pic)
        item.setZValue(10)
        item.setObjectName("northarrow")

        point = QgsLayoutPoint(
            self.margin_left + offset_x,
            self.margin_top + offset_y,
            QgsUnitTypes.LayoutMillimeters,
        )
        item.attemptMove(point)
        size = QgsLayoutSize(
            decoration.getWidth(),
            decoration.getHeight(),
            QgsUnitTypes.LayoutMillimeters,
        )
        item.attemptResize(size)
        return item

    def create_decoration_item(self, composer, decoration):
        """
        TODO:
        * scaleBarの追加
        * Composerの起動
        """
        item = None
        project = QgsProject.instance()
        crs = project.crs()

        option = decoration.getType()
        offset_x = decoration.getOffsetX()
        offset_y = decoration.getOffsetY()

        if decoration.getAffinityX() == "right":
            offset_x = (
                float(self.paperwidth) - self.margin_left - self.margin_right - offset_x
            )

        if decoration.getAffinityX() == "center":
            offset_x = float(self.paperwidth) * 0.5 - self.margin_left - offset_x

        if decoration.getAffinityY() == "bottom":
            offset_y = (
                float(self.paperheight)
                - self.margin_top
                - self.margin_bottom
                - decoration.getHeight()
                - offset_y
            )

        if option == "title" or option == "subtitle" or option == "person":
            item = self.create_title_item(
                composer, decoration, offset_x=offset_x, offset_y=offset_y
            )

        elif option == "text" or option == "author" or option == "copyright":
            item = self.create_text_item(
                composer, decoration, offset_x=offset_x, offset_y=offset_y
            )

        elif option == "date":
            item = self.create_date_item(
                composer, decoration, offset_x=offset_x, offset_y=offset_y
            )

        elif option == "picture":
            item = self.create_picture_item(
                composer, decoration, offset_x=offset_x, offset_y=offset_y
            )

        elif option == "northarrow" and self.crsdesc:
            item = self.create_arrow_item(
                composer, decoration, offset_x=offset_x, offset_y=offset_y
            )

        elif option == "legendpic" and self.legend:
            item = self.create_legendpic_item(
                composer, decoration, offset_x=offset_x, offset_y=offset_y
            )

        elif option == "legend" and self.legend:
            item = self.create_legend_item(
                composer, decoration, offset_x=offset_x, offset_y=offset_y
            )

        elif option == "map":
            item = self.create_map_item(
                composer, decoration, offset_x=offset_x, offset_y=offset_y
            )
            self.map_item = item
        elif option == "scaletext" and self.scalebar:
            item = self.create_scalebar_item(
                decoration, composer, self.map_item, offset_x, offset_y,
            )
        if item:
            item.setId(option)
            composer.addLayoutItem(item)
        return item

    def getMapExtentFromFeatureExtent(self, mapWidth, mapHeight, featExtent):
        featWidth = featExtent.width()
        featHeight = featExtent.height()

        print(mapWidth / mapHeight)
        print(featExtent.width() / featExtent.height())

        if (mapWidth / mapHeight) > (featWidth / featHeight):
            center = featExtent.center()
            xcenter = center.x()
            ycenter = center.y()

            minx = xcenter - (featHeight / (mapHeight / mapWidth)) / 2
            maxx = xcenter + (featHeight / (mapHeight / mapWidth)) / 2
            return QgsRectangle(
                minx, featExtent.yMinimum(), maxx, featExtent.yMaximum()
            )

        elif (mapWidth / mapHeight) < (featWidth / featHeight):
            center = featExtent.center()
            xcenter = center.x()
            ycenter = center.y()

            miny = ycenter - (featWidth / (mapWidth / mapHeight)) / 2
            maxy = ycenter + (featWidth / (mapWidth / mapHeight)) / 2
            return QgsRectangle(
                featExtent.xMinimum(), miny, featExtent.xMaximum(), maxy
            )

        else:
            return featExtent

    def getMapExtentFromPoint(self, mapWidth, mapHeight, scale, point):
        center = point
        xcenter = center.x()
        ycenter = center.y()

        mapWidth = mapWidth * scale / 1000
        mapHeight = mapHeight * scale / 1000

        minx = xcenter - mapWidth / 2
        miny = ycenter - mapHeight / 2
        maxx = xcenter + mapWidth / 2
        maxy = ycenter + mapHeight / 2

        return QgsRectangle(minx, miny, maxx, maxy)

    def getMapExtentFromMapCanvas(self, mapWidth, mapHeight, scale):
        xmin = self.canvas.extent().xMinimum()
        xmax = self.canvas.extent().xMaximum()
        ymin = self.canvas.extent().yMinimum()
        ymax = self.canvas.extent().yMaximum()
        xcenter = xmin + (xmax - xmin) / 2
        ycenter = ymin + (ymax - ymin) / 2

        mapWidth = mapWidth * scale / 1000
        mapHeight = mapHeight * scale / 1000
        minx = xcenter - mapWidth / 2
        miny = ycenter - mapHeight / 2
        maxx = xcenter + mapWidth / 2
        maxy = ycenter + mapHeight / 2
        return QgsRectangle(minx, miny, maxx, maxy)

    def getGridInterval(self, scale):
        # # Masstab dividiert durch 10 und runden auf die naechste Zahl
        # # der gleichen Potenz:
        # # 1:1821 -> 182.1 -> 200
        # # 1:123 -> 12.3 -> 10
        power = math.floor(math.log10(scale))
        interval = int(
            round((scale / 10) / (pow(10, power - 1))) * (pow(10, power - 1))
        )
        return interval

    def cuttingLines(self, composer):
        offset = 0.1
        lineLength = 10
        paperHeight = composer.paperHeight()
        paperWidth = composer.paperWidth()

        # # top,left
        item = QgsLayoutItemShape(0, 0, lineLength, 0, composer)
        item.setShapeType(1)
        # item.setLineWidth(0.0)
        pen = QPen()
        pen.setWidthF(0.05)
        pen.setJoinStyle(Qt.MiterJoin)
        item.setPen(pen)
        item.setPositionLock(1)

        composer.addLayoutItem(item)

        item = QgsLayoutItemShape(0, 0, 0, lineLength, composer)
        item.setShapeType(1)
        # item.setLineWidth(0.0)
        pen = QPen()
        pen.setWidthF(0.05)
        pen.setJoinStyle(Qt.MiterJoin)
        item.setPen(pen)
        item.setPositionLock(1)

        composer.addLayoutItem(item)

        # # top,right
        item = QgsLayoutItemShape(paperWidth - lineLength, 0, lineLength, 0, composer)
        item.setShapeType(1)
        # item.setLineWidth(0.0)
        pen = QPen()
        pen.setWidthF(0.05)
        pen.setJoinStyle(Qt.MiterJoin)
        item.setPen(pen)
        item.setPositionLock(1)

        composer.addLayoutItem(item)

        item = QgsLayoutItemShape(paperWidth - offset, 0, 0, lineLength, composer)
        item.setShapeType(1)
        # item.setLineWidth(0.0)
        pen = QPen()
        pen.setWidthF(0.05)
        pen.setJoinStyle(Qt.MiterJoin)
        item.setPen(pen)
        item.setPositionLock(1)

        composer.addLayoutItem(item)

        # # bottom,right
        item = QgsLayoutItemShape(
            paperWidth - lineLength, paperHeight - offset, lineLength, 0, composer
        )
        item.setShapeType(1)
        # item.setLineWidth(0.0)
        pen = QPen()
        pen.setWidthF(0.05)
        pen.setJoinStyle(Qt.MiterJoin)
        item.setPen(pen)
        item.setPositionLock(1)

        composer.addLayoutItem(item)

        item = QgsLayoutItemShape(
            paperWidth - offset, paperHeight - lineLength, 0, lineLength, composer
        )
        item.setShapeType(1)
        # item.setLineWidth(0.0)
        pen = QPen()
        pen.setWidthF(0.05)
        pen.setJoinStyle(Qt.MiterJoin)
        item.setPen(pen)
        item.setPositionLock(1)

        composer.addLayoutItem(item)

        # # bottom,left
        item = QgsLayoutItemShape(0, paperHeight - offset, lineLength, 0, composer)
        item.setShapeType(1)
        # item.setLineWidth(0.0)
        pen = QPen()
        pen.setWidthF(0.05)
        pen.setJoinStyle(Qt.MiterJoin)
        item.setPen(pen)
        item.setPositionLock(1)

        composer.addLayoutItem(item)

        item = QgsLayoutItemShape(0, paperHeight - lineLength, 0, lineLength, composer)
        item.setShapeType(1)
        # item.setLineWidth(0.0)
        pen = QPen()
        pen.setWidthF(0.05)
        pen.setJoinStyle(Qt.MiterJoin)
        item.setPen(pen)
        item.setPositionLock(1)

        composer.addLayoutItem(item)

    def foldingMarks(self, composer):
        markWidth = 210
        markHeight = 297
        lineLength = 4
        paperHeight = composer.paperHeight()
        paperWidth = composer.paperWidth()

        if paperWidth / markWidth > 1:
            count = int(round(paperWidth / markWidth, 0))
            for i in range(1, count):
                item = QgsLayoutItemShape(i * markWidth, 0, 0, lineLength, composer)
                item.setShapeType(1)
                # item.setLineWidth(0.0)
                pen = QPen()
                pen.setWidthF(0.05)
                pen.setJoinStyle(Qt.MiterJoin)
                item.setPen(pen)
                item.setPositionLock(1)

                composer.addLayoutItem(item)

                item = QgsLayoutItemShape(
                    i * markWidth, paperHeight - lineLength, 0, lineLength, composer
                )
                item.setShapeType(1)
                # item.setLineWidth(0.0)
                pen = QPen()
                pen.setWidthF(0.05)
                pen.setJoinStyle(Qt.MiterJoin)
                item.setPen(pen)
                item.setPositionLock(1)

                composer.addLayoutItem(item)

        if paperHeight / markHeight > 1:
            count = int(round(paperHeight / markHeight, 0))
            if count == 1:
                count = count + 1

            for i in range(1, count):
                item = QgsLayoutItemShape(0, i * markHeight, lineLength, 0, composer)
                item.setShapeType(1)
                # item.setLineWidth(0.0)
                pen = QPen()
                pen.setWidthF(0.05)
                pen.setJoinStyle(Qt.MiterJoin)
                item.setPen(pen)
                item.setPositionLock(1)

                composer.addLayoutItem(item)

                item = QgsLayoutItemShape(
                    paperWidth - lineLength, i * markHeight, lineLength, 0, composer
                )
                item.setShapeType(1)
                # item.setLineWidth(0.0)
                pen = QPen()
                pen.setWidthF(0.05)
                pen.setJoinStyle(Qt.MiterJoin)
                item.setPen(pen)
                item.setPositionLock(1)

                composer.addLayoutItem(item)

    def create_scalebar_item(
        self, decoration, composer, composerMap, offset_x, offset_y,
    ):
        # TODO: 関数かクラスにもっと分ける
        # TODO: 1クラスで、label, scalebar, scalebarと作成しているが分けるか検討
        textFont = QFont(decoration.getFontFamily(), decoration.getFontSize())

        scaleBarLabel = QgsLayoutItemScaleBar(composer)
        scaleBarLabel.setLinkedMap(composerMap)
        scaleBarLabel.setFont(textFont)
        scaleBarLabel.setStyle("Numeric")

        scaleBarLabel.setBoxContentSpace(0.3)  # heuristic
        scaleBarLabel.update()

        if decoration.getAffinityX() == "center":
            point = QgsLayoutPoint(
                self.margin_left
                + offset_x
                + 1
                - scaleBarLabel.boundingRect().width() * 0.5,
                self.margin_top + offset_y + 8,
                QgsUnitTypes.LayoutMillimeters,
            )
        else:
            point = QgsLayoutPoint(
                self.margin_left + offset_x + 1, self.margin_top + offset_y + 8,
            )
        scaleBarLabel.attemptMove(point)
        scaleBarLabel.setId("縮尺")
        composer.addLayoutItem(scaleBarLabel)

        # TODO: 固定幅ではなく、セグメント幅を指定する

        scaleBar = QgsLayoutItemScaleBar(composer)
        scaleBar.setLinkedMap(composerMap)
        scaleBar.setFont(textFont)
        scaleBar.setStyle("Line Ticks Up")

        scaleBar.setMapUnitsPerScaleBarUnit(1)
        scaleBar.setUnitsPerSegment(50)
        scaleBar.setHeight(3)

        scaleBar.setUnitLabel("m")
        scaleBar.setBoxContentSpace(0.3)  # heuristic2
        scaleBar.update()

        composer.addLayoutItem(scaleBar)

        if decoration.getAffinityX() == "center":
            point = QgsLayoutPoint(
                self.margin_left + offset_x + 1 - scaleBar.boundingRect().width() * 0.5,
                self.margin_top + offset_y - 3,
            )
        else:
            point = QgsLayoutPoint(
                self.margin_left + offset_x + 1, self.margin_top + offset_y
            )
        # FIXME: QGIS3
        # scaleBar.adjustBoxSize()
        scaleBar.attemptMove(point)

        # Sizeを固定にし、値のみを変化させる
        scaleBar.setMaximumBarWidth(offset_x - self.margin_left)
        scaleBar.setSegmentSizeMode(1)
        scaleBar.setId("スケールバー")
        scaleBar.update()

    def getComposerView(self):
        return self.composerView

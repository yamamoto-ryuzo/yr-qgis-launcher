#!/usr/bin/python
# -*- coding: utf-8 -*-

from qgis.PyQt.QtCore import Qt, QObject, QSize, QRectF
from qgis.PyQt.QtGui import QBrush, QIcon, QKeySequence, QPixmap
from qgis.PyQt.QtWidgets import (
    QAction,
    QTabWidget,
    QToolBar,
    QToolButton,
    QMessageBox,
    QFileDialog,
    QListWidgetItem,
)
from qgis.core import *
from qgis.gui import *
import os
import traceback
import sys
from .print_con import Form


# from easyprint import EasyPrint


class MyToolBar(QToolBar):
    def __init__(self, parent, iface, composer_view):
        self.iface = iface
        self.composer_view = composer_view
        self.composition = composer_view.composition()
        self.setting_ui = None
        self.undoAction = None
        self.redoAction = None
        self.adjustFrameSize = False
        self.picPath = ""
        self.select_item = None
        self.change_style = True

        super(QToolBar, self).__init__("myToolBar", parent)
        self.setObjectName("myToolBar")

    def run(self):
        self.add_toolbar(self.composer_view)
        self.zoom_all.trigger()

    def print_action_message(self):
        self.print_fom = Form(self.composer_view.composerWindow())
        self.print_fom.pushButton.clicked.connect(self.action_page_setting.trigger)
        self.print_fom.accepted.connect(self.print_accepted)
        self.print_fom.exec_()

    def print_accepted(self):
        check_state = self.print_fom.checkBox.isChecked()
        self.composition.setPrintAsRaster(check_state)
        self.print_action.trigger()

    def do_zoom_all(self):
        self.zoom_all.trigger()
        self.action_refresh.trigger()

    def create_actionmenu(self, actions):
        action_menu = QToolButton()
        action_menu.addActions(actions)
        action_menu.setAutoRaise(True)
        # action_menu.setDefaultAction(actions[-1])
        action_menu.setPopupMode(2)
        return action_menu

    def add_toolbar(self, composer_view):
        composer_window = composer_view.composerWindow()

        # objecNameでアクション取得

        item_actions_name = [
            u"mActionPrint",
            u"mActionExportAsImage",
            u"mActionExportAsPDF",
            u"mActionSelectMoveItem",
            u"mActionMoveItemContent",
            u"mActionAddNewLabel",
            u"mActionAddArrow",
            u"mActionAddBasicShape",
            u"mActionAddImage",
            u"mActionAddNewLegend",
            u"mActionRefreshView",
            u"mActionZoomAll",
            u"mActionPageSetup",
            u"mActionAddRectangle",
            u"mActionAddTriangle",
            u"mActionAddEllipse",
            u"mActionAddNewMap",
            u"mActionDeleteSelection",
        ]

        all_actions = composer_window.findChildren(QAction)
        for action in all_actions:
            action.setVisible(True)
        item_actions = self.find_actions_toname(all_actions, item_actions_name)
        self.action_print = item_actions["mActionPrint"]
        self.action_export_image = item_actions["mActionExportAsImage"]
        self.action_export_pdf = item_actions["mActionExportAsPDF"]
        self.action_move_item = item_actions["mActionSelectMoveItem"]
        self.action_moveitem_content = item_actions["mActionMoveItemContent"]
        self.action_add_image = item_actions["mActionAddImage"]
        self.action_add_bar = item_actions["mActionAddNewLegend"]
        self.action_add_label = item_actions["mActionAddNewLabel"]
        self.action_add_arrow = item_actions["mActionAddArrow"]
        self.action_zoom_all = item_actions["mActionZoomAll"]
        self.action_refresh = item_actions["mActionRefreshView"]
        self.action_page_setting = item_actions[u"mActionPageSetup"]
        self.action_add_map = item_actions["mActionAddNewMap"]
        self.action_add_shape = item_actions["mActionAddBasicShape"]
        delete_action = item_actions[u"mActionDeleteSelection"]

        icon = item_actions[u"mActionAddRectangle"].icon()
        text = u"図形の追加"
        directory = os.path.dirname(__file__)
        rectangle_icon = QIcon(os.path.join(directory, u"images/rectangle.png"))
        item_actions[u"mActionAddRectangle"].setIcon(rectangle_icon)
        triangle_icon = QIcon(os.path.join(directory, u"images/triangle.png"))
        item_actions[u"mActionAddTriangle"].setIcon(triangle_icon)
        ellipse_icon = QIcon(os.path.join(directory, u"images/ellipse.png"))
        item_actions[u"mActionAddEllipse"].setIcon(ellipse_icon)

        basic_shape_actions = [
            item_actions[u"mActionAddRectangle"],
            item_actions[u"mActionAddTriangle"],
            item_actions[u"mActionAddEllipse"],
        ]
        self.action_add_shape = self.create_actionmenu(basic_shape_actions)
        self.action_add_shape.setIcon(icon)
        self.action_add_shape.setText(text)
        self.action_add_shape.setToolTip(text)

        if delete_action is not None:
            delete_action.setShortcut(QKeySequence("Delete"))

        if self.action_print is not None:
            # okuda 印刷アクションをラップ
            self.print_action = self.action_print
            print_icon = self.action_print.icon()
            self.action_print = QAction(print_icon, self.action_print.text(), self)
            self.action_print.triggered.connect(self.print_action_message)
            self.addAction(self.action_print)
            self.action_print.setObjectName("my_mActionPrint")

        if self.action_page_setting is not None:
            self.addAction(self.action_page_setting)
            self.action_page_setting.setIcon(
                QIcon(os.path.dirname(__file__) + u"/images/mActionPageSetup.png")
            )
            self.action_page_setting.setObjectName(u"mActionPageSetup")

        if self.action_export_image is not None:
            self.addAction(self.action_export_image)
            self.action_export_image.setObjectName("my_mActionExportAsImage")

        if self.action_export_pdf is not None:
            self.addAction(self.action_export_pdf)
            self.action_export_pdf.setObjectName("my_mActionExportAsPDF")

        self.addSeparator()

        if self.action_add_image is not None:
            self.action_add_image.setCheckable(False)
            self.action_add_image.triggered.disconnect()
            self.action_add_image.setToolTip(u"イメージ・凡例を追加")
            self.addAction(self.action_add_image)
            self.action_add_image.setObjectName("my_mActionAddNewImage")
            self.action_add_image.triggered.connect(self.add_picture)

        if self.action_add_bar is not None and False:

            # 判例追加は不要

            self.addAction(self.action_add_bar)
            self.action_add_bar.setObjectName("my_mActionAddNewLegend")

        if self.action_add_label is not None:
            self.addAction(self.action_add_label)
            self.action_add_label.setObjectName("my_mActionAddNewLabel")

        if self.action_add_shape is not None:
            if self.qgis_version <= 10700:
                self.action_add_shape.setIcon(
                    QIcon(
                        os.path.dirname(__file__) + "/images/circle_stroked_18_2x.png"
                    )
                )
                self.addAction(self.action_add_shape)
            else:
                self.addWidget(self.action_add_shape)
            self.action_add_shape.setObjectName("my_mActionAddBasicShape")

        if self.action_add_arrow is not None:
            self.addAction(self.action_add_arrow)
            self.action_add_arrow.setObjectName("my_mActionAddArrow")

        if self.action_add_arrow is not None:
            self.addAction(self.action_add_map)
            self.action_add_map.setObjectName("my_mActionAddNewMap")

        self.addSeparator()

        if self.action_move_item is not None:
            self.addAction(self.action_move_item)
            self.action_move_item.setObjectName("mActionSelectMoveItem")

        if self.action_moveitem_content is not None:
            self.action_moveitem_content.setToolTip(u"地図を動かす")
            self.addAction(self.action_moveitem_content)
            self.action_moveitem_content.setObjectName("mActionMoveItemContent")

        if self.action_zoom_all is not None:
            self.zoom_all = self.action_zoom_all
            self.action_zoom_all = QAction(
                QIcon(":/btn/images/mActionZoomFullExtent.png"),
                self.zoom_all.text(),
                self,
            )
            self.addAction(self.action_zoom_all)
            self.action_zoom_all.triggered.connect(self.do_zoom_all)
            self.action_zoom_all.setObjectName("my_mActionZoomAll")

        self.action_edit_item = QAction(
            QIcon(":/btn/images/mActionChangeLabelProperties.png"), u"アイテム編集", self
        )
        self.addAction(self.action_edit_item)
        self.action_edit_item.triggered.connect(self.show_edit_item)
        self.action_edit_item.setObjectName("my_editItem")

        self.action_undo = QAction(QIcon(":/btn/images/mActionUndo.png"), u"元に戻す", self)
        self.action_undo.setVisible(False)
        self.addAction(self.action_undo)
        self.action_undo.triggered.connect(self.undo)
        if self.composition.undoStack().canUndo():
            self.action_undo.setEnabled(True)
        else:
            self.action_undo.setEnabled(False)
        self.action_undo.setObjectName("my_undo")

        self.action_redo = QAction(QIcon(":/btn/images/mActionRedo.png"), u"やり直し", self)
        self.action_redo.setVisible(False)
        self.addAction(self.action_redo)
        self.action_redo.triggered.connect(self.redo)
        if composer_window is not None and self.composition.undoStack().canRedo():
            self.action_redo.setEnabled(True)
        else:
            self.action_redo.setEnabled(False)
        self.action_redo.setObjectName("my_redo")

        layout_menu = composer_window.menuBar().findChildren(QMenu)[2]
        reun_actions = self.find_actions_toname(
            layout_menu.actions(), [u"mActionRedo", u"mActionUndo"]
        )
        for action in reun_actions.values():
            if action is not None:
                action.setShortcut(QKeySequence())

        # self.addSeparator()
        self.action_option = QAction(
            QIcon(":/btn/images/mActionOptions.png"), u"オプション", self
        )
        self.addAction(self.action_option)
        self.action_option.triggered.connect(self.show_setting_dock)
        self.action_option.setObjectName("my_hideshowDockWidget")

        # connect to signal

        composer_view.selectedItemChanged.connect(self.selected_item_changed)
        stack = self.composition.undoStack()
        stack.canUndoChanged.connect(self.set_undo_action_enabled)
        stack.canRedoChanged.connect(self.set_redo_action_enabled)

    def show_edit_item(self):
        try:
            from ui_control import ui_Control

            flags = (
                Qt.WindowTitleHint
                | Qt.WindowSystemMenuHint
                | Qt.WindowMaximizeButtonHint
            )

            # QgisGui.ModalDialogFlags

            self.setting_ui = ui_Control(self.composer_view.composerWindow(), flags)
            self.setup_ui()

            self.selected_item_changed()
            self.setting_ui.show()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def connect_label_signal(self):
        self.setting_ui.label_font_button, clicked.connect(self.setFont)
        self.setting_ui.label_font_color_button.clicked.connect(self.set_font_color)
        self.setting_ui.label_frame_color_button.clicked.connect(
            self.set_item_frame_color
        )
        self.setting_ui.label_background_color_button.clicked.connect(
            self.set_brush_color
        )
        self.setting_ui.pushButton_7.clicked.connect(self.show_setting_dock)
        self.setting_ui.checkBox.stateChanged.connect(self.set_label_frame_enable)
        self.setting_ui.checkBox_2.stateChanged.connect(
            self.set_label_background_color_enable
        )
        self.setting_ui.checkBox_3.stateChanged.connect(self.chkStateChanged_5)
        self.setting_ui.lineEdit.textEdited.connect(self.textEdited)
        self.setting_ui.doubleSpinBox.valueChanged.connect(self.set_item_frame_width)

    def connect_phot_signal(self):
        self.setting_ui.phot_rotation_spinbox.valueChanged.connect(
            self.set_phot_rotation
        )

        self.setting_ui.pushButton_5.clicked.connect(self.getFile)
        self.setting_ui.pushButton_6.clicked.connect(self.set_picture)

    def connect_shape_signal(self):
        # 基本図形
        self.setting_ui.shape_type_combobox.currentIndexChanged.connect(
            self.set_shape_type
        )
        self.setting_ui.shape_outline_color_button.clicked.connect(
            self.set_outline_color
        )
        self.setting_ui.shape_fill_color_button.clicked.connect(
            self.set_shape_fill_color
        )
        self.setting_ui.shape_frame_color_buttonclicked.connect(
            self.set_item_frame_color
        )
        self.setting_ui.shape_background_color_button.clicked.connect(
            self.set_brush_color
        )
        self.setting_ui.shape_show_settings_button.clicked.connect(
            self.show_setting_dock
        )

        self.setting_ui.shape_release_button.clicked.connect(
            self.set_shape_style_enable
        )
        self.setting_ui.shape_apply_button.clicked.connect(self.set_shape_style_disable)

        self.setting_ui.shape_outline_width_spinbox.valueChanged.connect(
            self.set_shape_outline_width
        )

        self.setting_ui.shape_rotation_spinbox.valueChanged.connect(
            self.set_shape_rotation
        )

        self.setting_ui.shape_frame_width_spinbox.valueChanged.connect(
            self.set_item_frame_width
        )
        self.setting_ui.shape_frame_checkbox.stateChanged.connect(self.set_shape_frame)
        self.setting_ui.shape_alpha_slider.valueChanged.connect(
            self.setFrameTranparentFill
        )

    def connect_arrow_signal(self):
        # 矢印
        self.setting_ui.arrow_frame_color_button.clicked.disconnect(
            self.set_item_frame_color
        )
        self.setting_ui.arrow_background_color_button.clicked.disconnect(
            self.set_brush_color
        )
        self.setting_ui.arrow_settings_button.clicked.disconnect(self.show_setting_dock)
        self.setting_ui.arrow_line_width_spinbox.valueChanged.disconnect(
            self.set_arrow_line_width
        )
        self.setting_ui.arrow_head_width_spinbox.valueChanged.disconnect(
            self.set_arrow_head_width
        )
        self.setting_ui.arrow_frame_width_spinbox.valueChanged.disconnect(
            self.set_item_frame_width
        )

        self.setting_ui.arrow_frame_checkbox.stateChanged.disconnect(
            self.set_arrow_frame
        )

        self.setting_ui.arrow_alpha_slider.valueChanged.disconnect(
            self.setFrameTranparentFill
        )

    def disconnect_label_signal(self):
        self.setting_ui.label_font_button.clicked.disconnect(self.setFont)
        self.setting_ui.label_font_color_button.clicked.disconnect(self.set_font_color)
        self.setting_ui.label_frame_color_button.clicked.disconnect(
            self.set_item_frame_color
        )
        self.setting_ui.label_background_color_button.clicked.disconnect(
            self.set_brush_color
        )
        self.setting_ui.pushButton_7.clicked.disconnect(self.show_setting_dock)
        self.setting_ui.checkBox.stateChanged.disconnect(self.set_label_frame_enable)
        self.setting_ui.checkBox_2.stateChanged.disconnect(
            self.set_label_background_color_enable
        )
        self.setting_ui.checkBox_3.stateChanged.disconnect(self.chkStateChanged_5)
        self.setting_ui.lineEdit.textEdited.disconnect(self.textEdited)
        self.setting_ui.doubleSpinBox.valueChanged.disconnect(self.set_item_frame_width)

    def disconnect_phot_signal(self):
        self.setting_ui.phot_rotation_spinbox.valueChanged.disconnect(
            self.set_phot_rotation
        )

        self.setting_ui.pushButton_5.clicked.disconnect(self.getFile)
        self.setting_ui.pushButton_6.clicked.disconnect(self.set_picture)

    def disconnect_shape_signal(self):
        # 基本図形
        self.setting_ui.shape_type_combobox.currentIndexChanged.disconnect(
            self.set_shape_type
        )
        self.setting_ui.shape_outline_color_button.clicked.disconnect(
            self.set_outline_color
        )
        self.setting_ui.shape_fill_color_button.clicked.disconnect(
            self.set_shape_fill_color
        )
        self.setting_ui.shape_frame_color_button.clicked.disconnect(
            self.set_item_frame_color
        )
        self.setting_ui.shape_background_color_button.clicked.disconnect(
            self.set_brush_color
        )
        self.setting_ui.shape_show_settings_button.clicked.disconnect(
            self.show_setting_dock
        )

        self.setting_ui.shape_release_button.clicked.disconnect(
            self.set_shape_style_enable
        )
        self.setting_ui.shape_apply_button.clicked.disconnect(
            self.set_shape_style_disable
        )

        self.setting_ui.shape_outline_width_spinbox.valueChanged.disconnect(
            self.set_shape_outline_width
        )

        self.setting_ui.shape_rotation_spinbox.valueChanged.disconnect(
            self.set_shape_rotation
        )

        self.setting_ui.shape_frame_width_spinbox.valueChanged.disconnect(
            self.set_item_frame_width
        )
        self.setting_ui.shape_frame_checkbox.stateChanged.disconnect(
            self.set_shape_frame
        )
        self.setting_ui.shape_alpha_slider.valueChanged.disconnect(
            self.setFrameTranparentFill
        )

    def disconnect_arrow_signal(self):
        # 矢印
        self.setting_ui.arrow_frame_color_button.clicked.disconnect(
            self.set_item_frame_color
        )
        self.setting_ui.arrow_background_color_button.clicked.disconnect(
            self.set_brush_color
        )
        self.setting_ui.arrow_settings_button.clicked.disconnect(self.show_setting_dock)
        self.setting_ui.arrow_line_width_spinbox.valueChanged.disconnect(
            self.set_arrow_line_width
        )
        self.setting_ui.arrow_head_width_spinbox.valueChanged.disconnect(
            self.set_arrow_head_width
        )
        self.setting_ui.arrow_frame_width_spinbox.valueChanged.disconnect(
            self.set_item_frame_width
        )

        self.setting_ui.arrow_frame_checkbox.stateChanged.disconnect(
            self.set_arrow_frame
        )

        self.setting_ui.arrow_alpha_slider.valueChanged.disconnect(
            self.setFrameTranparentFill
        )

    def setup_ui(self):
        tab_widget = self.setting_ui.tabWidget
        for i in xrange(4):
            tab_widget.setTabEnabled(i, False)

        self.setting_ui.label_4.setText(u"ファイル")

        self.setting_ui.label_frame_color_button.setEnabled(False)
        self.setting_ui.label_background_color_button.setEnabled(False)
        self.setting_ui.doubleSpinBox.setEnabled(False)
        self.setting_ui.doubleSpinBox.setKeyboardTracking(False)
        self.setting_ui.phot_rotation_spinbox.setKeyboardTracking(False)

        # ｱｳﾄﾗｲﾝ幅
        self.setting_ui.shape_outline_width_spinbox.setKeyboardTracking(False)
        # self.setting_ui.shape_outline_width_spinbox.setVisible(False)
        self.init_shape_combobox()
        # 回転
        self.setting_ui.shape_rotation_spinbox.setKeyboardTracking(False)
        # ﾌﾚｰﾑ幅
        self.setting_ui.shape_frame_width_spinbox.setKeyboardTracking(False)
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/btn/images/mActionOptions.png"), QIcon.Normal, QIcon.Off
        )
        self.setting_ui.shape_show_settings_button.setIcon(icon)
        self.setting_ui.shape_show_settings_button.setIconSize(QSize(30, 30))

        # 矢印
        # 線幅
        self.setting_ui.arrow_line_width_spinbox.setKeyboardTracking(False)
        # ヘッドの幅
        self.setting_ui.arrow_head_width_spinbox.setKeyboardTracking(False)
        # フレーム幅
        self.setting_ui.arrow_frame_width_spinbox.setKeyboardTracking(False)

        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/btn/images/mActionOptions.png"), QIcon.Normal, QIcon.Off
        )
        self.setting_ui.arrow_settings_button.setIcon(icon)
        self.setting_ui.arrow_settings_button.setIconSize(QSize(30, 30))

    def init_shape_combobox(self):
        self.setting_ui.shape_type_combobox.clear()
        self.setting_ui.shape_type_combobox.addItem(u"楕円")
        self.setting_ui.shape_type_combobox.addItem(u"四角形")
        self.setting_ui.shape_type_combobox.addItem(u"三角形")

    def show_setting_dock(self):
        composer_window = self.composer_view.composerWindow()
        if self.qgis_version <= 10700:
            tb = composer_window.findChildren(QTabWidget, "mOptionsTabWidget")
        else:
            tb = composer_window.findChildren(QDockWidget, u"ItemDock")
            tb.append(composer_window.findChild(QDockWidget, u"CompositionDock"))

        if tb:
            if False not in [dock.isVisible() for dock in tb]:
                for dock in tb:
                    dock.hide()
            else:
                for dock in tb:
                    dock.show()
                    dock.setMaximumWidth(400)
                    if hasattr(dock, "setCurrentIndex"):
                        # itemが目立たぬ
                        dock.setCurrentIndex(1)

    def set_undo_action_enabled(self, flg):
        if not self.composer_view:
            return

        if not self.undoAction:
            return

        act = self.undoAction
        if not act:
            return
        if flg:
            act.setEnabled(True)
        else:
            act.setEnabled(False)

    def set_redo_action_enabled(self, flg):
        if self.composer_view is None:
            return
        if self.redoAction is None:
            return
        act = self.redoAction
        if flg:
            act.setEnabled(True)
        else:
            act.setEnabled(False)

    def undo(self):
        self.composition.undoStack().undo()

    def redo(self):
        self.composition.undoStack().redo()

    def getFile(self):
        if True:

            # 仕様変更によりこっちに統一らしい

            filename = QFileDialog.getOpenFileName(
                self.composer_view.composerWindow(),
                u"ファイル選択",
                self.setting_ui.picture_file_line.text(),
                "All files(*.*)",
            )
        else:
            filename = QFileDialog.getExistingDirectory(
                self.composer_view.composerWindow(),
                u"フォルダ選択",
                self.setting_ui.picture_file_line.text(),
                QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
            )

        if filename:
            self.setting_ui.picture_file_line.setText(filename)
            self.picPath = filename

            myListView = self.setting_ui.listWidget
            myListView.clear()
            p = myListView.palette()
            p.setColor(QPalette.Highlight, Qt.gray)
            myListView.setPalette(p)

            if True:
                # 統一
                myListView.setIconSize(QSize(150, 150))
                listItem = QListWidgetItem()
                icon = QIcon()
                pic = QPixmap(self.picPath)
                pic.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                icon.addPixmap(pic, QIcon.Normal, QIcon.Off)
                listItem.setIcon(icon)
                listItem.setSizeHint(QSize(150, 150))
                listItem.setWhatsThis(self.picPath)

                myListView.addItem(listItem)
            else:
                for image in self._images(unicode(filename)):
                    myListView.setIconSize(QSize(40, 40))
                    myListView.setSpacing(1)
                    listItem = QListWidgetItem()
                    icon = QIcon()
                    pic = QPixmap(image)
                    pic.scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    icon.addPixmap(pic, QIcon.Normal, QIcon.Off)
                    listItem.setIcon(icon)
                    listItem.setWhatsThis(image)

                    myListView.addItem(listItem)

    def find_actions_toname(self, actions, object_names):
        """ actions関数を持っているオブジェクトからobjectNameが一致するactionを見つける"""

        actions_dict = {}
        for action in actions:
            if action.objectName() in object_names:
                actions_dict[unicode(action.objectName())] = action
        no_actions = list(set(object_names).difference(set(actions_dict.keys())))
        for no_action in no_actions:
            actions_dict[no_action] = None
        return actions_dict

    def get_item_label(self, item=None):
        try:
            if self.setting_ui is None or item is None:
                return
            self.adjustFrameSize = False
            self.setting_ui.checkBox_3.setChecked(True)
            # item.adjustSizeToText()
            # get item size
            self.prevXpos = item.scenePos().x()
            self.prevYpos = item.scenePos().y()
            self.prevWidth = item.boundingRect().width()
            self.prevHeight = item.boundingRect().height()

            self.setting_ui.tabWidget.setCurrentIndex(0)
            # text
            self.setting_ui.lineEdit.setText(item.text())
            # frame
            is_frame = item.frame() if self.qgis_version <= 10700 else item.hasFrame()

            self.frame_width = 0.3
            if is_frame:
                self.setting_ui.checkBox.setCheckState(Qt.Checked)
                self.frame_width = item.pen().widthF()
            self.setting_ui.doubleSpinBox.setValue(self.frame_width)

            # background
            if self.qgis_version > 20000:
                background_state = 2 if item.hasBackground() else 0
            elif item.brush().style() != Qt.NoBrush:
                background_state = 2
            else:
                background_state = 0
            self.setting_ui.checkBox_2.setCheckState(background_state)
            self.connect_label_signal()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def get_item_picture(self, item=None):
        try:
            if self.setting_ui is None or item is None:
                return

            myListView = self.setting_ui.listWidget
            p = myListView.palette()
            p.setColor(QPalette.Highlight, Qt.gray)
            myListView.setPalette(p)

            dirpath = (
                unicode(os.environ[u"home"], sys.getfilesystemencoding()) + u"\\desktop"
            )

            if item.objectName() == "legendpic" or item.pictureFile():
                self.setting_ui.picture_file_line.setText(item.pictureFile())
            else:
                self.setting_ui.picture_file_line.setText(dirpath)

            myListView.clear()

            self.setting_ui.lineEdit_3.setVisible(False)
            self.setting_ui.phot_rotation_spinbox.setVisible(True)
            self.setting_ui.label_5.setVisible(True)
            if item.objectName() == "legendpic" or os.path.isfile(item.pictureFile()):
                myListView.setIconSize(QSize(150, 150))
                listItem = QListWidgetItem()
                icon = QIcon()
                pic = QPixmap(item.pictureFile())
                pic.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                icon.addPixmap(pic, QIcon.Normal, QIcon.Off)
                listItem.setIcon(icon)
                listItem.setSizeHint(QSize(150, 150))
                listItem.setWhatsThis(item.pictureFile())

                myListView.addItem(listItem)

                self.setting_ui.phot_rotation_spinbox.setValue(item.rotation())
            elif False:
                self.setting_ui.lineEdit_3.setVisible(True)
                self.setting_ui.phot_rotation_spinbox.setVisible(False)
                self.setting_ui.label_5.setVisible(False)
                for image in self._images(dirpath):
                    myListView.setIconSize(QSize(40, 40))
                    myListView.setSpacing(1)
                    listItem = QListWidgetItem()
                    icon = QIcon()
                    pic = QPixmap(image)
                    pic.scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    icon.addPixmap(pic, QIcon.Normal, QIcon.Off)
                    listItem.setIcon(icon)
                    listItem.setWhatsThis(image)

                    myListView.addItem(listItem)
            else:
                self.setting_ui.phot_rotation_spinbox.setValue(0)
            self.connect_phot_signal()
        except:
            QMessageBox.information(
                self.iface.activeComposers()[0].composerWindow(),
                u"簡易印刷",
                traceback.format_exc(),
            )

    def get_item_shape(self, item=None):
        try:
            if self.setting_ui is None or item is None:
                return

            self.change_style = False
            shape_type = item.shapeType()
            self.setting_ui.shape_type_combobox.setCurrentIndex(shape_type)

            if self.qgis_version <= 10700:
                outline_width = item.lineWidth()
                is_frame = item.frame()
            else:
                outline_width = item.pen().width()
                is_frame = item.hasFrame()
            self.setting_ui.shape_outline_width_spinbox.setValue(outline_width)

            rotation = item.rotation()
            self.setting_ui.shape_rotation_spinbox.setValue(rotation)

            if is_frame:
                self.setting_ui.shape_frame_checkbox.setCheckState(Qt.Checked)
                self.setting_ui.shape_frame_width_spinbox.setValue(item.pen().widthF())
            else:
                self.setting_ui.shape_frame_checkbox.setCheckState(Qt.Unchecked)
                self.setting_ui.shape_frame_width_spinbox.setValue(0.00)

            frame_color = item.brush().color()
            self.frame_alpha = frame_color.alpha()
            self.setting_ui.shape_alpha_slider.setSliderPosition(self.frame_alpha)
            self.change_style = True
            self.connect_shape_signal()
        except:
            QMessageBox.information(
                self.iface.activeComposers()[0].composerWindow(),
                u"簡易印刷",
                traceback.format_exc(),
            )

    def get_item_arrow(self, item=None):
        try:
            if self.setting_ui is None or item is None:
                return

            is_frame = item.frame() if self.qgis_version <= 10700 else item.hasFrame()
            if is_frame:
                self.setting_ui.arrow_frame_checkbox.setCheckState(Qt.Checked)
                self.setting_ui.arrow_frame_width_spinbox.setValue(item.pen().widthF())
            else:
                self.setting_ui.arrow_frame_checkbox.setCheckState(Qt.Unchecked)
                self.setting_ui.arrow_frame_width_spinbox.setValue(0.00)

            frame_brush_color = item.brush().color()
            self.frame_alpha = frame_brush_color.alpha()
            self.setting_ui.arrow_alpha_slider.setSliderPosition(self.frame_alpha)
            self.connect_arrow_signal()
        except:
            QMessageBox.information(
                self.iface.activeComposers()[0].composerWindow(),
                u"簡易印刷",
                traceback.format_exc(),
            )

    def _images(self, _dirpath):
        # ディレクトリ内の画像探索
        images = []
        extensions = (
            "bmp",
            "BMP",
            "gif",
            "GIF",
            "ico",
            "ICO",
            "jpeg",
            "JPEG",
            "jpg",
            "JPG",
            "mng",
            "MNG",
            "pbm",
            "PBM",
            "pgm",
            "PGM",
            "png",
            "PNG",
            "ppm",
            "PPM",
            "svg",
            "SVG",
            "svgz",
            "SVGZ",
            "tif",
            "TIF",
            "tiff",
            "TIFF",
            "xbm",
            "XBM",
            "xpm",
            "XPM",
        )
        for file_name in os.listdir(_dirpath):
            if file_name.endswith(extensions):
                images.append(os.path.join(_dirpath, file_name))
        return images

    def supported_image_extensions(self):
        formats = QImageReader().supportedImageFormats()
        return [str(fmt) for fmt in formats]

    def set_picture(self):
        if self.picPath is not None and os.path.exists(self.picPath):
            for item in self.composition.selectedComposerItems():
                if item is not None and isinstance(item, QgsComposerPicture):
                    self.composition.beginCommand(item, u"画像が変更されました")
                    item.setPictureFile(self.picPath)
                    item.update()
                    self.composition.endCommand()
                    break
            self.setting_ui.close()

    def setFont(self):
        try:
            for item in self.composition.selectedComposerItems():
                if item is not None and isinstance(item, QgsComposerLabel):
                    font = self.FontDialog(item)

                    if font is not None:
                        self.composition.beginCommand(item, u"ラベルフォントが変更されました")
                        item.setFont(font)
                        if self.setting_ui.checkBox_3.isChecked():
                            item.adjustSizeToText()
                        item.update()
                        self.composition.endCommand()
                break
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_font_color(self):
        try:
            for item in self.composition.selectedComposerItems():
                if item is not None and isinstance(item, QgsComposerLabel):
                    itemColor = item.fontColor()
                    color = self.color_dialog(itemColor)
                    if color.isValid():
                        self.composition.beginCommand(item, u"ラベルフォントが変更されました")
                        item.setFontColor(color)
                        item.update()
                        self.composition.endCommand()
                    break
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_item_frame_color(self):
        try:
            if self.select_item is None:
                return
            item = self.select_item
            item_color = item.pen().color()
            color = self.color_dialog(item_color)
            if color.isValid():
                pen = QPen()
                pen.setColor(color)
                pen.setStyle(Qt.SolidLine)
                pen.setWidthF(self.frame_width)

                self.composition.beginCommand(item, u"フレーム色が変更されました")
                item.setPen(pen)
                if (
                    isinstance(item, QgsComposerLabel)
                    and self.setting_ui.checkBox_3.isChecked()
                ):
                    item.adjustSizeToText()
                item.update()
                self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_brush_color(self):
        try:
            item = self.select_item
            if item is None:
                return
            itemColor = item.brush().color()
            color = self.color_dialog(itemColor)
            if color.isValid():
                # self.setting_ui.shape_alpha_slider.value()
                # color.setAlpha(self.frame_alpha)
                brush = QBrush()
                brush.setStyle(Qt.SolidPattern)
                brush.setColor(color)
                self.composition.beginCommand(item, u"背景色が変更されました")
                item.setBrush(brush)
                if (
                    isinstance(item, QgsComposerLabel)
                    and self.setting_ui.checkBox_3.isChecked()
                ):
                    item.adjustSizeToText()
                item.update()
                self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_outline_color(self):
        try:
            for item in self.composition.selectedComposerItems():
                if item is not None and isinstance(item, QgsComposerShape):
                    item_color = (
                        item.outlineColor() if self.qgis_version <= 10900 else None
                    )
                    color = self.color_dialog(item_color)
                    if not color.isValid():
                        break
                    self.composition.beginCommand(item, u"図形の外周線の色")
                    if self.qgis_version <= 10700:
                        item.setOutlineColor(color)
                    else:
                        if self.change_style:
                            item.setUseSymbolV2(False)
                        pen = item.pen()
                        pen.setColor(color)
                        item.setPen(pen)
                    item.update()
                    self.composition.endCommand()
                    break
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_shape_fill_color(self):
        try:
            if not self.select_item:
                return
            item = self.select_item
            item_color = (
                item.fillColor() if self.qgis_version <= 10900 else item.brush().color()
            )
            color = self.color_dialog(item_color)
            if not color.isValid():
                return
            self.composition.beginCommand(item, u"図形塗りつぶし色")
            if self.qgis_version <= 10900:
                item.setFillColor(color)
            else:
                if self.change_style:
                    item.setUseSymbolV2(False)
                brush = item.brush()
                brush.setColor(color)
                item.setBrush(brush)
            item.update()
            self.composition.endCommand()
            return
        except:
            QMessageBox.warning(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_arrow_color(self):
        try:
            for item in self.composition.selectedComposerItems():
                if item is not None and isinstance(
                    item, (QgsComposerItem, QgsComposerArrow)
                ):
                    mArrowColorButton
                    QMessageBox.information(
                        self.composer_view.composerWindow(), u"簡易印刷", str(item.type())
                    )

                    item = super(QgsComposerItem, item)
                    chi = item.painter()
                    QMessageBox.information(
                        self.composer_view.composerWindow(), u"簡易印刷", str(chi)
                    )
                    itempainter = item.pen()
                    QMessageBox.information(
                        self.composer_view.composerWindow(),
                        u"簡易印刷",
                        str(itempainter.color().red())
                        + ","
                        + str(itempainter.color().green())
                        + ","
                        + str(itempainter.color().blue()),
                    )
                    item_color = item.arrowColor()

                    color = self.color_dialog(item_color)
                    if color.isValid():
                        self.composition.beginCommand(item, u"矢印カラーが変更されました")
                        item.setArrowColor(color)
                        item.update()
                        self.composition.endCommand()
                    break
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def FontDialog(self, item):
        try:
            (font, ok) = QFontDialog.getFont(item.font())
            if ok is True:
                return font
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def color_dialog(self, old_color=None):
        # show QColorDialog
        if old_color is not None:
            color = QColorDialog.getColor(
                old_color, self.composer_view.composerWindow()
            )
        else:
            color = QColorDialog.getColor(Qt.white, self.composer_view.composerWindow())
        return color

    def textEdited(self, strText, item=None):
        if item is None:
            item = self.select_item
        try:
            self.composition.beginCommand(item, u"ラベルテキストが変更されました")
            item.setText(strText)
            if self.setting_ui.checkBox_3.isChecked():
                item.adjustSizeToText()
            item.update()
            self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_item_frame_width(self, value, item=None):
        if item is None:
            item = self.select_item
        try:
            # set frame width
            self.frame_width = value
            is_frame = item.frame() if self.qgis_version <= 10700 else item.hasFrame()
            if is_frame:
                pen = item.pen()
                pen.setWidthF(value)
                self.composition.beginCommand(item, u"アイテム外周線太さが変更されました")
                item.setPen(pen)
                if (
                    self.setting_ui.checkBox_3.isChecked()
                    and self.setting_ui.checkBox_3.isEnabled()
                ):
                    item.adjustSizeToText()
                item.update()
                self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_phot_rotation(self, value, item=None):
        if item is None:
            item = self.select_item
        try:
            # set picture rotation
            self.composition.beginCommand(item, u"画像の傾きが変更されました")
            item.setRotation(value)
            item.update()
            self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_shape_outline_width(self, width_value, item=None):
        if item is None:
            item = self.select_item
        try:
            # set shape outline width
            self.composition.beginCommand(item, u"図形の外周線の幅")

            if self.qgis_version <= 10700:
                item.setLineWidth(width_value)
            else:
                if self.change_style:
                    item.setUseSymbolV2(False)
                pen = item.pen()
                pen.setWidth(width_value)
                item.setPen(pen)
            item.update()
            self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_shape_rotation(self, value, item=None):
        # 図形の傾き設定
        if item is None:
            item = self.select_item
        try:
            # set shape rotation
            self.composition.beginCommand(item, u"図形の傾きが変更されました")
            item.setRotation(value)
            item.update()
            self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_arrow_line_width(self, value, item=None):
        # 矢印の幅設定
        if item is None:
            item = self.select_item
        try:
            # set arrow outline width
            self.composition.beginCommand(item, u"矢印アウトラインの太さ")
            item.setOutlineWidth(value)
            item.update()
            self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_arrow_head_width(self, value, item=None):
        if item is None:
            item = self.select_item
        # 矢印の線の太さ設定
        try:
            # set arrow outline width
            self.composition.beginCommand(item, u"矢印ヘッドの太さ")
            item.setArrowHeadWidth(value)
            item.update()
            self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_shape_type(self, idx, item=None):
        if item is None:
            item = self.select_item
        try:
            self.composition.beginCommand(item, u"図形のタイプが変更されました")
            item.setShapeType(idx)
            item.update()
            self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def setFrameTranparentFill(self, alpha, item=None):
        if item is None:
            item = self.select_item
        try:
            self.frame_alpha = alpha
            brush = item.brush()
            color = brush.color()
            color.setAlpha(alpha)
            brush.setColor(color)

            self.composition.beginCommand(item, u"アイテムの透過度が変更されました")
            item.setBrush(brush)
            item.update()
            self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def init_label_tab(self):
        try:
            if self.setting_ui is None:
                return
            self.setting_ui.lineEdit.setEnabled(True)
            self.setting_ui.lineEdit.setText("")
            self.setting_ui.label_font_button.setEnabled(True)
            self.setting_ui.label_font_color_button.setEnabled(True)
            self.setting_ui.checkBox.setCheckState(Qt.Unchecked)
            self.setting_ui.checkBox_2.setCheckState(Qt.Unchecked)
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def init_picture_tab(self):
        try:
            if self.setting_ui is None:
                return
            self.setting_ui.picture_file_line.setEnabled(True)
            self.setting_ui.picture_file_line.setText("")
            self.setting_ui.pushButton_5.setEnabled(True)
            self.setting_ui.pushButton_6.setEnabled(True)
            gridCnt = self.setting_ui.gridLayout.count()

            self.setting_ui.lineEdit_3.setVisible(True)
            self.setting_ui.phot_rotation_spinbox.setVisible(False)
            self.setting_ui.label_5.setVisible(False)
            if gridCnt > 0:
                for i in reversed(range(gridCnt)):
                    self.setting_ui.gridLayout.itemAt(i).widget().setParent(None)
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def init_shape_tab(self):
        try:
            if self.setting_ui is None:
                return
            self.init_shape_combobox()
            # self.setting_ui.shape_symbol_checkbox.setCheckState(Qt.Checked)

            # self.setting_ui.shape_fill_color_button.setEnabled(False)

            self.setting_ui.shape_outline_width_spinbox.setValue(1.00)
            self.setting_ui.shape_rotation_spinbox.setValue(0)
            self.setting_ui.shape_frame_checkbox.setCheckState(Qt.Checked)
            self.setting_ui.shape_frame_color_button.setEnabled(True)
            self.setting_ui.shape_background_color_button.setEnabled(True)
            self.setting_ui.shape_frame_width_spinbox.setValue(0.00)
            self.setting_ui.shape_alpha_slider.setSliderPosition(0)
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def init_arrow_tab(self):
        try:
            if self.setting_ui is None:
                return
            self.setting_ui.arrow_line_width_spinbox.setValue(1.00)
            self.setting_ui.arrow_head_width_spinbox.setValue(4.00)
            self.setting_ui.arrow_frame_checkbox.setCheckState(Qt.Checked)
            self.setting_ui.arrow_frame_width_spinbox.setValue(0.00)
            self.setting_ui.arrow_alpha_slider.setSliderPosition(0)
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def selected_item_changed(self, item=None):
        items = self.composition.selectedComposerItems()
        composer_item = items[-1] if items else None
        if self.select_item == composer_item and item is not None:
            return
        self.select_item = composer_item

        try:
            if self.setting_ui:
                self.reset_tab()
            else:
                return

            item_type = self.set_item_settings(composer_item)
            if item_type != -1:
                tab_widget = self.setting_ui.tabWidget
                tab_widget.setTabEnabled(item_type, True)
                tab_widget.setCurrentIndex(item_type)
            acts = self.iface.activeComposers()
            if len(acts) >= 1:
                for act in acts:
                    composer_window = act.composerWindow()
                    tb = composer_window.findChild(QTabWidget, "mOptionsTabWidget")
                    if tb and tb.isVisible():
                        tb.setCurrentIndex(1)
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def reset_tab(self):
        disconnect_methods = [
            self.disconnect_label_signal,
            self.disconnect_phot_signal,
            self.disconnect_shape_signal,
            self.disconnect_arrow_signal,
        ]
        init_methods = [
            self.init_label_tab,
            self.init_picture_tab,
            self.init_shape_tab,
            self.init_arrow_tab,
        ]
        tab_widget = self.setting_ui.tabWidget
        for i, method in enumerate(disconnect_methods):
            state = tab_widget.isTabEnabled(i)
            if state:
                method()
                init_methods[i]()
                tab_widget.setTabEnabled(i, False)

    def set_item_settings(self, item):
        if item is None:
            return -1
        if isinstance(item, QgsComposerLabel):
            # font tab
            self.get_item_label(item)
            return 0

        elif isinstance(item, QgsComposerPicture):
            self.picPath = item.pictureFile()
            # picture tab
            self.get_item_picture(item)
            return 1
        elif isinstance(item, QgsComposerShape):
            # shape tab
            self.get_item_shape(item)
            return 2
        elif isinstance(item, (QgsComposerItem, QgsComposerArrow)):

            # arrow tab
            self.get_item_arrow(item)
            return 3
        return -1

    def set_label_frame_enable(self, check_state, item=None):
        if item is None:
            item = self.select_item
        try:
            self.composition.beginCommand(item, u"アイテムフレームの有効無効が切り替えられました")
            if self.qgis_version <= 10700:
                item.setFrame(check_state)
            else:
                item.setFrameEnabled(check_state)

            self.setting_ui.label_frame_color_button.setEnabled(check_state)
            self.setting_ui.doubleSpinBox.setEnabled(check_state)
            self.setting_ui.checkBox_3.setCheckState(check_state)
            self.setting_ui.checkBox_3.setEnabled(check_state)
            item.update()
            self.composition.endCommand()
        except:
            print(traceback.format_exc())

    def set_label_background_color_enable(self, check_state, item=None):
        if item is None:
            item = self.select_item
        try:
            self.composition.beginCommand(item, u"背景色が変更されました")
            self.setting_ui.label_background_color_button.setEnabled(check_state)
            if self.qgis_version > 20000:
                item.setBackgroundEnabled(check_state)
            elif check_state == 0:  # unchecked
                # 透過
                brush = item.brush()
                brush.setStyle(Qt.NoBrush)
                item.setBrush(brush)
            elif check_state == 2:
                # checked
                brush = item.brush()
                brush.setStyle(Qt.SolidPattern)
                item.setBrush(brush)
            item.update()
            self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def chkStateChanged_5(self, check_state, item=None):
        if item is None:
            item = self.select_item
        try:
            self.composition.beginCommand(item, u"アイテム位置を変更する")
            if check_state == 0:  # unchecked
                if self.adjustFrameSize is True:
                    item.setItemPosition(
                        self.prevXpos, self.prevYpos, self.prevWidth, self.prevHeight
                    )
                self.adjustFrameSize = False
            elif check_state == 2:
                # checked
                if self.adjustFrameSize is False:
                    self.prevXpos = item.scenePos().x()
                    self.prevYpos = item.scenePos().y()
                    self.prevWidth = item.boundingRect().width()
                    self.prevHeight = item.boundingRect().height()
                    item.adjustSizeToText()
                self.adjustFrameSize = True
            item.update()
            self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_shape_style_enable(self):
        try:
            if self.qgis_version <= 10700:
                return
            self.composition.beginCommand(self.select_item, u"図形のstyle設定が切替えられました")
            self.select_item.setUseSymbolV2(True)
            self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_shape_style_disable(self):
        try:
            if self.qgis_version <= 10700:
                return
            self.composition.beginCommand(self.select_item, u"図形のstyle設定が切替えられました")
            self.select_item.setUseSymbolV2(False)
            self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_shape_frame(self, check_state, item=None):
        # 図形のフレーム設定
        if item is None:
            item = self.select_item
        try:
            self.composition.beginCommand(item, u"アイテムフレームの有効無効が切替えられました")
            if self.qgis_version <= 10700:
                item.setFrame(check_state)
            else:
                item.setFrameEnabled(check_state)
            item.update()
            self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def set_arrow_frame(self, check_state, item=None):
        # 矢印のフレーム定
        if item is None:
            item = self.select_item
        try:
            self.composition.beginCommand(item, u"アイテムフレームの有効無効が切替えられました")
            if self.qgis_version <= 10700:
                item.setFrame(check_state)
            else:
                item.setFrameEnabled(check_state)
            item.update()
            self.composition.endCommand()
        except:
            QMessageBox.information(
                self.composer_view.composerWindow(), u"簡易印刷", traceback.format_exc()
            )

    def add_picture(self):
        item = QgsComposerPicture(self.composition)
        directry = os.environ[u"home"], sys.getfilesystemencoding() + "\\desktop"
        pic = QFileDialog.getOpenFileName(
            self.composer_view.composerWindow(), u"ファイル選択", directry, "All files(*.*)"
        )
        if not pic:
            return
        item.setPictureFile(pic)
        item.setSceneRect(QRectF(0, 0, 39, 39))
        item.setItemPosition(
            self.composition.width() / 2 - 39, self.composition.height() / 2 - 39
        )
        item.setZValue(10)
        # item.setPositionLock(1)
        # 20140317 add
        brush = QBrush()
        brush.setStyle(Qt.NoBrush)
        brush.setColor(Qt.white)
        item.setBrush(brush)
        if self.qgis_version <= 10700:
            item.setFrame(0)
            self.composer_view.addComposerPicture(item)
        else:
            item.setFrameEnabled(0)
            self.composition.addComposerPicture(item)

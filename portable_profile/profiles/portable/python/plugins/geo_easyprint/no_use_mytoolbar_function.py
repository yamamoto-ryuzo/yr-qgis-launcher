    def setFontColor_2(self):
        # ラベルの追加時に使用している関数？
        try:
            color = QColorDialog.getColor(Qt.black,
                                          self.composerView.composerWindow())
            if color.isValid():
                self.newLabelFontColor = color

                palette = QPalette()
                palette.setColor(QPalette.WindowText, color)
                self.pluginGui2.label_4.setPalette(palette)
        except:
            QMessageBox.information(self.composerView.composerWindow(),
                                    u"簡易印刷", traceback.format_exc())

    def set_framecolor_label(self):
        # ラベルのフレーム色設定
        try:
            color = QColorDialog.getColor(Qt.black,
                                          self.composerView.composerWindow())
            if color.isValid():
                pen = QPen()
                pen.setColor(color)
                pen.setStyle(Qt.SolidLine)
                self.newLabelPen = pen
        except:
            QMessageBox.information(self.composerView.composerWindow(),
                                    u"簡易印刷", traceback.format_exc())

    def change_backcolor_label(self):
        # ラベルの背景色の変更
        try:
            color = QColorDialog.getColor(Qt.white,
                                          self.composerView.composerWindow())
            if color.isValid():
                brush = QBrush()
                brush.setStyle(Qt.SolidPattern)
                brush.setColor(color)
                self.newLabelBrush = brush
        except:
            QMessageBox.information(self.composerView.composerWindow(),
                                    u"簡易印刷", traceback.format_exc())

    def chkStateChanged_3(self, check_state):
        try:
            if check_state == 0:
                # unchecked
                self.pluginGui2.pushButton_3.setEnabled(False)
                self.pluginGui2.doubleSpinBox.setValue(0.3)
                self.pluginGui2.doubleSpinBox.setEnabled(False)
            elif check_state == 2:
                # checked
                self.pluginGui2.pushButton_3.setEnabled(True)
                self.pluginGui2.doubleSpinBox.setValue(0.3)
                self.pluginGui2.doubleSpinBox.setEnabled(True)
        except:
            QMessageBox.information(self.composerView.composerWindow(),
                                    u"簡易印刷", traceback.format_exc())

    def set_backcolor_label(self, value):
        # ラベルの背景の表示切替
        try:
            if value == 0:  # unchecked
                brush = QBrush()
                brush.setStyle(Qt.NoBrush)
                self.newLabelBrush = brush

                self.pluginGui2.pushButton_4.setEnabled(False)
            elif value == 2:
                # checked
                brush = QBrush()
                brush.setStyle(Qt.SolidPattern)
                brush.setColor(Qt.white)
                self.newLabelBrush = brush

                self.pluginGui2.pushButton_4.setEnabled(True)
        except:
            QMessageBox.information(self.composerView.composerWindow(),
                                    u"簡易印刷", traceback.format_exc())

    def valueChanged_2(self, dvalue):
        try:
            self.newLabelPen.setWidthF(dvalue)
        except:
            QMessageBox.information(self.composerView.composerWindow(),
                                    u"簡易印刷", traceback.format_exc())

    def addPicture(self):
        try:
            picFile = self.pluginGui2.picture_file_line.text().trimmed()
            if picFile == '' or not os.path.exists(picFile):
                QMessageBox.information(self.composerView.composerWindow(),
                                        u"簡易印刷", u"ファイル名に誤りがあります")
                self.pluginGui2.picture_file_line.setFocus()
                return
            else:
                composition = self.composerView.composition()

                composerPicture = QgsComposerPicture(composition)
                composerPicture.setPictureFile(picFile)
                composerPicture.setSceneRect(QRectF(0, 0, 50, 50))
                composerPicture.setItemPosition(0, 0)
                composerPicture.setZValue(10)
                if self.qgis_version <= 10700:
                    composerPicture.setFrame(0)
                    self.composerView.addComposerPicture(composerPicture)
                else:
                    composerPicture.setFrameEnabled(0)
                    self.composerView.composition().addComposerPicture(composerPicture)

                self.pluginGui2.close()
        except:
            QMessageBox.information(self.composerView.composerWindow(),
                                    u"簡易印刷", traceback.format_exc())

    def setFont_2(self):
        try:
            (font, ok) = QFontDialog.getFont(QFont(self.pluginGui2.label_4.font()),
                                             self.composerView.composerWindow())
            if ok is True:
                self.newLabelFont = font
                self.pluginGui2.label_4.setFont(font)
        except:
            QMessageBox.information(self.composerView.composerWindow(),
                                    u"簡易印刷", traceback.format_exc())

    def textEdited_2(self, strText):
        try:
            self.newLabelText = strText
        except:
            QMessageBox.information(self.composerView.composerWindow(),
                                    u"簡易印刷", traceback.format_exc())

    def addLabel(self):
        try:
            strText = self.pluginGui2.lineEdit.text().trimmed()
            if strText == '':
                QMessageBox.information(self.composerView.composerWindow(),
                                        u"簡易印刷", u"テキストが入力されていません")
                self.pluginGui2.lineEdit.setFocus()
                return

            composerLabel = self.newLabel
            composerLabel.setFont(self.newLabelFont)
            composerLabel.setFontColor(self.newLabelFontColor)
            composerLabel.setText(strText)

            if self.pluginGui2.checkBox.isChecked():
                # setFrame(0):no frame, setFrame(bool):with frame??
                if self.qgis_version <= 10700:
                    composerLabel.setFrame(1)
                else:
                    composerLabel.setFrameEnabled(1)
                self.newLabelPen.setWidthF(self.pluginGui2.doubleSpinBox.value())
                composerLabel.setPen(self.newLabelPen)
            else:
                if self.qgis_version <= 10700:
                    composerLabel.setFrame(0)
                else:
                    composerLabel.setFrameEnabled(0)
            composerLabel.setMargin(1.0)

            if self.pluginGui2.checkBox_2.isChecked():
                self.newLabelBrush.setStyle(Qt.SolidPattern)
            else:
                self.newLabelBrush.setStyle(Qt.NoBrush)
            composerLabel.setBrush(self.newLabelBrush)

            composerLabel.adjustSizeToText()

            if self.qgis_version <= 10700:
                self.composerView.addComposerLabel(composerLabel)
            else:
                self.composerView.composition().addComposerLabel(composerLabel)

            self.pluginGui2.close()
        except Exception, e:
            QMessageBox.information(self.composerView.composerWindow(),
                                    u"簡易印刷", traceback.format_exc())

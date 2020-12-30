# -*- coding: utf-8 -*-

#
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GeneratorTab(object):
    def setupUi(self, GeneratorTab):
        GeneratorTab.setObjectName("GeneratorTab")
        GeneratorTab.resize(1287, 774)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(GeneratorTab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(GeneratorTab)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1287, 774))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.scrollAreaWidgetContents)
        self.splitter.setStyleSheet("QSplitter::handle:horizontal {\n"
"margin: 4px 0px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"stop:0 rgba(255, 255, 255, 0), \n"
"stop:0.5 rgba(100, 100, 100, 100), \n"
"stop:1 rgba(255, 255, 255, 0));\n"
"image: url(:/icons/icons/splitter_handle_vertical.svg);\n"
"}")
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(6)
        self.splitter.setObjectName("splitter")
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_proto = QtWidgets.QWidget()
        self.tab_proto.setObjectName("tab_proto")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_proto)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.treeProtocols = GeneratorTreeView(self.tab_proto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeProtocols.sizePolicy().hasHeightForWidth())
        self.treeProtocols.setSizePolicy(sizePolicy)
        self.treeProtocols.setObjectName("treeProtocols")
        self.treeProtocols.header().setDefaultSectionSize(57)
        self.verticalLayout_4.addWidget(self.treeProtocols)
        self.tabWidget.addTab(self.tab_proto, "")
        self.tab_pauses = QtWidgets.QWidget()
        self.tab_pauses.setObjectName("tab_pauses")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_pauses)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lWPauses = GeneratorListWidget(self.tab_pauses)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lWPauses.sizePolicy().hasHeightForWidth())
        self.lWPauses.setSizePolicy(sizePolicy)
        self.lWPauses.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.lWPauses.setProperty("showDropIndicator", False)
        self.lWPauses.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.lWPauses.setObjectName("lWPauses")
        self.gridLayout_5.addWidget(self.lWPauses, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab_pauses, "")
        self.tab_fuzzing = QtWidgets.QWidget()
        self.tab_fuzzing.setObjectName("tab_fuzzing")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_fuzzing)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.listViewProtoLabels = GeneratorListView(self.tab_fuzzing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewProtoLabels.sizePolicy().hasHeightForWidth())
        self.listViewProtoLabels.setSizePolicy(sizePolicy)
        self.listViewProtoLabels.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.listViewProtoLabels.setObjectName("listViewProtoLabels")
        self.verticalLayout_9.addWidget(self.listViewProtoLabels)
        self.groupBox = QtWidgets.QGroupBox(self.tab_fuzzing)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.stackedWidgetFuzzing = QtWidgets.QStackedWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidgetFuzzing.sizePolicy().hasHeightForWidth())
        self.stackedWidgetFuzzing.setSizePolicy(sizePolicy)
        self.stackedWidgetFuzzing.setObjectName("stackedWidgetFuzzing")
        self.pageFuzzingUI = QtWidgets.QWidget()
        self.pageFuzzingUI.setObjectName("pageFuzzingUI")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.pageFuzzingUI)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnFuzz = QtWidgets.QPushButton(self.pageFuzzingUI)
        self.btnFuzz.setObjectName("btnFuzz")
        self.horizontalLayout_4.addWidget(self.btnFuzz)
        self.rBSuccessive = QtWidgets.QRadioButton(self.pageFuzzingUI)
        self.rBSuccessive.setChecked(True)
        self.rBSuccessive.setObjectName("rBSuccessive")
        self.horizontalLayout_4.addWidget(self.rBSuccessive)
        self.rbConcurrent = QtWidgets.QRadioButton(self.pageFuzzingUI)
        self.rbConcurrent.setObjectName("rbConcurrent")
        self.horizontalLayout_4.addWidget(self.rbConcurrent)
        self.rBExhaustive = QtWidgets.QRadioButton(self.pageFuzzingUI)
        self.rBExhaustive.setObjectName("rBExhaustive")
        self.horizontalLayout_4.addWidget(self.rBExhaustive)
        self.stackedWidgetFuzzing.addWidget(self.pageFuzzingUI)
        self.pageFuzzingProgressBar = QtWidgets.QWidget()
        self.pageFuzzingProgressBar.setObjectName("pageFuzzingProgressBar")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.pageFuzzingProgressBar)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.progressBarFuzzing = QtWidgets.QProgressBar(self.pageFuzzingProgressBar)
        self.progressBarFuzzing.setProperty("value", 24)
        self.progressBarFuzzing.setObjectName("progressBarFuzzing")
        self.horizontalLayout_7.addWidget(self.progressBarFuzzing)
        self.stackedWidgetFuzzing.addWidget(self.pageFuzzingProgressBar)
        self.horizontalLayout_6.addWidget(self.stackedWidgetFuzzing)
        self.verticalLayout_9.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_fuzzing, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.modulationLayout_2 = QtWidgets.QGridLayout()
        self.modulationLayout_2.setObjectName("modulationLayout_2")
        self.lCarrierFreqValue = QtWidgets.QLabel(self.layoutWidget_2)
        self.lCarrierFreqValue.setObjectName("lCarrierFreqValue")
        self.modulationLayout_2.addWidget(self.lCarrierFreqValue, 1, 1, 1, 1)
        self.lModType = QtWidgets.QLabel(self.layoutWidget_2)
        self.lModType.setObjectName("lModType")
        self.modulationLayout_2.addWidget(self.lModType, 1, 2, 1, 1)
        self.lModTypeValue = QtWidgets.QLabel(self.layoutWidget_2)
        self.lModTypeValue.setObjectName("lModTypeValue")
        self.modulationLayout_2.addWidget(self.lModTypeValue, 1, 3, 1, 1)
        self.label_carrier_phase = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_carrier_phase.setObjectName("label_carrier_phase")
        self.modulationLayout_2.addWidget(self.label_carrier_phase, 2, 0, 1, 1)
        self.lCarrierPhaseValue = QtWidgets.QLabel(self.layoutWidget_2)
        self.lCarrierPhaseValue.setObjectName("lCarrierPhaseValue")
        self.modulationLayout_2.addWidget(self.lCarrierPhaseValue, 2, 1, 1, 1)
        self.lBitLength = QtWidgets.QLabel(self.layoutWidget_2)
        self.lBitLength.setObjectName("lBitLength")
        self.modulationLayout_2.addWidget(self.lBitLength, 3, 0, 1, 1)
        self.lBitLenValue = QtWidgets.QLabel(self.layoutWidget_2)
        self.lBitLenValue.setObjectName("lBitLenValue")
        self.modulationLayout_2.addWidget(self.lBitLenValue, 3, 1, 1, 1)
        self.lEncoding = QtWidgets.QLabel(self.layoutWidget_2)
        self.lEncoding.setObjectName("lEncoding")
        self.modulationLayout_2.addWidget(self.lEncoding, 0, 0, 1, 1)
        self.lEncodingValue = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lEncodingValue.sizePolicy().hasHeightForWidth())
        self.lEncodingValue.setSizePolicy(sizePolicy)
        self.lEncodingValue.setObjectName("lEncodingValue")
        self.modulationLayout_2.addWidget(self.lEncodingValue, 0, 1, 1, 1)
        self.lSampleRate = QtWidgets.QLabel(self.layoutWidget_2)
        self.lSampleRate.setObjectName("lSampleRate")
        self.modulationLayout_2.addWidget(self.lSampleRate, 0, 2, 1, 1)
        self.lSampleRateValue = QtWidgets.QLabel(self.layoutWidget_2)
        self.lSampleRateValue.setObjectName("lSampleRateValue")
        self.modulationLayout_2.addWidget(self.lSampleRateValue, 0, 3, 1, 1)
        self.lCarrierFrequency = QtWidgets.QLabel(self.layoutWidget_2)
        self.lCarrierFrequency.setObjectName("lCarrierFrequency")
        self.modulationLayout_2.addWidget(self.lCarrierFrequency, 1, 0, 1, 1)
        self.labelParameterValues = ElidedLabel(self.layoutWidget_2)
        self.labelParameterValues.setObjectName("labelParameterValues")
        self.modulationLayout_2.addWidget(self.labelParameterValues, 3, 3, 1, 1)
        self.lParamCaption = QtWidgets.QLabel(self.layoutWidget_2)
        self.lParamCaption.setObjectName("lParamCaption")
        self.modulationLayout_2.addWidget(self.lParamCaption, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.modulationLayout_2.addWidget(self.label, 2, 2, 1, 1)
        self.labelBitsPerSymbol = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelBitsPerSymbol.setObjectName("labelBitsPerSymbol")
        self.modulationLayout_2.addWidget(self.labelBitsPerSymbol, 2, 3, 1, 1)
        self.gridLayout_6.addLayout(self.modulationLayout_2, 0, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.layoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_6.addWidget(self.line, 1, 0, 1, 3)
        self.cBoxModulations = QtWidgets.QComboBox(self.layoutWidget_2)
        self.cBoxModulations.setObjectName("cBoxModulations")
        self.cBoxModulations.addItem("")
        self.gridLayout_6.addWidget(self.cBoxModulations, 2, 1, 1, 1)
        self.prBarGeneration = QtWidgets.QProgressBar(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prBarGeneration.sizePolicy().hasHeightForWidth())
        self.prBarGeneration.setSizePolicy(sizePolicy)
        self.prBarGeneration.setProperty("value", 0)
        self.prBarGeneration.setObjectName("prBarGeneration")
        self.gridLayout_6.addWidget(self.prBarGeneration, 5, 0, 1, 1)
        self.btnSend = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnSend.setEnabled(False)
        icon = QtGui.QIcon.fromTheme("media-playback-start")
        self.btnSend.setIcon(icon)
        self.btnSend.setObjectName("btnSend")
        self.gridLayout_6.addWidget(self.btnSend, 5, 2, 1, 1)
        self.btnEditModulation = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnEditModulation.setObjectName("btnEditModulation")
        self.gridLayout_6.addWidget(self.btnEditModulation, 2, 2, 1, 1)
        self.lModulation = QtWidgets.QLabel(self.layoutWidget_2)
        self.lModulation.setObjectName("lModulation")
        self.gridLayout_6.addWidget(self.lModulation, 2, 0, 1, 1)
        self.btnGenerate = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnGenerate.setEnabled(False)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.btnGenerate.setIcon(icon)
        self.btnGenerate.setObjectName("btnGenerate")
        self.gridLayout_6.addWidget(self.btnGenerate, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_6)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cbViewType = QtWidgets.QComboBox(self.layoutWidget)
        self.cbViewType.setObjectName("cbViewType")
        self.cbViewType.addItem("")
        self.cbViewType.addItem("")
        self.cbViewType.addItem("")
        self.gridLayout_2.addWidget(self.cbViewType, 2, 6, 1, 1)
        self.lViewType = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lViewType.sizePolicy().hasHeightForWidth())
        self.lViewType.setSizePolicy(sizePolicy)
        self.lViewType.setObjectName("lViewType")
        self.gridLayout_2.addWidget(self.lViewType, 2, 5, 1, 1)
        self.tableMessages = GeneratorTableView(self.layoutWidget)
        self.tableMessages.setAcceptDrops(True)
        self.tableMessages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableMessages.setDragEnabled(False)
        self.tableMessages.setDragDropOverwriteMode(False)
        self.tableMessages.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.tableMessages.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.tableMessages.setAlternatingRowColors(True)
        self.tableMessages.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableMessages.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableMessages.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableMessages.setShowGrid(False)
        self.tableMessages.setObjectName("tableMessages")
        self.tableMessages.horizontalHeader().setHighlightSections(False)
        self.tableMessages.verticalHeader().setHighlightSections(False)
        self.gridLayout_2.addWidget(self.tableMessages, 1, 0, 1, 7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelGeneratedData = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelGeneratedData.sizePolicy().hasHeightForWidth())
        self.labelGeneratedData.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelGeneratedData.setFont(font)
        self.labelGeneratedData.setAlignment(QtCore.Qt.AlignCenter)
        self.labelGeneratedData.setObjectName("labelGeneratedData")
        self.horizontalLayout.addWidget(self.labelGeneratedData)
        self.btnSave = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.btnSave.setIcon(icon)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnOpen = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpen.sizePolicy().hasHeightForWidth())
        self.btnOpen.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.btnOpen.setIcon(icon)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout.addWidget(self.btnOpen)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 7)
        self.btnNetworkSDRSend = QtWidgets.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon.fromTheme("network-wired")
        self.btnNetworkSDRSend.setIcon(icon)
        self.btnNetworkSDRSend.setCheckable(True)
        self.btnNetworkSDRSend.setObjectName("btnNetworkSDRSend")
        self.gridLayout_2.addWidget(self.btnNetworkSDRSend, 2, 0, 1, 1)
        self.btnRfCatSend = QtWidgets.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon.fromTheme("network-wireless")
        self.btnRfCatSend.setIcon(icon)
        self.btnRfCatSend.setObjectName("btnRfCatSend")
        self.gridLayout_2.addWidget(self.btnRfCatSend, 2, 1, 1, 1)
        self.lEstimatedTime = QtWidgets.QLabel(self.layoutWidget)
        self.lEstimatedTime.setObjectName("lEstimatedTime")
        self.gridLayout_2.addWidget(self.lEstimatedTime, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(38, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 3, 1, 2)
        self.verticalLayout_2.addWidget(self.splitter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(GeneratorTab)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidgetFuzzing.setCurrentIndex(0)

    def retranslateUi(self, GeneratorTab):
        _translate = QtCore.QCoreApplication.translate
        GeneratorTab.setWindowTitle(_translate("GeneratorTab", "Form"))
        self.treeProtocols.setToolTip(_translate("GeneratorTab", "<html><head/><body><p>Drag&amp;Drop Protocols to the table on the right to fill the generation table.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_proto), _translate("GeneratorTab", "Protocols"))
        self.lWPauses.setToolTip(_translate("GeneratorTab", "<html><head/><body><p>The pauses will be added automatically when you drag a protocol from the tree above to the table on the right.<br/></p><p>You can see the <span style=\" font-weight:600;\">position</span> of each pause by <span style=\" font-weight:600;\">selecting it</span>. There will be drawn a line in the table indicating the position of the pause.<br/></p><p>Use context menu or double click to <span style=\" font-weight:600;\">edit a pauses\' length</span>.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_pauses), _translate("GeneratorTab", "Pauses"))
        self.groupBox.setTitle(_translate("GeneratorTab", "Add fuzzing values to generated data"))
        self.btnFuzz.setText(_translate("GeneratorTab", "Fuzz"))
        self.rBSuccessive.setToolTip(_translate("GeneratorTab", "<html><head/><body><p>For multiple labels per message the fuzzed values are inserted <span style=\" font-weight:600;\">one-by-one</span>.</p></body></html>"))
        self.rBSuccessive.setText(_translate("GeneratorTab", "S&uccessive"))
        self.rbConcurrent.setToolTip(_translate("GeneratorTab", "<html><head/><body><p>For multiple labels per message the labels are fuzzed <span style=\" font-weight:600;\">at the same time</span>.</p></body></html>"))
        self.rbConcurrent.setText(_translate("GeneratorTab", "&Concurrent"))
        self.rBExhaustive.setToolTip(_translate("GeneratorTab", "<html><head/><body><p>For multiple labels per message the fuzzed values are inserted in <span style=\" font-weight:600;\">all possible combinations</span>.</p></body></html>"))
        self.rBExhaustive.setText(_translate("GeneratorTab", "E&xhaustive"))
        self.progressBarFuzzing.setFormat(_translate("GeneratorTab", "%v/%m"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fuzzing), _translate("GeneratorTab", "Fuzzing"))
        self.lCarrierFreqValue.setText(_translate("GeneratorTab", "TextLabel"))
        self.lModType.setText(_translate("GeneratorTab", "Modulation Type:"))
        self.lModTypeValue.setText(_translate("GeneratorTab", "TextLabel"))
        self.label_carrier_phase.setText(_translate("GeneratorTab", "Carrier Phase:"))
        self.lCarrierPhaseValue.setText(_translate("GeneratorTab", "TextLabel"))
        self.lBitLength.setText(_translate("GeneratorTab", "Symbol Length:"))
        self.lBitLenValue.setText(_translate("GeneratorTab", "TextLabel"))
        self.lEncoding.setText(_translate("GeneratorTab", "Encoding:"))
        self.lEncodingValue.setText(_translate("GeneratorTab", "-"))
        self.lSampleRate.setText(_translate("GeneratorTab", "Sample Rate:"))
        self.lSampleRateValue.setText(_translate("GeneratorTab", "TextLabel"))
        self.lCarrierFrequency.setText(_translate("GeneratorTab", "Carrier Frequency:"))
        self.labelParameterValues.setText(_translate("GeneratorTab", "0/100"))
        self.lParamCaption.setText(_translate("GeneratorTab", "Amplitudes:"))
        self.label.setText(_translate("GeneratorTab", "Bits per Symbol:"))
        self.labelBitsPerSymbol.setText(_translate("GeneratorTab", "TextLabel"))
        self.cBoxModulations.setItemText(0, _translate("GeneratorTab", "MyModulation"))
        self.prBarGeneration.setFormat(_translate("GeneratorTab", "Modulating %p%"))
        self.btnSend.setText(_translate("GeneratorTab", "Send data..."))
        self.btnEditModulation.setText(_translate("GeneratorTab", "Edit ..."))
        self.lModulation.setText(_translate("GeneratorTab", "Modulation:"))
        self.btnGenerate.setToolTip(_translate("GeneratorTab", "Generate the complex file of the modulated signal, after tuning all parameters above."))
        self.btnGenerate.setText(_translate("GeneratorTab", "Generate file..."))
        self.cbViewType.setItemText(0, _translate("GeneratorTab", "Bit"))
        self.cbViewType.setItemText(1, _translate("GeneratorTab", "Hex"))
        self.cbViewType.setItemText(2, _translate("GeneratorTab", "ASCII"))
        self.lViewType.setText(_translate("GeneratorTab", "Viewtype:"))
        self.labelGeneratedData.setText(_translate("GeneratorTab", "Generated Data"))
        self.btnSave.setToolTip(_translate("GeneratorTab", "Save current fuzz profile."))
        self.btnSave.setText(_translate("GeneratorTab", "..."))
        self.btnOpen.setToolTip(_translate("GeneratorTab", "Load a fuzz profile."))
        self.btnOpen.setText(_translate("GeneratorTab", "..."))
        self.btnNetworkSDRSend.setToolTip(_translate("GeneratorTab", "<html><head/><body><p><span style=\" font-weight:600;\">Send encoded data to your external application via TCP.</span></p></body></html>"))
        self.btnNetworkSDRSend.setText(_translate("GeneratorTab", "Send via Network"))
        self.btnRfCatSend.setToolTip(_translate("GeneratorTab", "<html><head/><body><p><span style=\" font-weight:600;\">Send encoded data via RfCat. </span></p><p><span style=\" font-style:italic;\">Hit again for stopping the sending process. Note that you can set the number of repetitions (from 1 to infinite) in:</span></p><p><span style=\" font-style:italic;\">Edit-&gt;Options-&gt;Device-&gt;\'Device sending repetitions\'</span></p></body></html>"))
        self.btnRfCatSend.setText(_translate("GeneratorTab", "Send via RfCat"))
        self.lEstimatedTime.setToolTip(_translate("GeneratorTab", "<html><head/><body><p>The estimated average time is based on the average number of bits per message and average sample rate, you set for the modulations.</p></body></html>"))
        self.lEstimatedTime.setText(_translate("GeneratorTab", "Estimated Time: "))
from urh.ui.ElidedLabel import ElidedLabel
from urh.ui.GeneratorListWidget import GeneratorListWidget
from urh.ui.views.GeneratorListView import GeneratorListView
from urh.ui.views.GeneratorTableView import GeneratorTableView
from urh.ui.views.GeneratorTreeView import GeneratorTreeView
from . import urh_rc

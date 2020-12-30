# -*- coding: utf-8 -*-

#
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogCosta(object):
    def setupUi(self, DialogCosta):
        DialogCosta.setObjectName("DialogCosta")
        DialogCosta.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogCosta)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DialogCosta)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelLoopBandwidth = QtWidgets.QLabel(DialogCosta)
        self.labelLoopBandwidth.setObjectName("labelLoopBandwidth")
        self.horizontalLayout.addWidget(self.labelLoopBandwidth)
        self.doubleSpinBoxLoopBandwidth = QtWidgets.QDoubleSpinBox(DialogCosta)
        self.doubleSpinBoxLoopBandwidth.setDecimals(4)
        self.doubleSpinBoxLoopBandwidth.setObjectName("doubleSpinBoxLoopBandwidth")
        self.horizontalLayout.addWidget(self.doubleSpinBoxLoopBandwidth)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogCosta)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(DialogCosta)
        self.buttonBox.accepted.connect(DialogCosta.accept)
        self.buttonBox.rejected.connect(DialogCosta.reject)

    def retranslateUi(self, DialogCosta):
        _translate = QtCore.QCoreApplication.translate
        DialogCosta.setWindowTitle(_translate("DialogCosta", "Configure Costas Loop"))
        self.label.setText(_translate("DialogCosta", "URH uses a Costas loop for PSK demodulation. Configure the loop bandwidth below."))
        self.labelLoopBandwidth.setText(_translate("DialogCosta", "Loop Bandwidth:"))

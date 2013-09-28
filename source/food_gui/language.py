# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'language.ui'
#
# Created: Sat Apr 13 17:21:18 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Language(object):
    def setupUi(self, Language):
        Language.setObjectName(_fromUtf8("Language"))
        Language.resize(232, 66)
        Language.setMinimumSize(QtCore.QSize(232, 66))
        self.centralwidget = QtGui.QWidget(Language)
        self.centralwidget.setMinimumSize(QtCore.QSize(232, 66))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.rus_radio = QtGui.QRadioButton(self.centralwidget)
        self.rus_radio.setMinimumSize(QtCore.QSize(100, 25))
        self.rus_radio.setMaximumSize(QtCore.QSize(16777215, 25))
        self.rus_radio.setObjectName(_fromUtf8("rus_radio"))
        self.gridLayout.addWidget(self.rus_radio, 1, 0, 1, 1)
        self.cancelbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelbut.sizePolicy().hasHeightForWidth())
        self.cancelbut.setSizePolicy(sizePolicy)
        self.cancelbut.setMinimumSize(QtCore.QSize(100, 25))
        self.cancelbut.setMaximumSize(QtCore.QSize(100, 25))
        self.cancelbut.setDefault(True)
        self.cancelbut.setObjectName(_fromUtf8("cancelbut"))
        self.gridLayout.addWidget(self.cancelbut, 1, 1, 1, 1)
        self.eng_radio = QtGui.QRadioButton(self.centralwidget)
        self.eng_radio.setMinimumSize(QtCore.QSize(100, 25))
        self.eng_radio.setMaximumSize(QtCore.QSize(16777215, 25))
        self.eng_radio.setObjectName(_fromUtf8("eng_radio"))
        self.gridLayout.addWidget(self.eng_radio, 0, 0, 1, 1)
        self.okbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okbut.sizePolicy().hasHeightForWidth())
        self.okbut.setSizePolicy(sizePolicy)
        self.okbut.setMinimumSize(QtCore.QSize(100, 25))
        self.okbut.setMaximumSize(QtCore.QSize(100, 25))
        self.okbut.setDefault(True)
        self.okbut.setObjectName(_fromUtf8("okbut"))
        self.gridLayout.addWidget(self.okbut, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        Language.setCentralWidget(self.centralwidget)

        #self.retranslateUi(Language)
        QtCore.QMetaObject.connectSlotsByName(Language)
        Language.setTabOrder(self.eng_radio, self.rus_radio)
        Language.setTabOrder(self.rus_radio, self.okbut)
        Language.setTabOrder(self.okbut, self.cancelbut)

    def retranslateUi(self, Language):
        Language.setWindowTitle(_translate("Language", "Change language", None))
        self.rus_radio.setText(_translate("Language", "Русский", None))
        self.cancelbut.setText(_translate("Language", "Отмена", None))
        self.eng_radio.setText(_translate("Language", "English", None))
        self.okbut.setText(_translate("Language", "Ok", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'language.ui'
#
# Created: Sun Jan 13 00:37:47 2013
#      by: PyQt4 UI code generator 4.9.6
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
        Language.resize(232, 68)
        self.centralwidget = QtGui.QWidget(Language)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.eng_radio = QtGui.QRadioButton(self.centralwidget)
        self.eng_radio.setGeometry(QtCore.QRect(10, 10, 99, 21))
        self.eng_radio.setObjectName(_fromUtf8("eng_radio"))
        self.rus_radio = QtGui.QRadioButton(self.centralwidget)
        self.rus_radio.setGeometry(QtCore.QRect(10, 35, 99, 21))
        self.rus_radio.setObjectName(_fromUtf8("rus_radio"))
        self.okbut = QtGui.QPushButton(self.centralwidget)
        self.okbut.setGeometry(QtCore.QRect(130, 10, 91, 24))
        self.okbut.setDefault(True)
        self.okbut.setObjectName(_fromUtf8("okbut"))
        self.cancelbut = QtGui.QPushButton(self.centralwidget)
        self.cancelbut.setGeometry(QtCore.QRect(130, 35, 91, 24))
        self.cancelbut.setDefault(True)
        self.cancelbut.setObjectName(_fromUtf8("cancelbut"))
        Language.setCentralWidget(self.centralwidget)

        self.retranslateUi(Language)
        QtCore.QMetaObject.connectSlotsByName(Language)
        Language.setTabOrder(self.eng_radio, self.rus_radio)
        Language.setTabOrder(self.rus_radio, self.okbut)
        Language.setTabOrder(self.okbut, self.cancelbut)

    def retranslateUi(self, Language):
        Language.setWindowTitle(_translate("Language", "Change language", None))
        self.eng_radio.setText(_translate("Language", "English", None))
        self.rus_radio.setText(_translate("Language", "Русский", None))
        self.okbut.setText(_translate("Language", "Ok", None))
        self.cancelbut.setText(_translate("Language", "Отмена", None))


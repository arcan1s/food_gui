# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notfound.ui'
#
# Created: Fri Jan 11 17:32:12 2013
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

class Ui_NotFound(object):
    def setupUi(self, NotFound):
        NotFound.setObjectName(_fromUtf8("NotFound"))
        NotFound.resize(320, 90)
        self.centralwidget = QtGui.QWidget(NotFound)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 291, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.okbut = QtGui.QPushButton(self.centralwidget)
        self.okbut.setGeometry(QtCore.QRect(110, 60, 95, 24))
        self.okbut.setDefault(True)
        self.okbut.setObjectName(_fromUtf8("okbut"))
        NotFound.setCentralWidget(self.centralwidget)

        self.retranslateUi(NotFound)
        QtCore.QObject.connect(self.okbut, QtCore.SIGNAL(_fromUtf8("clicked()")), NotFound.close)
        QtCore.QMetaObject.connectSlotsByName(NotFound)

    def retranslateUi(self, NotFound):
        NotFound.setWindowTitle(_translate("NotFound", "Ошибка!", None))
        self.label.setText(_translate("NotFound", "<html><head/><body><p align=\"justify\">Продукт %s не найден в базе данных</p></body></html>", None))
        self.okbut.setText(_translate("NotFound", "Ok", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'complete.ui'
#
# Created: Sat Jan 12 20:43:49 2013
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

class Ui_Complete_Window(object):
    def setupUi(self, Complete_Window):
        Complete_Window.setObjectName(_fromUtf8("Complete_Window"))
        Complete_Window.resize(311, 259)
        self.centralwidget = QtGui.QWidget(Complete_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.list = QtGui.QListWidget(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(10, 10, 291, 211))
        self.list.setObjectName(_fromUtf8("list"))
        self.exitbut = QtGui.QPushButton(self.centralwidget)
        self.exitbut.setGeometry(QtCore.QRect(210, 225, 91, 24))
        self.exitbut.setDefault(True)
        self.exitbut.setObjectName(_fromUtf8("exitbut"))
        Complete_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Complete_Window)
        QtCore.QObject.connect(self.exitbut, QtCore.SIGNAL(_fromUtf8("clicked()")), Complete_Window.close)
        QtCore.QMetaObject.connectSlotsByName(Complete_Window)

    def retranslateUi(self, Complete_Window):
        Complete_Window.setWindowTitle(_translate("Complete_Window", "Подставить", None))
        self.exitbut.setText(_translate("Complete_Window", "Закрыть", None))


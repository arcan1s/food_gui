# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'complete.ui'
#
# Created: Sat Apr 13 17:00:51 2013
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

class Ui_Complete_Window(object):
    def setupUi(self, Complete_Window):
        Complete_Window.setObjectName(_fromUtf8("Complete_Window"))
        Complete_Window.resize(311, 259)
        Complete_Window.setMinimumSize(QtCore.QSize(311, 259))
        self.centralwidget = QtGui.QWidget(Complete_Window)
        self.centralwidget.setMinimumSize(QtCore.QSize(311, 259))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.list = QtGui.QListWidget(self.centralwidget)
        self.list.setMinimumSize(QtCore.QSize(291, 211))
        self.list.setObjectName(_fromUtf8("list"))
        self.gridLayout.addWidget(self.list, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.exitbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbut.sizePolicy().hasHeightForWidth())
        self.exitbut.setSizePolicy(sizePolicy)
        self.exitbut.setMinimumSize(QtCore.QSize(100, 25))
        self.exitbut.setMaximumSize(QtCore.QSize(100, 25))
        self.exitbut.setDefault(True)
        self.exitbut.setObjectName(_fromUtf8("exitbut"))
        self.horizontalLayout.addWidget(self.exitbut)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        Complete_Window.setCentralWidget(self.centralwidget)

        #self.retranslateUi(Complete_Window)
        QtCore.QMetaObject.connectSlotsByName(Complete_Window)

    def retranslateUi(self, Complete_Window):
        Complete_Window.setWindowTitle(_translate("Complete_Window", "Подставить", None))
        self.exitbut.setText(_translate("Complete_Window", "Закрыть", None))


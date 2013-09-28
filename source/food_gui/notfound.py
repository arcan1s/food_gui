# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notfound.ui'
#
# Created: Sat Apr 13 17:23:56 2013
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

class Ui_NotFound(object):
    def setupUi(self, NotFound):
        NotFound.setObjectName(_fromUtf8("NotFound"))
        NotFound.resize(320, 89)
        NotFound.setMinimumSize(QtCore.QSize(320, 89))
        self.centralwidget = QtGui.QWidget(NotFound)
        self.centralwidget.setMinimumSize(QtCore.QSize(320, 89))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
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
        self.horizontalLayout.addWidget(self.okbut)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        NotFound.setCentralWidget(self.centralwidget)

        #self.retranslateUi(NotFound)
        QtCore.QMetaObject.connectSlotsByName(NotFound)

    def retranslateUi(self, NotFound):
        NotFound.setWindowTitle(_translate("NotFound", "Ошибка!", None))
        self.label.setText(_translate("NotFound", "<html><head/><body><p align=\"justify\">Продукт %s не найден в базе данных</p></body></html>", None))
        self.okbut.setText(_translate("NotFound", "Ok", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbselect.ui'
#
# Created: Sat Apr 13 17:07:09 2013
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

class Ui_DB_Select(object):
    def setupUi(self, DB_Select):
        DB_Select.setObjectName(_fromUtf8("DB_Select"))
        DB_Select.resize(422, 70)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DB_Select.sizePolicy().hasHeightForWidth())
        DB_Select.setSizePolicy(sizePolicy)
        DB_Select.setMinimumSize(QtCore.QSize(422, 70))
        self.centralwidget = QtGui.QWidget(DB_Select)
        self.centralwidget.setMinimumSize(QtCore.QSize(422, 70))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dbstring = QtGui.QLineEdit(self.centralwidget)
        self.dbstring.setMinimumSize(QtCore.QSize(100, 25))
        self.dbstring.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dbstring.setObjectName(_fromUtf8("dbstring"))
        self.horizontalLayout.addWidget(self.dbstring)
        self.dbsearch = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbsearch.sizePolicy().hasHeightForWidth())
        self.dbsearch.setSizePolicy(sizePolicy)
        self.dbsearch.setMinimumSize(QtCore.QSize(100, 25))
        self.dbsearch.setMaximumSize(QtCore.QSize(100, 25))
        self.dbsearch.setDefault(True)
        self.dbsearch.setObjectName(_fromUtf8("dbsearch"))
        self.horizontalLayout.addWidget(self.dbsearch)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.dbselect = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbselect.sizePolicy().hasHeightForWidth())
        self.dbselect.setSizePolicy(sizePolicy)
        self.dbselect.setMinimumSize(QtCore.QSize(100, 25))
        self.dbselect.setMaximumSize(QtCore.QSize(100, 25))
        self.dbselect.setDefault(True)
        self.dbselect.setObjectName(_fromUtf8("dbselect"))
        self.horizontalLayout_2.addWidget(self.dbselect)
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
        self.horizontalLayout_2.addWidget(self.cancelbut)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 3, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        DB_Select.setCentralWidget(self.centralwidget)

        #self.retranslateUi(DB_Select)
        QtCore.QMetaObject.connectSlotsByName(DB_Select)

    def retranslateUi(self, DB_Select):
        DB_Select.setWindowTitle(_translate("DB_Select", "Выбор базы данных", None))
        self.dbsearch.setText(_translate("DB_Select", "Обзор", None))
        self.dbselect.setText(_translate("DB_Select", "Ok", None))
        self.cancelbut.setText(_translate("DB_Select", "Отмена", None))


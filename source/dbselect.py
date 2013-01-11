# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbselect.ui'
#
# Created: Fri Jan 11 20:50:31 2013
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

class Ui_DB_Select(object):
    def setupUi(self, DB_Select):
        DB_Select.setObjectName(_fromUtf8("DB_Select"))
        DB_Select.resize(422, 71)
        self.centralwidget = QtGui.QWidget(DB_Select)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.dbselect = QtGui.QPushButton(self.centralwidget)
        self.dbselect.setGeometry(QtCore.QRect(360, 10, 51, 24))
        self.dbselect.setDefault(True)
        self.dbselect.setObjectName(_fromUtf8("dbselect"))
        self.dbsearch = QtGui.QPushButton(self.centralwidget)
        self.dbsearch.setGeometry(QtCore.QRect(285, 10, 71, 24))
        self.dbsearch.setDefault(True)
        self.dbsearch.setObjectName(_fromUtf8("dbsearch"))
        self.dbstring = QtGui.QLineEdit(self.centralwidget)
        self.dbstring.setGeometry(QtCore.QRect(10, 10, 271, 23))
        self.dbstring.setObjectName(_fromUtf8("dbstring"))
        self.cancelbut = QtGui.QPushButton(self.centralwidget)
        self.cancelbut.setGeometry(QtCore.QRect(320, 40, 91, 24))
        self.cancelbut.setDefault(True)
        self.cancelbut.setObjectName(_fromUtf8("cancelbut"))
        DB_Select.setCentralWidget(self.centralwidget)

        self.retranslateUi(DB_Select)
        QtCore.QObject.connect(self.cancelbut, QtCore.SIGNAL(_fromUtf8("clicked()")), DB_Select.close)
        QtCore.QMetaObject.connectSlotsByName(DB_Select)
        DB_Select.setTabOrder(self.dbstring, self.dbsearch)
        DB_Select.setTabOrder(self.dbsearch, self.dbselect)
        DB_Select.setTabOrder(self.dbselect, self.cancelbut)

    def retranslateUi(self, DB_Select):
        DB_Select.setWindowTitle(_translate("DB_Select", "Выбор базы данных", None))
        self.dbselect.setText(_translate("DB_Select", "Ok", None))
        self.dbsearch.setText(_translate("DB_Select", "Обзор", None))
        self.cancelbut.setText(_translate("DB_Select", "Отмена", None))


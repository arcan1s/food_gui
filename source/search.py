# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created: Sun Jan 13 03:19:23 2013
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

class Ui_Search_Window(object):
    def setupUi(self, Search_Window):
        Search_Window.setObjectName(_fromUtf8("Search_Window"))
        Search_Window.resize(322, 329)
        self.centralwidget = QtGui.QWidget(Search_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.search_box = QtGui.QTextBrowser(self.centralwidget)
        self.search_box.setGeometry(QtCore.QRect(10, 60, 301, 231))
        self.search_box.setObjectName(_fromUtf8("search_box"))
        self.exitbut = QtGui.QPushButton(self.centralwidget)
        self.exitbut.setGeometry(QtCore.QRect(220, 295, 91, 24))
        self.exitbut.setDefault(True)
        self.exitbut.setObjectName(_fromUtf8("exitbut"))
        self.search_line = QtGui.QLineEdit(self.centralwidget)
        self.search_line.setGeometry(QtCore.QRect(10, 10, 301, 23))
        self.search_line.setText(_fromUtf8(""))
        self.search_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.search_line.setObjectName(_fromUtf8("search_line"))
        self.searchbut = QtGui.QPushButton(self.centralwidget)
        self.searchbut.setGeometry(QtCore.QRect(220, 35, 91, 24))
        self.searchbut.setDefault(True)
        self.searchbut.setObjectName(_fromUtf8("searchbut"))
        Search_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Search_Window)
        QtCore.QMetaObject.connectSlotsByName(Search_Window)
        Search_Window.setTabOrder(self.search_line, self.searchbut)
        Search_Window.setTabOrder(self.searchbut, self.search_box)
        Search_Window.setTabOrder(self.search_box, self.exitbut)

    def retranslateUi(self, Search_Window):
        Search_Window.setWindowTitle(_translate("Search_Window", "Поиск", None))
        self.exitbut.setText(_translate("Search_Window", "Закрыть", None))
        self.searchbut.setText(_translate("Search_Window", "Искать", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created: Sat Apr 13 17:26:03 2013
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

class Ui_Search_Window(object):
    def setupUi(self, Search_Window):
        Search_Window.setObjectName(_fromUtf8("Search_Window"))
        Search_Window.resize(322, 330)
        Search_Window.setMinimumSize(QtCore.QSize(322, 330))
        self.centralwidget = QtGui.QWidget(Search_Window)
        self.centralwidget.setMinimumSize(QtCore.QSize(322, 330))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.search_line = QtGui.QLineEdit(self.centralwidget)
        self.search_line.setMinimumSize(QtCore.QSize(100, 25))
        self.search_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.search_line.setText(_fromUtf8(""))
        self.search_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.search_line.setObjectName(_fromUtf8("search_line"))
        self.gridLayout.addWidget(self.search_line, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.searchbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchbut.sizePolicy().hasHeightForWidth())
        self.searchbut.setSizePolicy(sizePolicy)
        self.searchbut.setMinimumSize(QtCore.QSize(100, 25))
        self.searchbut.setMaximumSize(QtCore.QSize(100, 25))
        self.searchbut.setDefault(True)
        self.searchbut.setObjectName(_fromUtf8("searchbut"))
        self.horizontalLayout.addWidget(self.searchbut)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.search_box = QtGui.QTextBrowser(self.centralwidget)
        self.search_box.setMinimumSize(QtCore.QSize(301, 231))
        self.search_box.setObjectName(_fromUtf8("search_box"))
        self.gridLayout.addWidget(self.search_box, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
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
        self.horizontalLayout_2.addWidget(self.exitbut)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        Search_Window.setCentralWidget(self.centralwidget)

        #self.retranslateUi(Search_Window)
        QtCore.QMetaObject.connectSlotsByName(Search_Window)
        Search_Window.setTabOrder(self.search_line, self.search_box)

    def retranslateUi(self, Search_Window):
        Search_Window.setWindowTitle(_translate("Search_Window", "Поиск", None))
        self.searchbut.setText(_translate("Search_Window", "Искать", None))
        self.exitbut.setText(_translate("Search_Window", "Закрыть", None))


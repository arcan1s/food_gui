# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbcp.ui'
#
# Created: Sat Apr 13 17:04:04 2013
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

class Ui_db_cp_window(object):
    def setupUi(self, db_cp_window):
        db_cp_window.setObjectName(_fromUtf8("db_cp_window"))
        db_cp_window.resize(451, 101)
        db_cp_window.setMinimumSize(QtCore.QSize(451, 101))
        self.centralwidget = QtGui.QWidget(db_cp_window)
        self.centralwidget.setMinimumSize(QtCore.QSize(451, 101))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.old_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.old_lab.sizePolicy().hasHeightForWidth())
        self.old_lab.setSizePolicy(sizePolicy)
        self.old_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.old_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.old_lab.setObjectName(_fromUtf8("old_lab"))
        self.horizontalLayout.addWidget(self.old_lab)
        self.old_line = QtGui.QLineEdit(self.centralwidget)
        self.old_line.setMinimumSize(QtCore.QSize(100, 25))
        self.old_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.old_line.setObjectName(_fromUtf8("old_line"))
        self.horizontalLayout.addWidget(self.old_line)
        self.oldbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldbut.sizePolicy().hasHeightForWidth())
        self.oldbut.setSizePolicy(sizePolicy)
        self.oldbut.setMinimumSize(QtCore.QSize(100, 25))
        self.oldbut.setMaximumSize(QtCore.QSize(100, 25))
        self.oldbut.setObjectName(_fromUtf8("oldbut"))
        self.horizontalLayout.addWidget(self.oldbut)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.new_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_lab.sizePolicy().hasHeightForWidth())
        self.new_lab.setSizePolicy(sizePolicy)
        self.new_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.new_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.new_lab.setObjectName(_fromUtf8("new_lab"))
        self.horizontalLayout_2.addWidget(self.new_lab)
        self.new_line = QtGui.QLineEdit(self.centralwidget)
        self.new_line.setMinimumSize(QtCore.QSize(100, 25))
        self.new_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.new_line.setObjectName(_fromUtf8("new_line"))
        self.horizontalLayout_2.addWidget(self.new_line)
        self.newbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newbut.sizePolicy().hasHeightForWidth())
        self.newbut.setSizePolicy(sizePolicy)
        self.newbut.setMinimumSize(QtCore.QSize(100, 25))
        self.newbut.setMaximumSize(QtCore.QSize(100, 25))
        self.newbut.setObjectName(_fromUtf8("newbut"))
        self.horizontalLayout_2.addWidget(self.newbut)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.okbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okbut.sizePolicy().hasHeightForWidth())
        self.okbut.setSizePolicy(sizePolicy)
        self.okbut.setMinimumSize(QtCore.QSize(100, 25))
        self.okbut.setMaximumSize(QtCore.QSize(100, 25))
        self.okbut.setObjectName(_fromUtf8("okbut"))
        self.horizontalLayout_3.addWidget(self.okbut)
        self.cancelbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelbut.sizePolicy().hasHeightForWidth())
        self.cancelbut.setSizePolicy(sizePolicy)
        self.cancelbut.setMinimumSize(QtCore.QSize(100, 25))
        self.cancelbut.setMaximumSize(QtCore.QSize(100, 25))
        self.cancelbut.setObjectName(_fromUtf8("cancelbut"))
        self.horizontalLayout_3.addWidget(self.cancelbut)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        db_cp_window.setCentralWidget(self.centralwidget)

        #self.retranslateUi(db_cp_window)
        QtCore.QMetaObject.connectSlotsByName(db_cp_window)

    def retranslateUi(self, db_cp_window):
        db_cp_window.setWindowTitle(_translate("db_cp_window", "Скопировать базу данных", None))
        self.old_lab.setText(_translate("db_cp_window", "Старый файл", None))
        self.oldbut.setText(_translate("db_cp_window", "Обзор", None))
        self.new_lab.setText(_translate("db_cp_window", "Новый файл", None))
        self.newbut.setText(_translate("db_cp_window", "Обзор", None))
        self.okbut.setText(_translate("db_cp_window", "Ok", None))
        self.cancelbut.setText(_translate("db_cp_window", "Отмена", None))


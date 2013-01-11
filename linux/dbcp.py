# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbcp.ui'
#
# Created: Fri Jan 11 17:31:54 2013
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

class Ui_db_cp_window(object):
    def setupUi(self, db_cp_window):
        db_cp_window.setObjectName(_fromUtf8("db_cp_window"))
        db_cp_window.resize(451, 103)
        self.centralwidget = QtGui.QWidget(db_cp_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.oldbut = QtGui.QPushButton(self.centralwidget)
        self.oldbut.setGeometry(QtCore.QRect(345, 10, 95, 24))
        self.oldbut.setObjectName(_fromUtf8("oldbut"))
        self.newbut = QtGui.QPushButton(self.centralwidget)
        self.newbut.setGeometry(QtCore.QRect(345, 35, 95, 24))
        self.newbut.setObjectName(_fromUtf8("newbut"))
        self.cancelbut = QtGui.QPushButton(self.centralwidget)
        self.cancelbut.setGeometry(QtCore.QRect(350, 70, 81, 24))
        self.cancelbut.setObjectName(_fromUtf8("cancelbut"))
        self.okbut = QtGui.QPushButton(self.centralwidget)
        self.okbut.setGeometry(QtCore.QRect(260, 70, 81, 24))
        self.okbut.setObjectName(_fromUtf8("okbut"))
        self.old_line = QtGui.QLineEdit(self.centralwidget)
        self.old_line.setGeometry(QtCore.QRect(100, 10, 241, 23))
        self.old_line.setObjectName(_fromUtf8("old_line"))
        self.new_line = QtGui.QLineEdit(self.centralwidget)
        self.new_line.setGeometry(QtCore.QRect(100, 35, 241, 23))
        self.new_line.setObjectName(_fromUtf8("new_line"))
        self.old_lab = QtGui.QLabel(self.centralwidget)
        self.old_lab.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.old_lab.setObjectName(_fromUtf8("old_lab"))
        self.new_lab = QtGui.QLabel(self.centralwidget)
        self.new_lab.setGeometry(QtCore.QRect(10, 35, 91, 21))
        self.new_lab.setObjectName(_fromUtf8("new_lab"))
        db_cp_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(db_cp_window)
        QtCore.QObject.connect(self.cancelbut, QtCore.SIGNAL(_fromUtf8("clicked()")), db_cp_window.close)
        QtCore.QMetaObject.connectSlotsByName(db_cp_window)
        db_cp_window.setTabOrder(self.old_line, self.oldbut)
        db_cp_window.setTabOrder(self.oldbut, self.new_line)
        db_cp_window.setTabOrder(self.new_line, self.newbut)
        db_cp_window.setTabOrder(self.newbut, self.okbut)
        db_cp_window.setTabOrder(self.okbut, self.cancelbut)

    def retranslateUi(self, db_cp_window):
        db_cp_window.setWindowTitle(_translate("db_cp_window", "Скопировать базу данных", None))
        self.oldbut.setText(_translate("db_cp_window", "Обзор", None))
        self.newbut.setText(_translate("db_cp_window", "Обзор", None))
        self.cancelbut.setText(_translate("db_cp_window", "Отмена", None))
        self.okbut.setText(_translate("db_cp_window", "Ok", None))
        self.old_lab.setText(_translate("db_cp_window", "Старый файл", None))
        self.new_lab.setText(_translate("db_cp_window", "Новый файл", None))


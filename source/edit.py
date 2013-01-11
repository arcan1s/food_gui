# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit.ui'
#
# Created: Fri Jan 11 17:32:00 2013
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

class Ui_Edit(object):
    def setupUi(self, Edit):
        Edit.setObjectName(_fromUtf8("Edit"))
        Edit.resize(321, 200)
        self.centralwidget = QtGui.QWidget(Edit)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.cancelbut = QtGui.QPushButton(self.centralwidget)
        self.cancelbut.setGeometry(QtCore.QRect(230, 170, 81, 24))
        self.cancelbut.setDefault(True)
        self.cancelbut.setObjectName(_fromUtf8("cancelbut"))
        self.okbut = QtGui.QPushButton(self.centralwidget)
        self.okbut.setGeometry(QtCore.QRect(145, 170, 81, 24))
        self.okbut.setDefault(True)
        self.okbut.setObjectName(_fromUtf8("okbut"))
        self.search_line = QtGui.QLineEdit(self.centralwidget)
        self.search_line.setGeometry(QtCore.QRect(80, 10, 231, 23))
        self.search_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.search_line.setObjectName(_fromUtf8("search_line"))
        self.carb_line = QtGui.QLineEdit(self.centralwidget)
        self.carb_line.setGeometry(QtCore.QRect(82, 90, 231, 23))
        self.carb_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.carb_line.setObjectName(_fromUtf8("carb_line"))
        self.prot_line = QtGui.QLineEdit(self.centralwidget)
        self.prot_line.setGeometry(QtCore.QRect(82, 40, 231, 23))
        self.prot_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prot_line.setObjectName(_fromUtf8("prot_line"))
        self.lip_line = QtGui.QLineEdit(self.centralwidget)
        self.lip_line.setGeometry(QtCore.QRect(82, 65, 231, 23))
        self.lip_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lip_line.setObjectName(_fromUtf8("lip_line"))
        self.ccal_line = QtGui.QLineEdit(self.centralwidget)
        self.ccal_line.setGeometry(QtCore.QRect(162, 115, 151, 23))
        self.ccal_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ccal_line.setObjectName(_fromUtf8("ccal_line"))
        self.glyc_line = QtGui.QLineEdit(self.centralwidget)
        self.glyc_line.setGeometry(QtCore.QRect(162, 140, 151, 23))
        self.glyc_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.glyc_line.setObjectName(_fromUtf8("glyc_line"))
        self.deletebut = QtGui.QPushButton(self.centralwidget)
        self.deletebut.setGeometry(QtCore.QRect(10, 170, 81, 24))
        self.deletebut.setDefault(True)
        self.deletebut.setObjectName(_fromUtf8("deletebut"))
        self.prot_lab = QtGui.QLabel(self.centralwidget)
        self.prot_lab.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.prot_lab.setObjectName(_fromUtf8("prot_lab"))
        self.lip_lab = QtGui.QLabel(self.centralwidget)
        self.lip_lab.setGeometry(QtCore.QRect(10, 65, 71, 21))
        self.lip_lab.setObjectName(_fromUtf8("lip_lab"))
        self.carb_lab = QtGui.QLabel(self.centralwidget)
        self.carb_lab.setGeometry(QtCore.QRect(10, 90, 71, 21))
        self.carb_lab.setObjectName(_fromUtf8("carb_lab"))
        self.ccal_lab = QtGui.QLabel(self.centralwidget)
        self.ccal_lab.setGeometry(QtCore.QRect(10, 115, 151, 21))
        self.ccal_lab.setObjectName(_fromUtf8("ccal_lab"))
        self.glyc_lab = QtGui.QLabel(self.centralwidget)
        self.glyc_lab.setGeometry(QtCore.QRect(10, 140, 151, 21))
        self.glyc_lab.setObjectName(_fromUtf8("glyc_lab"))
        self.subs_lab = QtGui.QLabel(self.centralwidget)
        self.subs_lab.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.subs_lab.setObjectName(_fromUtf8("subs_lab"))
        Edit.setCentralWidget(self.centralwidget)

        self.retranslateUi(Edit)
        QtCore.QObject.connect(self.cancelbut, QtCore.SIGNAL(_fromUtf8("clicked()")), Edit.close)
        QtCore.QMetaObject.connectSlotsByName(Edit)
        Edit.setTabOrder(self.search_line, self.prot_line)
        Edit.setTabOrder(self.prot_line, self.lip_line)
        Edit.setTabOrder(self.lip_line, self.carb_line)
        Edit.setTabOrder(self.carb_line, self.ccal_line)
        Edit.setTabOrder(self.ccal_line, self.glyc_line)
        Edit.setTabOrder(self.glyc_line, self.deletebut)
        Edit.setTabOrder(self.deletebut, self.okbut)
        Edit.setTabOrder(self.okbut, self.cancelbut)

    def retranslateUi(self, Edit):
        Edit.setWindowTitle(_translate("Edit", "Редактировать", None))
        self.cancelbut.setText(_translate("Edit", "Отмена", None))
        self.okbut.setText(_translate("Edit", "Ok", None))
        self.deletebut.setText(_translate("Edit", "Удалить", None))
        self.prot_lab.setText(_translate("Edit", "Белки", None))
        self.lip_lab.setText(_translate("Edit", "Жиры", None))
        self.carb_lab.setText(_translate("Edit", "Углеводы", None))
        self.ccal_lab.setText(_translate("Edit", "Калорийность, ккал", None))
        self.glyc_lab.setText(_translate("Edit", "Гликемический индекс", None))
        self.subs_lab.setText(_translate("Edit", "Продукт", None))


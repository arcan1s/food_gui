# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created: Fri Jan 11 17:37:59 2013
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

class Ui_Add(object):
    def setupUi(self, Add):
        Add.setObjectName(_fromUtf8("Add"))
        Add.resize(321, 193)
        self.centralwidget = QtGui.QWidget(Add)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.cancelbut = QtGui.QPushButton(self.centralwidget)
        self.cancelbut.setGeometry(QtCore.QRect(230, 165, 81, 24))
        self.cancelbut.setDefault(True)
        self.cancelbut.setObjectName(_fromUtf8("cancelbut"))
        self.okbut = QtGui.QPushButton(self.centralwidget)
        self.okbut.setGeometry(QtCore.QRect(145, 165, 81, 24))
        self.okbut.setDefault(True)
        self.okbut.setObjectName(_fromUtf8("okbut"))
        self.prot_line = QtGui.QLineEdit(self.centralwidget)
        self.prot_line.setGeometry(QtCore.QRect(82, 35, 231, 23))
        self.prot_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prot_line.setObjectName(_fromUtf8("prot_line"))
        self.lip_line = QtGui.QLineEdit(self.centralwidget)
        self.lip_line.setGeometry(QtCore.QRect(82, 60, 231, 23))
        self.lip_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lip_line.setObjectName(_fromUtf8("lip_line"))
        self.carb_line = QtGui.QLineEdit(self.centralwidget)
        self.carb_line.setGeometry(QtCore.QRect(82, 85, 231, 23))
        self.carb_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.carb_line.setObjectName(_fromUtf8("carb_line"))
        self.ccal_line = QtGui.QLineEdit(self.centralwidget)
        self.ccal_line.setGeometry(QtCore.QRect(162, 110, 151, 23))
        self.ccal_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ccal_line.setObjectName(_fromUtf8("ccal_line"))
        self.glyc_line = QtGui.QLineEdit(self.centralwidget)
        self.glyc_line.setGeometry(QtCore.QRect(162, 135, 151, 23))
        self.glyc_line.setText(_fromUtf8(""))
        self.glyc_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.glyc_line.setObjectName(_fromUtf8("glyc_line"))
        self.subs_lab = QtGui.QLabel(self.centralwidget)
        self.subs_lab.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.subs_lab.setObjectName(_fromUtf8("subs_lab"))
        self.prot_lab = QtGui.QLabel(self.centralwidget)
        self.prot_lab.setGeometry(QtCore.QRect(10, 35, 61, 21))
        self.prot_lab.setObjectName(_fromUtf8("prot_lab"))
        self.lip_lab = QtGui.QLabel(self.centralwidget)
        self.lip_lab.setGeometry(QtCore.QRect(10, 60, 61, 20))
        self.lip_lab.setObjectName(_fromUtf8("lip_lab"))
        self.carb_lab = QtGui.QLabel(self.centralwidget)
        self.carb_lab.setGeometry(QtCore.QRect(10, 85, 61, 21))
        self.carb_lab.setObjectName(_fromUtf8("carb_lab"))
        self.ccal_lab = QtGui.QLabel(self.centralwidget)
        self.ccal_lab.setGeometry(QtCore.QRect(10, 110, 151, 21))
        self.ccal_lab.setObjectName(_fromUtf8("ccal_lab"))
        self.glyc_lab = QtGui.QLabel(self.centralwidget)
        self.glyc_lab.setGeometry(QtCore.QRect(10, 135, 151, 21))
        self.glyc_lab.setObjectName(_fromUtf8("glyc_lab"))
        self.subs_line = QtGui.QLineEdit(self.centralwidget)
        self.subs_line.setGeometry(QtCore.QRect(82, 10, 231, 23))
        self.subs_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.subs_line.setObjectName(_fromUtf8("subs_line"))
        Add.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add)
        QtCore.QObject.connect(self.cancelbut, QtCore.SIGNAL(_fromUtf8("clicked()")), Add.close)
        QtCore.QMetaObject.connectSlotsByName(Add)
        Add.setTabOrder(self.subs_line, self.prot_line)
        Add.setTabOrder(self.prot_line, self.lip_line)
        Add.setTabOrder(self.lip_line, self.carb_line)
        Add.setTabOrder(self.carb_line, self.ccal_line)
        Add.setTabOrder(self.ccal_line, self.glyc_line)
        Add.setTabOrder(self.glyc_line, self.okbut)
        Add.setTabOrder(self.okbut, self.cancelbut)

    def retranslateUi(self, Add):
        Add.setWindowTitle(_translate("Add", "Добавить", None))
        self.cancelbut.setText(_translate("Add", "Отмена", None))
        self.okbut.setText(_translate("Add", "Ok", None))
        self.subs_lab.setText(_translate("Add", "Продукт", None))
        self.prot_lab.setText(_translate("Add", "Белки", None))
        self.lip_lab.setText(_translate("Add", "Жиры", None))
        self.carb_lab.setText(_translate("Add", "Углеводы", None))
        self.ccal_lab.setText(_translate("Add", "Калорийность, ккал", None))
        self.glyc_lab.setText(_translate("Add", "Гликемический индекс", None))


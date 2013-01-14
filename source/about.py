# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Sun Jan 13 03:31:10 2013
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

class Ui_About_Window(object):
    def setupUi(self, About_Window):
        About_Window.setObjectName(_fromUtf8("About_Window"))
        About_Window.resize(361, 236)
        self.centralwidget = QtGui.QWidget(About_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.about = QtGui.QTextBrowser(self.centralwidget)
        self.about.setEnabled(True)
        self.about.setGeometry(QtCore.QRect(0, 0, 361, 211))
        self.about.setFocusPolicy(QtCore.Qt.NoFocus)
        self.about.setAutoFillBackground(True)
        self.about.setObjectName(_fromUtf8("about"))
        self.exit = QtGui.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(260, 210, 95, 24))
        self.exit.setDefault(True)
        self.exit.setObjectName(_fromUtf8("exit"))
        About_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(About_Window)
        QtCore.QObject.connect(self.exit, QtCore.SIGNAL(_fromUtf8("clicked()")), About_Window.close)
        QtCore.QMetaObject.connectSlotsByName(About_Window)

    def retranslateUi(self, About_Window):
        About_Window.setWindowTitle(_translate("About_Window", "О программе", None))
        self.about.setHtml(_translate("About_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Food 1.1.0</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Лицензия: GPL</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Простенькая программа-калькулятор на питоне, подсчитывающая БЖУ, калорийность и гликемический индекс употребляемых продуктов на основании базы данных.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Автор: Евгений Алексеев aka arcanis</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e-mail: esalexeev@gmail.com</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jabber: arcanis@jabber.ru</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ICQ: 407-398-235</p></body></html>", None))
        self.exit.setText(_translate("About_Window", "Закрыть", None))


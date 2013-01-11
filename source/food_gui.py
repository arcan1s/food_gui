#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
 
import numpy,  os, shutil,  sys
from PyQt4 import QtCore, QtGui
from mainwin import Ui_Food
from about import Ui_About_Window
from add import Ui_Add
from notfound import Ui_NotFound
from edit import Ui_Edit
from dbcp import Ui_db_cp_window
from calcwin import Ui_Calc_Window
from dbselect import Ui_DB_Select

db = "db.dat"


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


class AboutWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_About_Window()
        self.ui.setupUi(self)


class DBselWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        global db
        
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_DB_Select()
        self.ui.setupUi(self)
        
        QtCore.QObject.connect(self.ui.dbsearch, QtCore.SIGNAL("clicked()"), self.db_select)
        QtCore.QObject.connect(self.ui.dbselect, QtCore.SIGNAL("clicked()"), self.db_set)
        
    def db_select(self):
        global db
        
        db_name = QtGui.QFileDialog.getOpenFileNames(self, u'Select Database file','','Datafile (*.dat);;All files (*)')
        if (len(db_name) > 0):
            dbfile_string = QtCore.QString(u'')
            for liter in db_name:
                dbfile_string.append(liter)
            self.ui.dbstring.setText(dbfile_string)
            db = dbfile_string

    def db_set(self):
        global db
        
        if (len(self.ui.dbstring.text()) > 0):
            dbfile_string = self.ui.dbstring.text()
            
            if (sys.platform[0:3] == 'win'):
                config_new = os.getcwd()+"\\food_gui.ini"
                config_old = os.getcwd()+"/food_gui.ini.bckp"
            else:
                config_new = os.getcwd()+"/food_gui.ini"
                config_old = os.getcwd()+"/food_gui.ini.bckp"
            os.rename(config_new,  config_old)
            
            with open(config_old,  'r') as config_old_file:
                with open(config_new,  'w') as config_new_file:
                    for line in config_old_file:
                        if (line.split('=')[0] == 'DATABASE'):
                            config_new_file.write('DATABASE='+dbfile_string+'=\n')
                        else:
                            config_new_file.write(line)
            
            mainwin = MainWindow()
            mainwin.database()
            os.remove (config_old)
            self.close()
    

class DBcpWindow(QtGui.QMainWindow):
    def __init__(self,  parent=None):
        global db
        
        QtGui.QMainWindow.__init__(self,  parent)
        self.ui = Ui_db_cp_window()
        self.ui.setupUi(self)
        
        if (sys.platform[0:3] == 'win'):
            db_new = os.getcwd()+"\\db_new.dat"
        else:
            db_new = os.getcwd()+"/db_new.dat"
        db_old = db
        self.ui.new_line.setText(db_new)
        self.ui.old_line.setText(db_old)
        
        QtCore.QObject.connect(self.ui.oldbut, QtCore.SIGNAL("clicked()"), self.old_select)
        QtCore.QObject.connect(self.ui.newbut, QtCore.SIGNAL("clicked()"), self.new_select)
        QtCore.QObject.connect(self.ui.okbut, QtCore.SIGNAL("clicked()"), self.dbcp)
    
    def old_select(self):
        db_old = QtGui.QFileDialog.getOpenFileNames(self, u'Select old Database file','','Datafile (*.dat);;All files (*)')
        if (len(db_old) > 0):
            db_old_string = QtCore.QString(u'')
            for liter in db_old:
                db_old_string.append(liter)
            self.ui.old_line.setText(db_old_string)
    
    def new_select(self):
        db_new = QtGui.QFileDialog.getSaveFileName(self, u'Select new Database file','','Datafile (*.dat);;All files (*)')
        if (len(db_new) > 0):
            self.ui.new_line.setText(db_new)
    
    def dbcp(self):
        if (len(self.ui.new_line.text()) == 0):
            inv_subs = u"<html><head/><body><p align=\"center\">Имя новой базы данных не задано</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        else:
            db_new = self.ui.new_line.text()
        
        if (len(self.ui.old_line.text()) == 0):
            inv_subs = u"<html><head/><body><p align=\"center\">Имя старой базы данных не задано</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        else:
            db_old = self.ui.old_line.text()
        
        shutil.copy(db_old,  db_new)
        self.close()


class AddWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        global db
        
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Add()
        self.ui.setupUi(self)
        
        self.ui.subs_line.setText("")
        self.ui.prot_line.setText("0.0")
        self.ui.lip_line.setText("0.0")
        self.ui.carb_line.setText("0.0")
        self.ui.ccal_line.setText("0.0")
        self.ui.glyc_line.setText("0.0")
        
        QtCore.QObject.connect(self.ui.okbut, QtCore.SIGNAL("clicked()"), self.add)
        
    def add(self):
        global db
        
        if (len(self.ui.subs_line.text()) == 0):
            inv_subs = u"<html><head/><body><p align=\"center\">Продукт не задан</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        else:
            subs = self.ui.subs_line.text()
        
        if (len(self.ui.prot_line.text()) == 0):
            prot = 0.0
        else:
            prot = float(self.ui.prot_line.text())
        
        if (len(self.ui.lip_line.text()) == 0):
            lip = 0.0
        else:
            lip = float(self.ui.lip_line.text())
        
        if (len(self.ui.carb_line.text()) == 0):
            carb = 0.0
        else:
            carb = float(self.ui.carb_line.text())
        
        if (len(self.ui.ccal_line.text()) == 0):
            ccal = 0.0
        else:
            ccal = float(self.ui.ccal_line.text())
        
        if (len(self.ui.glyc_line.text()) == 0):
            glyc = 0.0
        else:
            glyc = float(self.ui.glyc_line.text())
        
        if (sys.platform[0:3] == 'win'):
            dbold = os.getcwd()+"\\db.dat.bckp"
        else:
            dbold = os.getcwd()+"/db.dat.bckp"
        os.rename(db,  dbold)
        i = 0
        with open (dbold,  'r') as dbfile_old:
            with open (db,  'w') as dbfile:
                for line in dbfile_old:
                    dbfile.write (line)
                    if (subs == line.split(';;')[0]):
                        i = 1
                        inv_subs = u"<html><head/><body><p align=\"center\">Продукт \""+subs+u"\"<br>уже существует в базе данных</p></body></html>"
                        not_found = NotFound(parent=self, text=inv_subs)
                        not_found.show()
        
        os.remove (dbold)
    
        if (i == 0):
            dbfile = open (db,  'a')
            dbfile.write (subs+";;"+str(round(prot, 3))+";;"+str(round(lip, 3))+";;"+str(round(carb, 3))+";;"+str(round(ccal, 3))+";;"+str(round(glyc, 3))+"\n")
            dbfile.close()
            
            self.ui.subs_line.clear()
            self.ui.prot_line.setText("0.0")
            self.ui.lip_line.setText("0.0")
            self.ui.carb_line.setText("0.0")
            self.ui.ccal_line.setText("0.0")
            self.ui.glyc_line.setText("0.0")


class EditWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        global db
        
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Edit()
        self.ui.setupUi(self)
        
        self.ui.prot_line.setText("0.0")
        self.ui.lip_line.setText("0.0")
        self.ui.carb_line.setText("0.0")
        self.ui.ccal_line.setText("0.0")
        self.ui.glyc_line.setText("0.0")
        
        QtCore.QObject.connect(self.ui.deletebut, QtCore.SIGNAL("clicked()"), self.delete)
        QtCore.QObject.connect(self.ui.okbut, QtCore.SIGNAL("clicked()"), self.edit)
        
    def delete(self):
        global db
        
        if (len(self.ui.search_line.text()) == 0):
            inv_subs = u"<html><head/><body><p align=\"center\">Продукт не задан</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        else:
            subs = self.ui.search_line.text()
        
        if (sys.platform[0:3] == 'win'):
            dbold = os.getcwd()+"\\db.dat.bckp"
        else:
            dbold = os.getcwd()+"/db.dat.bckp"
        os.rename(db,  dbold)
        i = 0
        with open (dbold,  'r') as dbfile_old:
            with open (db,  'w') as dbfile:
                for line in dbfile_old:
                    if (subs == line.split(';;')[0]):
                        i = 1
                    else:
                        dbfile.write (line)
        
        os.remove (dbold)
        
        if (i == 0):
            inv_subs = u"<html><head/><body><p align=\"center\">Продукт \""+subs+u"\"<br>не найден в базе данных</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
        
        self.ui.search_line.clear()
        self.ui.prot_line.setText("0.0")
        self.ui.lip_line.setText("0.0")
        self.ui.carb_line.setText("0.0")
        self.ui.ccal_line.setText("0.0")
        self.ui.glyc_line.setText("0.0")
    
    def edit(self):
        global db
        
        if (len(self.ui.search_line.text()) == 0):
            inv_subs = u"<html><head/><body><p align=\"center\">Продукт не задан</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        else:
            subs = self.ui.search_line.text()
        
        if (len(self.ui.prot_line.text()) == 0):
            prot = 0.0
        else:
            prot = float(self.ui.prot_line.text())
        
        if (len(self.ui.lip_line.text()) == 0):
            lip = 0.0
        else:
            lip = float(self.ui.lip_line.text())
        
        if (len(self.ui.carb_line.text()) == 0):
            carb = 0.0
        else:
            carb = float(self.ui.carb_line.text())
        
        if (len(self.ui.ccal_line.text()) == 0):
            ccal = 0.0
        else:
            ccal = float(self.ui.ccal_line.text())
        
        if (len(self.ui.glyc_line.text()) == 0):
            glyc = 0.0
        else:
            glyc = float(self.ui.glyc_line.text())
        
        if (sys.platform[0:3] == 'win'):
            dbold = os.getcwd()+"\\db.dat.bckp"
        else:
            dbold = os.getcwd()+"/db.dat.bckp"
        os.rename(db,  dbold)
        i = 0
        with open (dbold,  'r') as dbfile_old:
            with open (db,  'w') as dbfile:
                for line in dbfile_old:
                    if (subs == line.split(';;')[0]):
                        i = 1
                        dbfile.write (subs+";;"+str(round(prot, 3))+";;"+str(round(lip, 3))+";;"+str(round(carb, 3))+";;"+str(round(ccal, 3))+";;"+str(round(glyc, 3))+"\n")
                    else:
                        dbfile.write (line)
        
        os.remove (dbold)
    
        if (i == 0):
            inv_subs = u"<html><head/><body><p align=\"center\">Продукт \""+subs+u"\"<br>не найден в базе данных</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
        else:
            self.ui.search_line.clear()
            self.ui.prot_line.setText("0.0")
            self.ui.lip_line.setText("0.0")
            self.ui.carb_line.setText("0.0")
            self.ui.ccal_line.setText("0.0")
            self.ui.glyc_line.setText("0.0")


class NotFound(QtGui.QMainWindow):
    def __init__(self, parent=None, text=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_NotFound()
        self.ui.setupUi(self)
        
        self.ui.label.setText(text)


class CalcWindow(QtGui.QMainWindow):
    def __init__(self,  parent=None):
        global db
        
        QtGui.QMainWindow.__init__(self,  parent)
        self.ui = Ui_Calc_Window()
        self.ui.setupUi(self)
        
        self.ui.mass_line.setText("100")
        self.ui.tot_prot_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
        self.ui.tot_lip_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
        self.ui.tot_ccal_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
        self.ui.tot_carb_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
        
        QtCore.QObject.connect(self.ui.searchbut, QtCore.SIGNAL("clicked()"), self.search)
        QtCore.QObject.connect(self.ui.addbut,  QtCore.SIGNAL("clicked()"),  self.add)
        QtCore.QObject.connect(self.ui.savebut,  QtCore.SIGNAL("clicked()"),  self.save)
        QtCore.QObject.connect(self.ui.deletebut,  QtCore.SIGNAL("clicked()"),  self.clear)
    
    def search(self):
        global db
        
        search = self.ui.search_line.text()
    
        if (len(search) == 0):
            inv_subs = u"<html><head/><body><p align=\"center\">Продукт не задан</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        
        if (len(self.ui.mass_line.text()) == 0):
            inv_subs = u"<html><head/><body><p align=\"center\">Масса не задана</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        else:
            mass = float(self.ui.mass_line.text())
        
        with open(db,'r') as dbfile:
            i = 0
            for line in dbfile:
                if (search == line.split(';;')[0]):
                    prop = mass/100*numpy.array([line.split(';;')[1:5]], dtype=float)
                    glyc_fl = float(line.split(';;')[5])
                    i = 1
        
            if (i == 0):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт \""+search+u"\"<br>не найден в базе данных</p></body></html>"
                not_found = NotFound(parent=self, text=inv_subs)
                not_found.show()
                return
    
        prot = "<html><head/><body><p align=\"right\">"+str(round(sum(numpy.hsplit(prop,  (0, 1))[1]), 3))+"</p></body></html>"
        lip = "<html><head/><body><p align=\"right\">"+str(round(sum(numpy.hsplit(prop,  (1, 2))[1]), 3))+"</p></body></html>"
        carb = "<html><head/><body><p align=\"right\">"+str(round(sum(numpy.hsplit(prop,  (2, 3))[1]), 3))+"</p></body></html>"
        ccal = "<html><head/><body><p align=\"right\">"+str(round(sum(numpy.hsplit(prop,  (3, 3))[2]), 3))+"</p></body></html>"
        glyc = "<html><head/><body><p align=\"right\">"+str(round(glyc_fl, 3))+"</p></body></html>"
    
        self.ui.prot_sec_lab.setText(prot)
        self.ui.lip_sec_lab.setText(lip)
        self.ui.carb_sec_lab.setText(carb)
        self.ui.ccal_sec_lab.setText(ccal)
        self.ui.glyc_sec_lab.setText(glyc)
    
    def add(self):
        global db
        
        if (self.ui.search_line.text() != ""):
            search = self.ui.search_line.text()
        else:
            inv_subs = u"<html><head/><body><p align=\"center\">Продукт не задан</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        if (self.ui.mass_line.text() != ""):
            mass = float(self.ui.mass_line.text())
        else:
            inv_subs = u"<html><head/><body><p align=\"center\">Масса не задана</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        
        with open(db,'r') as dbfile:
            i = 0
            for line in dbfile:
                if (search == line.split(';;')[0]):
                    prop = mass/100*numpy.array([line.split(';;')[1:5]], dtype=float)
                    i = 1
        
            if (i == 0):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт \""+search+u"\"<br>не найден в базе данных</p></body></html>"
                not_found = NotFound(parent=self, text=inv_subs)
                not_found.show()
                return
        
        prot_fl = float(self.ui.tot_prot_sec_lab.text()[36:-18]) + round(sum(numpy.hsplit(prop,  (0, 1))[1]), 3)
        lip_fl = float(self.ui.tot_lip_sec_lab.text()[36:-18]) + round(sum(numpy.hsplit(prop,  (1, 2))[1]), 3)
        carb_fl = float(self.ui.tot_carb_sec_lab.text()[36:-18]) + round(sum(numpy.hsplit(prop,  (2, 3))[1]), 3)
        ccal_fl = float(self.ui.tot_ccal_sec_lab.text()[36:-18]) + round(sum(numpy.hsplit(prop,  (3, 3))[2]), 3)
            
        prot = "<html><head/><body><p align=\"right\">"+str(prot_fl)+"</p></body></html>"
        lip = "<html><head/><body><p align=\"right\">"+str(lip_fl)+"</p></body></html>"
        carb = "<html><head/><body><p align=\"right\">"+str(carb_fl)+"</p></body></html>"
        ccal = "<html><head/><body><p align=\"right\">"+str(ccal_fl)+"</p></body></html>"
            
        self.ui.tot_prot_sec_lab.setText(prot)
        self.ui.tot_lip_sec_lab.setText(lip)
        self.ui.tot_carb_sec_lab.setText(carb)
        self.ui.tot_ccal_sec_lab.setText(ccal)
            
        self.ui.text_selected.append(search+u", "+str(round(mass,  3))+u" г")
    
    def save(self):
        menu_name = QtGui.QFileDialog.getSaveFileName(self, u'Select menu file','','Text (*.txt);;All files (*)')
        if (len(menu_name) > 0):
            with open(menu_name,'w') as menu_file:
                prot = self.ui.tot_prot_sec_lab.text()[36:-18]
                lip = self.ui.tot_lip_sec_lab.text()[36:-18]
                carb = self.ui.tot_carb_sec_lab.text()[36:-18]
                ccal = self.ui.tot_ccal_sec_lab.text()[36:-18]
                menu_file.write (u"Белки: "+prot+u"\nЖиры: "+lip+u"\nУглеводы: "+carb+u"\nКалорийность, ккал: "+ccal+u"\n\n")
                
                for line in self.ui.text_selected.toPlainText():
                    menu_file.write(line)
        
    def clear(self):
        self.ui.search_line.clear()
        self.ui.mass_line.setText("100")
        
        self.ui.prot_sec_lab.setText("<html><head/><body><p align=\"right\"></br></p></body></html>")
        self.ui.lip_sec_lab.setText("<html><head/><body><p align=\"right\"></br></p></body></html>")
        self.ui.ccal_sec_lab.setText("<html><head/><body><p align=\"right\"></br></p></body></html>")
        self.ui.carb_sec_lab.setText("<html><head/><body><p align=\"right\"></br></p></body></html>")
        self.ui.glyc_sec_lab.setText("<html><head/><body><p align=\"right\"></br></p></body></html>")
        
        self.ui.text_selected.clear()
        
        self.ui.tot_prot_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
        self.ui.tot_lip_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
        self.ui.tot_ccal_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
        self.ui.tot_carb_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        global db
        
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Food()
        self.ui.setupUi(self)

        self.database()
        if (os.path.exists(db) == False):
            with open(db,  'w') as dbfile:
                dbfile.write("")
        
        about_window = AboutWindow (parent=self)
        add_window = AddWindow (parent=self)
        edit_window = EditWindow (parent=self)
        dbcp_window = DBcpWindow (parent=self)
        calc_window = CalcWindow (parent=self)
        dbselect_window = DBselWindow(parent=self)
        
        QtCore.QObject.connect(self.ui.menu_about, QtCore.SIGNAL("triggered()"), about_window.show)
        QtCore.QObject.connect(self.ui.menu_add, QtCore.SIGNAL("triggered()"), add_window.show)
        QtCore.QObject.connect(self.ui.menu_edit, QtCore.SIGNAL("triggered()"), edit_window.show)
        QtCore.QObject.connect(self.ui.menu_dbcp, QtCore.SIGNAL("triggered()"), dbcp_window.show)
        QtCore.QObject.connect(self.ui.menu_create, QtCore.SIGNAL("triggered()"), calc_window.show)
        QtCore.QObject.connect(self.ui.menu_dbsel, QtCore.SIGNAL("triggered()"), dbselect_window.show)
        QtCore.QObject.connect(self.ui.searchbut, QtCore.SIGNAL("clicked()"), self.calcucate)

        self.ui.mass_line.setText("100")
    
    def database(self):
        global db
        
        if (sys.platform[0:3] == 'win'):
            config = os.getcwd()+"\\food_gui.ini"
        else:
            config = os.getcwd()+"/food_gui.ini"
        if (os.path.exists(config)):
            with open(config,  'r') as config_file:
                for line in config_file:
                    if (line.split('=')[0] == 'DATABASE'):
                        db = line.split('=')[1]
        else:
            with open(config,  'w') as config_file:
                if (sys.platform[0:3] == 'win'):
                    db = os.getcwd()+"\\db.dat"
                    config_file.write('DATABASE='+db+'=\n')
                else:
                    db = os.getcwd()+"/db.dat"
                    config_file.write('DATABASE='+db+'=\n')
    
    def calcucate(self):
        global db
        
        search = self.ui.search_line.text()
    
        if (len(search) == 0):
            inv_subs = u"<html><head/><body><p align=\"center\">Продукт не задан</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        
        if (len(self.ui.mass_line.text()) == 0):
            inv_subs = u"<html><head/><body><p align=\"center\">Масса не задана</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        else:
            mass = float(self.ui.mass_line.text())
    
        with open(db,'r') as dbfile:
            i = 0
            for line in dbfile:
                if (search == line.split(';;')[0]):
                    prop = mass/100*numpy.array([line.split(';;')[1:5]], dtype=float)
                    glyc_fl = float(line.split(';;')[5])
                    i = 1
        
            if (i == 0):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт \""+search+u"\"<br>не найден в базе данных</p></body></html>"
                not_found = NotFound(parent=self, text=inv_subs)
                not_found.show()
                return
    
        prot = "<html><head/><body><p align=\"right\">"+str(round(sum(numpy.hsplit(prop,  (0, 1))[1]), 3))+"</p></body></html>"
        lip = "<html><head/><body><p align=\"right\">"+str(round(sum(numpy.hsplit(prop,  (1, 2))[1]), 3))+"</p></body></html>"
        carb = "<html><head/><body><p align=\"right\">"+str(round(sum(numpy.hsplit(prop,  (2, 3))[1]), 3))+"</p></body></html>"
        ccal = "<html><head/><body><p align=\"right\">"+str(round(sum(numpy.hsplit(prop,  (3, 3))[2]), 3))+"</p></body></html>"
        glyc = "<html><head/><body><p align=\"right\">"+str(round(glyc_fl, 3))+"</p></body></html>"
    
        self.ui.prot_sec_lab.setText(prot)
        self.ui.lip_sec_lab.setText(lip)
        self.ui.carb_sec_lab.setText(carb)
        self.ui.ccal_sec_lab.setText(ccal)
        self.ui.glyc_sec_lab.setText(glyc)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    codec = QtCore.QTextCodec.codecForName("UTF-8")
    QtCore.QTextCodec.setCodecForCStrings(codec)
    
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

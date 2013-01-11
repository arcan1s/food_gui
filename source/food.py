#!/usr/bin/python2.7

import numpy,  os,  sys,  shutil


def add_str(db,  dbold):
    subs = str(raw_input("Name: "))
    prot = float(input("Protein: "))
    lip = float(input("Lipid: "))
    carb = float(input("Carbohydrate: "))
    ccal = float(input("ccal: "))
    glyc = float(input("Glycemic index: "))
    
    lab = 0
    with open (dbold,  'r') as dbfile_old:
        with open (db,  'w') as dbfile:
            for line in dbfile_old:
                dbfile.write (line)
                if (subs == line.split()[0]):
                    lab = 1
                    print("Substance "+subs+" is exist")
    
    if (lab == 0):
        dbfile = open (db,  'a')
        dbfile.write (subs+" "+str(round(prot, 2))+" "+str(round(lip, 2))+" "+str(round(carb, 2))+" "+str(round(ccal, 2))+" "+str(round(glyc, 2))+"\n")
        dbfile.close()
    
    os.remove (dbold)
    
    
def read_tab(dbfile):
    for line in dbfile:
        subs = line.split()[0]
        prop = numpy.array([line.split()[1:]], dtype=float)
        
        print ("\nName: "+subs+"\nProtein: "+str(prop[0][0])+"\nLipid: "+str(prop[0][1])+"\nCarbohydrate: "+str(prop[0][2]))
        print ("ccal: "+str(prop[0][3])+"\nGlycemic index: "+str(prop[0][4]))
    

def calculate(db):
    rep = "1"
    i = 0
    while (rep == "y" or rep == "Y" or rep == "1"):
        search = str(raw_input("Substance: "))
        k = i
    
        with open(db,'r') as dbfile:
            for line in dbfile:
                if (search == line.split()[0]):
                    mass = float(input("Mass (g): "))
                    prop = mass/100*numpy.array([line.split()[1:]], dtype=float)
                    i = i + 1
                    if (rep == "1"):
                        propall = prop
                    else:
                        propall = numpy.vstack([propall, prop])
        
        if (i == k):
            print ("Substance "+search+" not found!")
        rep = str(raw_input("Repeat [y/n]: "))
    
    if (i != 0):
        prot = sum(numpy.hsplit(propall,  (0, 1))[1])
        lip = sum(numpy.hsplit(propall,  (1, 2))[1])
        carb = sum(numpy.hsplit(propall,  (2, 3))[1])
        ccal = sum(numpy.hsplit(propall,  (3, 4))[1])
        glyc = sum(numpy.hsplit(propall,  (4, 4))[2])
    
    print ("\nProteins: "+str(round(prot, 2))+"\nLipids: "+str(round(lip, 2))+"\nCarbohydrates: "+str(round(carb, 2))+"\nccal: "+str(round(ccal, 2))+"\nGlycemic index: "+str(round(glyc, 2)))
    
    
def edit_tab(db,  dbold):
    search = str(raw_input("Substance: "))
    
    with open(dbold,  'r') as dbfile_old:
        with open(db,  'w') as dbfile:
            for line in dbfile_old:
                if (search == line.split()[0]):
                    chs = str(raw_input("[E]dit or [R]emove?: "))
                    if (chs == "E" or chs == "e"):
                        subs = search
                        print ("Name: "+subs)
                        prot = float(input("Protein: "))
                        lip = float(input("Lipid: "))
                        carb = float(input("Carbohydrate: "))
                        ccal = float(input("ccal: "))
                        glyc = float(input("Glycemic index: "))
                        
                        dbfile.write (subs+" "+str(round(prot, 2))+" "+str(round(lip, 2))+" "+str(round(carb, 2))+" "+str(round(ccal, 2))+" "+str(round(glyc, 2))+"\n")
                    elif (chs != "R" and chs != "r"):
                        print ("What?")
                        dbfile.write(line)
                else:
                    dbfile.write(line)
    
    os.remove(dbold)
    
    
def menu(db):
    menu_file = str(raw_input("Menu file: "))
    
    rep = "1"
    i = 0
    item = []
    item_mass = []
    while (rep == "y" or rep == "Y" or rep == "1"):
        search = str(raw_input("Substance: "))
        k = i
        lab = 1
        lab1 = 1
    
        with open(db,'r') as dbfile:
            for line in dbfile:
                if (search == line.split()[0]):
                    mass = float(input("Mass (g): "))
                    prop = mass/100*numpy.array([line.split()[1:]], dtype=float)
                    i = i + 1
                    
                    print ("\nName: "+search+"\nProtein: "+str(prop[0][0])+"\nLipid: "+str(prop[0][1])+"\nCarbohydrate: "+str(prop[0][2]))
                    print ("ccal: "+str(prop[0][3])+"\nGlycemic index: "+str(prop[0][4]))
                    if (rep == "1"):
                        propall = prop
                        
                        prot = sum(numpy.hsplit(propall,  (0, 1))[1])
                        lip = sum(numpy.hsplit(propall,  (1, 2))[1])
                        carb = sum(numpy.hsplit(propall,  (2, 3))[1])
                        ccal = sum(numpy.hsplit(propall,  (3, 4))[1])
                        glyc = sum(numpy.hsplit(propall,  (4, 4))[2])
                        print ("\nTotal:\nProteins: "+str(round(prot, 2))+"\nLipids: "+str(round(lip, 2))+"\nCarbohydrate: "+str(round(carb, 2))+"\nccal: "+str(round(ccal, 2))+"\nGlycemic index: "+str(round(glyc, 2))+"\n")
                        
                        chs = str(raw_input("Confirm? [y/n] "))
                        if (chs == "N" or chs == "n"):
                            i = i - 1
                            lab = 0
                            lab1 = 0
                        elif (chs == "Y" or chs == "y"):
                            item += [search]
                            item_mass += [str(round(mass,  1))]
                    else:
                        propall = numpy.vstack([propall, prop])
                        
                        prot = sum(numpy.hsplit(propall,  (0, 1))[1])
                        lip = sum(numpy.hsplit(propall,  (1, 2))[1])
                        carb = sum(numpy.hsplit(propall,  (2, 3))[1])
                        ccal = sum(numpy.hsplit(propall,  (3, 4))[1])
                        glyc = sum(numpy.hsplit(propall,  (4, 4))[2])
                        print ("\nTotal:\nProteins: "+str(round(prot, 2))+"\nLipids: "+str(round(lip, 2))+"\nCarbohydrate: "+str(round(carb, 2))+"\nccal: "+str(round(ccal, 2))+"\nGlycemic index: "+str(round(glyc, 2))+"\n")
                        
                        chs = str(raw_input("Confirm? [y/n] "))
                        if (chs == "N" or chs == "n"):
                            propall = numpy.vsplit(propall,  (-1, -1))[0]
                            i = i - 1
                            lab1 = 0
                        elif (chs == "Y" or chs == "y"):
                            item += [search]
                            item_mass += [str(round(mass,  1))]
        
        if (i == k and lab1 == 1):
            print ("Substance "+search+" not found!")
        rep = str(raw_input("Repeat [y/n]: "))
        if (lab == 0):
            rep = "1"
    
    if (i != 0):
        with open (menu_file,  'w') as outpt:
            l = 0
            for name in item:
                outpt.write (name+" - "+item_mass[l]+"\n")
                l = l + 1
            
            prot = sum(numpy.hsplit(propall,  (0, 1))[1])
            lip = sum(numpy.hsplit(propall,  (1, 2))[1])
            carb = sum(numpy.hsplit(propall,  (2, 3))[1])
            ccal = sum(numpy.hsplit(propall,  (3, 4))[1])
            glyc = sum(numpy.hsplit(propall,  (4, 4))[2])
            outpt.write ("=======================================\nTotal:")
            outpt.write ("\nProteins: "+str(round(prot, 2))+"\nLipids: "+str(round(lip, 2))+"\nCarbohydrate: "+str(round(carb, 2))+"\nccal: "+str(round(ccal, 2))+"\nGlycemic index: "+str(round(glyc, 2))+"\n")



if __name__ == '__main__':
    print ("1 - Add string in table\n2 - Write table\n3 - Calculate\n4 - Delete or edit string in table\n5 - Create menu")
    choise = int(input())
    
    
    if (choise == 1):
        db = "db.dat"
        dbold = "db.dat.bckp"
        if (os.path.exists(db)):
            os.rename(db,  dbold)
            add_str(db,  dbold)
        else:
            dbfile = open(db,  'w')
            add_str(dbfile)
            dbfile.close()
    elif (choise == 2):
        db = "db.dat"
        if (os.path.exists(db)):
            dbfile = open(db, 'r')
            read_tab(dbfile)
            dbfile.close()
        else:
            print ("Database file isn't exist!\n")
    elif (choise == 3):
        db = "db.dat"
        if (os.path.exists(db)):
            calculate(db)
        else:
            print ("Database file isn't exist!\n")
    elif (choise == 4):
        db = "db.dat"
        dbold = "db.dat.bckp"
        os.rename (db,  dbold)
        edit_tab(db,  dbold)
    elif (choise == 5):
        db = "db.dat"
        menu(db)

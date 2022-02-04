import os
from tkinter import E
from xml.etree.ElementTree import PI

argsfile = open(os.path.join("exec", "args.txt"), "r")
argsTemp = argsfile.readlines()
args = []
for i in argsTemp:
    if i == argsTemp[len(argsTemp)-1]:
        args.append(i)
    else:
        args.append(i[0:-1])

infofile = open(os.path.join("exec", "info.txt"), "r")
infoTemp = infofile.readlines()
info = []
for i in infoTemp:
    if i == infoTemp[len(infoTemp)-1]:
        info.append(i)
    else:
        info.append(i[0:-1])
username = info[0]
dir = info[1]
dirDisplay = info[2]
try:
    prefs = open(os.path.join("Home",username,".prefs","pip.pref"),"a")
except Exception:
    pass
if not os.path.exists(os.path.join("Home",username,".prefs","pip.pref")):
    pref = input("Which command does your system use? ('1' for pip3 or '2' for pip'?):")
    try:
        prefs = open(os.path.join("Home",username,".prefs","pip.pref"),"a")
    except FileNotFoundError:
        try:
            prefs = open(os.path.join("Home",username,".prefs","pip.pref"),"w+")
            prefs.close()
            prefs = open(os.path.join("Home",username,".prefs","pip.pref"),"a")
        except FileNotFoundError:
            os.mkdir(os.path.join("Home",username,".prefs"))
            prefs = open(os.path.join("Home",username,".prefs","pip.pref"),"a")
        try:
            os.mkdir(os.path.join("Home",username,".prefs"))
        except FileExistsError:
            pass
        prefs = open(os.path.join("Home",username,".prefs","pip.pref"),"a")
    if pref == "1":
        prefs.write("command=pip3")
    elif pref == "2":
        prefs.write("command=pip")
    else:
        raise KeyboardInterrupt
prefs.close()
prefs = open(os.path.join("Home",username,".prefs","pip.pref"),"r")
prefslinesraw = prefs.readlines()
prefslines = []
for line in prefslinesraw:
    try:
        prefslines.append(line.split("\n"[0]))
    except:
        prefslines.append(line)
PipCommandUsed = False
for line in prefslines:
    if line == "command=pip":
        PipCommandUsed = "pip"
    elif line == line == ["command=pip3"]:
        PipCommandUsed = "pip3"
prefs.close()
prefs = open(os.path.join("Home",username,".prefs","pip.pref"),"a")
if PipCommandUsed == False:
    pref = input("Which command does your system use? ('1' for pip3 or '2' for pip'?):")
    if pref == "1":
        prefs.write("command=pip3")
    elif pref == "2":
        prefs.write("command=pip")
    else:
        raise KeyboardInterrupt
arguments = " "
for arg in args:
    arguments += arg + " "

os.system(str(PipCommandUsed) + str(arguments))

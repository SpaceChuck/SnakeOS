### SnakeOS Arguments and Info Template

import os

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
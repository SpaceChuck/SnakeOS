### SPKG, the SnakeOS package manager

import os
import requests
from tqdm import tqdm

argsfile = open(os.path.join("exec", "args.txt"), "r")
argsTemp = argsfile.readlines()
args = []
for i in argsTemp:
    if i == argsTemp[len(argsTemp)-1]:
        args.append(i)
    else:
        args.append(i[0:-1])
try:
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
    try:
        exec(open(os.path.join("Home","groups.py"),"r").read())
        if not username in groups.get("Administrators"):
            print("You cannot install software!")
            raise KeyboardInterrupt
    except FileNotFoundError:
        pass
except FileNotFoundError:
    pass

if args[0] == "install":
    url = "https://raw.githubusercontent.com/SpaceChuck/spkg-repo/main/" + args[1] + "/install.py"
    print("Downloading install script from: " + url + "...")
    try:
        r = requests.get(url, allow_redirects=True)
    except Exception as e:
        print("Couldn't download uninstall script!")
        print(e)
    try:
        open("install.py", 'wb').write(r.content)
    except Exception as e:
        print("Couldn't download uninstall script!")
        print(e)
    print("Downloaded install script!")
    print("Running install script..")
        
    try:
        exec(open("install.py").read())
    except Exception as e:
        print(e)
        print(r.content)
    os.remove("install.py")
    print("Removed install script")
    print("Successfully installed " + args[1] + "!")

elif args[0] == "uninstall" or args[0] == "remove":
    url = "https://raw.githubusercontent.com/SpaceChuck/spkg-repo/main/" + args[1] + "/uninstall.py"
    print("Downloading uninstall script from: " + url + "...")
    try:
        r = requests.get(url, allow_redirects=True)
    except Exception as e:
        print("Couldn't download uninstall script!")
        print(e)
    try:
        open("uninstall.py", 'wb').write(r.content)
    except Exception as e:
        print("Couldn't download uninstall script!")
        print(e)
    print("Downloaded uninstall script!")
    print("Running uninstall script...")
    try:
        exec(open("uninstall.py").read())
    except Exception as e:
        print(e)
        print(r.content)
    os.remove("uninstall.py")
    print("Removed uninstall script")
    print("Successfully uninstalled " + args[1] + "!")

else:
    print("""
    SPKG, the SnakeOS package manager
        spkg install <package> - install a package
        spkg uninstall <package> - uninstall a package
    """)






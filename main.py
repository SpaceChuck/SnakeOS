import os
import time
import sys
import shutil


if os.path.join("t","i")[1] == "\\":
    winMode = True
else:
    try:
        open("WinMode") # Create an empty file called "WinMode" (no extension) to enable Windows Mode
        winMode = True
    except Exception:
        winMode = False

def quit():
    print("\n")
    print("Running shutdown plugins...")
    for plugin in pluginsShutdown:
        try:
            exec(open(os.path.join("plugins", plugin)).read())
        except Exception as e:
            print("An exception has occured while running " + str(plugin))
            print(e)
        except KeyboardInterrupt:
            continue
    print("Shutting down SnakeOS...")
    time.sleep(0.2)
    print("Goodbye!")
    time.sleep(0.8)
    sys.exit()

def convertPathToWin(path):
    newPath = ""
    for i in path:
        if i == "/":
            newI = "\\"
        else:
            newI = i
        newPath += newI
    return newPath

print("Starting SnakeOS...")
if winMode:
    print("Running under Windows, some problems with paths might occur!")
print("Loading executables...")
executables = 0

try:
    executables = os.listdir("exec")
except Exception:
    print("Failed while loading executables!")
for i in executables:
    if i.split(".")[1] == "py":
        print("Found " + str(i).split(".")[0])

try:
    pluginsDir = os.listdir("plugins")
    pluginsLoaded = True
except Exception:
    pluginsLoaded = False

if pluginsLoaded:
    print("Loading plugins...")
    for i in pluginsDir:
        if i.split(".")[1] == "py":
            print("Found " + str(i).split(".")[0])

pluginsStartup = [] 
pluginsCommand = []
pluginsShutdown = []

for plugin in pluginsDir:
    i = open(os.path.join("plugins",plugin), errors="replace")
    firstline = i.readline(17)
    if firstline == "# snakeos_runat 0":
        pluginsStartup.append(plugin)
    if firstline == "# snakeos_runat 1":
        pluginsCommand.append(plugin)
    if firstline == "# snakeos_runat 2":
        pluginsShutdown.append(plugin)

print("Running startup plugins...")
for plugin in pluginsStartup:
    try:
        exec(open(os.path.join("plugins", plugin)).read())
    except Exception as e:
        print("An exception has occured while running " + str(plugin))
        print(e)
    except KeyboardInterrupt:
        continue

dir = "Home"
dirDisplay = "—"

print("Welcome to SnakeOS!")
if "help.py" in executables:
    print("Type 'help' To get help.")
else:
    print("'help' is not found!")

while True:
    try:
        command = input(dirDisplay + ">>")
    except Exception:
        print("Bad command!")
    except KeyboardInterrupt:
        quit()
    for plugin in pluginsCommand:
        try:
            exec(open(os.path.join("plugins", plugin)).read())
        except Exception as e:
            print("An exception has occured while running " + str(plugin))
            print(e)
        except KeyboardInterrupt:
            continue
    cmd = command.split(" ")[0] + ".py"
    cmdargs = command.split(" ")
    cmdargs.append(" ")
    cmdargs = cmdargs[1:-1]
    if cmd == "cd.py":
        dirTemp = command.split(" ")[1]
        if command.split(" ")[1] == "-" or command.split(" ")[1] == "—":
            dir = "Home"
            dirDisplay = "—"
        elif command.split(" ")[1] == "*":
            dir = os.getcwd()
            dirDisplay = "*"
        else:
            if dirTemp[0:2] == "*/" or command.split(" ")[0:2] == "*\\":
                dirTemp = dirTemp[2:len(dirTemp)]
            elif dirTemp[0:2] == "-/" or command.split(" ")[0:2] == "-\\":
                dirTemp = dirTemp[2:len(dirTemp)]
            try:
                if winMode:
                    os.listdir(os.path.join(convertPathToWin(dir),convertPathToWin(dirTemp)))
                else:
                    dirTemp = os.path.join(dir,dirTemp) 
            except Exception:
                try:
                    if winMode:
                        os.listdir(convertPathToWin(dirTemp)) # Used to check if a directory exists
                    else:
                        os.listdir(dirTemp) # Used to check if a directory exists
                except Exception:
                    print("Unknown directory!")
                    continue
            if winMode:
                dir = convertPathToWin(dirTemp)
            else:
                dir = dirTemp
            dirDisplay = "*/" + dir
        try:
            if dirDisplay == "Home":
                dirDisplay = "—"
            elif dirDisplay.split("/")[0] == "*" and dirDisplay.split("/")[1] == "Home" or dirDisplay.split("/")[1] == "home":
                dirDisplay = "—" + dirDisplay[6:len(dirDisplay)]
        except Exception:
            continue
    elif cmd == "ls.py" or cmd == "list.py":
        try:
            listDir = os.listdir(dir)
        except Exception:
            print("Unknown directory!")
            continue

        for file in listDir:
            print(file)

    elif cmd == "quit.py" or cmd == "exit.py":
        quit()
    elif cmd == "make.py" or cmd == "mk.py":
        file = command.split(" ")[1]
        f = open(os.path.join(dir, file), "x")
        f = 0
    elif cmd == "makedir.py" or cmd == "makedir.py":
        os.mkdir(os.path.join(dir, command.split(" ")[1]))
    elif cmd == "del.py" or cmd == "delete.py" or cmd == "del.py" or cmd == "delete.py":
        try:
            shutil.rmtree(os.path.join(dir, command.split(" ")[1]))
        except Exception:
            try:
                os.remove(os.path.join(dir, command.split(" ")[1]))
            except Exception:
                print("Unknown file/directory!")
    elif cmd == "edit.py":
        try:
            edit_file = open(command.split(" ")[1], "w")
        except Exception:
            print("File not found!")
            break
        edit_string = "" 
        for line in command.split(" ")[2:]:
            edit_string += line + " "
        try:
            edit_file.write(edit_string)
        except:
            print("Couldn't write to file!")
        edit_file.close()
    elif cmd in executables:
        for i in range(2): # Required because of my garbage coding. It writes on the second try.
            arguments = open(os.path.join("exec", "args.txt"),"w").close()
            cmdargs = command.split(" ")
            cmdargs.append(" ")
            cmdargs = cmdargs[1:-1]
            arguments = open(os.path.join("exec", "args.txt"),"a")
            for i in cmdargs:
                if i == cmdargs[0]:
                    arguments.write(str(i))
                else:
                    arguments.write("\n" + str(i))
            arguments.close()
        try:
            exec(open(os.path.join("exec", command.split(" ")[0] + ".py")).read())
        except Exception as e:
            print("An error has occured while running " + cmd)
            print(e)
        except KeyboardInterrupt:
            continue
    else:
        print("Bad command!")

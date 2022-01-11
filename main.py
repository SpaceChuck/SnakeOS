import os
import time
import sys
import shutil

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

print("Starting SnakeOS...")
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

print("Welcome to SnakeOS!")
if "help.py" in executables:
    print("Type 'help' To get help.")
else:
    print("'help' is not found!")

while True:
    try:
        command = input(dir + ">>")
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
        try:
            os.listdir(dirTemp) # Used to check if a directory exists
        except Exception:
            print("Unknown directory!")
            continue
        dir = dirTemp
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
        f = open(os.path.join(dir, command.split(" ")[1]), "x")
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

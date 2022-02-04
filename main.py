import os
import time
import sys
import shutil


## Windows Mode

if os.path.join("t","i")[1] == "\\":
    winMode = True
else:
    try:
        open("WinMode") # Create an empty file called "WinMode" (no extension) to enable Windows Mode
        winMode = True
    except Exception:
        winMode = False

## Shutdown SnakeOS
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

## Convert path to Windows format (using backslashes)
def convertPathToWin(path):
    newPath = ""
    for i in path:
        if i == "/":
            newI = "\\"
        else:
            newI = i
        newPath += newI
    return newPath

def login():
    print("Login to SnakeOS")
    while True:
        print("Type 'list' to list users or 'quit' to exit")
        username = input("Username:")
        if username != "list" and username != "quit" and not username in users:
            print("User doesn't exist!")
            continue
        if username == "list":
            for user in users:
                if user != "admin" and user != ".ds_store":
                    print(user)
            continue
        if username == "quit":
            quit()
        try:
            passwordtxt = open(os.path.join("Home", username,".password"),"r")
        except FileNotFoundError:
            home = os.path.join("Home", username)
            break
        password = input("Password:")
        if passwordtxt.readlines()[0] != password:
            print("Wrong password!")
            passwordtxt.close()
            continue
        passwordtxt.close()
        home = os.path.join("Home", username)
        dir = home
        dirDisplay = "—"
        break
    print("Running login plugins...")
    try:
        for plugin in pluginsLogin:
            try:
                exec(open(os.path.join("plugins", plugin)).read())
            except Exception as e:
                print("An exception has occured while running " + str(plugin))
                print(e)
            except KeyboardInterrupt:
                continue
    except Exception:
        1+1
    print("Welcome to SnakeOS, " + username + "!")
    if "help.py" in executables:
        print("Type 'help' To get help.")
    else:
        print("'help' is not found!")
    return [home,username]


## Start SnakeOS
print("Starting SnakeOS...")
if winMode:
    print("Running under Windows, some problems with paths might occur!")
## Load executables
print("Loading executables...")
executables = []
try:
    executables = os.listdir("exec")
except Exception:
    print("Failed while loading executables!")
for i in executables:
    try:
        if i.split(".")[1] == "py":
            print("Found " + str(i).split(".")[0])
    except:
        continue

## Load plugins
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
pluginsLogin = []
pluginsLogoff = []
for plugin in pluginsDir:
    i = open(os.path.join("plugins",plugin), errors="replace")
    firstline = i.readline(17)
    if firstline == "# snakeos_runat 0":
        pluginsStartup.append(plugin)
    if firstline == "# snakeos_runat 1":
        pluginsCommand.append(plugin)
    if firstline == "# snakeos_runat 2":
        pluginsShutdown.append(plugin)
    if firstline == "# snakeos_runat 3":
        pluginsLogin.append(plugin)
    if firstline == "# snakeos_runat 4":
        pluginsLogoff.append(plugin)


## Run startup plugins
print("Running startup plugins...")
for plugin in pluginsStartup:
    try:
        exec(open(os.path.join("plugins", plugin)).read())
    except Exception as e:
        print("An exception has occured while running " + str(plugin))
        print(e)
    except KeyboardInterrupt:
        continue

## List users
users = []
for user in os.listdir("Home"):
    if user.lower() == ".ds_store":
        continue
    users.append(user.lower())

## Setup
if users == [] or users == ["admin"]:
    print("Welcome to SnakeOS setup!")
    print("Setup will help you create a user and set an administrator password.")
    username = input("Username:")
    if username == "list" or username == "quit":
        print("You cannot make an account called list or quit!")
        sys.exit()
    else:
        os.mkdir(os.path.join("Home", username))
    password = input("Password:")
    if password == "":
        print("You entered a blank password, that's not secure!")
        answer = input("Do you really want to continue? (Y/N):").lower()
        if answer == "n":
            sys.exit()
    else:
        passwordtxt = open(os.path.join("Home", username,".password"),"w")
        passwordtxt.write(password)
        passwordtxt.close()
    print("TIP: You can add more users with the 'useradd' command.")
    print("Now we need to add an administrator password, otherwise people will be able to login as 'admin' and have full acess to the system.")
    try:
        os.mkdir(os.path.join("Home", "admin"))
    except Exception:
        1+1
    password = input("Password:")
    if password == "":
        print("You entered a blank password, that's not secure!")
        answer = input("Do you really want to continue? (Y/N):").lower()
        if answer == "n":
            sys.exit()
    else:
        passwordtxt = open(os.path.join("Home", "admin",".password"),"w")
        passwordtxt.write(password)
        passwordtxt.close()


## Login screen
try:
    loginResults = login()
except KeyboardInterrupt:
    quit()
dir = loginResults[0]
username = loginResults[1]
dirDisplay = "—"

## Loop
while True:
    ## Command input
    try:
        command = input(username + "@" + dirDisplay + ">>")
    except Exception as e:
        print("Bad command!")
        print(e)
    except KeyboardInterrupt:
        quit()
    ## On command plugins
    for plugin in pluginsCommand:
        try:
            exec(open(os.path.join("plugins", plugin)).read())
        except Exception as e:
            print("An exception has occured while running " + str(plugin))
            print(e)
        except KeyboardInterrupt:
            continue
    ## Variables
    cmd = command.split(" ")[0] + ".py"
    cmdargs = command.split(" ")
    cmdargs.append(" ")
    cmdargs = cmdargs[1:-1]
    ## cd command
    if cmd == "cd.py":
        try:
            dirTemp = command.split(" ")[1]
        except Exception:
            print("Bad command!")
            continue
        if command.split(" ")[1] == "-" or command.split(" ")[1] == "—":
            dir = os.path.join("Home",username)
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
                    dirTemp = os.path.join(convertPathToWin(dir),convertPathToWin(dirTemp))
                else:
                    os.listdir(os.path.join(dir,dirTemp))
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
            if dirDisplay == os.path.join("*","Home",username):
                dirDisplay = "—"
            elif dirDisplay.split("/")[0] == "*" and dirDisplay.split("/")[1] == "Home" or dirDisplay.split("/")[1] == "home":
                if dirDisplay.split("/")[2] == username:
                    dirDisplay = "—" + dirDisplay[7 + len(username):len(dirDisplay)]
        except Exception:
            continue
    ## ls command
    elif cmd == "ls.py" or cmd == "list.py":
        try:
            listDir = os.listdir(dir)
        except Exception:
            print("Unknown directory!")
            continue

        for file in listDir:
            print(file)
    ## quit command
    elif cmd == "quit.py" or cmd == "exit.py" or cmd == "logoff.py" or cmd == "logout.py":
        print("Running logoff plugins...")
        for plugin in pluginsLogoff:
            try:
                exec(open(os.path.join("plugins", plugin)).read())
            except Exception as e:
                print("An exception has occured while running " + str(plugin))
                print(e)
            except KeyboardInterrupt:
                continue
        print("Logged off " + username)
        try:
            loginResults = login()
        except KeyboardInterrupt:
            quit()
        dir = loginResults[0]
        username = loginResults[1]
        dirDisplay = "—"
    ## make command
    elif cmd == "make.py" or cmd == "mk.py":
        file = command.split(" ")[1]
        f = open(os.path.join(dir, file), "x")
        f = 0
    ## makedir command
    elif cmd == "makedir.py" or cmd == "mkdir.py":
        os.mkdir(os.path.join(dir, command.split(" ")[1]))
    ## del command
    elif cmd == "del.py" or cmd == "delete.py" or cmd == "rm.py" or cmd == "remove.py":
        try:
            shutil.rmtree(os.path.join(dir, command.split(" ")[1]))
        except Exception:
            try:
                os.remove(os.path.join(dir, command.split(" ")[1]))
            except Exception:
                print("Unknown file/directory!")
    ## edit command
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
        for i in range(2): # Required because of my garbage coding. It writes on the second try.
            info = open(os.path.join("exec", "info.txt"),"w").close()
            infolist = [username,dir,dirDisplay]
            information = open(os.path.join("exec", "info.txt"),"a")
            for i in infolist:
                if i == infolist[0]:
                    information.write(str(i))
                else:
                    information.write("\n" + str(i))
            information.close()
        try:
            exec(open(os.path.join("exec", command.split(" ")[0] + ".py")).read())
        except Exception as e:
            print("An error has occured while running " + cmd)
            print(e)
        except KeyboardInterrupt:
            print("\n")
            continue
    else:
        print("Bad command!")

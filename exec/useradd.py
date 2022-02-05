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
exec(open(os.path.join("Home","groups.py"),"r").read())
if not username in groups.get("Administrators"):
    print("You cannot add users!")
    raise KeyboardInterrupt

if args != []:
    try:
        username = args[0]
        password = args[1]
        if username == "list" or username == "quit":
            print("You cannot make an account called list or quit!")
            raise KeyboardInterrupt
        else:
            os.mkdir(os.path.join("Home", username))
        os.mkdir(os.path.join("Home", username))
        if password == "":
            print("You entered a blank password, that's not secure!")
            answer = input("Do you really want to continue? (Y/N):").lower()
            if answer == "n":
                raise KeyboardInterrupt
        else:
            passwordtxt = open(os.path.join("Home", username,".password"),"w")
            passwordtxt.write(password)
            passwordtxt.close()
    except Exception:
        username = args[0]
        if username == "list" or username == "quit":
            print("You cannot make an account called list or quit!")
            raise KeyboardInterrupt
        else:
            os.mkdir(os.path.join("Home", username))
        password = input("Password:")
        if password == "":
            print("You entered a blank password, that's not secure!")
            answer = input("Do you really want to continue? (Y/N):").lower()
            if answer == "n":
                raise KeyboardInterrupt
        else:
            passwordtxt = open(os.path.join("Home", username,".password"),"w")
            passwordtxt.write(password)
            passwordtxt.close()
else:
    username = input("Username:")
    if username == "list" or username == "quit":
        print("You cannot make an account called list or quit!")
        raise KeyboardInterrupt
    else:
        os.mkdir(os.path.join("Home", username))
    password = input("Password:")
    if password == "":
        print("You entered a blank password, that's not secure!")
        answer = input("Do you really want to continue? (Y/N):").lower()
        if answer == "n":
            raise KeyboardInterrupt
    else:
        passwordtxt = open(os.path.join("Home", username,".password"),"w")
        passwordtxt.write(password)
        passwordtxt.close()
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
user = info[0]
dir = info[1]
#groups = {}
exec(open(os.path.join("Home","groups.py"),"r").read())
if args != []:
    try:
        username = args[0]
        if not user in groups.get("Administrators") and user != username:
            print("You cannot change the password of other users!")
            raise KeyboardInterrupt
        password = args[1]
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
        if not user in groups.get("Administrators") and user != username:
            print("You cannot change the password of other users!")
            raise KeyboardInterrupt
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
    if not user in groups.get("Administrators") and user != username:
        print("You cannot change the password of other users!")
        raise KeyboardInterrupt
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
import os

argsfile = open(os.path.join("exec", "args.txt"), "r")
argsTemp = argsfile.readlines()
args = []
for i in argsTemp:
    if i == argsTemp[len(argsTemp)-1]:
        args.append(i)
    else:
        args.append(i[0:-1])

if args != []:
    try:
        username = args[0]
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
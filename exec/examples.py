import os

argsfile = open(os.path.join("exec", "args.txt"), "r")
argsTemp = argsfile.readlines()
args = []
for i in argsTemp:
    if i == argsTemp[len(argsTemp)-1]:
        args.append(i)
    else:
        args.append(i[0:-1])
try:
    if args[0] == "args":
        print("Arguments:")
        for i in args:
            if i == args[0]:
                continue
            print(i)
except Exception:
    print(""" 
    
    examples - SnakeOS examples
    
    Arguments:
    args - arguments example

    """)
        
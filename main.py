from math import *


num1 = input("Number 1:")
try: 
    num1 = int(num1)
except Exception:
    try:
        num1 = float(num1)
    except:
        raise KeyboardInterrupt
num2 = input("Number 2:")
try:
    num2 = int(num2)
except Exception:
    try:
        num2 = float(num2)
    except Exception:
        num2 = 0
op = input("Operation (+,-,*,/,%,**,abs,sqrt,ezp,mog,log10):")
    
if op == "+":
    print("Result: " + str(num1+num2))
elif op == "-":
    print("Result: " + str(num1-num2))
elif op == "*":
    print("Result: " + str(num1*num2))
elif op == "/":
    print("Result: " + str(num1/num2))
elif op == "%":
    print("Result: " + str(num1%num2))
elif op == "**":
    print("Result: " + str(num1**num2))
elif op == "abs":
    print("Result: " + str(abs(num1)))
elif op == "sqrt":
    print("Result: " + str(sqrt(num1)))
elif op == "exp":
    print("Result: " + str(exp(num1)))
elif op == "log":
    print("Result: " + str(log(num1)))
elif op == "log10":
    print("Result: " + str(log10(num1)))

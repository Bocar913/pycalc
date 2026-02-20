import sys

a = float(sys.argv[1])
b = float(sys.argv[3])
op = sys.argv[2]
if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "/":
    if b == 0 :
        print("impossible")
    else :
        print(a/b)
elif op == "*":
    print (a*b)
elif op == "*":
    print (a*b)
else :
    print("Opérateur non valide")
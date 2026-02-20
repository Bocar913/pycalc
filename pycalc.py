a = 
b = 
op = ""
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
else :
    print("Opérateur non valide")

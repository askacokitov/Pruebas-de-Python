a = int(input("ingresa el numero 1:"))
b = int(input("ingresa el numero 2:"))

c = a + b
d = a - b
f = a * b

if b != 0:
    g = a / b
else:
    g = print("No es posible realizar división por 0.")

print("la suma es:" + str(c))
print("la resta es:" + str(d))
print("la multiplicacion es:" + str(f))
print("la division es:" + str(g))

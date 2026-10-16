a = int(input("ingresa el precio de compra:"))

if a >= 200000:
    b = a * 0.20
    print("el descuento es:" + str(b))
elif a >= 100000:
    c = a * 0.10
    print("el descuento es:" + str(c))
elif a < 100000:
    d = a
    print("el descuento es:" + str(d))

j = a - b
print("el precio final es:" + str(j))
k = a - c
print("el precio final es:" + str(k))


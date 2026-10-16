lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

if lado1 > 0 and lado2 > 0 and lado3 > 0:

    if lado1 == lado2 and lado2 == lado3:
        print("El triángulo es equilatero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isóceles.")
    else:
        print("El triángulo es escaleno.")
else:
    print("Los lados ingresados no forman un triángulo válido")

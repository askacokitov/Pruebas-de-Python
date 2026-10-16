print ("1. Sumar")
print ("2. Restar")
print ("3. Multiplicar")
print ("4. Dividir")

option = input("Seleccione una opción (1-4): ")

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if option == "1":
    resultado = numero1 + numero2
    print("El resultado de la suma es: ", resultado)

elif option == "2":
    resultado = numero1 - numero2
    print("El resultado de la suma es: ", resultado)

elif option == "3":
    resultado = numero1 * numero2
    print("El resultado de la multiplicación es: ", resultado)

elif option == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("El resultado de la división es: ", resultado)
    else:
        print("Error: no se puede dividir entre cero.")
else:
    print("Opción no válida.")
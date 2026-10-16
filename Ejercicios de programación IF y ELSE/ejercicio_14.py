saldo = 500000
opcion = 0

while opcion != 4:
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        print("Su saldo actual es: $", saldo)

    elif opcion == 2:
        retiro = float(input("Ingrese el valor a retirar: $"))

        if retiro > 0 and retiro <= saldo:
            saldo = saldo - retiro
            print("Retiro exitoso.")
            print("Su nuevo saldo es: $", saldo)
        elif retiro <= 0:
            print("El valor debe ser mayor que cero.")
        else:
            print("Saldo insuficiente.")

    elif opcion == 3:
        deposito = float(input("Ingrese el valor a depositar: $"))

        if deposito > 0:
            saldo = saldo + deposito
            print("Deposito exitoso.")
            print("Su nuevo saldo es: $", saldo)
        else:
            print("El deposito debe ser mayor que cero.")

    elif opcion == 4:
        print("Gracias por utilizar el cajero.")

    else:
        print("Opcion no valida. Intente nuevamente.")
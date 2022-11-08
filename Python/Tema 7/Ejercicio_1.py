import operaciones as op


def main():


    bucle = 1

    while bucle == True:


        x = int(input("Ingresa un numero :"))
        y = int(input("Ingresa otro numero :"))

        print("\nMenu de Opciones :")
        opc = int(input("\n1. Suma \n2. Resta \n3. Divide \n4. Multiplica "))

        if opc == 1:
            print("\nLa suma de", x, " y ", y, " es : ", op.suma(x, y))

        elif opc == 2:
            print("\nLa resta de ", x, " y ", y, "es : ", op.resta(x, y))
        
        elif opc == 3:
            print("\nLa division de ", x, " y ", y, "es : ", op.divide(x, y).__round__(2))
        
        elif opc == 4:
            print("\nLa multiplicacion de ", x, " y ", y, "es : ", op.multiplica(x, y))

        else:
            print("\nOpcion invalida ")

        bucle = int(input("\n1. Continuar \n2. Salir "))
        


if __name__ == '__main__':
    main()

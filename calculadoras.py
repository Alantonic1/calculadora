import math
import os
Tipo = 0
while (Tipo != "3"): # Mientras no se use 3 el menu se seguira imprimiendo
    print("""
          1. Simple
          2. Cientifica
          3. Apagar""")
    Tipo = input("selecciona tipo de calculadora ")
    Acum = 0
    evitarerror = "0" # este valor lo cree para evitar que de el mensaje de opcióne erronea al volver
    Uso = "0" # Este valor se usara para saber si el usuario ya lleva un acumulado o no, saber si quiere reusar lo que obtuvo de la operación anterior o no
    while (Tipo == "1"):
        print ("""
               1. Suma
               2. Resta
               3. División
               4. Multiplicación
               5. Reset 
               6. Regresar
               Resultado:""", Acum)
        ciclo = "1"
        Opcion = input("Selecciona operacion ")
        if (Opcion == "1" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("ingresa primer valor ")) #Recuerden usar floats para que acepte decimales
            v2 = float(input("ingresa segundo valor "))
            Acum = v1 + v2
            Uso = "1"
            while (ciclo == "1"):
                omt = input("¿Deseas agregar otro valor? S/N ")
                if (omt == "S" or omt == "s"):
                    print ("resultado:", Acum)
                    v1 = float(input("ingresa valor "))
                    Acum = Acum + v1
                elif (omt == "N" or omt == "n"):
                    ciclo = "0"
        elif (Opcion == "1" and Uso == "1"):
            os.system ("cls")
            so = input("¿deseas reusar el acumulado para la siguiente operación?  S/N ") # Profesor pidio le preguntaramos al usuario si queria reusar el acumulado
            if (so == "s" or so == "S"):
                v1 = float(input("ingresa valor "))
                Acum = Acum + v1
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum + v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresar primer valor "))
                v2 = float(input("ingresa segundo valor "))
                Acum = v1 + v2
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum + v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
            else:
                print ("opcion erronea")
        elif (Opcion == "2" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("ingresa primer valor "))
            v2 = float(input("ingresa segundo valor "))
            Acum = v1 - v2
            Uso = "1"
            while (ciclo == "1"):
                omt = input("¿Deseas agregar otro valor? S/N ")
                if (omt == "S" or omt == "s"):
                    print ("resultado:", Acum)
                    v1 = float(input("ingresa valor "))
                    Acum = Acum - v1
                elif (omt == "N" or omt == "n"):
                    ciclo = "0"
                else:
                    print ("opción erronea")
        elif (Opcion == "2" and Uso == "1"):
            os.system ("cls")
            so = input("¿deseas reusar el acumulado para la siguiente operación?  S/N ")
            if (so == "s" or so == "S"):
                v1 = float(input("ingresa valor "))
                Acum = Acum - v1
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum - v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresar primer valor "))
                v2 = float(input("ingresa segundo valor "))
                Acum = v1 - v2
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum - v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
            else:
                print ("opcion erronea")
        elif (Opcion == "3" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("ingresa primer valor "))
            v2 = float(input("ingresa segundo valor "))
            if (v1 == 0 or v2 == 0):
                print ("valor invalido")
            else:
                while (ciclo == "1"):
                    Acum = v1/v2
                    Uso = "1"
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum / v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
        elif (Opcion == "3" and Uso == "1"):
            os.system ("cls")
            so = input("¿deseas reusar el acumulado para la siguiente operación?  S/N ")
            if (so == "s" or so == "S"):
                v1 = float(input("ingresa valor "))
                if (v1 == 0):
                    print("valor invalido")
                else:
                    Acum = Acum / v1
                    while (ciclo == "1"):
                        omt = input("¿Deseas agregar otro valor? S/N ")
                        if (omt == "S" or omt == "s"):
                            print ("resultado:", Acum)
                            v1 = float(input("ingresa valor "))
                            Acum = Acum / v1
                        elif (omt == "N" or omt == "n"):
                            ciclo = "0"
                        else:
                            print ("opción erronea")
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresar primer valor "))
                v2 = float(input("ingresa segundo valor "))
                if (v1 == 0 or v2 == 0):
                    print ("valor invalido")
                else:
                    Acum = v1 / v2
                    while (ciclo == "1"):
                        omt = input("¿Deseas agregar otro valor? S/N ")
                        if (omt == "S" or omt == "s"):
                            print ("resultado:", Acum)
                            v1 = float(input("ingresa valor "))
                            Acum = Acum / v1
                        elif (omt == "N" or omt == "n"):
                            ciclo = "0"
                        else:
                            print ("opción erronea")
        elif (Opcion == "4" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("ingresa primer valor "))
            v2 = float(input("ingresa segundo valor "))
            Acum = v1 * v2
            Uso = "1"
            while (ciclo == "1"):
                omt = input("¿Deseas agregar otro valor? S/N ")
                if (omt == "S" or omt == "s"):
                    print ("resultado:", Acum)
                    v1 = float(input("ingresa valor "))
                    Acum = Acum * v1
                elif (omt == "N" or omt == "n"):
                    ciclo = "0"
                else:
                    print ("opción erronea")
        elif (Opcion == "4" and Uso == "1"):
            os.system ("cls")
            so = input("¿deseas reusar el acumulado para la siguiente operación?  S/N ")
            if (so == "s" or so == "S"):
                v1 = float(input("ingresa valor "))
                Acum = Acum * v1
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum * v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresar primer valor "))
                v2 = float(input("ingresa segundo valor "))
                Acum = v1 * v2
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum * v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
            else:
                print ("opcion erronea")
        elif (Opcion == "5"):
            os.system ("cls")
            Acum = 0
            Uso = "0"
        elif (Opcion == "6"):
            os.system ("cls")
            Tipo = "0"
            evitarerror = "1"
        else:
            print ("Opción erronea")
    while (Tipo == "2"):
        print ("""
               1. Suma
               2. Resta
               3. División
               4. Multiplicación
               5. Seno
               6. Coseno
               7. Tangente
               8. Cotangente
               9. Arcoseno
               10. Arcocoseno
               11. Raiz Cuadrada
               12. Potencia
               13. Factorial
               14. Reset
               15. Regresar
               Resultado:""", Acum)
        ciclo = "1"
        Opcion = input("Selecciona operacion ")
        if (Opcion == "1" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("ingresa primer valor ")) 
            v2 = float(input("ingresa segundo valor "))
            Acum = v1 + v2
            Uso = "1"
            while (ciclo == "1"):
                omt = input("¿Deseas agregar otro valor? S/N ")
                if (omt == "S" or omt == "s"):
                    print ("resultado:", Acum)
                    v1 = float(input("ingresa valor "))
                    Acum = Acum + v1
                elif (omt == "N" or omt == "n"):
                    ciclo = "0"
                else:
                    print ("opción erronea")
        elif (Opcion == "1" and Uso == "1"):
            os.system ("cls")
            so = input("¿deseas reusar el acumulado para la siguiente operación?  S/N ") 
            if (so == "s" or so == "S"):
                v1 = float(input("ingresa valor "))
                Acum = Acum + v1
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum + v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresar primer valor "))
                v2 = float(input("ingresa segundo valor "))
                Acum = v1 + v2
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum + v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
            else:
                print ("opcion erronea")
        elif (Opcion == "2" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("ingresa primer valor "))
            v2 = float(input("ingresa segundo valor "))
            Acum = v1 - v2
            Uso = "1"
            while (ciclo == "1"):
                omt = input("¿Deseas agregar otro valor? S/N ")
                if (omt == "S" or omt == "s"):
                    print ("resultado:", Acum)
                    v1 = float(input("ingresa valor "))
                    Acum = Acum - v1
                elif (omt == "N" or omt == "n"):
                    ciclo = "0"
                else:
                    print ("opción erronea")
        elif (Opcion == "2" and Uso == "1"):
            os.system ("cls")
            so = input("¿deseas reusar el acumulado para la siguiente operación?  S/N ")
            if (so == "s" or so == "S"):
                v1 = float(input("ingresa valor "))
                Acum = Acum - v1
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum - v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresar primer valor "))
                v2 = float(input("ingresa segundo valor "))
                Acum = v1 - v2
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum - v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
            else:
                print ("opcion erronea")
        elif (Opcion == "3" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("ingresa primer valor "))
            v2 = float(input("ingresa segundo valor "))
            if (v1 == 0 or v2 == 0):
                print ("valor invalido")
            else:
                Acum = v1 / v2
                Uso = "1"
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum / v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
        elif (Opcion == "3" and Uso == "1"):
            os.system ("cls")
            so = input("¿deseas reusar el acumulado para la siguiente operación?  S/N ")
            if (so == "s" or so == "S"):
                v1 = float(input("ingresa valor "))
                if (v1 == 0):
                    print("valor invalido")
                else:
                    Acum = Acum / v1
                    while (ciclo == "1"):
                        omt = input("¿Deseas agregar otro valor? S/N ")
                        if (omt == "S" or omt == "s"):
                            print ("resultado:", Acum)
                            v1 = float(input("ingresa valor "))
                            Acum = Acum / v1
                        elif (omt == "N" or omt == "n"):
                            ciclo = "0"
                        else:
                            print ("opción erronea")
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresar primer valor "))
                v2 = float(input("ingresa segundo valor "))
                if (v1 == 0 or v2 == 0):
                    print ("valor invalido")
                else:
                    Acum = v1 / v2
                    while (ciclo == "1"):
                        omt = input("¿Deseas agregar otro valor? S/N ")
                        if (omt == "S" or omt == "s"):
                            print ("resultado:", Acum)
                            v1 = float(input("ingresa valor "))
                            Acum = Acum / v1
                        elif (omt == "N" or omt == "n"):
                            ciclo = "0"
                        else:
                            print ("opción erronea")
            else:
                print ("opcion erronea")
        elif (Opcion == "4" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("ingresa primer valor "))
            v2 = float(input("ingresa segundo valor "))
            Acum = v1 * v2
            Uso = "1"
            while (ciclo == "1"):
                omt = input("¿Deseas agregar otro valor? S/N ")
                if (omt == "S" or omt == "s"):
                    print ("resultado:", Acum)
                    v1 = float(input("ingresa valor "))
                    Acum = Acum * v1
                elif (omt == "N" or omt == "n"):
                    ciclo = "0"
                else:
                    print ("opción erronea")
        elif (Opcion == "4" and Uso == "1"):
            os.system ("cls")
            so = input("¿deseas reusar el acumulado para la siguiente operación?  S/N ")
            if (so == "s" or so == "S"):
                v1 = float(input("ingresa valor "))
                Acum = Acum * v1
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum * v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresar primer valor "))
                v2 = float(input("ingresa segundo valor "))
                Acum = v1 * v2
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum * v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
            else:
                print ("opcion erronea")
        elif (Opcion == "5" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("Ingresa valor "))
            Acum = math.sin(math.radians(v1))
            Uso = "1"
        elif (Opcion == "5" and Uso == "1"):
            os.system ("cls")
            so = input("¿Deseas reusar el acumulado para la siguiente operación? S/N ")
            if (so == "s" or so == "S"):
                Acum = math.sin(math.radians(Acum))
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresa valor "))
                Acum = math.sin(math.radians(v1))
            else:
                print ("opcion erronea")
        elif (Opcion == "6" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("Ingresa valor "))
            Acum = math.cos(math.radians(v1))
            Uso = "1"
        elif (Opcion == "6" and Uso == "1"):
            os.system ("cls")
            so = input("¿Deseas reusar el acumulado para la siguiente operación? S/N ")
            if (so == "s" or so == "S"):
                Acum = math.cos(math.radians(Acum))
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresa valor "))
                Acum = math.cos(math.radians(v1))
            else:
                print ("opcion erronea")
        elif (Opcion == "7" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("Ingresa valor "))
            Acum = math.tan(math.radians(v1))
            Uso = "1"
        elif (Opcion == "7" and Uso == "1"):
            os.system ("cls")
            so = input("¿Deseas reusar el acumulado para la siguiente operación? S/N ")
            if (so == "s" or so == "S"):
                Acum = math.tan(math.radians(Acum))
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresa valor "))
                Acum = math.tan(math.radians(v1))
            else:
                print ("opcion erronea")
        elif (Opcion == "8" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("Ingresa valor "))
            Acum = math.atan(math.radians(v1))
            Uso = "1"
        elif (Opcion == "8" and Uso == "1"):
            os.system ("cls")
            so = input("¿Deseas reusar el acumulado para la siguiente operación? S/N ")
            if (so == "s" or so == "S"):
                Acum = math.atan(math.radians(Acum))
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresa valor "))
                Acum = math.atan(math.radians(v1))
            else:
                print ("opcion erronea")
        elif (Opcion == "9" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("Ingresa valor "))
            Acum = math.asin(math.radians(v1))
            Uso = "1"
        elif (Opcion == "9" and Uso == "1"):
            os.system ("cls")
            so = input("¿Deseas reusar el acumulado para la siguiente operación? S/N ")
            if (so == "s" or so == "S"):
                Acum = math.asin(math.radians(Acum))
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresa valor "))
                Acum = math.asin(math.radians(v1))
            else:
                print ("opcion erronea")
        elif (Opcion == "10" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("Ingresa valor "))
            Acum = math.acos(math.radians(v1))
            Uso = "1"
        elif (Opcion == "10" and Uso == "1"):
            os.system ("cls")
            so = input("¿Deseas reusar el acumulado para la siguiente operación? S/N ")
            if (so == "s" or so == "S"):
                Acum = math.acos(math.radians(Acum))
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresa valor "))
                Acum = math.acos(math.radians(v1))
            else:
                print ("opcion erronea")
        elif (Opcion == "11" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("Ingresa valor "))
            Acum = math.sqrt(v1)
            Uso = "1"
        elif (Opcion == "11" and Uso == "1"):
            os.system ("cls")
            so = input("¿Deseas reusar el acumulado para la siguiente operación? S/N ")
            if (so == "s" or so == "S"):
                Acum = math.sqrt(Acum)
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresa valor "))
                Acum = math.sqrt(v1)
            else:
                print ("opcion erronea")
        elif (Opcion == "12" and Uso == "0"):
            os.system ("cls")
            v1 = float(input("ingresa primer valor "))
            v2 = float(input("ingresa segundo valor "))
            Acum = v1**v2
            Uso = "1"
            while (ciclo == "1"):
                omt = input("¿Deseas agregar otro valor? S/N ")
                if (omt == "S" or omt == "s"):
                    print ("resultado:", Acum)
                    v1 = float(input("ingresa valor "))
                    Acum = Acum ** v1
                elif (omt == "N" or omt == "n"):
                    ciclo = "0"
                else:
                    print ("opción erronea")
        elif (Opcion == "12" and Uso == "1"):
            os.system ("cls")
            so = input("¿Deseas reusar el acumulado para la siguiente operación? S/N ")
            if (so == "s" or so == "S"):
                v1 = float(input("ingresa valor "))
                Acum = Acum**v1
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum ** v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
            elif (so == "n" or so == "N"):
                v1 = float(input("ingresa primer valor "))
                v2 = float(input("ingresa segundo valor "))
                Acum = v1**v2
                while (ciclo == "1"):
                    omt = input("¿Deseas agregar otro valor? S/N ")
                    if (omt == "S" or omt == "s"):
                        print ("resultado:", Acum)
                        v1 = float(input("ingresa valor "))
                        Acum = Acum ** v1
                    elif (omt == "N" or omt == "n"):
                        ciclo = "0"
                    else:
                        print ("opción erronea")
            else:
                print ("opcion erronea")
        elif (Opcion == "13" and Uso == "0"):
            os.system ("cls")
            v1 = int(input("ingresa valor "))
            Acum = math.factorial(v1)
            Uso = "1"
        elif (Opcion == "13" and Uso == "1"):
            os.system ("cls")
            so = input("¿Deseas reusar el acumulado para la siguiente operación? S/N ")
            if (so == "s" or so == "S"):
                Acum = math.factorial(int(Acum))
            elif (so == "n" or so == "N"):
                v1 = int(input("ingresa valor "))
                Acum = math.factorial(v1)
            else:
                print ("opcion erronea")
        elif (Opcion == "14"):
            os.system ("cls")
            Acum = 0
            Uso = "0"
        elif (Opcion == "15"):
            os.system ("cls")
            Tipo = "0"
            evitarerror = "1"
        else:
            print ("Opción erronea")
    if (Tipo == "3"):
        print ("apagando")
    elif (evitarerror != "1"): # Validación de datos, igual lo pidio el profe
        print ("opción erronea")
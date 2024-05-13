#Diego Escobar Osorio
import math
print("Semana 12, Ejercicio 1")

print("Seleccionar opción" , "a. Sumatoria",
"b. Factorial" , 
"c. Tablas de Multiplicar",
"d. Número perfecto",
sep = "\n")

opción = input("Seleccione la opción: ")

match opción:
    case "a":
        num = int(input("Ingrese un numero positivo: "))
        if num <=0: 
            print("Error, número no valido")
        else: 
            suma = 0
            for contador in range (1,num+1):
                suma += contador
            print("La sumatoria del numero es", suma)
    case "b":
        num2 = int(input("Ingrese un número positivo: "))
        if num2 <= 0:
            print("Error, número no valido")
        else:
            #factorial = math.factorial
            factorial = 1
            for i in range (1, num2+1):
                factorial *= i
                print("El factorial es", factorial)
    case "c":
        titulo = "\t"
        #Imprimir titulo de columnas
        for columna in range (1,11):
            titulo += str(columna) + "\t"
        print(titulo)

        #Imprimir las filas
        TextFil = ""
        for fila in range (1,11):
            TextFil = str(fila) + "\t"
        
        for columna in range (1,11):
            TextFil += str(fila * columna) + "\t"
        print(TextFil)
    case "d":
        num1 = int(input("Inserte un número: "))
        if num1 <= 0:
            print("Error, ingrese un número positivo")
        else: 
            suma = 0
        for x in range (1, num1):
            if num1 % x == 0:
                suma += x
        if suma == num1:
            print("El numero es completamente perfecto")
        else:
            print("El numero no es perfecto")

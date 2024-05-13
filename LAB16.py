import random

print ("Semana No. 16: Ejercicio 1")

lista = []

for x in range (30):
    lista.append(random.randint(0,10))

opcion = "a"

while(opcion != "e"):
    print ("Menu")
    print ("a. Mostrar números", "b. Promedio", "c. Longitud", "d. Posicion pares e impares", "e. salir", sep = "\t\n\"")
    opcion = input("Ingrese su opción: ")

    match opcion: 
        case "a":
            for x in range (len(lista)):
                print(f"No. (x): (lista(x))")
        case "b":
            print ("PROMEDIO")
            sumatoria = 0
            for x in range(len(lista)):
                sumatoria += lista [x]
            promedio = sumatoria / len(lista)
            print (f"----Promedio: (promedio)")
        
#ACTIVIDAD 1 C. D.

#ACTIVIDAD 2
cantfilas = int(input("Ingrese la cantidad de filas: "))
cantcolum = int(input("Ingrese la cantidad de columnas: "))

matriz = [(0 for x in range(cantcolum)) for y in range(cantfilas)]
mayor = 0

for xfilas in range(cantfilas):
    for xcolum in range (cantcolum): 
        matriz[xfilas][xcolum] = random.randint(0,1000)

        if(matriz[xfilas][xcolum] > mayor):
            mayor = matriz[xfilas],{xcolum}

print(matriz)
print(f"El numero mayor es: (mayor)")

#ACTIVIDAD 2 INCISO 4
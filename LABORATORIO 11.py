##Trabajo entre Diego Escobar y Jose Javier Birriondo

#Actividad 1 Inciso A

num = int(input("Ingrese un número mayor a 0: "))

if (num <= 0):
    print("Error: el número debe ser mayor a 0")

resultadoA = 0
for x in range (1, num +1):
    resultadoA += 1/x

print("Inciso A:", resultadoA)


#Inciso B

num2 = int(input("Ingrese un número mayor a 0: "))

if (num2 <= 0):
    print("Error: el número debe ser mayor a 0")

num3 = int(input("Ingrese un número mayor a 0: "))

if (num3 <= 0):
    print("Error: el número debe ser mayor a 0")

resultadoB = 0
for w in range (1, num2 +1):
    for y in range (1, num3 +1):
        resultadoA += 1/w**y



print("Inciso B:", resultadoB)

#Inciso C

num4 = int(input("Ingrese un número mayor a 0: "))

if (num4 <= 0):
    print("Error: el número debe ser mayor a 0")

a = int(input("Ingrese un número mayor a 0: "))

if (a <= 0):
    print("Error: el número debe ser mayor a 0")

n = int(input("Ingrese un número mayor a 0: "))

if (n <= 0):
    print("Error: el número debe ser mayor a 0")

k = 0
resultadoC = 0
for z in range (1, num4 +1):
    resultadoC += (z*k)*a*(n*-k)
    k += 1
print("Inciso C:", resultadoC)




#Actividad 2
n= int(input("Ingrese un número mayor a 0  "))

if(n <= 0):
        print("Error, debe ser mayor a 0")

#Definición de variables
a = 0
b = 1
c = 0
i = 2
resultado = ""

if (n > 0):
    resultado = str(a)

    if(n>1) : 
        resultado += "," + str (b)

    while (i < n):
        c = a + b
        resultado += "," + str(c)
        a = b
        b = c
        i = i + 1
        #print ("Adentro ciclo:, resultado")

    print (resultado)
else:
    print(resultado)



print("Semana No. 11: Ejercicio 2")
n2 = int(input("Ingrese un número mayor a 0  "))
if(n2 <= 0):
    print("Error, debe ser mayor a 0")


#Inciso A 
resultadoA = 0
for x in range(1, n2 + 1):
    resultadoA += 1/x

print("Inciso A:" , resultadoA)
print("Actividad #1")

def triangulo (base, altura):
    calcular1 = base * altura
    area1 = calcular1 / 2
    return area1

def rectangulo (base, altura):
    area2 = base * altura
    return area2

def cuadrado (lado):
    area3 = lado**2
    return area3

def circulo (radio):
    pi = 3.14159
    radio1 = radio**2
    area4 = radio1 * pi
    return area4

print("Menú:", 
"a. Area del circulo", 
"b. Area del triangulo",
"c. Area del cuadrado",
"d. Area del rectangulo",
sep = "\n")

opcion = input("Ingresar opción: ")

match opcion:

    case "a":
        numero1 = int(input("Ingresar radio: "))

        print("El área del circulo es: " + str(circulo(numero1)))

    case "b":
        numero1 = int(input("Ingresar base: "))
        numero2 = int(input("Ingresar altura: "))

        print("El área del triangulo es: " + str(triangulo(numero1, numero2)))

    case "c":
        numero1 = int(input("Ingresar lado: "))

        print("El área del cuadrado es: " + str(cuadrado(numero1)))

    case "d":
        numero1 = int(input("Ingresar base: "))
        numero2 = int(input("Ingresar altura: "))

        print("La sumatoria es: " + str(rectangulo(numero1, numero2)))

    case _:
        print("Opción no válida, ingresar una del menú")

#ACTIVIDAD #2
x=0
y=0

def MoverPosicion(cantX, cantY):
    global x, y 
    x += cantX
    y += cantY

opcion="a"
while(opcion != "e"):
    print("Menú")
    print("a. Sube", "b. Baja", "c. Izquierda", "d. Derecha", "e. Salir", sep= "\t\n")
    opcion= input("Ingresar opción:  ")

    match opcion:
        case "a":
            MoverPosicion(0,1)
        case "b":
            MoverPosicion(0,-1)
        case "c":
            MoverPosicion(-1,0)
        case "d":
            MoverPosicion(1,0)
        case "x":
            x=0
            y=0

    print(f"La posición actual es de: [{x}][{y}]")

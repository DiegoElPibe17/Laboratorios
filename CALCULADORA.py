import math
print("Programa de suma")
num1 = input("ingrese un numero para sumar: ")
num2 = input("ingrese segundo numero: ")
num1 = int(num1)
num2 = int(num2)
resultadosuma = num1+num2
print ("El resultado es:",resultadosuma)

raíz = math.sqrt(num1)
print (f"La raíz cuadrada es,{raíz:.2f}")

potencia = num1 ** num2
print("La potencia es ", str(potencia))

print("Programa de resta")
num3 = input("ingrese un numero para restar: ")
num4 = input("ingrese otro numero: ")
num3 = int(num3)
num4 = int(num4)
resultadoresta= num3-num4
print("El resultado es:",resultadoresta)

print("Programa de multiplicacion")
num5 = input("ingrese un numero para multiplicar: ")
num6 = input("ingrese otro numero: ")
num5 = int(num5)
num6 = int(num6)
resultadomulti= num5*num6
print("El resultado es:",resultadomulti)

print("Programa de division")
num7 = input("ingrese un numero para dividir: ")
num8 = input("ingrese otro numero: ")
num7 = int(num7)
num8 = int(num8)
resultadodiv= num7/num8
print("El resultado es:",resultadodiv)
 for x in range (1, num1):
        if num1 % x == 0:
            suma += x

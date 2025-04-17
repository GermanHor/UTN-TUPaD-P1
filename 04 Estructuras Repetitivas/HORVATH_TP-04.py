#Ejercicio 1
for num in range(101):
    print(num)

#Ejercicio 2
contador = 0 
num = int(input("ingrese un numero"))
while num > 0:
    num = num // 10
    contador += 1
print("la cantidad de digitos de el numero ingresado es",contador)

#Ejercicio 3
num1 = int(input("ingese un numero"))
num2 = int(input("ingese otro numero"))
if num1 < num2:
    chico = num1
    grande = num2
else:
    chico = num2
    grande = num1
    
acumulado = 0
for sumatoria in range (chico + 1, grande):
    acumulado += sumatoria   
print(acumulado)

#Ejercicio 4
acumulado = 0
num = -1
while num != 0:
    num = int(input("ingrese un numero entero. Ingrese 0 para terminar: "))
    acumulado += num
    print ("El acumulado es:",acumulado)

#Ejercicio 5
import random
num = random.randint(0, 9)
num2 = -1
while num !=num2:
    num2 = int(input("ingrese un numero entre 0 y 9: "))
    if num2 == num:
        print("\nFelicitaciones, es el numero correcto")
    else:
        print("No es el numero correcto")

#Ejercicio 6
for i in range(100, 0, -2):
    print(i)

#Ejercicio 7
num = int(input("ingrese un numero entero positivo: "))
sumatoria = 0
for i in range(0, num+1):
    sumatoria += i
print("La suma de todos los numeros comprendidos entre",num, "y 0 es:",sumatoria)

#Ejercicio 8
pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range(0, 100):
   num = int(input("Ingrese un numero: "))
   if num % 2 == 0:
       pares += 1
   else:
       impares +=1
   if num < 0:
        negativos += 1
   elif num > 0:
        positivos += 1
print("\n Pares:",pares,"\n Impares:",impares,"\n Positivos:",positivos,"\n Negativos:", negativos,"\n")

#Ejercicio 9
num = 0
sum = 0
rango = 100
for i in range(0,rango):
   num = int(input("ingrese un numero: "))
   sum += num
print("La media es ", sum/rango,) 

#Ejercicio 10
num = int(input("ingrese un numero"))
mun = ""
digito = 0
while num > 1:
    digito = num % 10
    mun = mun + str(digito)
    num = num // 10
print(mun) 
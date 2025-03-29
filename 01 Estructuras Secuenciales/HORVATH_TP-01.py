
# TRABAJO PRACTICO NUMERO 1 
# ALUMNO: GERMAN HORVATH


#Ejercicio 1
print ("Hola mundo!")

#Ejercicio 2

nombre = input("ingrese su nombre")
print ("Hola", nombre, "!")

#Ejercicio 3
nombre = input("Ingrese su nombre")
apellido = input("ingrese su apellido")
edad = input("Ingrese su edad")
pais = input("ingrese su pais")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}")

#Ejercicio 4
radio = input("Ingrese el radio")
radio = int(radio)
perimetro = radio 
pi = 3.1416
area = radio * radio * pi
perimetro = radio * 2 * pi
print(f"El area es {area} y su perimetro es {perimetro}")

#Ejercicio 5
radio = input("Ingrese el radio")
radio = int(radio)
perimetro = radio 
pi = 3.1416
area = radio * radio * pi
perimetro = radio * 2 * pi
print(f"El area es {area} y su perimetro es {perimetro}")

#Ejercicio 6
num = input("Ingrese dos numeros")
num = int(num)

print(f"1 x {num} = {num *  1}")
print(f"2 x {num} = {num *  2}")
print(f"3 x {num} = {num *  3}")
print(f"4 x {num} = {num *  4}")
print(f"5 x {num} = {num *  5}")
print(f"6 x {num} = {num *  6}")
print(f"7 x {num} = {num *  7}")
print(f"8 x {num} = {num *  8}")
print(f"9 x {num} = {num *  9}")
print(f"10 x {num} = {num *  10}")

#Ejercicio 7
num1 = int(input("Ingrese un numero distinto de cero"))
num2 = int(input("Ingrese otro numero distinto de cero"))

print(f"{num1} mas {num2} es {num1 + num2}")
print(f"{num1} dividido {num2} es {num1 / num2}")
print(f"{num1} multiplicado {num2} es {num1 * num2}")
print(f"{num1} menos {num2} es {num1 - num2}")

#Ejercicio 8
peso = float(input("Ingrese su peso en kg"))
altura = float(input("Ingrese su altura en metros"))

print(f"Su indice de masa corporal es: {peso/altura**2}")

#Ejercicio 9
temperatura = float(input("Ingrese la temperatura en grados celsius"))

print(f"La temperatura en fahrenheit es: {(9/5)*temperatura + 32}")

#Ejercicio 10
num1 = int(input("ingrese el primer numero"))
num2 = int(input("ingrese el segundo numero"))
num3 = int(input("ingrese el tercer numero"))
promedio =(num1 + num2 + num3) / 3

print(f"el promedio es: {promedio}")
# Trabajo Practico N°3
#Alumno German Horavth
#
#Ejercicio 1
edad = int(input("¿Cuál es su edad?"))
if edad >= 18:
    print("es mayor de edad")
    
#Ejercicio 2
nota = int(input("Ingrese la nota"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
numero = int(input("Ingrese un numero par"))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4
edad = int(input("ingrese su edad"))
if edad < 12:
    print("niño")
elif edad >= 12 and edad < 18:
    print("adolescente")
elif edad >= 18 and edad < 30:
    print ("Adulto/a joven")
else:
    print ("Adulto/a")

#Ejercicio 5
contrase = (len(input("introducir contraseñas de entre 8 y 14 caracteres")))
if contrase > 7 and contrase < 15:
    print("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
#Ejercicio 6
from statistics import mode, median, mean 
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)


if media > mediana:
    print ("hay sesgo positivo")
elif media < mediana:
    print ("hay sesgo negativo")
elif media == mediana == moda:
    print("No hay sesgo")

#Ejercicio 7
frase = input("Ingrese una frase o palabra")
ultima = frase[-1]
if ultima in "aeiou":
    print(frase + "!")
else:
    print(frase)

#Ejercicio 8
nombre = input("Ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. \n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. \n3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion = int(input("ingrese una opcion (1, 2 o 3) "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("opcion no valida")

#Ejercicio 9
magnitud = int(input("ingrese la magnitud"))
if magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("muy leve")
elif 4 <= magnitud < 5:
    print("moderado")
elif 5 <= magnitud < 6:
    print("fuerte")
elif 6 <= magnitud < 7:
    print("muy fuerte")
elif magnitud > 7:
    print("Extremo")

#Ejercicio 10
emisferio = input("¿En que esmisferio se encuentra? (N para norte S para sur) ").lower()
mes = int(input("¿Mes del año? (numero)"))
dia = int(input("¿Dia del mes? "))
mes = mes * 100
fecha = mes + dia
if emisferio == "n":
    if fecha >= 321 and fecha <= 620:
        print("primavera")
    elif fecha >= 621 and fecha <= 920:
        print("verano")
    elif fecha >= 921 and fecha <= 1220:
        print("otoño")
    elif 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        print("invierno")
    
elif emisferio == "s":
    if fecha >= 321 and fecha <= 620:
      print("otoño") 
    elif fecha >= 621 and fecha <= 920:
     print("invierno")
    elif fecha >= 921 and fecha <= 1220:
     print("primavera")
    elif 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
     print("invierno") 
else:
    print("texto no valido")


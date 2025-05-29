#EJERCICIO 1

# Funcion
def imprimir_hola_mundo():
    print("Hola Mundo!")
# programa principal
imprimir_hola_mundo()

#EJERCICIO 2
#Funcion
def saludar_usuario(nombre):
    return "Hola, "+nombre
           
#Principal
print(saludar_usuario("pol"))

#EJERCICIO 3
#Funcion
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    
#Principal
nombre = input("Ingrese su nombre: ")
apellido = input("ingrese su apellodo: ")
edad = input("ingrese su edad: ")
residencia = input("ingrese la ciudad donde vive: ")

informacion_personal(nombre, apellido, edad, residencia)

#EJERCICIO 4
#Funcion area circulo
def calcular_area_circulo(radio):
    return (radio)**2 * 3.14
#Funcion perimetro de circulo
def calcular_perimetro_circulo(radio):
    return (radio) * 3.14 * 2

#Principal
radio = float(input("Ingrese el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print (f"el area del circulo es {area} y el perimetro es {perimetro}")

#EJERCICIO 5
#Funciones
def segundos_a_horas(segundos):
    return segundos/3600 

#Principal
segundos = int(input("ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
radio = print(f"{segundos} equivale a {horas} horas")

#EJERCICIO 6
#Funciones
def tabla_multiplicar(numero):
    for i in range (1, 11):
        resultado = numero * i
        print (f"{numero} x {i} = {resultado}")

#Principal
numero = int(input("ingrese un numero: "))
tabla_multiplicar(numero)

#EJERCICIO 7
#Funciones
def operaciones_basicas(a, b):
   suma = a + b
   resta = a - b
   multiplicacion = a * b
   division = a / b 
   return (suma, resta, multiplicacion, division)


#Principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo numero: "))

resultados = operaciones_basicas(a, b)

print(f"\nResultados: ")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}")
print(f"División: {resultados[3]}")

#EJERCICIO 8
#Funciones
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
    
#Principal
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"El indice de masa corporal es: {imc}")


#EJERCICIO 9
#Funciones
def celsius_a_fahrenheit(celsius):
    return (celsius * (9/5)) + 32    

#Principal
celsius = float(input("ingrese los grados celsius: "))
print(f"{celsius} grados celsius son {celsius_a_fahrenheit(celsius)} grados fahrenheit")


#EJERCICIO 10
#Funciones
def calcular_promedio(a, b, c):
    return (a + b + c)/3
    

#Principal
a = int(input("ingrese un numero: "))
b = int(input("ingrese otro numero: "))
c = int(input("ingrese otro numero: "))

print(f"El promedio es {calcular_promedio(a, b, c)}")
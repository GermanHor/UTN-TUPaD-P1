#TRABAJO PRACTICO 5
# Alumno: German Horvath

#EJercicio 1

multiplos = list(range(4, 101, 4))
print(multiplos)

#Ejercicio 2
vehiculos = ["bicicleta", "auto", "moto", "colectivo", "avion"]
print(vehiculos[-2])

#Ejercicio 3
lista = []
lista.append("perro")
lista.append("gato")
lista.append("conejo")
print(lista)


#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#Ejercicio 5
#En el ejemplo mostrado, se elimina el mayor de la lista
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#Ejercicio 6
lista = list(range(10, 31, 5))
print(lista[0:2])

#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["vento", "ranger"]
print(autos)

#Ejercicio 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1]= "tallarines"
compras[0].remove("pan")
print(compras)
 
 #Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
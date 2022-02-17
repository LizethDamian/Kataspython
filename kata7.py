#Ejercicio 1 uso de ciclos while en python 
from hashlib import new


newplanet = input("Favor de ingresar el nombre de los planetas: ")

planets = []

while newplanet.lower() != 'done':
    if newplanet:
        planets.append(newplanet)

        newplanet = input("Ingrese otro planeta o coloque 'done' si ya ha terminado: ")

#Ejercicio 2 Mostrar los planetas ingresados por el usuario 

for planet in planets: 
    print(planets)


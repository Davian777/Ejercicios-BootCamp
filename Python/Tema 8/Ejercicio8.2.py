
from pickle import *

class Vehiculo:

    def __init__(self, marca, color, puertas):
        self.marca = marca
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return self.marca + " " + self.color + " " + self.puertas


auto1 = Vehiculo("Toyota", "Azul", "4")
print(auto1)

file = open('vehiculo_objeto', 'w+b')

dump(auto1, file)

file.seek(0)
nuevo_auto = load(file)

print(nuevo_auto)
file.close()
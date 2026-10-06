# Los módulos proporcionan funciones que podemos reutilizar

# Se importa el módulo matemático completo
import math

resultado = math.sqrt(25)

print(resultado)


# También se puede importar únicamente una función
from math import sqrt

resultado = sqrt(25)

print(resultado)


# random permite generar valores aleatorios
import random

numero_aleatorio = random.randint(1, 10)

print(numero_aleatorio)


# datetime permite trabajar con fechas y horas
import datetime

fecha_actual = datetime.datetime.now()

print(fecha_actual)
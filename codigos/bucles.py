# Los ciclos permiten repetir instrucciones automáticamente

# Se recorren todos los elementos de una lista
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)


# Este ciclo continúa mientras se cumpla la condición
contador = 0

while contador < 5:
    print(contador)
    contador += 1


# break permite detener un ciclo
contador = 0

while True:
    print(contador)
    contador += 1

    if contador == 5:
        break


# continue permite saltar una repetición
for i in range(10):
    if i % 2 == 0:
        continue

    print(i)


# pass permite dejar un bloque sin instrucciones por el momento
for i in range(5):
    pass
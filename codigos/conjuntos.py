# Los conjuntos almacenan elementos sin repetir valores

frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])

print(frutas)
print(numeros)


# Se realizan operaciones entre dos conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union = conjunto1 | conjunto2
print(union)

interseccion = conjunto1 & conjunto2
print(interseccion)

diferencia = conjunto1 - conjunto2
print(diferencia)

diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)


# Se agregan y eliminan elementos
frutas = {"manzana", "banana", "naranja"}

frutas.add("pera")
print(frutas)

frutas.remove("banana")
print(frutas)

frutas.discard("uva")
print(frutas)

frutas.clear()
print(frutas)
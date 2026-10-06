# Las listas permiten guardar varios elementos en una variable

frutas = ["manzana", "banana", "naranja"]

# Se accede a cada elemento mediante su posición
print(frutas[0])
print(frutas[1])
print(frutas[2])


# Los índices negativos comienzan desde el final
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])


# Se prueban diferentes métodos para modificar una lista
frutas = ["manzana", "banana", "naranja"]

frutas.append("pera")
print(frutas)

frutas.insert(1, "uva")
print(frutas)

frutas.remove("banana")
print(frutas)

fruta_eliminada = frutas.pop(2)
print(frutas)
print(fruta_eliminada)

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)


# Se genera una lista con cuadrados de números pares
numeros = [1, 2, 3, 4, 5]

cuadrados = [x ** 2 for x in numeros if x % 2 == 0]

print(cuadrados)
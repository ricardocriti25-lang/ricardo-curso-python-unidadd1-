# Las tuplas almacenan varios valores y conservan su contenido

punto = (3, 4)

# Se consultan los valores mediante índices
print(punto[0])
print(punto[1])


# Ejemplo de algunos métodos disponibles para las tuplas
mi_tupla = (1, 2, 3, 2, 4, 2)

print(mi_tupla.count(2))
print(mi_tupla.index(2))
print(mi_tupla.index(2, 2))
print(mi_tupla.index(2, 2, 4))

# Se obtiene la cantidad total de elementos
print(len(mi_tupla))
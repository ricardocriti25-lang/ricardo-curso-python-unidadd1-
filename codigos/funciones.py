# Las funciones permiten reutilizar bloques de código

# Función sencilla que muestra un saludo
def saludo():
    print("¡Hola, mundo!")


saludo()


# Una función también puede recibir información
def saludo_nombre(nombre):
    print(f"¡Hola, {nombre}!")


saludo_nombre("Juan")
saludo_nombre("María")


# return permite devolver un resultado
def suma(a, b):
    return a + b


resultado = suma(3, 4)
print(resultado)


# Ejemplo de una función anónima
cuadrado = lambda x: x ** 2

print(cuadrado(5))


# Ejemplo de variable creada dentro de una función
def funcion():
    variable_local = 10
    print(variable_local)


variable_global = 20


# Esta función utiliza una variable externa
def funcion2():
    print(variable_global)


funcion()
funcion2()
print(variable_global)


# Función documentada mediante un docstring
def area_rectangulo(base, altura):
    """
    Obtiene el área utilizando la base y la altura.
    """
    return base * altura


print(area_rectangulo(5, 3))


# * permite recibir diferentes cantidades de números
def suma_variable(*numeros):
    total = 0

    for numero in numeros:
        total += numero

    return total


print(suma_variable(1, 2, 3))
print(suma_variable(4, 5, 6, 7))
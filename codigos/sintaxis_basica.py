# Ejemplos para conocer las reglas principales de Python

# Se comprueba la edad mediante una condición
edad = 19

if edad >= 18:
    print("La condición es verdadera")
    print("Eres mayor de edad")
else:
    print("La condición es falsa")
    print("Eres menor de edad")


# Los comentarios ayudan a explicar lo que realiza el programa

# Comentario escrito en una sola línea

"""
Este texto sirve como ejemplo
de un comentario escrito
en varias líneas
"""

print("Ejemplo de comentarios realizado correctamente")


# Python diferencia entre letras mayúsculas y minúsculas

variable = "minúsculas"
Variable = "Primera letra mayúscula"
VARIABLE = "mayúsculas"

print(variable)
print(Variable)
print(VARIABLE)


# Es posible colocar varias instrucciones en una misma línea

print("Instrucción 1"); print("Instrucción 2"); print("Instrucción 3")


# Los paréntesis permiten indicar el orden de las operaciones

a = 5
b = 3
c = 2

resultado = (a + b) * c

print("Resultado:", resultado)
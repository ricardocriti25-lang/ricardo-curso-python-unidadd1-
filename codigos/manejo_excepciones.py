# Las excepciones permiten controlar errores durante la ejecución

# Se intenta realizar una división entre cero
try:
    resultado = 10 / 0
    print(resultado)

except ZeroDivisionError:
    print("Error: División por cero")


# Se pueden controlar diferentes tipos de errores
try:
    resultado = 10 / 0
    print(resultado)

except ZeroDivisionError:
    print("Error: División por cero")

except ValueError:
    print("Error: Valor inválido")


# finally se ejecutará independientemente del resultado
archivo = None

try:
    archivo = open("archivo.txt", "r")

except FileNotFoundError:
    print("Error: Archivo no encontrado")

finally:
    if archivo is not None:
        archivo.close()

    print("Bloque finally ejecutado")
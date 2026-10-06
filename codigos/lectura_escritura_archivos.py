# Python permite guardar información en archivos externos

# Se crea un archivo y se escribe información
archivo = open("datos.txt", "w")

archivo.write("Hola, mundo!")

archivo.close()

print("El archivo se creó correctamente.")


# Ahora se abre el mismo archivo para consultar su contenido
archivo = open("datos.txt", "r")

contenido = archivo.read()

print(contenido)

archivo.close()


# with realiza el cierre del archivo automáticamente
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
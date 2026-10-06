# También es posible generar errores de forma intencional

def funcion():
    # Esta condición se utiliza para provocar la excepción
    condicion = True

    if condicion:
        raise Exception("Descripción del error")


# Se captura la excepción para evitar que el programa termine abruptamente
try:
    funcion()

except Exception as e:
    print(f"Error: {str(e)}")
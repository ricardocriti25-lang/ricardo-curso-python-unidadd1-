# El programa principal utiliza funciones de otros módulos

import operaciones
import utilidades

resultado = operaciones.sumar(5, 3)

utilidades.imprimir_mensaje(
    f"El resultado de la suma es: {resultado}"
)

nombre = utilidades.obtener_nombre_usuario()

utilidades.imprimir_mensaje(
    f"Hola, {nombre}!"
)
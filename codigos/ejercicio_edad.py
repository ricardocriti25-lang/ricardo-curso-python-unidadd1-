# Ejercicio para practicar diferentes condiciones con una edad

edad = 20

# Primero se comprueba si la persona todavía es menor de edad
if edad < 18:
    print("Eres menor de edad.")

# Si tiene entre 18 y 59 años se considera adulto
elif edad >= 18 and edad < 60:
    print("Eres un adulto.")

# Esta condición comprueba si la edad supera los 15 años
elif edad > 15:
    print("Mayor de 15 años.")

# Se comprueba específicamente cuando la edad es 60
elif edad == 60:
    print("¡Feliz 60 cumpleaños!")

# Si ninguna condición anterior se cumple entra aquí
else:
    print("Eres adulto mayor.")
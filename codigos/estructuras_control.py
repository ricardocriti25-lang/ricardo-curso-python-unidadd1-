# Las estructuras condicionales permiten tomar decisiones

# Se ejecuta una instrucción cuando la condición se cumple
edad = 18

if edad >= 18:
    print("Eres mayor de edad.")


# Se consideran dos posibles resultados
edad = 15

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


# Se analizan diferentes rangos de calificaciones
calificacion = 85

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Muy bueno")
elif calificacion >= 70:
    print("Bueno")
else:
    print("Necesita mejorar")
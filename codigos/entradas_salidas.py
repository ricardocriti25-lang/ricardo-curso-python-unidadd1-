# input permite recibir información escrita por el usuario

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

# Se muestran los datos proporcionados
print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")


# Se convierte el texto ingresado a un número entero
edad = int(input("Ingresa nuevamente tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


# Las f-strings facilitan la combinación de texto y variables
nombre = "Juan"
edad = 25

print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
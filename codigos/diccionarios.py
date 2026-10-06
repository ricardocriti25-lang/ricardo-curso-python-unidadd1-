# Un diccionario guarda información mediante claves y valores

persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

# Se obtiene información utilizando las claves
print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])


# get permite consultar una clave de manera sencilla
print(persona.get("nombre"))
print(persona.get("profesion"))


# Se muestran las diferentes partes del diccionario
print(persona.keys())
print(persona.values())
print(persona.items())


# Se agrega nueva información al diccionario
persona.update({"profesion": "Ingeniero"})

print(persona)
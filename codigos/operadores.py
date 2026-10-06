# Uso de diferentes operadores disponibles en Python

a = 10
b = 3


# Se realizan operaciones matemáticas con dos valores
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
modulo = a % b
exponenciacion = a ** b

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)
print("Módulo:", modulo)
print("Exponenciación:", exponenciacion)


# Las comparaciones generan resultados True o False
igual = a == b
diferente = a != b
mayor_que = a > b
menor_que = a < b
mayor_o_igual = a >= b
menor_o_igual = a <= b

print("Igual:", igual)
print("Diferente:", diferente)
print("Mayor que:", mayor_que)
print("Menor que:", menor_que)
print("Mayor o igual:", mayor_o_igual)
print("Menor o igual:", menor_o_igual)


# Combinación de condiciones mediante operadores lógicos
resultado_and = (a > 5) and (b < 5)
resultado_or = (a > 15) or (b < 5)
resultado_not = not (a > 5)

print("AND:", resultado_and)
print("OR:", resultado_or)
print("NOT:", resultado_not)
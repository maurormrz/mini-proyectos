# Título.

print("CALCULADORA")

# Solicita al usuario que ingrese los dos valores a operar.
# Se aceptarán como valores números Enteros y Decimales.

valor1 = float(input("Ingrese el primer valor:\n"))
valor2 = float(input("Ingrese el segundo valor:\n"))

# Selección del tipo de operación.
# Se aceptarán solamente la suma, la resta, la multiplicación y la división.

opcion = input("Seleccione la operación que desee realizar:\n\
S = Suma\n\
R = Resta\n\
M = Multiplicación\n\
D = División\n"
)

opcion = opcion.lower()

# Realizar la operación elegida.

resultado = 0

if opcion == "s":
    resultado = valor1 + valor2
elif opcion == "r":
    resultado = valor1 - valor2
elif opcion == "m":
    resultado = valor1 * valor2
elif opcion == "d":
    if valor2 != 0:
        resultado = valor1 / valor2
    else:
        print("No se puede dividir entre cero.")
        quit()
else:
    print("Opción Incorrecta.")
    quit()

print(f"Resultado:\n{resultado}")
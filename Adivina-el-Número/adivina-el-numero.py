import random

def adivina(x):

    print("ADIVINA EL NÚMERO")
    print("Debes adivinar el número generado por la computadora.")

    numero_aleatorio = random.randint(1, x)
    prediccion = 0

    while prediccion != numero_aleatorio:
        prediccion = int(input(f'Adivina un número entre 1 y {x}: '))
        if prediccion < numero_aleatorio:
            print('Intenta otra vez. Este número es más pequeño.')
        elif prediccion > numero_aleatorio:
            print('Intenta otra vez. Este número es más grande.')
    print(f'¡Felicitaciones, lo adivinaste! El número {numero_aleatorio} es el correcto.')

adivina(15)
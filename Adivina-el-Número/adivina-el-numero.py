import random

def adivina(x):

    # Título y descripción del juego.

    print("ADIVINA EL NÚMERO")
    print("Debes adivinar el número generado por la computadora.")

    numero_aleatorio = random.randint(1, x) # número aleatorio entre 1 y x.
 
    prediccion = 0 # La predicción es 0 inicialmente para que no coincida con el número aleatorio. 


    while prediccion != numero_aleatorio:
        prediccion = int(input(f'Adivina un número entre 1 y {x}: ')) # El input pasa a ser entero.
        if prediccion < numero_aleatorio:
            print('Intenta otra vez. Este número es más pequeño.')
        elif prediccion > numero_aleatorio:
            print('Intenta otra vez. Este número es más grande.')
    print(f'¡Felicitaciones, lo adivinaste! El número {numero_aleatorio} es el correcto.') # El bucle se detiene cuando el usuario adivina el número correctamente y se muestra un mensaje final.

adivina(15) # Número máximo a adivinar.
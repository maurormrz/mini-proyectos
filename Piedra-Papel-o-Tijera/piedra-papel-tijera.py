import random

def piedra_papel_tijera():

    # Título y descripción del juego.

    print("PIEDRA, PAPEL O TIJERA")
    usuario = input('Escribe "Piedra", "Papel" o "Tijera" para comenzar a jugar:\n').lower()
    computadora = random.choice(['piedra', 'papel', 'tijera'])

    # Condiciones si se Empata, se Gana o se Pierde el juego.

    if usuario == computadora:
        return 'Empate.'

    if ganar(usuario, computadora):
        return 'Ganaste.'

    return 'Perdiste.'


def ganar(jugador, oponente):

    # Reglas para que el Usuario gane el juego.

    if ((jugador == 'piedra' and oponente == 'tijera')
        or (jugador == 'tijera' and oponente == 'papel')
        or (jugador == 'papel' and oponente == 'piedra')):
        return True
    else:
        return False


print(piedra_papel_tijera())
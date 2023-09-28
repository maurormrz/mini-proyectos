# Convierte horas, minutos y segundos a segundos.

def tiempo_a_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

# Convierte segundos en horas, minutos y segundos.

def segundos_a_tiempo(segundos_totales):
    horas = segundos_totales // 3600
    segundos_totales %= 3600
    minutos = segundos_totales // 60
    segundos = segundos_totales % 60
    return horas, minutos, segundos

def main():

    # Título y opciones

    print("CONVERSOR DE TIEMPO") 
    print("Elija una opción: ")
    print("1. Convertir tiempo a segundos")
    print("2. Convertir segundos a tiempo")
    
    opcion = int(input("\n"))
    
    if opcion == 1: # Conversión de Tiempo (horas, minutos y segundos) a Segundos.
        horas = int(input("Horas: "))
        minutos = int(input("Minutos: "))
        segundos = int(input("Segundos: "))
        segundos_totales = tiempo_a_segundos(horas, minutos, segundos)
        print(f"El tiempo en segundos es: {segundos_totales} segundos.")
    elif opcion == 2: # Conversión de Segundos a Tiempo (horas, minutos y segundos).
        segundos_totales = int(input("Segundos totales: "))
        horas, minutos, segundos = segundos_a_tiempo(segundos_totales)
        print(f"El tiempo es: {horas} horas, {minutos} minutos, {segundos} segundos.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
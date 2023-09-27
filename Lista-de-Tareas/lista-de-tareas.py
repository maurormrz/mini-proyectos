lista = []

while True:
    print("Selecciona una opción:")
    print("1. Agregar tarea")
    print("2. Mostrar lista")
    print("3. Salir")
    
    opcion = input("\n") # Elegir una opción.

    if opcion == "1":
        tarea = input("Ingresa una tarea: ")
        lista.append(tarea) # Agregar la tarea a la lista.
        print("Tarea agregada.")
    elif opcion == "2":
        print("Lista de Tareas:")
        for i, tarea in enumerate(lista, start=1): # Enumerar la lista desde el 1.
            print(f"{i}. {tarea}")
    elif opcion == "3":
        break
    else:
        print("Opción no válida")
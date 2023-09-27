# Colección de datos para crear la historia.

nombre = input("Ingresa tu Nombre: ") # Input nombre.
apellido = input("Ingresa tu Apellido: ") # Input apellido.
edad = input("Ingresa tu Edad: ") # Input edad.
ubicacion = input("Ingresa tu Ubicación: ") # Input ubicacion.
estudio = input("Ingresa que estas estudiando: ") # Input estudio.

# Título del juego.

print("HISTORIAS LOCAS")

# Variable con f-string (reemplaza con los datos ingresados).

historialoca = f"¡Hola, un gusto conocerte!. Me llamo {nombre}, mi apellido es {apellido} y tengo {edad} años de edad. Actualmente estoy viviendo en {ubicacion} en donde estoy estudiando la carrera de {estudio}. ¡Y con gusto te llevaré a conocer mi ciudad!."

print(historialoca)
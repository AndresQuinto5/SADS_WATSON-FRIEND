def obtener_datos_paciente():
    nombre = input("Nombre del paciente: ")
    edad = input("Edad del paciente: ")
    genero = input("Género del paciente: ")
    fecha = input("Fecha de la evaluación: ")
    referente = input("Referente: ")
    return {"nombre": nombre, "edad": edad, "genero": genero, "fecha": fecha, "referente": referente}

def calificar_sads():
    items_inversos = [2, 5, 8, 10, 11, 13, 14, 16, 18, 20, 21, 23, 24, 26]
    puntuacion_total = 0

    print("\nResponda a los siguientes 28 ítems con 'V' para Verdadero o 'F' para Falso:")
    
    for i in range(1, 29):
        while True:
            respuesta = input(f"Ítem {i}: ").upper()
            if respuesta in ['V', 'F']:
                break
            else:
                print("Por favor, ingrese 'V' para Verdadero o 'F' para Falso.")
        
        if i in items_inversos:
            puntuacion_total += 1 if respuesta == 'V' else 0
        else:
            puntuacion_total += 1 if respuesta == 'F' else 0

    return puntuacion_total

def main():
    print("Bienvenido al sistema de calificación SADS (Escala de Ansiedad Social de Watson y Friend)")
    
    datos_paciente = obtener_datos_paciente()
    puntuacion = calificar_sads()
    
    print("\nResultados:")
    print(f"Paciente: {datos_paciente['nombre']}")
    print(f"Edad: {datos_paciente['edad']}")
    print(f"Género: {datos_paciente['genero']}")
    print(f"Fecha de evaluación: {datos_paciente['fecha']}")
    print(f"Referente: {datos_paciente['referente']}")
    print(f"Puntuación total SADS: {puntuacion}/28")

if __name__ == "__main__":
    main()
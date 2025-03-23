# Diccionario con los nombres y números de teléfono
agenda = {
    "Celianna": "(809) 555-1111",
    "Luis": "(829) 555-2222",
    "Dariel": "(849) 555-3333",
    "Liliana": "(809) 555-4444",
    "Sarah": "(829) 555-5555"
}

# Función para mostrar la agenda
def mostrar_agenda():
    print("Agenda de Contactos:")
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")

# Función para agregar un contacto
def agregar_contacto():
    nombre = input("Nombre del nuevo contacto: ")
    telefono = input("Número de teléfono: ")
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado con éxito.")

# Función para eliminar un contacto
def eliminar_contacto():
    nombre = input("Nombre del contacto que deseas eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print(f"No se encontró a {nombre} en la agenda.")

# Función principal
def menu():
    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Mostrar agenda")
        print("2. Agregar contacto")
        print("3. Eliminar contacto")
        print("4. Salir")
        
        opcion = input("\nElige una opción (1-4): ")

        if opcion == "1":
            mostrar_agenda()
        elif opcion == "2":
            agregar_contacto()
        elif opcion == "3":
            eliminar_contacto()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Llamamos a la función para ejecutar el programa
menu()
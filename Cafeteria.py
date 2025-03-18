print("¡Bienvenido a la Cafetería Python!")
print("=" * 40)

# Menú de la cafetería
print("")
print("--- MENÚ DE LA CAFETERÍA ---")
print("1. Café Americano - $25")
print("2. Café Latte - $30")
print("3. Capuchino - $35")
print("4. Té - $20")
print("5. Croissant - $40")
print("6. Galletas - $15")
print("")

# Simulación de entrada a la cafetería
nombre = input("¿Cuál es tu nombre? ")
print("Hola " + nombre + ", ¡bienvenido/a a nuestra cafetería!")

# Pedir al usuario que elija un producto
print("\nPor favor, elige un producto del menú:")
opcion = input("Selecciona una opción (1-6): ")

# Inicializar variables para el pedido
producto = ""
precio = 0

# Asignar el producto según la opción elegida
if opcion == "1":
    producto = "Café Americano"
    precio = 25
elif opcion == "2":
    producto = "Café Latte"
    precio = 30
elif opcion == "3":
    producto = "Capuchino"
    precio = 35
elif opcion == "4":
    producto = "Té"
    precio = 20
elif opcion == "5":
    producto = "Croissant"
    precio = 40
elif opcion == "6":
    producto = "Galletas"
    precio = 15
else:
    print("Opción no válida. Por favor reinicia el programa.")

# Si seleccionó un producto válido
if producto != "":
    print("Has seleccionado: " + producto)
    
    # Mostrar resumen de la cuenta
    print("\n--- TU CUENTA ---")
    print("Cliente: " + nombre)
    print("-" * 30)
    print("1. " + producto + " - $" + str(precio))
    print("-" * 30)
    print("Total a pagar: $" + str(precio))
    print("¡Gracias por visitarnos! ¡Vuelve pronto!")

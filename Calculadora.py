print("¡Bienvenido a la Calculadora Python!")
print("=" * 40)


a = int(input("\ningrese el valor de a: "))
b = int(input("\ningrese el valor de b: "))

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

# Menú de la Calculadora
print("\n--- MENÚ DE LA CALCULADORA ---")  
print("1. suma")
print("2. resta")
print("3. mutliplicacion")
print("4. division")

# Pedir al usuario que elija una operacion
print("\nPor favor, elige una operación del menú:")
opcion = input("Selecciona una opción (1-4): ")

# Asignar el producto según la opción elegida
if opcion == "1":
    print("\nla suma de " , a , " y " , b , " es " , suma)
elif opcion == "2":
    print("\nla resta de " , a , " y " , b , " es " , resta)
elif opcion == "3":
    print("\nla multiplicacion de " , a , " y " , b , " es " , multiplicacion)
elif opcion == "4":
    print("\nla division de " , a , " y " , b , " es " , division)

else:
    print("Opción no válida. Por favor reinicia el programa.")


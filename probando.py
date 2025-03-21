print("""
                                                    
 _____ _____ _____ _____    _____ _____ _____ _____ 
|   __|  _  |     |   __|  |     |  |  |   __| __  |
|  |  |     | | | |   __|  |  |  |  |  |   __|    -|
|_____|__|__|_|_|_|_____|  |_____|\___/|_____|__|__|
                                                    
""")

print("--------------------------------------")
print("Bienvenido a mi sala de videos juegos")
print("--------------------------------------")

registro = {
    "usuario": "admin",
    "contrasena": "grisel"
}

usuario = input("\nIngrese su nombre de usario: ")
contrasena = input("\nIngrese su contraseña: ")


if usuario == registro["usuario"] and contrasena == registro["contrasena"]:
    print(f"\nBienvenido a mi sala de videos juegos {usuario}!")
else:
    print("\nUsuario o contraseña incorrectos")


print(r"""
 __      __.__            .___                   
/  \    /  \__| ____    __| _/______  _  ________
\   \/\/   /  |/    \  / __ |/  _ \ \/ \/ /  ___/
 \        /|  |   |  \/ /_/ (  <_> )     /\___ \ 
  \__/\  / |__|___|  /\____ |\____/ \/\_//____  >
       \/          \/      \/                 \/ 
""")

usuario_correcto = "grisel"

contrasena_correcta = "123"

usuario = input("\ningrese su usuario:")

contrasena = input("\nPor favor, ingrese su contraseña:")

while usuario != usuario_correcto or contrasena != contrasena_correcta:
    print("\nUsuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")
    usuario = input("\ningrese su usuario:")
    contrasena = input("\nPor favor, ingrese su contraseña:")

print("\nAcceso permitido. Bienvenido a Windows " + usuario)

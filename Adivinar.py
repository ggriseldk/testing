print("Bienvenido al juego de adivinar el numero")

numero_adivinar = 9
numero_intento = int(input("\ningrese un numero del 1 al 10:"))

while numero_intento != numero_adivinar:
    if numero_intento < numero_adivinar:
        print("\nEl numero es mayor")
    else: 
        print("\nEl numero es menor")

    numero_intento = int(input("\ningrese otro numero:"))

print("\n¡Felicidades! Has adivinado el número.")

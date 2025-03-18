print("---------------------------------------")
print("Estoy aprendiendo a programar en Python")
print("---------------------------------------")
print("")

nombre = input("¿Cómo te llamas? ") 
print("")
print("Me alegro de conocerte " + nombre) 
print("")
edad = input("¿Cual es tu edad? ")
print("")

if int(edad) < 18:
    print("No eres mayor de edad!")
else:
    print("Eres mayor de edad!")

print("")
if nombre == "Julio": 
    print("Bienvenido Jefe!")
    print("")
else: 
    print("Bienvenido, no te conozco!")
# Ejercicio 1 
# Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

vocal = input ("Ingrese una vocal: ")

if vocal.lower() == "a" or vocal.lower() == "e" or vocal.lower() == "i" or vocal.lower() == "o" or vocal.lower() == "u":
    print ("Es Vocal")
else:
    print("No es vocal")

# otra forma es con la palabra reservada "in"

if vocal.lower() in "aeiou":
    print ("Es Vocal")
else:
    print ("No es Vocal")
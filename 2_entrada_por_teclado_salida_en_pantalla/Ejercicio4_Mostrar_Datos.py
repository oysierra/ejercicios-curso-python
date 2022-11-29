# Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:
# Te llamas: <nombre>
# Tu edad es: <edad>
# Eres: <sexo>

nombre = input("Ingresa tu nombre: ") # Ingreso de nombre
edad = int(input("Ingresa tu edad: ")) # Ingreso de edad
genero = input("Ingresa tu genero: ") # Ingreso de genero


print("Te llamas {} \nTu edad es {} años \nEres: {}".format(nombre, edad, genero)) # Se usa \n para el salto de línea 
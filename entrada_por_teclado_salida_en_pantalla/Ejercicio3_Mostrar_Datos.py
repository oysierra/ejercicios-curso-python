# Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. 
# El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas

vocal = input("Ingrese una vocal en minuscula: ")
letra = input("Ingrese una letra en mayuscula: ")

vocal = vocal.upper()
letra = letra.lower()

print("vocal {} letra {}".format(vocal, letra))
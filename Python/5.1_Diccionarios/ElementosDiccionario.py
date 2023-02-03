diccionarios = {'Nombre': "Lina" , 'Apellido': "Mendoza" , 'Estatura': 1.65}

print(diccionarios) # Imprime toda la información del diccionario : claves y valores

print(diccionarios.keys()) # Devuelve solo las llaves del diccionario con .keys

print(diccionarios.values()) # Devuelve solo los valores del diccionario con .values

print(diccionarios["Estatura"]) # Devuelve el valor de la llave que indiquemos

diccionarios["Masa"] = "55 Kg" # Agrega una nueva clave y un nuevo valor

print(diccionarios)

diccionarios["Nombre"] = "Lina Paola" # Modifica el valor de la clave que se indique

print(diccionarios)
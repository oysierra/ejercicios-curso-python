
diccionario = {1: 2, 2: 3, 3: 4}
diccionario2 = {4 : 5, 5 : 6}
print(diccionario)

# Recibe el parametro clave y elimina la clave y valor que esté almacenado
diccionario.pop(3) 
print(diccionario)

# get nos devuelve el valor según el parametro (llave) que se indique
print(diccionario.get(2))

# setdefault recibe la llave y su valor
diccionario.setdefault(4 , 5)
print(diccionario)

# update unifica 2 diccionarios
diccionario.update(diccionario2)
print(diccionario)

# copy copia genera uan copia del diccionario
diccionario.copy()
print(diccionario)

# clear borra todo el diccionario
diccionario.clear()
print(diccionario)
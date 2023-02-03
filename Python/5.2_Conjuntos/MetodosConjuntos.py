conjunto = {1 , 1 , 2 , 3 , 3 , 4 , 5}
lista = [1 , 1 , 2 , 3 , 4 , 4]

print(lista) # La lista permite datos repetidos

print(conjunto) # El conjunto no permite que se repitan los datos


# add agrega un nuevo elemento al final del conjunto
conjunto.add(20)
print(conjunto)

# remove o discard elminina un valor del conjunto
conjunto.remove(1)
print(conjunto)

# pop elimina al azar cualquier valor del conjunto
conjunto.pop()
print(conjunto)

# update añade elementos al conjunto, deben ser elementos iterables
conjunto.update([6 , 7 , 8])
print(conjunto)

# clear deja al conjunto vacio
conjunto.clear()
print(conjunto)
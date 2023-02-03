lista = [5 , 2 , 1 , 4 , 3]

print(lista)

# Agrega un elemento al final de la lista
lista.append(6)
print(lista)

# Inserta en una posición especifica con insert(posicion , valor)
lista.insert(2 , 2.5)
print(lista)

# Count cuenta la cantidad de veces que aparece un elemento determinado en la lista
print(lista.count(5))

# Index indica la posición del elemento que se le indique, si ese elemento se repite varias veces, index muestra el primero
print(lista.index(4))

# Sort ordena la lista de manera ascendente, solo funciona en listas homogeneas
lista.sort()
print(lista)

# Reverse ordena la lista de manera descendente, solo funciona en listas homogeneas
lista.reverse()
print(lista)

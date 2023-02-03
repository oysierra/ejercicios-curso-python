lista = ['Python' , 24 , "Omar" , "Lina" , 12 , "Hola"]

# Actualizar la lista
lista[3] = "Lina Paola"
print(lista)
print(lista[3])

# Pop toma el ultimo elemento de la lista y lo elimina
lista.pop()
print(lista)

# Remove permite dar un valor de un elemento de la listapara eliminar dicho elemento elemento
lista.remove(24)
print(lista)
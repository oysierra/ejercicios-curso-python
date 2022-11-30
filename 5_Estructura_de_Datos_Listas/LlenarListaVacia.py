lista = [1 , 2 , 3]
lista2 = [4 , 5 , 6]

# el operador '+' permite sumar las listas, no el contenido
lista3 = lista + lista2
print(lista3)

# la coma ',' permite que se concatene, nunca se concatena con el signo +
print("esta es una lista de datos" , lista)

# Llenar una lista de forma manual, ya que normalmente se usa el ciclo for
lista_vacia = []

edad = int(input("Digite la edad: "))

lista_vacia.append(edad)
print(lista_vacia)
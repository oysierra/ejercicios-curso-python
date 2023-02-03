# Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. 
# Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas
lista = []
longitud_lista = int(input("Digite cuantos numeros va a solicitar: "))

def Crear_Lista():
    for i in range(longitud_lista):
        numero = int(input("Digite un número: "))
        lista.append(numero)
    print(lista)

def Ordenar_Pares_Impares():
    Lista_Pares = []
    Lista_Impares = []
    for i in lista:
      if i % 2 == 0:
        Lista_Pares.append(i)
      else:
        Lista_Impares.append(i)
      Lista_Pares.sort()
      Lista_Impares.sort()
    print(Lista_Pares)
    print(Lista_Impares)

Crear_Lista()
Ordenar_Pares_Impares()
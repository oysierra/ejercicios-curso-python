# Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, 
# el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; 
# si ambos son iguales, debe retornar 0

def comparar_numero():
  numero1 = int(input("Indique un numero: "))
  numero2 = int(input("Indique otro numero: "))
  if numero1 == numero2:
    return 0
  elif numero1 > numero2:
    return 1
  else:
    return -1

print(comparar_numero())
# Escribir una función que reciba un número entero positivo y devuelva su factorial.

from math import factorial


def Numero_Factorial():
  numero = int(input("Digite un numero: "))
  if numero > 0:
    print("el factorial de {} es: {}".format(numero, factorial(numero)))
  else:
    print("El numero es negativo")
Numero_Factorial()
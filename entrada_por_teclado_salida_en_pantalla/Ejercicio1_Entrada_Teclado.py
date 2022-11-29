# Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, 
# el usuario debe ingresar los valores de “a”, “b” y “c”, # y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”

import math

a = float(input("Ingrese el valor de a: ")) # ingresa el valor de a
b = float(input("Ingrese el valor de b: ")) # ingresa el valor de b
c = float(input("Ingrese el valor de c: ")) # ingresa el valor de c
d = float(input("Ingrese el valor de d: ")) # ingresa el valor de d


resultado = (-b + math.sqrt(pow(b,2) - 4*a*c))/2*a

print (resultado)
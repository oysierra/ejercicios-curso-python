# Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, 
# el usuario debe ingresar los valores de “a”, “b” y “c”, # y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”

from math import sqrt

a = float(input("Ingrese el valor de a: ")) # ingresa el valor de a
b = float(input("Ingrese el valor de b: ")) # ingresa el valor de b
c = float(input("Ingrese el valor de c: ")) # ingresa el valor de c
resultado_x1 = 0
resultado_x2 = 0


if(((b**2)- 4 * a * c)) < 0:
    print("No se puede realizar con raices negativas")
else:
    resultado_x1 = (-b + sqrt((b**2) - (4*a*c)))/(2*a)
    resultado_x2 = (-b - sqrt((b**2) - (4*a*c)))/(2*a)
    print ("x1 = " , resultado_x1)
    print ("x2 = " , resultado_x2)
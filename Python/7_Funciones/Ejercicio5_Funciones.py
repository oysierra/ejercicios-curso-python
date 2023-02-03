# Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; 
# y la otra el area de un circulo con argumento de radio

import math

def area_cuadraro(base, altura):
  area = base * altura
  return area

def area_circulo(radio):
  return pow(radio, 2) * 3.14

print(area_cuadraro(10 , 10))

print(area_circulo(10))
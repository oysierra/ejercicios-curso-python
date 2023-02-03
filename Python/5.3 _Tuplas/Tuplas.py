# Las tuplas tienen datos inmutables, es decir que no se pueden modificar
# En las tuplas se usa () es lo mas recomendable y como buena practica
# Se puede usar el debanado
# Se pueden "concatenar" varias tuplas

Tupla = (1 , 2 , 3 , 4 , 5)
Tupla2 = (6 , 7 , 8 , 9 , 10)

print(Tupla)
print(type(Tupla))

print(Tupla[2])
print(Tupla[0 : 3])

print(Tupla + Tupla2)
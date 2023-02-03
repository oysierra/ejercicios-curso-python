# Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares

numero_inicio = int(input("Digite el numero inicial: "))
numero_fin = int(input("Digite el limite del rango: "))

for i in range(numero_inicio, numero_fin):
    if i % 2 == 0:
        continue
    print(i)
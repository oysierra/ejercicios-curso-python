# Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras

for i in range(1 , 11):
    print (i)

numero_inicio = int(input("Digite el numero inicial: "))
numero_fin = int(input("Digite el limite del rango: "))

for j in range(numero_inicio, numero_fin+1):
    print(j)

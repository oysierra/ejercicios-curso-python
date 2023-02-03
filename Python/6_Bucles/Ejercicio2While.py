# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Ingrese su edad: "))
i = 0;
anio = 2022 - edad + 1

while i < edad:
    i += 1
    print("usted cumplio {} año en {}".format(i , anio))
    anio += 1
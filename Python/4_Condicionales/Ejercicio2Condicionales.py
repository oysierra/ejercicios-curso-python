# Ejercicio 2 Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto 
# es igual al número (el valor absoluto de 52 es 52), # mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

numero = int(input("Digite un numero: "))

'''if numero < 0:
    numero = numero * (-1)
    print("el valor absoluto es: ", numero)
else:
    print("el valor absoluto es: ", numero)'''

# otra forma concatenando y usando el format y abs este metodo es para el valor absoluto

if numero > 0:
    print("El valor absoluto de {} es: {}".format(numero, numero))
else:
    print("El valor absoluto de {} es: {}".format(numero,abs(numero)))

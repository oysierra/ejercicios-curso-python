# Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa

letras_alfabeto = ("a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z")

letra = int(input("Un numero: "))

if letra >= 1 and letra <= 26:
    letra -= 1
    print(letras_alfabeto[letra])
else:
    print("Numero incorrecto")
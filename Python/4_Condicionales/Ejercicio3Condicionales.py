# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. 
# Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

palabra_uno = input("Digite la primer palabra: ")
palabra_dos = input("Digite la segunda palabra: ")


if palabra_uno.lower()[-3 : ] == palabra_dos.lower()[-3 : ]:
    print ("Las palabras riman")
elif palabra_uno.lower()[-2 : ] == palabra_dos.lower()[-2 : ]:
    print ("Las palabras riman un poco")
else:
    print("Las palabras no riman")
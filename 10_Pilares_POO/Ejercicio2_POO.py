# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
# Calcular después la suma, resta, multiplicación y división. 
# Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():
    def __init__(self, numero1, numero2):
        self._numero1 = numero1
        self._numero2 = numero2
    
    # Getter
    def numero1(self):
        return self._numero1
    
    def numero2(self):
        return self._numero2
    
    # Setter
    def numero1(self, numero1):
        self._numero1 = numero1
    
    def numero2(self, numero2):
        self._numero2 = numero2
    
    # Metodo Suma
    def sumar(numero1, numero2):
        suma = numero1 + numero2
        print("La suma es {}".format(suma))
    
    # Metodo Resta
    def restar(numero1, numero2):
        resta = numero1 - numero2
        print("La resta es {}".format(resta))
    
    # Metodo Multiplicar
    def multiplicar(numero1, numero2):
        multiplicacion = numero1 * numero2
        print("La multiplicacion es {}".format(multiplicacion))
    
    # Metodo Dividir
    def dividir(numero1, numero2):
        try:
            division = numero1/numero2
            print("La division es {}".format(division))
        except ZeroDivisionError: # se usa para indicar que no se puede dividir entre 0
            print("No se puede dividir entre cero")

calculadora = Calculadora(1, 1)
calculadora.numero1 = int(input("Digite el primer numero: "))
calculadora.numero2 = int(input("Indique el siguiente numero: "))

calculadora.sumar(calculadora.numero2)
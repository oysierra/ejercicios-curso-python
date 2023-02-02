# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
# Calcular después la suma, resta, multiplicación y división. 
# Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():
    def __init__(self, numero1, numero2):
        self._numero1 = numero1
        self._numero2 = numero2
    
    # Getter
    @property
    def numero1(self):
        return self._numero1
    
    @property
    def numero2(self):
        return self._numero2
    
    # Setter
    @numero1.setter
    def numero1(self, numero1):
        self._numero1 = numero1
    
    @numero2.setter
    def numero2(self, numero2):
        self._numero2 = numero2
    
    # Metodo Suma
    def sumar(self):
        self.suma = self._numero1 + self._numero2
        print("La suma es {}".format(self.suma))
    
    # Metodo Resta
    def restar(self):
        self.resta = self._numero1 - self._numero2
        print("La resta es {}".format(self.resta))
    
    # Metodo Multiplicar
    def multiplicar(self):
        self.multiplicacion = self._numero1 * self._numero2
        print("La multiplicacion es {}".format(self.multiplicacion))
    
    # Metodo Dividir
    def dividir(self):
        try:
            self.division = self._numero1/self._numero2
            print("La division es {}".format(self.division))
        except ZeroDivisionError: # se usa para indicar que no se puede dividir entre 0
            print("No se puede dividir entre cero")


numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Indique el siguiente numero: "))
calculadora = Calculadora(numero1, numero2)


calculadora.sumar()
calculadora.restar()
calculadora.multiplicar()
calculadora.dividir()

class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    @property # de esta manera se realiza em metodo get 
    def cuenta(self):
        return self._cuenta
    
    @cuenta.setter # de esta manera se realiza em metodo set
    def cuenta(self, cuenta):
        self._cuenta = cuenta
    
    @property # de esta manera se realiza em metodo get 
    def contador(self):
        return self._contador
    
    @contador.setter # de esta manera se realiza em metodo set
    def contador(self, contador):
        self._contador = contador

a = A()
# print(a._contador) # forma incorrecta para ver, se debe usar en el set la palabra reservada setter: ejemplo @atributo.setter
print(a.cuenta)
a.cuenta = 20
print(a.cuenta)
a.contador = 40
print(a.contador)
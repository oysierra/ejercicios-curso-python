class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    @property # de esta manera se realiza em metodo get 
    def cuenta(self):
        return self._cuenta
    
    @property # de esta manera se realiza em metodo get 
    def contador(self):
        return self._contador

a = A()
# print(a._contador) # forma incorrecta para ver, se debe usar el get @property
print(a.cuenta)
print(a.contador)


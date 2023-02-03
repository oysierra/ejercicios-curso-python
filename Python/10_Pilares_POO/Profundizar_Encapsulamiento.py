# se recomienda que en python se use para encapsular _, es decir solo 1 guion bajo self._atributo
class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0
    
    def incrementar(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador

a = A()

'''print(a.cuenta) # esta es la forma incorrecta de conocer el valor de un atributo
a.cuenta = 20
print(a.cuenta)'''
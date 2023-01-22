class Animales():
    def __init__(self, nombre):
        self._nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

class Perro(Animales):
    def __init__(self, nombre, sonido):
        super().__init__(nombre) # Con el super se hereda 
        self._sonido = sonido
    
    @property
    def nombre(self):
        return self._sonido
    
    @nombre.setter
    def nombre(self, sonido):
        self._sonido = sonido



perro = Perro("nombre", "sonido")
perro.nombre = "Lucas"
perro.sonido = "Guauuuu"

print(perro.nombre , perro.sonido)
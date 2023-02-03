class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje
    
    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Guau!")

class Pez(Animales):
    def hablar(self):
        print("Glup ... Glup")

perro = Perro("Yo no hablo")
perro.hablar()

animal = Animales("Miau!")
animal.hablar()

pez = Pez("Nada")
pez.hablar()
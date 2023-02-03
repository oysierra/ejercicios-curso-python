class Fabrica_Telefonos():
    def __init__(self, marca, *colores, **modelos): # * como tupla ** como diccionario
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = Fabrica_Telefonos("Nokia", "Negro" , "Azul" , "Rojo" , m1 = 500 , m2 = 1000)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
telefono.memoria = 512 # así se crea un atributo temporal y pertenece a un solo objeto en este caso a telefono
print(telefono.memoria)
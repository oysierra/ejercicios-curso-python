'''class Fabrica_Telefonos():
    marca = "Samsung"
    
    def ElaborarHuawei(self):
        self.marca = "Huawei"

telefono = Fabrica_Telefonos()
telefono.ElaborarHuawei()
print(telefono.marca)'''

# El init es el constructor en python

class Fabrica_Telefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

telefono = Fabrica_Telefonos("Huawei" , "Negro")

print(telefono.marca)
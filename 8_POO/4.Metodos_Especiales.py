class Fabrica_Telefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("El objeto {} se ha creado".format(self.marca))
        
    def __str__(self):
        return "El objeto es {}".format(self.marca)    
        
    def __del__(self):
        print("El objeto {} se ha destruido".format(self.marca))
        
telefono = Fabrica_Telefonos("Nokia", "Color")
print(telefono.marca)
print(telefono)
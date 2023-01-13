
class Fabrica_Telefonos():
    # Atributos
    marca = "Huawei"
    color = "Negro"
    memoria_ram = 32
    almacenamiento = 128
    
    # Método
    def llamar(self, mensaje): # Método de instancia se le conoce como método de instancia
        return mensaje    
    
    def escuchar_musica(self):
        print("Estas escuchando a Slipknot")
telefono = Fabrica_Telefonos()
# telefono.marca se pone el atributo de marca al objeto telefono objeto.atributo
print(telefono.marca)

print(telefono.llamar("Hola!, ¿con quien hablo?"))
telefono.escuchar_musica()
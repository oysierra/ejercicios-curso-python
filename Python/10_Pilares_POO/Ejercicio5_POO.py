# Crear un programa con tres clases:
# Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). 
# Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
# Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
# El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.

class Universidad():
    def __init__(self, nombre_universidad):
        self._nombre_universidad = nombre_universidad
    
    # getter
    @property
    def nombre_universidad(self):
        return self._nombre_universidad

class Carrera():
    def carrera(self, especialidad):
        self._especialidad = especialidad

    # getter
    @property
    def especialidad(self):
        return self._especialidad

class Estudiante(Universidad, Carrera):
    def datos(self, nombre_estudiante, edad):
        self._nombre_estudiante = nombre_estudiante
        self._edad = edad
        print("Mi nombre es {}, tengo {} años, estudio {} en la {}".format(self.nombre_estudiante, self.edad, self.especialidad, self.nombre_universidad))
    
    # getter
    @property
    def nombre_estudiante(self):
        return self._nombre_estudiante
    
    @property
    def edad(self):
        return self._edad


persona = Estudiante("Universidad de Manizales")
persona.carrera("Ingenieria de Sistemas")
persona.datos("Omar Sierra", 35)



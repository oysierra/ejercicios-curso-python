# Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. 
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Estudiante():
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
    
    # Getter
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def nota(self):
        return self._nota
    
    # Setter
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @nota.setter
    def nota(self, nota):
        self._nota = nota
    
    # Transformar la ubicacion del objeto a String
    def __str__(self):
        return self._nombre
    
    # Metodo para validar nota
    def aprobo(nombre, nota):
        if nota >= 3:
            print("El alumno {} aprobo, su nota fue {}".format(nombre, nota))
        else:
            print("El alumno {} no aprobo, su nota fue {}".format(nombre, nota))

# se crea el objeto estudiante
estudiante = Estudiante("Nuevo", 0)

# se solicitan valores al usuario
estudiante.nombre = input("Indique el nombre del estudiante: ")
estudiante.nota = float(input("Indique la nota del estudiante: "))

# se imprime el resultado
estudiante.aprobo(estudiante.nota)

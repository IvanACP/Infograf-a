#Ivan Agustin Coria Palafox
#17/04/23
# Topicos Avanzados de Programacion 
#Infrografia de Ejemplos en codigo 

# Definir una clase llamada "Persona"
class Persona:
    # Definir los atributos de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Definir un método de la clase
    def presentarse(self):
        print("Hola, mi nombre es", self.nombre, "y tengo", self.edad, "años.")
    
# Crear una instancia de la clase "Persona"
ivan = Persona("Ivan", 19)

# Llamar al método "presentarse" de la instancia "juan"
ivan.presentarse()

# Definir una subclase de "Persona" llamada "Estudiante"
class Estudiante(Persona):
    # Definir un nuevo atributo de la subclase
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    # Definir un nuevo método de la subclase
    def estudiar(self):
        print("Estoy estudiando", self.carrera)

# Crear una instancia de la subclase "Estudiante"
felipe = Estudiante("Felipe", 20, "Ingeniería")

# Llamar al método "presentarse" heredado de la clase "Persona" desde la instancia "ana"
felipe.presentarse()

# Llamar al método "estudiar" de la instancia "ana"
felipe.estudiar()

class Persona:
    
    def __init__(self, nombre, edad, altura, sexo ):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

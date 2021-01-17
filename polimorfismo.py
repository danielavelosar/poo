class Persona :
    def __init__(self, nombre):
        self.nombre=nombre
    def desplazar(self):
        print(f"{self.nombre} anda caminando")
    
class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def desplazar(self):
        print(f"{self.nombre} anda en bicicleta" )
        


if __name__ == "__main__":
    Roberto= Persona("Roberto")
    Mathias = Ciclista("Mathias")
    Roberto.desplazar()
    Mathias.desplazar()

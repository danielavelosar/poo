class Rectangulo:
    def __init__(self, base, altura):
        self.altura=altura
        self.base=base
    def area (self):
        return self.base*self.altura 
    
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado,lado)
    


if __name__ == "__main__":
    rect_1=Rectangulo(base=5,altura=4)
    print(rect_1.area())
    cuadrado=Cuadrado(lado=5)
    print(cuadrado.area())

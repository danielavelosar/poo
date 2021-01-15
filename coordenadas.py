import unittest

class coordenadas:
    def __init__(self, x, y ):
        self.x = x
        self.y = x

    def distancia (self, otra_coordenada):
        x_diff= (self.x - otra_coordenada.x)**2
        y_diff= (self.y - otra_coordenada.y)**2

        return ( x_diff+y_diff)**0.5


class blackboxtest(unittest.TestCase):
    def test_coordenadas(self):
        prueba_coord_1= coordenadas(1,1)
        prueba_coord_2= coordenadas(4,5)

        answer= prueba_coord_1.distancia(prueba_coord_2)
        self.assertEqual(answer,5)

if __name__ == "__main__":
    coord_1= coordenadas(2,65)
    coord_2= coordenadas(3,54)

    distancia_resultado=(coord_1.distancia(coord_2))

    print(distancia_resultado)

    unittest.main()



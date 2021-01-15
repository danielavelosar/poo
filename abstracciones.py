""" la idea es crear una intrefaz para no preocuparnos por los detalles
"""
class Lavadora:
    def __init__(self):
        pass
    def lavar(self, temperatura="fría"):
        self._llenar_agua(temperatura)
        self._echar_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_agua(self, temperatura):
        print(f"lleno la lavadora de agua {temperatura}")
    def _echar_jabon(self):
        print("se aplica jabón")
    def _lavar(self):
        print("se lava la ropa")
    def _centrifugar(self):
        print(" se centrifuga")

if __name__=="__main__":
    lavadora=Lavadora()
    lavadora.lavar()
class Automovil:
    def __init__(self, modelo, año):
        self.modelo=modelo
        self.año=año
        self._estado="en_reposo"
        self._motor=Motor(cilindros=4)
        self._llantas=Llantas(25,25,20,20)
    

    def acelerar(self, tipo= "despacio"):
        if tipo== "rapido":
            self._motor.inyectar_gasolina(10)
        else:
            self._motor.inyectar_gasolina(3)
    
    def girar(self, dirección="izquierda"):
        if dirección== "derecha":
            self._llantas.desviar_llantas("derecha")
        else:
            self._llantas.desviar_llantas("izquierda")



class Motor:
    def __init__(self, cilindros, tipo="otto"):
        self.cilindros=cilindros
        self.tipo=tipo
    
    def inyectar_gasolina(self, galones):
        pass

class Llantas:
    def __init__(self, derecha_atras, izquierda_atras, derecha_delante, izquierda_delante ):
        self.derecha_atras=derecha_atras
        self.izquierda_atras=izquierda_atras
        self.derecha_delante=derecha_delante
        self.izquierda_delante=izquierda_delante
    
    def desviar_llantas(self, dirección):
        if dirección== "derecha":
            self.derecha_atras="derecha"
            self.izquierda_atras="derecha"
            self.derecha_delante="izquierda"
            self.izquierda_delante="izquierda"
        elif dirección=="izquierda":
            self.derecha_atras="izquierda"
            self.izquierda_atras="izquierda"
            self.derecha_delante="derecha"
            self.izquierda_delante="derecha"
        else:
            self.derecha_atras="derecho"
            self.izquierda_atras="derecho"
            self.derecha_delante="derecho"
            self.izquierda_delante="derecho"                   
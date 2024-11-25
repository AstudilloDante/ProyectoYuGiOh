import Carta
import TipoAtributo
class CartTrampa(Carta):
    def __init__(self,nombre,descripcion,tipo_carta,atributo):
        super().__init__(nombre,descripcion,tipo_carta)
        tipo_carta="Trampa"
        self.atributo=TipoAtributo
        
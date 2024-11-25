import Carta
import TipoMounstro
import TipoAtributo
class CartaMounstro(Carta):
    def __init__(self,nombre,descripcion,tipo_carta,ataque,defensa,tipoMounstro,atributo):
        super().__init__(nombre,descripcion,tipo_carta)
        tipo_carta="Mounstro"
        self.ataque=ataque
        self.defensa=defensa
        self.tipoMounstro=TipoMounstro
        self.atributo=TipoAtributo
        
        
import Carta
import TipoMounstro

class CartaMagica(Carta):
    def __init__(self,nombre,descripcion,tipo_carta,tipoMounstro,aumento,estadistica):
        super().__init__(nombre,descripcion,tipo_carta)
        tipo_carta="Magica"
        self.tipoMounstro=TipoMounstro
        self.aumento=aumento   
    
    def aplicar_efecto(self,cartaMounstro): 
        if cartaMounstro.tipoMonstruo == self.tipoMounstro: 
            if self.estadistica=="ataque":
                cartaMounstro.ataque += self.aumento 
            else:
                cartaMounstro.defensa +=self.aumento
            
                
        
        
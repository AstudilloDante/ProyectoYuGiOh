
import random

class Jugador:
    def __init__(self,nombre,deck,mano,puntos):
        puntos=4000
        self.deck=[]
        self.mano=[]
    
    def robar_carta(self):
        if not self.deck:
            print("El mazo está vacío.")
            return None
        else:
            carta_robada = random.choice(self.deck)
            self.mano.append(carta_robada)
            self.deck.remove(carta_robada)
            print(f"{self.nombre} ha robado una carta")
        
            return carta_robada
    

        
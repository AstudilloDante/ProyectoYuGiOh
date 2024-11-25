import random 
import CartaMagica
import CartaMounstro
import CartaTrampa

class Deckbuilder:
    @staticmethod
    def leer_cartas(archivo):
        cartas = []
        with open(archivo, 'r') as file: 
            for linea in file: 
                if linea.strip(): # Ignorar líneas vacías 
                    partes = linea.strip().split(',')# Separa cada parte de la carta
                    tipo_carta = partes[2]#El tipo de carta en el texto plano esta en la parte 3
                    if tipo_carta == "Monstruo": 
                        carta =CartaMounstro(partes[0], partes[1], partes[2], int(partes[3]), int(partes[4]), partes[5],partes[6],partes[7]) 
                    elif tipo_carta == "Magica": 
                        carta = CartaMagica(partes[0], partes[1],partes[2],int(partes[3])) 
                    elif tipo_carta == "Trampa": 
                        carta = CartaTrampa(partes[0], partes[1],partes[2],partes[3]) 
                    cartas.append(carta)
        
        return cartas
    @staticmethod
    def crear_deck(cartas):
        mounstros=[]
        magicas=[]
        trampas=[]
        for carta in cartas:
            if isinstance(CartaMounstro):
                mounstros.append(carta)
            elif isinstance(CartaMagica):
                magicas.append(carta)
            elif isinstance(CartaTrampa):
                trampas.append(carta)
        deck = random.sample(mounstros, 20) + random.sample(magicas, 5) + random.sample(trampas, 5)
        random.shuffle(deck)
        return deck
        
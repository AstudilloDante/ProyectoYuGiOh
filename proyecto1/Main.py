import random 
import CartaMounstro, CartaMagica, CartaTrampa 
import Jugador 
import Deckbuilder 
import Tablero
import TipoAtributo
import TipoMounstro

def main():
    cartas_disponibles = Deckbuilder.leer_cartas_desde_archivo('cartas.txt') 
    # Crear jugadores 
    a=input("Ingresa tu nombre")
    jugador = Jugador(a) 
    maquina = Jugador("Máquina")
    #Crear los decks de el jugador y la maquina ellos solo tienen 30 cartas por deck
    jugador.deck = Deckbuilder.crear_deck(cartas_disponibles) 
    maquina.deck = Deckbuilder.crear_deck(cartas_disponibles)
    
    # Cada jugador empieza con 5 cartas 
    jugador.mano = [jugador.deck.pop() for _ in range(5)] 
    maquina.mano = [maquina.deck.pop() for _ in range(5)]
    
    #Creamos una instancia de tablero
    tablero = Tablero()
    #mostramos la mano al jugadro
    
   

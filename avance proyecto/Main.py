import random 
import CartaMounstro
import CartaMagica
import CartaTrampa
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
    
   
    i=0           
    turno_jugador = random.choice([True, False]) 
    if turno_jugador: 
        print("\nEl jugador comienza primero.")
    
    else: 
        print("\nLa máquina comienza primero.")

    if turno_jugador is True:
        turno_actual = jugador.nombre
    else:
        turno_actual="maquina"
    while jugador.puntos>0 and maquina.puntos>0:
        
        if turno_actual == "Jugador": 
            print("\nTurno del Jugador") 
            carta_robada = jugador.robar_carta() 
            if carta_robada: 
                print(f"El jugador robó la carta: {carta_robada.nombre}") 
        
            else: 
                print("El jugador no puede robar más cartas, su deck está vacío.")
            
            print("Mano del Jugador:")
            for i,carta in enumerate(jugador.mano) : 
                if isinstance(CartaMounstro):
                    print(f"{i+1} {carta.nombre}  {carta.descripcion} {carta.ataque} {carta.defensa} {carta.tipoMounstro} {carta.atributo}")
            
                elif isinstance(CartaMagica):
                    print(f"{i+1} {carta.nombre} {carta.descripcion}{carta.aumento} {carta.estadistica}")
            
                elif isinstance(CartaTrampa):
                    print(f"{i+1} {carta.nombre} {carta.descripcion}{carta.atributo} ")

            
            accion = input("\nElija una carta para jugar o ponga no para pasar")
            while accion !="no":
                if accion.isdigit() and 1 <= int(accion) <= len(jugador.mano):
                    indice_carta = int(accion) - 1 
                    carta = jugador.mano.pop(indice_carta)
                    if isinstance(CartaMounstro): 
                        posicion = input("Elija la posición para el monstruo (ataque/defensa): ").strip().lower()
                        if posicion=="ataque":
                            estado="boca arriba"
                        else:
                            estado="boca abajo"
                        tablero.colocar_carta_monstruo(carta, posicion,estado)
                        maquina.mano.remove(carta)
                    elif isinstance(CartaMagica):
                        tablero.colocar_carta_magica_trampa(carta)
                        jugador.mano.remove(carta)
                        for carta1 in tablero.espacios_monstruos_jugador[:]:
                            if carta.atributo==carta1.atributo:
                                if carta1.estado=="ataque":
                                    carta.ataque+=carta1.aumento
                                else:
                                    carta.defensa+=carta1.aumento
                    elif isinstance(CartaTrampa):
                        tablero.colocar_carta_magica_trampa(carta)
                        jugador.mano.remove(carta)
                    tablero_estado = tablero.mostrar_tablero() 
                    for seccion, estado in tablero_estado.items(): 
                        print(f"{seccion}: {estado}")
                accion = input("\nElija una carta para jugar o ponga no para pasar")
            #FASE DE BATALLA
            if i>1:
                realizar_batalla = input("¿Desea declarar una batalla? (si/no): ").strip().lower()
                if realizar_batalla == "si":
                    atacante =int(input("Seleccione el monstruo atacante (1-3):"))
                    atacante=atacante
                    while atacante <0 or atacante>3 :
                        print("posicion incorrecta")
                        atacante =int(input("Seleccione el monstruo atacante (1-3):"))
                        atacante=atacante
                    if tablero.espacios_monstruos_jugador[atacante-1]is not None:
                        carta_atacante, posicion_atacante, estado_atacante = tablero.espacios_monstruos_jugador[atacante-1]
                        
                    if estado_atacante =="boca arriba":
                        if  all(espacio is None for espacio in tablero.espacios_monstruos_maquina) and all(espacio is None for espacio in tablero.tablero_magicas_trampas_maquina):
                            print("Ataque directo!!")
                            maquina.puntos=maquina.puntos-carta_atacante.ataque
                            
                            
                        else:
                            objetivo=int(input("Seleccione el objetivo (1-3):"))
                            while objetivo <0 or objetivo>3:
                                print("posicion incorrecta")
                                objetivo=int(input("Seleccione el objetivo (1-3) ")) 
                            if 0 <= objetivo-1 < 3 and tablero.espacios_monstruos_maquina[objetivo-1] is not None and tablero.magicas_trampas_maquina[objetivo-1]is not None:
                                carta_defensora, posicion_defensora, estado_defensora = tablero.espacios_monstruos_maquina[objetivo -1]
                                if tablero.magicas_trampas_maquina[objetivo-1]is not None:
                                    for carta in tablero.magicas_trampas_maquina[:]:
                                        if carta_atacante.atributo==carta.atributo:
                                            print(f"El ataque es anulado por{carta.nombre}")
                                else:
                                    if posicion_defensora == "ataque":
                                        if carta_atacante.ataque > carta_defensora.ataque:
                                            print(f"{carta_atacante.nombre} destruye {carta_defensora.nombre} y el oponente pierde {carta_atacante.ataque - carta_defensora.ataque} puntos")
                                            maquina.puntos=carta_atacante.ataque - carta_defensora.ataque
                                            tablero.espacios_monstruos_maquina[objetivo-1] = None
                                        elif carta_atacante.ataque < carta_defensora.ataque:
                                            print(f"{carta_defensora.nombre} destruye {carta_atacante.nombre} y el jugador pierde {carta_defensora.ataque - carta_atacante.ataque} puntos")
                                            jugador.puntos=carta_defensora.ataque - carta_atacante.ataque
                                            tablero.espacios_monstruos_jugador[atacante-1] = None
                                        else: 
                                            print("Ambas cartas son destruidas") 
                                            tablero.espacios_monstruos_maquina[objetivo-1] = None 
                                            tablero.espacios_monstruos_jugador[atacante-1] = None
                                    else:
                                        if carta_atacante.ataque > carta_defensora.defensa:
                                            print(f"{carta_atacante.nombre} destruye {carta_defensora.nombre} en defensa") 
                                            tablero.espacios_monstruos_maquina[objetivo-1] = None
                                        elif carta_atacante.ataque < carta_defensora.defensa: 
                                            print(f"{carta_atacante.nombre} no puede destruir a {carta_defensora.nombre} y el jugador pierde {carta_defensora.defensa - carta_atacante.ataque} puntos") 
                                            jugador.puntos=(carta_defensora.defensa - carta_atacante.ataque)
                                            if estado_defensora == "boca abajo": 
                                                tablero.espacios_monstruos_maquina[objetivo-1] = (carta_defensora, posicion_defensora, "boca arriba")
            turno_actual = "Máquina"
            i+=1                                   
                                
                        
        else:
            print("\nTurno de la Máquina") 
            if carta_robada: 
                print(f"La máquina robó la carta: {carta_robada.nombre}") 
            else: 
                print("La máquina no puede robar más cartas, su deck está vacío.")
            
            for carta in maquina.mano[:]:
                if isinstance( CartaMounstro):
                    posicion = "defensa" 
                    estado="boca abajo"
                    tablero.colocar_carta_monstruo(carta, posicion,estado)
                
                elif isinstance(CartaMagica):
                        tablero.colocar_carta_magica_trampa(carta)
                        jugador.mano.remove(carta)
                        for carta1 in tablero.espacios_monstruos_jugador[:]:
                            if carta.atributo==carta1.atributo:
                                if carta1.estado=="ataque":
                                    carta.ataque+=carta1.aumento
                                else:
                                    carta.defensa+=carta1.aumento
                elif isinstance(CartaTrampa):
                        tablero.colocar_carta_magica_trampa(carta)
                        jugador.mano.remove(carta)
            if i > 1:
                print("La máquina declara una batalla!!!")
                for p, espacio in enumerate(tablero.espacios_monstruos_maquina):
                    
                    if espacio is not None: 
                        carta_atacante, posicion_atacante, estado_atacante = espacio
                        if posicion_atacante=="ataque":
                            if  all(espacio is None for espacio in tablero.espacios_monstruos_jugador) and all(espacio is None for espacio in tablero.tablero_magicas_trampas_jugador):
                                print("Ataque directo!!")
                                jugador.puntos-=carta_atacante.ataque
                            
                        
                            elif tablero.espacios_monstruos_jugador[p] is not None:
                                carta_defensora,posicion_defensora,estado_defensora=tablero.espacios_monstruos_jugador[p]
                                if posicion_defensora == "ataque":
                                        if carta_atacante.ataque > carta_defensora.ataque:
                                            print(f"{carta_atacante.nombre} destruye {carta_defensora.nombre} y el oponente pierde {carta_atacante.ataque - carta_defensora.ataque} puntos")
                                            maquina.puntos=carta_atacante.ataque - carta_defensora.ataque
                                            tablero.espacios_monstruos_maquina[objetivo-1] = None
                                        elif carta_atacante.ataque < carta_defensora.ataque:
                                            print(f"{carta_defensora.nombre} destruye {carta_atacante.nombre} y el jugador pierde {carta_defensora.ataque - carta_atacante.ataque} puntos")
                                            jugador.puntos=carta_defensora.ataque - carta_atacante.ataque
                                            tablero.espacios_monstruos_jugador[atacante-1] = None
                                        else: 
                                            print("Ambas cartas son destruidas") 
                                            tablero.espacios_monstruos_maquina[objetivo-1] = None 
                                            tablero.espacios_monstruos_jugador[atacante-1] = None
                                else:
                                        if carta_atacante.ataque > carta_defensora.defensa:
                                            print(f"{carta_atacante.nombre} destruye {carta_defensora.nombre} en defensa") 
                                            tablero.espacios_monstruos_maquina[objetivo-1] = None
                                        elif carta_atacante.ataque < carta_defensora.defensa: 
                                            print(f"{carta_atacante.nombre} no puede destruir a {carta_defensora.nombre} y el jugador pierde {carta_defensora.defensa - carta_atacante.ataque} puntos") 
                                            jugador.puntos=(carta_defensora.defensa - carta_atacante.ataque)
                                            if estado_defensora == "boca abajo": 
                                                tablero.espacios_monstruos_maquina[objetivo-1] = (carta_defensora, posicion_defensora, "boca arriba")
                turno_actual = "Máquina"
                i+=1   
if __name__ == "__main__":
    main()         
                             
                                
                            
                            
                            
                    
                
                
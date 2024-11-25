import CartaMagica,CartaMounstro,CartaMounstro
class Tablero: 
    def __init__(self):
        self.espacios_monstruos_jugador = [None] * 3 
        self.espacios_magicas_trampas_jugador = [None] * 3 
        self.espacios_monstruos_maquina = [None] * 3 
        self.espacios_magicas_trampas_maquina = [None] * 3
        
    
    def mostrar_tablero(self): 
        tablero_jugador = [carta.nombre if carta else "Vacío" for carta in self.espacios_monstruos_jugador] 
        tablero_magicas_trampas_jugador = [carta.nombre if carta else "Vacío" for carta in self.espacios_magicas_trampas_jugador] 
        tablero_maquina = [carta.nombre if carta else "Vacío" for carta in self.espacios_monstruos_maquina] 
        tablero_magicas_trampas_maquina = [carta.nombre if carta else "Vacío" for carta in self.espacios_magicas_trampas_maquina] 
    
        return {"Máquina - Monstruos": tablero_maquina,
                "Máquina - Mágicas/Trampas": tablero_magicas_trampas_maquina,
                "Jugador - Monstruos": tablero_jugador, 
                "Jugador - Mágicas/Trampas": tablero_magicas_trampas_jugador}
    
    def colocar_carta_mountro(self,carta,posicion,estado):
        espacios=self.espacios_monstruos_jugador
        i=input("ingrese el espacio donde desea ingrear la carta")
        while int(i)>3 or int(i) <=0:
            print("Espacio incorrecto")
            i=input("ingrese el espacio donde desea ingrear la carta")
        if self.espacios_monstruos_jugador[i-1] is None:
            if posicion.lower()=="ataque" and estado.lower()=="boca arriba":
                self.espacios[i-1]=carta
                espacios[i-1] = (carta, posicion,estado) 
                print(f"Monstruo '{carta.mombre}' colocado en el espacio {i} en posición de {posicion} .")
                print(carta)
                
            elif posicion.lower()=="defensa":
                self.espacios_monstruos_jugador[i-1]=carta
                espacios[i-1] = (carta, posicion) 
                print(f"carta Mounstro colocado en el espacio {i} en posición de {posicion} .")

        else:
            print("Espacio ocupado")
            
    def cambiar_posicion(self,carta,posicion):
        espacios=self.espacios_monstruos_jugador
        for i,(carta1,posicion1,estado1) in enumerate(espacios):
            if carta1==carta and estado1=="boca arriba" and posicion1=="ataque":
                espacios[i] = (carta1, "defensa",estado1)
                return ("La posición del monstruo '{carta1.nombre}' ha sido cambiada a defensa.")
            elif carta1==carta and estado1=="boca arriba" and posicion1=="defensa":
                espacios[i] = (carta1, "ataque",estado1)
                return ("La posición del monstruo '{carta1.nombre}' ha sido cambiada a ataque.")
            
            
    def colocar_carta_trampa_magica(self,carta):
        espacios=self.espacios_magicas_trampas_jugador
        i=input("ingrese el espacio donde desea ingrear la carta")
        while int(i)>3 or int(i) <=0:
            print("Espacio incorrecto")
            i=input("ingrese el espacio donde desea ingrear la carta")
        if self.espacios_magicas_trampas_jugador[i-1] is None:
            self.espacios_magicas_trampas_jugador[i-1]=carta
            print(f"Carta {carta} colocada en el espacio {i}.")
        else:
            print("Espacio ocupado")
    
    
            
        
        
            
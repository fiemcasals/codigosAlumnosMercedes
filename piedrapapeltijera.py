import random

while True:
    print("-------------------------------------------------")
    print("============ Piedra, Papel o Tijeras ============")
    print(' Juagaras contra la maquina ')
    juego = ['piedra', 'papel', 'tijera']
    def eleccion_maquina():
        return random.choice(['piedra', 'papel', 'tijera'])



    def comprobacion_respuesta(eleccion_usuario, eleccion_maq):
        
        if eleccion_maq == eleccion_usuario:
         return '\n~~ empataste ~~'

        elif eleccion_usuario ==  'tijera' and eleccion_maq == 'papel' or \
             eleccion_usuario == 'piedra' and eleccion_maq == 'tijera' or \
             eleccion_usuario == 'papel' and eleccion_maq == 'piedra':
            return'\n~ ganaste 🌟 ~'
        
        else:
           return ' -- perdiste -- '
            


    for i in range (3):
        
     def main():
        
        eleccion_usuario = input('elige tu opcion: ').lower()
        eleccion_maq = eleccion_maquina()
        print(comprobacion_respuesta(eleccion_usuario, eleccion_maq))
        print(f"\n elegiste: {eleccion_usuario}")
        print(f"La máquina eligio: {eleccion_maq}")
        if i < 2 : print(".vuelve a jugar.\n")
           
     main()
    
    
    vuelve_al_juego = input("\nquieres volver a jugar si/salir: ").lower()
    if vuelve_al_juego == "si":
       print('~ volvemos al juego ~\n')
       continue
    else:
       print("salimos del juego")
       break
    



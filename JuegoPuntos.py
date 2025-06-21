#juego

import random

def genera_pregunta():
 a = random.randint (1, 10) 
 b = random.randint (1, 10) 
 signo = random.choice(["+", "-", "*", "/"]) 
 return (a, signo , b ) 

print("~~ bienvenido al juego ~~\n")
print("tu objetivo sera llegar a los 50 puntos respondiendo correctamente\n")
decision= input("quieres jugar? ( si / salir):").lower() 
puntos= 0

if decision == "salir":  
     print("ha finalizado el juego")
     
elif decision == "si":
     print("comencemos")
     print(f"tus puntos actuales son {puntos}")
         
     while puntos < 50 > 0: 
          print("\nresponde correctamente para sumar puntos\n")
      
          a, signo , b =genera_pregunta()
      
          respuesta_correcta = eval(f"{a} {signo} {b}")
        
          respuesta_persona =input(f"cuanto es {a} {signo} {b}:").strip() 
          try:
              if int(respuesta_persona) == respuesta_correcta:
                print("correcto\n") 
                print("has ganado 2 puntos")
                puntos+= 2 #suma de punto
                print(f"tus puntos son {puntos}\n")
         
              else: 
               print("incorrecto\n")
               print("has perdido 1 punto")
               puntos-= 1
               print(f"tus puntos son {puntos}\n")
               print(f'la respuesta correcta era {respuesta_correcta}')
                
          except ValueError:
           if respuesta_persona.lower() == "salir":
             print("genial! \n")
             print(f"tus puntos son {puntos}")
             break
          
          if puntos >= 50:
           print("has ganado el juego")
           break
          elif puntos <= 0:
           print("has perdido")
           break


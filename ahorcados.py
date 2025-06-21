
print( "~~~~ juego de ahorcado ~~~~")
palabra_adivinar = input("pon la palabra a adivinar: ")

visible = ["_"] * (len(palabra_adivinar))

vidas = 6

while vidas > 0 and "_" in visible:
    print(" ".join(visible))
     
    letra_elegida = input("pon una letra: ")
    if letra_elegida in palabra_adivinar:
      print("la letra esta en la palabra")
      
      for i in range(len(palabra_adivinar)):
            if letra_elegida == palabra_adivinar[i]:
             visible[i] = letra_elegida

    elif letra_elegida != palabra_adivinar:
     vidas -= 1
     print(f"incorrecto, tu cantidad de vidas son: {vidas}")

    else:
       if letra_elegida != 1: 
        print("esto no es valido, por favor ingrese solo una letra")  
   
       print("\n ganaste! " if "_" not in visible else f"perdiste, la palabra era {palabra_adivinar}")




numero = int(input("escribe un numero"))

contador=numero

while contador <= 1000 :
    if contador ==3:
        break
    print(contador)
    contador +=10
else:
    print("El bucle ha terminado")
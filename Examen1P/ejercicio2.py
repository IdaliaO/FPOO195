primerpalabra=input("introduce una palabra ")
segundapalabra =input("introduce una segunda palabra")
letras1 =len (primerpalabra)
letras2 =len(segundapalabra)
resta = letras1 -letras2
print (resta)
if letras1 > letras2:
    print( f" la primera palabra es mas larga por {resta}")
else:
    invertir = -1 * resta
    print(f"La segunda palabra es mas larga por {invertir}")


def numeros ():
    num = int(input("Ingrese un numero entero para crear una tupla de ese tamaño: "))
    numlista=[]
    for i in range (num):
        todos  =int(input(f"Ingrese un numero {i+1}:  "))
        numlista.append(todos)
    return tuple (numlista)

def menu():
    print("Escriba un numero para seleccionar una opcion")
    print("1. Sumatoria de los elementos de la lista")
    print("2. Numero mayor de la lista")
    print("3. Numero menor de la lista")
    print("4. Promedio")
    print("5. Moda")
    print("6. Rango")
    print("7. Salir")
tuplanum = numeros()
while True:
    menu()
    opcion = int(input("No. Opcion: "))
    if opcion == 1:
        print ("La sumatoria de los numeros que ingresaste es: ", sum(tuplanum))
    elif opcion == 2:
        print ("El numero mayor que ingresaste en la lista es: ", max(tuplanum))
    elif opcion == 3:
        print ("El numero menor  que ingresaste en la lista es: ",min(tuplanum) )
    elif opcion == 4:
        print("El promedio de los numeros que ingresaste es: ", sum(tuplanum)/len(tuplanum))
    elif opcion == 5:
        contar = {num: tuplanum.count(num) for num in tuplanum}
        modanum = max(contar, key =contar.get)
        print("La moda en la lista es: ", modanum)
    elif opcion == 6:
        print("El rango de la lista es: ", max(tuplanum)-min(tuplanum))
    elif opcion == 7:
        print("Salir")
        break
    else:
        print("No exite esta opcion")
        
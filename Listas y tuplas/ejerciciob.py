import random
def lista():
    aleatorios =[random.randint(10,20)for _ in range (30)]
    return aleatorios
def menu():
    print("Escribe una letra para seleccionar una opcion")
    print("A. Contar numeros repetidos")
    print("B. Eliminar numeros repetidos")
    print("C. Remplazar los repetidos con 0")
    print("D. Salir")
aleatorios = lista ()
print("Esta es la lista aleatoria de numeros creada", aleatorios)
while True:
    menu()
    opcion = input ("Opcion: ")
    if opcion == 'a':
        contar ={}
        for num in aleatorios:
            if num in contar:
                contar[num] += 1
            else:
                contar[num] =1
        print("Los numeros se repiten", contar)
    elif opcion =='b':
        print("la lista sin numeros repetidos es:", list(set(aleatorios)) )
    elif opcion == 'c':
        numcero =[]
        for num in aleatorios:
            if aleatorios.count(num) > 1:
                numcero.append(0)
            else:
                numcero.append(num)        
        print("Los numero repetidos se remplazaron con 0:", numcero)
    elif opcion == 'd':
        print ("Salir")
        break
    else:
        print("No existe esa opcion")
        
            
            
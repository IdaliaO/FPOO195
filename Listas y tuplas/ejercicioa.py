def numeros():
    numing= int(input("¿Que cantidad de numeros desea ingresar"))
    cantidad =()
    for i in range (numing):
        valornum = int(input(f"Ingrese los numeros 1 a 1 {i+1}:"))
        numeros.append(valornum)    
    return tuple (cantidad)

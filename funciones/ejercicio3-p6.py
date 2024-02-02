def decimalbinario(decimal):
    return bin(decimal)[2:]
def binariodecimal(binario):
    return int(binario,2)
numdecimal =int(input("Ingrece un numero deccimal"))
print(f"El numero decimal que ingreso equivale a: {decimalbinario(numdecimal)}")
numbinario = input("Ingrese un numero en binario")
print(f"El numero decimal que ingreso equivale al numero: {binariodecimal(numbinario)}")
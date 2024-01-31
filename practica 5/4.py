varaltura = int(input("Ingrese un numero entero"))
varcontador = 1
while varcontador  <= varaltura:
    varfila = 0
    while varfila < varaltura -varcontador:
        print("", end='')
        varfila += 1
    varabajo = varcontador
    while varabajo >=1:
        print(varabajo, end=' ')
        varabajo -= 2
    print()
    varcontador += 2
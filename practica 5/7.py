varbase = int (input("Ingrese el tamaño de la base (No. entero)"))
varcontador =1
while varcontador <= varbase:
    varespacio=varbase-varcontador
    print(" "*varespacio, end='')
    print("*" * (2*varcontador-1))
    varcontador +=1
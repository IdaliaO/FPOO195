varsaldo = 0
while True:
    varentrada = input()
    if not varentrada:
        break
    movimiento, cantidad = varentrada.split()
    if cantidad.replace('.',',',1).isdigit():
        varcantidad= int(cantidad)
        if movimiento.upper() =='D':
            varsaldo +=varcantidad
        elif movimiento.upper() =='R':
            varsaldo -= varcantidad
    else:
        print ("ingrese formato valido")
print(f"\nSaldo total $: {varsaldo} ")        
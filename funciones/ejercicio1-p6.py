def facturaiva():
    factura =float(input("Escriba el total de su factura"))
    iva = input("Ingrese el porcentaje de Iva que se va a realizar ") 
    if not iva:
        total_factura = (factura * 0.21) + factura
        print(f"El total de la factura con el 21% de IVA es {total_factura}")
    else :
        iva = float(iva)
        totalfactura = (factura * (iva/100)) + factura
        print(f"El total de la factura con el {iva} % es de {totalfactura}")
    
facturaiva ()
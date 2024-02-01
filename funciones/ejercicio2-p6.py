import math
def area_circulo (radio):
    pi =3.1616
    return pi*radio**2
def volumen_cilindro (area_circulo,altura):
    return area_circulo*altura

radio_circulo = float(input("Ingrese el radio del circulo"))
altura_circulo = float(input("Ingrese la altura del cilindro"))
resultadovolumen= volumen_cilindro( altura_circulo)
resultadoarea=area_circulo (radio_circulo)
print(f"Area del circulo: {resultadoarea} Volumen del circulo: {resultadovolumen}")



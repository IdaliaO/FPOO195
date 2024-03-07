from  Personaje import *
from Armas import *

#Solicitar datos del Spartan
print("====Datos de Heroe=====")
nombreS = input ("Escribe el nombre de tu Spartan ")
especieS = input ("Escribe la especie de tu Spartan ")
alturaS = float(input("Escribe la altura de tu Spartan "))
print("")
#Solicitar el datos del Nemesis
print("=====Datos del Villano=====")
nombreN = input ("Escribe el nombre del Nemesis ")
especieN = input ("Escribe la especie del Nemesis ")
alturaN = float(input("Escribe la altura del Nemesis "))
print("")

# creamos el objeto Spartan de la clase del personaje
Spartan = Personaje(especieS,nombreS,alturaS)
Nemesis = Personaje(especieN,nombreN,alturaN)
Arma= Armas ()

#Usamos los atributos Spartan
print ("==========El objeto Spartean contiene====")
print (Spartan.getNombre)
print (Spartan.getEspecie)
print (Spartan.getAltura)


#Usamos los metodos del Spartan
print("=====Metodos del objeto Spartan=====")
Spartan.correr (False)
Spartan.lanzarGranada()
print("")

print("=====Metodos del objeto Nemesis=====")
Nemesis.correr (True)
Nemesis.lanzarGranada()
print("")

#Usamos los metodos del Arma
print ("=======Selecciona arma del Spartan")
Arma.seleccionarArma(Spartan.getNombre())
Arma.regargarArma(65)
print("") 

print("=============Cambio de Villano======")
Arma.seleccionarArma(Nemesis.getNombre())
Arma.recargarArma(10)
print ("")

#Cambiamos atributos del objeto Nemesis

print("=======Cambio de Villano ======")
cambioN=input("Escribe el nombre del nuevo villano: ")
Nemesis.setNombre(cambioN)
cambioE = input ("Escribe la especie del nuevo villano: ")
Nemesis.setEspecie (cambioE)
print("")

print("=========Villano nuevo==========")
print(Nemesis.getNombre())
print(Nemesis.getEspecie())
print("")
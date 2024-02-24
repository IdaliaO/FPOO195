from  Personaje import *
from Armas import *
# cramos el objeto 
Spartan = Personaje()
Arma= Armas ()

#Usamos los atributos Spartan
print (Spartan.nombre)
print (Spartan.especie)
print (Spartan.altura)

#Usamos los metodos del Spartan
Spartan.correr (False)
Spartan.lanzarGranada()

#Usamos los metodos del Arma
Arma.seleccionarArma(Spartan.nombre)
Arma.recargarArma(50)
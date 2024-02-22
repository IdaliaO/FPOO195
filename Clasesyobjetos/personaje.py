class Personaje:
    #atributo de personaje
    especie ="Humano"
    nombre= "John"
    altura= 2.18
    #metodos del personaje
    def correr (self, estado):
        if(estado):
            print("el personaje"+self.nombre +"esta corriendo")
        else: 
            print ("El personaje"+self.nombre +"esta muerto")
    def lanzarGranada (self):
        print(self.nombre + "Pego una granada")
        
    def recargarArma(self, municion):
        cargador = 25
        cargador = cargador + municion
        print ("Arma recargada al"+str(cargador)+"%")
        
#creamos el objeto de la clase del personaje
spartan = Personaje()

print (spartan.nombre)
print (spartan.especie)
print (spartan.altura)
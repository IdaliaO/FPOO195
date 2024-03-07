class Personaje:
    
    
    #atributo de personaje.
    #Declaramos el consturctor para crear los objetos
    def __init__(self,esp,nom,alt):
        self.especie = esp 
        self.nombre = nom
        self.altura = alt
    
    
    #metodos del personaje
    def correr (self, estado):
        if(estado):
            print("el personaje "+self.nombre +" esta corriendo")
        else: 
            print ("El personaje "+self.nombre +" esta muerto")
    def lanzarGranada (self):
        print(self.nombre + " Pego una granada")
        
        #Definimos getters y setters para acceder a los atributos
    def getEspecie(self):
        return self.__especie
    def setEspecie(self, ex):
        self.__especie = ex
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nx):
        self.__nombre =nx
    
    def getAltura(self):
        return self.altura
    
    def setSaltura(self, ax):
        self.__altura = ax
    
        
  
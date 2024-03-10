#librerias
import string, secrets 
#constructor
class generador:
    def __init__(self, long=8, mayus=True, esp=False):
        self.long= long #longitud de contraseña
        self.mayus = mayus #verificar si se van a icluir mayusculas
        self.esp =esp # verificamos los caracteres especiales
    def generar(self): #metodo para crear contraseña
        caracteres=string.ascii_letters +string.digits #selecciona los caracteres alfanumericos comunes
        if self.mayus:#añade mayusculas cuando el check este seleccionado
            caracteres +=string.ascii_uppercase#añade caracteres especiales si esta activo
        if self.esp:
            caracteres += string.punctuation
        return ''.join(secrets.choice(caracteres) for _ in range (self.long))#se creara la contraseña de tal forma que cumpla con las condiciones
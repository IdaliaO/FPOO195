# usuario.py

class Usuario:
    def _init_(self, nombre, contrasena, correo, numero="", calle="", genero="", ciudad="", fecha=""):
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__correo = correo
        self.__numero = numero
        self.__calle = calle
        self.__genero = genero
        self.__ciudad = ciudad
        self.__fecha = fecha

    def get_nombre(self):
        return self.__nombre

    def get_contrasena(self):
        return self.__contrasena

    def get_correo(self):
        return self.__correo

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_calle(self):
        return self.__calle

    def set_calle(self, calle):
        self.__calle = calle

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero

    def get_ciudad(self):
        return self.__ciudad

    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad

    def get_fecha(self):
        return self.__fecha

    def set_fecha(self, fecha):
        self.__fecha = fecha
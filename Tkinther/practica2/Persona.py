class Persona:
    def __init__(self):
        self.__listaBD = []

    def Insertar(self, id, nom, edad, cont):
        self.__listaBD.append({"Id": id, "Nombre": nom, "Edad": edad, "Contraseña": cont})

    def consultarTodos(self):
        for usuario in self.__listaBD:
            print(usuario)

    def buscarUsuario(self, id):
        encontrado = False
        for usuario in self.__listaBD:
            if usuario['Id'] == id:
                print(usuario)
                encontrado = True
                break
        if not encontrado:
            print("Usuario no encontrado")

    def eliminar(self, id):
        for usuario in self.__listaBD:
            if usuario['Id'] == id:
                self.__listaBD.remove(usuario)
                print(" :: Usuario Eliminado ::")
                break
        self.consultarTodos()

    def editar(self, id, nom, edad):
        for usuario in self.__listaBD:
            if usuario['Id'] == id:
                usuario['Nombre'] = nom
                usuario['Edad'] = edad
                print(" :: Usuario Editado :: ")
                break
        self.consultarTodos()

    def validar(self, id, cont):
        for usuario in self.__listaBD:
            if usuario['Id'] == id and usuario['Contraseña'] == cont:
                return True
        return False

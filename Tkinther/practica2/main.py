import sys
from Persona import *

objectPeople = Persona()

while True:
    print("======Menu=========")
    print("1. Registrar Persona: ")
    print("2. Consultar todos: ")
    print("3. Buscar una Persona: ")
    print("4. Eliminar una Persona: ")
    print("5. Editar una persona: ")
    print("6. Validar usuario")
    print("7. Salir")
    opcion = input ("Elige una opcion:")
    
    if opcion == "1":
        print (" == Ingrese los datos de usuario ==")
        id =input ("Escribe el Id: ")
        nom= input("Escribe el Nombre: ")
        edad =input ("Escribe la Edad: ")
        cont = input ("Escribe tu contraseña")
        
        
        objectPeople.Insertar(id, nom, edad, cont)
        print(" :: Persona Agregada Correctamente ::")
        
    elif opcion == "2":
        print (" :: Estas son las Personas Guardadas :: ")
        objectPeople.consultarTodos()
    
    elif opcion  == "3":
        print(" :: Introduce Id de la persona :: ")
        id =input("Id: ")
        objectPeople.buscarUsuario(id)
        
    elif opcion =="4":
        print (" :: Introduce Id de la persona a eliminar :: ")
        id =input("Id: ")
        objectPeople.eliminar(id)
        
    elif opcion == "5":
        print(" :: Introduce Id de la persona a editar :: ")
        id =input("Id: ")
        nm = input("Nombre: ")
        ed =input ("Edad: ")
        cont = input("Contraseña: ")
        objectPeople.editar(id, nm, edad, cont)
        
    elif opcion == "6":
        print(" :: Validar usuario ::")   
        id = input ("Id:" )
        cont = input ("contraseña")
        objectPeople.validar(id, cont)
        
    elif opcion == "7":
        print ("¡Hasta Luego !")
        sys.exit()
    
    else:
        print ("Opcion no valida. Intente de nuevo")
        
        
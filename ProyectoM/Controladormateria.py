from tkinter import messagebox
import sqlite3
import bcrypt 

class Controladormateria:
    def conexion(self):
        try:
            conex = sqlite3.connect("C:/Users/IDALI/OneDrive/Documentos/GitHub/FPOO195/ProyectoM/ProyectaMateria.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo concetar")
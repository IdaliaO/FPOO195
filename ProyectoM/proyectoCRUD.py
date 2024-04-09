from tkinter import *
from tkinter import ttk
import tkinter as tk 
from Controladormateria import *

objControlador= Controladormateria ()
Ventana = Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("500x300")

# 2 Preparar el notebook para las pestañas
panel = ttk.Notebook(Ventana)
panel.pack(fill='both', expand="yes")

# 3 Definir las pestañas del notebook
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

# 4 Agregamos las pestañas 

panel.add(pestana1, text="Control de acceso")
panel.add(pestana2, text="Articulos")
panel.add(pestana3, text="Consultar Usuario")
panel.add(pestana4, text="Editar Usuario")
panel.add(pestana5, text="Borrar Usuario")


Ventana.mainloop()
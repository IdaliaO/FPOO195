import tkinter as tk
from tkinter import messagebox
from Persona import Persona

class ValidarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Validar")
        self.persona = Persona()

        self.lbl_id = tk.Label(master, text="Id:")
        self.lbl_id.pack()

        self.txt_id = tk.Entry(master)
        self.txt_id.pack()

        self.lbl_contraseña = tk.Label(master, text="Contraseña:")
        self.lbl_contraseña.pack()

        self.txt_contraseña = tk.Entry(master, show="*")
        self.txt_contraseña.pack()

        self.btn_validar = tk.Button(master, text="Validar", command=self.validacion)
        self.btn_validar.pack()

    def validacion(self):
        id = self.txt_id.get()
        contraseña = self.txt_contraseña.get()
        if self.persona.validar(id, contraseña):  
            messagebox.showinfo("Validación exitosa", "Bienvenido")
        else:
            messagebox.showinfo("Validación fallida", "Revise sus datos.")

root = tk.Tk()
app = ValidarApp(root)
root.mainloop()

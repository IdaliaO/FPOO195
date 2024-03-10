from clase import generador
from tkinter import messagebox
import tkinter as tk

class App:
    def __init__ (self, master):
        self.master = master#creamos la ventana
        self.master.title("Generador de contraseñas")#añadimos titulo a la ventana
        self.master.configure(bg="white")#se asigna un color de fondo al generador
        self.gen = generador()  # Inicializa el codigo del generador 
        self.long = tk.IntVar(value=8)  # Longitud 
        self.mayus = tk.BooleanVar()  # mayúsculas
        self.esp = tk.BooleanVar()  # Caracteres especiales
        tk.Label(master, text="Longitud:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        tk.Entry(master, textvariable=self.long).grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        tk.Checkbutton(master, text="Incluir Mayúsculas", variable=self.mayus).grid(row=1, column=0, padx=10, pady=2, sticky="e")
        tk.Checkbutton(master, text="Incluir Especiales", variable=self.esp).grid(row=1, column=1, padx=10, pady=2, sticky="w")
        tk.Button(master, text="Generar", command=self.generar).grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        self.entrada = tk.Entry(master)
        self.entrada.grid(row=4, sticky="w")
        tk.Button(master, text="Verificar Fortaleza", command=self.comprobar).grid(row=5, sticky="w")
    def generar(self):#crear la contraseña
        self.gen = generador(self.long.get(), self.mayus.get(), self.esp.get())
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, self.gen.generar())     
    def comprobar(self):#comprobamos la fortaleza de la contraseña por medio de if y desplegamos una ventana con la fortaleza
        contra = self.entrada.get()
        fortaleza = "Baja"
        if len(contra) >= 8:
            if any(c.isupper() for c in contra) and any(c.islower() for c in contra) and any(c.isdigit() for c in contra):
                fortaleza = "Alta"
            else:
                fortaleza = "Moderada"
        messagebox.showinfo("Fortaleza", f"La fortaleza es: {fortaleza}")
def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()
if __name__ == "__main__":
    main()
        
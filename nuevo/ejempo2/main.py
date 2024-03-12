import tkinter as tk
from Serie import Serie
from tkinter import simpledialog
import tkinter as tk
from tkinter import simpledialog

class SerieGUI:
    def __init__(self, master):
        self.master = master
        master.title("Gestor de Series")

        self.serie = Serie("Ejemplo", "Género", 5)

        self.estado_label = tk.Label(master, text="Estado: Sin reproducir")
        self.estado_label.pack()

        self.reproducir_button = tk.Button(master, text="Reproducir", command=self.reproducir)
        self.reproducir_button.pack()

        self.agregar_button = tk.Button(master, text="Agregar a mi lista", command=self.agregar_a_mi_lista)
        self.agregar_button.pack()

        self.completar_button = tk.Button(master, text="Completar", command=self.completar)
        self.completar_button.pack()

        self.calificar_button = tk.Button(master, text="Calificar", command=self.calificar)
        self.calificar_button.pack()

    def reproducir(self):
        mensaje = self.serie.reproducir()
        self.estado_label.config(text=mensaje)

    def agregar_a_mi_lista(self):
        mensaje = self.serie.agregar_a_mi_lista()
        self.estado_label.config(text=mensaje)

    def completar(self):
        mensaje = self.serie.marcar_como_completada()
        self.estado_label.config(text=mensaje)

    def calificar(self):
        calificacion = simpledialog.askinteger("Calificar", "Ingresa la calificación (0-10):", minvalue=0, maxvalue=10)
        if calificacion is not None:
            mensaje = self.serie.calificar(calificacion)
            self.estado_label.config(text=mensaje)

root = tk.Tk()
mi_gui = SerieGUI(root)
root.mainloop()

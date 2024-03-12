import tkinter as tk
from tkinter import ttk
from Fracciones import Fracciones

def calcular():
    try:
        num1 = Fracciones(int(entry_numerador1.get()), int(entry_denominador1.get()))
        num2 = Fracciones(int(entry_numerador2.get()), int(entry_denominador2.get()))
        resultado = None
        operacion = operaciones_combobox.get()
        
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            resultado = num1 / num2

        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError as e:
        resultado_label.config(text=f"Error: {e}")

# Configuración inicial de la app
app = tk.Tk()
app.title("Calculadora de Fracciones")
app.geometry("400x200") # Ajusta el tamaño inicial de la ventana

# Estilo
style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10), background="#A3D2CA")

# Numerador 1
ttk.Label(app, text="Numerador 1:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_numerador1 = ttk.Entry(app)
entry_numerador1.grid(row=0, column=1, padx=5, pady=5)

# Denominador 1
ttk.Label(app, text="Denominador 1:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_denominador1 = ttk.Entry(app)
entry_denominador1.grid(row=1, column=1, padx=5, pady=5)

# Operaciones
operaciones_combobox = ttk.Combobox(app, values=["+", "-", "*", "/"], width=5)
operaciones_combobox.grid(row=0, column=2, rowspan=2, padx=15, pady=5)
operaciones_combobox.current(0)

# Numerador 2
ttk.Label(app, text="Numerador 2:").grid(row=0, column=3, padx=5, pady=5, sticky="w")
entry_numerador2 = ttk.Entry(app)
entry_numerador2.grid(row=0, column=4, padx=5, pady=5)

# Denominador 2
ttk.Label(app, text="Denominador 2:").grid(row=1, column=3, padx=5, pady=5, sticky="w")
entry_denominador2 = ttk.Entry(app)
entry_denominador2.grid(row=1, column=4, padx=5, pady=5)

# Botón de calcular
calcular_btn = ttk.Button(app, text="Calcular", command=calcular)
calcular_btn.grid(row=2, column=2, padx=5, pady=10)

# Etiqueta de resultado
resultado_label = ttk.Label(app, text="Resultado: ")
resultado_label.grid(row=3, column=0, columnspan=5, padx=5, pady=5)

app.mainloop()

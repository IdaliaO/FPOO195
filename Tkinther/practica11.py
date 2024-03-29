from tkinter import Tk, Frame, Button, messagebox
#metodos para mensaje
def mostrarMensajes():
    print(messagebox.showinfo('showinput','Information'))
    print(messagebox.showerror('showwerror','Error'))
    print(messagebox.showwarning('showwarning','Warning'))
    print(messagebox.askokcancel(message = "¿Desea continuar?", title ="Soy el titulo" ))

def addbtn():
    botonVerde.config(text="+")
    botonrosa= Button(seccion3, text="Nuevo", bg ="#EE1064")
    botonrosa.configure(height=2, width=10)
    botonrosa.pack()


#1. Creamos la ventana
Ventana = Tk() #uso de POO creando un Obj Ventana
Ventana.title("Ejemplo con 3 frames")
Ventana.geometry("600x400")
#2. Colocamos los frames de la ventana
seccion1 = Frame (Ventana, bg="red")
seccion1.pack(expand=True, fill='both')

seccion2 = Frame (Ventana, bg="yellow")
seccion2.pack(expand=True, fill='both')

seccion3 = Frame (Ventana, bg="blue")
seccion3.pack(expand=True, fill='both')

#3.posicionar Botones


#place
botonAzul= Button(seccion1, text="Azul", fg= "#50A6AB")
botonAzul.place(x=60, y=60, width=100, height=30)

#grid

botonNegro = Button(seccion2, text="Negro", fg= "#5138AD", bg ="#090909")
botonNegro.configure (height=2, width=10)
botonNegro.grid(row=0, column=1)

botonAmarillo= Button(seccion2, text="amarillo", bg="#4FEC51", command = mostrarMensajes)
botonAmarillo.configure(height=2, width=10)
botonAmarillo.grid(row=1, column=2)

#pack
botonVerde= Button(seccion3, text="verde", bg="#DDEE10", command=addbtn)
botonVerde.configure(height=2, width=10)
botonVerde.pack()


#Ejecuta  la ventana 
Ventana.mainloop()




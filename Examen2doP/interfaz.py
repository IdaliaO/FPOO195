from tkinter import Tk, Frame, Button, Label, messagebox, Entry
from clase import  clase
from tkinter import ttk

def crearmatricula(self, objPeople):     
    def pedirdatos():
        status = objPeople.matricula (nombre.get(), paterno.get(), materno.get(), año.get(), carrera.get()) 
             
        Ventana = Tk ()
        Ventana.title("Matriculas")
        Ventana.geometry("600x400")
    
        seccion1= Frame(Ventana)
        seccion1.pack(expand =True, fill ='both')
        
        Label (seccion1, text="Crear matricula", bg="black", fg = "white", font =("Mono",18)).pack()
        
        nombre = Tk.StringVar()
        Label(seccion1, text="Nombre: ", font=("Helvetica, 14")).pack()
        Entry(seccion1, takefocus= True, textvariable= nombre).pack()
        
        paterno= Tk.StringVar()
        Label (seccion1, text="Apellido Paterno", font = ("Helvetica", 14)).pack
        Entry(seccion1, takefocus= True, textvariable= paterno).pack()
        
        materno= Tk.StringVar()
        Label (seccion1, text="Apellido Materno", font = ("Helvetica", 14)).pack
        Entry(seccion1, takefocus= True, textvariable= materno).pack()
        
        año= Tk.StringVar()
        Label (seccion1, text="Año de nacimiento", font = ("Helvetica", 14)).pack
        Entry(seccion1, takefocus= True, textvariable= año).pack()
        
        carrera= Tk.StringVar()
        Label (seccion1, text="Carrera", font = ("Helvetica", 14)).pack
        Entry(seccion1, takefocus= True, textvariable= carrera).pack()
        
        botonAcesso= Button(seccion1, text="Acceder", command = pedirdatos())
        botonAcesso.pack()
        
        Ventana.mainloop()
        
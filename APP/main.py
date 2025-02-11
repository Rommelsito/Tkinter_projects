from tkinter import *
import tkinter as tk
from logica import saveJSON

ventana = tk.Tk()
ventana.title("Usuario")
ventana.geometry("400x450")
ventana.iconbitmap(r"C:\Users\lacar\OneDrive\Desktop\TO-DO-LIST\APP\usuario-ico.ico")
ventana.resizable(False, False)

title_var = tk.StringVar()
title_var.set("INTERFAZ DE USUARIO")

main_title = Label(master= ventana, textvariable = title_var, width= 20, height= 2, font= ("Arial", 14 , "bold"))
main_title.grid(row= 0, column= 0, pady=(0,12))

#LABEL Y ENTRADA DE TEXTO DEL NOMBRE
nombre_label = tk.Label(ventana)
nombre_label.config(text= "Nombre")
nombre_label.grid(row= 1, column= 0, pady= 5, sticky="W", padx= (20,2))

nombre_input = tk.Entry(ventana)
nombre_input.config(bg="gray88")
nombre_input.grid(row= 1, column= 0, ipadx= 20)

# LABEL Y ENTRADA DE TEXTO DEL APELLIDO
apellidos_label = tk.Label(ventana)
apellidos_label.config(text= "Apellidos")
apellidos_label.grid(row= 2, column= 0, pady= 5, sticky="W", padx= (20,2))

apellidos_input = tk.Entry(ventana)
apellidos_input.config(bg="gray88")
apellidos_input.grid(row= 2, column= 0, ipadx= 20)

#LABEL Y ENTRADA DE TEXTO DEL EMAIL
email_label = tk.Label(ventana)
email_label.config(text= "Email:")
email_label.grid(row= 3, column= 0, pady= 5, sticky="W", padx= (20,2))

email_input = tk.Entry(ventana)
email_input.config(bg="gray88")
email_input.grid(row= 3, column= 0, ipadx= (20))

#LABELFRAME PARA ALBERGAR DESCRIPCION
description_label = tk.LabelFrame(ventana)
description_label.config(text= "Description: ", width= 300, height= 150)
description_label.grid(row= 4, column= 0, pady= 5, sticky="W", padx= (12,2))

#ENTRADA MAYOR DE TEXTO
description_input = Text(description_label)
description_input.config(height=8, width=36, font= ("Arial", 12))
description_input.grid(pady= 8, padx=8)

#ESTE FRAME SIRVE PARA ALMACENAR BOTONES
frame_boton = tk.Frame(ventana)
frame_boton.grid(pady= 25)

boton_guardar = tk.Button(frame_boton)
boton_guardar.config(text="Guardar",font= ("Bold", 10), width= 6, bd= 3, cursor= "hand2")
boton_guardar.pack(side= "left", padx= 45)

boton = tk.Button(frame_boton)
boton.config(text= 'Salir', font= ("Bold", 10),command= ventana.destroy, width= 6, bd= 3, cursor= "hand2")
boton.pack(side= "right", padx= 45)

#? FUNCIONES MANEJADORES DE EVENTOS
def handleSave(event):
    nombre = nombre_input.get()
    apellido = apellidos_input.get()
    email = email_input.get()
    description = description_input.get("1.0", tk.END)

    saveJSON(nombre, apellido, email, description)

    print(f"Nombre: {nombre}\nApellido: {apellido}\nEmail: {email}\nDescripcion:{description}")
    print("Boton ~Guardar~ presionado")

def handleExit(event):
    print("Boton ~Salir~ presionado")

def handleKeyPress(event):
    if event.char == "a":
        print('Presionaste la letra "a')

#? MANEJAMOS LOS EVENTOS DE LA APP
# MANEJAMOS EL GUARDADO
boton_guardar.bind("<Button-1>", handleSave)
# MANEJAMOS LA SALIDA
boton.bind("<Button-1>", handleExit)

ventana.mainloop()


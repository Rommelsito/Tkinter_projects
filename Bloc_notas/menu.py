from tkinter import *
import tkinter as tk
from tkinter import filedialog

#DISEÑO DE LA VENTANA
ventana = tk.Tk()
ventana.title("Menu")
ventana.geometry("700x450")
ventana.config(bg= "gray13")
ventana.resizable(False,False)

#VARIABLE AUXILIAR
ruta_archivo = "" 

#FUNCIONES 
def handlNew_file():
    text_entry.delete(1.0, tk.END)

def handlOpen():
    global ruta_archivo
    ruta_archivo = filedialog.askopenfilename(defaultextension= ".TXT", 
                                                filetypes = [("Archivos de texto", "*.TxT"),
                                                            ("Archivos python", "*.py"),
                                                            ("Todo tipo de archivo","*.*")])
    
    with open(ruta_archivo, "r", encoding= "utf-8") as file:
        text_entry.insert(tk.INSERT, file.read())

def handlSave():
    print("Guardando...")

#CREACION DE LA BARRA MENU
barra_menu = tk.Menu(ventana)
ventana.config(menu = barra_menu)

#MENU ARCHIVO
archivo_menu = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Archivo", menu= archivo_menu)

#COMANDOS AGREGADOS AL MENU ARCHIVO(PRINCIPAL)
archivo_menu.add_command(label="Nuevo", command= handlNew_file)
archivo_menu.add_command(label="Abrir", command= handlOpen)
archivo_menu.add_command(label= "Guardar", command= handlSave)
archivo_menu.add_separator()
archivo_menu.add_command(label= "Salir", command= ventana.destroy)

#MENU EDITAR
editar_menu = tk.Menu(barra_menu)
barra_menu.add_cascade(label= "Editar", menu= editar_menu)

#COMANDOS AGREGADOS AL MENU EDITAR
editar_menu.add_command(label= "Copiar")
editar_menu.add_command(label="Pegar")
editar_menu.add_separator()
editar_menu.add_command(label= "Cortar")

#ENTRADA DE MAYOR TEXTO
text_entry = tk.Text(ventana)
text_entry.config(font=("Times New Roman", 12))
text_entry.pack(fill= tk.BOTH, expand= True)

ventana.mainloop()
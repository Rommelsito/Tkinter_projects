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

#FUNCIONE PARA REESTABLECER
def handlNew_file():
    text_entry.delete(1.0, tk.END)

#FUNCION PARA CARGAR ARCHIVOS TEXTOS
def handlOpen():
    global ruta_archivo
    ruta_archivo = filedialog.askopenfilename(defaultextension= ".TXT", 
                                                filetypes = [("Archivos de texto", "*.TxT"),
                                                            ("Archivos python", "*.py"),
                                                            ("Todo tipo de archivo", "*.*")])
    
    with open(ruta_archivo, "r", encoding= "utf-8") as file:
        text_entry.insert(tk.INSERT, file.read())

#FUNCION PARA GUARDAR
def handlSave():
    global ruta_archivo
    ruta_archivo = filedialog.asksaveasfilename(defaultextension= ".TXT", 
                                                filetypes = [("Archivos de texto", "*.TxT"),
                                                            ("Archivos python", "*.py"),
                                                            ("Todo tipo de archivo", "*.*")])
    if ruta_archivo:
        try:

            with open(ruta_archivo, "w", encoding= "utf-8") as file:
                file.write(text_entry.get(1.0, tk.END))
        
        except:
            print("No se guardo el archivo")

#FUNCIONES PARA COPIAR, PEGAR, Y CORTAR TEXTO
def handlCopy():
    text_entry.event_generate("<<Copy>>")
    print("Copiado")

def handlPaste():
    text_entry.event_generate("<<Paste>>")
    print("Pegado")

def handlCut():
    text_entry.event_generate("<<Cut>>")
    print('Cortado')

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
editar_menu.add_command(label= "Copiar", command= handlCopy)
editar_menu.add_command(label="Pegar", command= handlPaste)
editar_menu.add_separator()
editar_menu.add_command(label= "Cortar", command= handlCut)

#ENTRADA DE MAYOR TEXTO
text_entry = tk.Text(ventana)
text_entry.config(font=("Times New Roman", 12))
text_entry.pack(fill= tk.BOTH, expand= True)

ventana.mainloop()
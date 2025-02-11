import json

def saveJSON(nombre, apellido, email, descripcion):
    data = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Email": email,
        "Descripcion": descripcion
    }

    datos = []
    # LEEMOS EL ARCHIVO "data.json" Y OBTENEMOS LA LISTA DE DATOS 
    with open("APP/data.json", "r") as archivo:
        datos = json.load(archivo)

    # AGREGAMOS LOS NUEVOS DATOS A LOS DATOS EXISTENTES 
    datos.append(data)

    with open("APP/data.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

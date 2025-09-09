# Escritura en formato binario
import pickle

# Objeto a serializar
datos = {"nombre": "Fernando", "edad": 18, "correo": "fsanudo@hotmail.com"}

# Abrir el archivo en modo escritura binaria
with open("info.bin", "wb") as archivo:
    # Escribir el objeto serializado en el archivo
    pickle.dump(datos, archivo)

with open("info.bin","rb") as archivo:
    datos2 = pickle.load(archivo)
    print(datos2)
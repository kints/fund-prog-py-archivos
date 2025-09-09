archivo = open("archivo_nu.txt", "r")

print(archivo.readline())
print("hola")
print(archivo.read())
print("Hola")
print(archivo.read())

# Esta instrucción cierra el archivo
archivo.close()
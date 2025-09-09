try:

  archivo = open("archivo_nu.txt", "+w")

  archivo.write('Saludos\n')
  archivo.write('Acabas de agregar contenido a tu nuevo archivo\n')
  archivo.write('Una línea nueva')
  i = 0
  while i<1_000_000:
    i+=1
    print(i)
  # Esta instrucción cierra el archivo
  5/0
finally:
  archivo.close()
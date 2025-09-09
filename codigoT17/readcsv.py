import csv

with open("envios_2025-09-09.csv","r") as archivo:
  csv_reader = csv.reader(archivo)
  for fila in csv_reader:
    print(fila)

with open("envios_2025-09-09.csv","r", encoding='utf-8') as archivo:
  csv_reader = csv.DictReader(archivo)
  for fila in csv_reader:
    print(dict(fila))

print("Código")
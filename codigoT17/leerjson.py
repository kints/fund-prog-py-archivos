import json
datos =""
with open("ejemplo.json",'r', encoding="utf-8") as archivo:
  datos = json.load(archivo)
print(datos)

import json

# Data to write
data = {
    "name": "Alice",
    "age": 25,
    "city": "Morelia"
}

# Writing JSON to a file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # Use indent for pretty formatting

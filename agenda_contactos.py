import csv
import pickle

# Agenda inicial con 3 contactos de ejemplo
agenda = {
    "Juan": "5551234567",
    "Maria": "5559876543",
    "Pedro": "5554567890"
}

# Funciones para manejo de la agenda

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el teléfono del contacto: ")
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado correctamente.")

def editar_contacto():
    nombre = input("Ingrese el nombre del contacto a editar: ")
    if nombre in agenda:
        telefono = input("Ingrese el nuevo teléfono: ")
        agenda[nombre] = telefono
        print(f"Contacto {nombre} editado correctamente.")
    else:
        print("Contacto no encontrado.")

def borrar_contacto():
    nombre = input("Ingrese el nombre del contacto a borrar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} borrado correctamente.")
    else:
        print("Contacto no encontrado.")

def guardar_csv():
    try:
        with open("agenda.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for nombre, telefono in agenda.items():
                writer.writerow([nombre, telefono])
        print("Agenda guardada en agenda.csv correctamente.")
    except Exception as e:
        print(f"Error al guardar CSV: {e}")

def cargar_csv():
    try:
        with open("agenda.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            agenda.clear()
            for row in reader:
                if len(row) == 2:
                    nombre, telefono = row
                    agenda[nombre] = telefono
        print("Agenda cargada desde agenda.csv correctamente.")
    except FileNotFoundError:
        print("El archivo agenda.csv no existe.")
    except Exception as e:
        print(f"Error al cargar CSV: {e}")

def guardar_serializado():
    try:
        with open("agenda.pkl", "wb") as f:
            pickle.dump(agenda, f)
        print("Agenda guardada como objeto serializado correctamente.")
    except Exception as e:
        print(f"Error al guardar objeto serializado: {e}")

def cargar_serializado():
    try:
        with open("agenda.pkl", "rb") as f:
            data = pickle.load(f)
            if isinstance(data, dict):
                agenda.clear()
                agenda.update(data)
                print("Agenda cargada desde objeto serializado correctamente.")
            else:
                print("El archivo no contiene un formato válido.")
    except FileNotFoundError:
        print("El archivo agenda.pkl no existe.")
    except Exception as e:
        print(f"Error al cargar objeto serializado: {e}")

# Menú principal
def menu():
    opciones = {
        "1": agregar_contacto,
        "2": editar_contacto,
        "3": borrar_contacto,
        "4": guardar_csv,
        "5": cargar_csv,
        "6": guardar_serializado,
        "7": cargar_serializado
    }
    
    while True:
        print("""
        1. Agregar nuevo contacto
        2. Editar contacto
        3. Borrar contacto
        4. Guardar como archivo CSV
        5. Cargar archivo CSV
        6. Guardar como objeto serializado
        7. Cargar como archivo serializado
        8. Salir
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == "8":
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()

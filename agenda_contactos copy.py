import csv
import sys
import select
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

def mostrar_contactos():
    for contacto in agenda:
        print(f"Nombre: {contacto} Telefono: {agenda[contacto]}")

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
        "3": mostrar_contactos,
        "4": borrar_contacto,
        "5": guardar_csv,
        "6": cargar_csv,
        "7": guardar_serializado,
        "8": cargar_serializado
    }
    
    while True:
        entrada_usuario = None
        print("""
        1. Agregar nuevo contacto
        2. Editar contacto
        3. Mostrar contacto
        4. Borrar contacto
        5. Guardar como archivo CSV
        6. Cargar archivo CSV
        7. Guardar como objeto serializado
        8. Cargar como archivo serializado
        9. Salir
        """)
        rlist, _, _ = select.select([sys.stdin],[],[],15)
        
        if rlist:
            entrada_usuario = sys.stdin.readline().strip()
            # Pide al usuario que decida si quiere continuar
            if entrada_usuario == "9":
                break
            elif entrada_usuario in opciones:
                opciones[entrada_usuario]()
            else:
                print("Opción no válida.")
        else:
            continuar = input("¿Quieres continuar? (s/n): ").lower()
            if continuar == 's':
                print("Continuando el menú...\n")
            else:
                print("Saliendo del programa...")
                exit() # Sale del bucle infinito

if __name__ == "__main__":
    menu()

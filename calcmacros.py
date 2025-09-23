import json
import os

class MacroFunction:
  def __init__(self, name, variables, constants, operations):
    self.name = name
    self.variables = variables  # Dict of variable names, values are placeholders (no values at creation)
    self.constants = constants
    self.operations = operations  # List of dicts: {'op_type': '+', 'op1': 'a', 'op2': 'b'}

  def execute(self):
    # Solicita los valores de las variables al ejecutar
    input_vars = {}
    for var in self.variables:
      val = float(input(f"Ingresa el valor para la variable '{var}': "))
      input_vars[var] = val

    temp_vars = {}
    last_result = None
    for i, op in enumerate(self.operations):
      op_type = op['op_type']
      op1 = op['op1']
      op2 = op['op2']

      val1 = input_vars.get(op1, self.constants.get(op1, temp_vars.get(op1, 0)))
      val2 = input_vars.get(op2, self.constants.get(op2, temp_vars.get(op2, 0)))

      if op_type == '+':
        result = val1 + val2
      elif op_type == '-':
        result = val1 - val2
      elif op_type == '*':
        result = val1 * val2
      elif op_type == '/':
        result = val1 / val2 if val2 != 0 else 0
      else:
        result = 0

      temp_name = f"temp_{i+1}"
      temp_vars[temp_name] = result
      last_result = result
      print(f"Resultado guardado en '{temp_name}': {result}")

    print("\nResumen de variables:")
    for k, v in input_vars.items():
      print(f"{k}: {v}")
    print("Resumen de constantes:")
    for k, v in self.constants.items():
      print(f"{k}: {v}")
    print("Resumen de temporales:")
    for k, v in temp_vars.items():
      print(f"{k}: {v}")
    print(f"\nResultado final: {last_result}")

  def to_dict(self):
    return {
      'name': self.name,
      'variables': self.variables,
      'constants': self.constants,
      'operations': self.operations
    }

  @staticmethod
  def from_dict(data):
    return MacroFunction(
      data['name'],
      data['variables'],
      data['constants'],
      data['operations']
    )

def save_macros(macros, filename):
  with open(filename, 'w', encoding='utf-8') as f:
    json.dump([m.to_dict() for m in macros], f, indent=2)

def load_macros(filename):
  if not os.path.exists(filename):
    return []
  with open(filename, 'r', encoding='utf-8') as f:
    data = json.load(f)
    return [MacroFunction.from_dict(d) for d in data]

def create_macro():
  name = input("Nombre de la función: ")
  variables = {}
  constants = {}
  operations = []

  num_vars = int(input("¿Cuántas variables necesitas? "))
  for i in range(num_vars):
    var_name = input(f"Nombre de la variable #{i+1}: ")
    var_value = float(input(f"Valor para '{var_name}': "))
    variables[var_name] = var_value

  num_consts = int(input("¿Cuántas constantes necesitas? "))
  for i in range(num_consts):
    const_name = input(f"Nombre de la constante #{i+1}: ")
    const_value = float(input(f"Valor para '{const_name}': "))
    constants[const_name] = const_value

  num_ops = int(input("¿Cuántas operaciones necesitas? "))
  for i in range(num_ops):
    print(f"\nOperación #{i+1}:")
    op_type = input("Tipo de operación (+, -, *, /): ")
    op1 = input("Primer operando (nombre de variable, constante o temp): ")
    op2 = input("Segundo operando (nombre de variable, constante o temp): ")
    operations.append({'op_type': op_type, 'op1': op1, 'op2': op2})

  return MacroFunction(name, variables, constants, operations)

def main():
  macros = []
  filename = "macros.json"
  macros = load_macros(filename)

  while True:
    print("\nMenú:")
    print("1. Crear nueva función")
    print("2. Listar funciones cargadas")
    print("3. Ejecutar una función")
    print("4. Guardar funciones actuales")
    print("5. Cargar funciones desde archivo")
    print("6. Salir")
    choice = input("Elige una opción: ")

    if choice == '1':
      macro = create_macro()
      macros.append(macro)
      print(f"Función '{macro.name}' creada y agregada.")
    elif choice == '2':
      if not macros:
        print("No hay funciones cargadas.")
      else:
        for i, m in enumerate(macros):
          print(f"{i+1}. {m.name}")
    elif choice == '3':
      if not macros:
        print("No hay funciones cargadas.")
      else:
        for i, m in enumerate(macros):
          print(f"{i+1}. {m.name}")
        idx = int(input("Selecciona el número de función a ejecutar: ")) - 1
        if 0 <= idx < len(macros):
          macros[idx].execute()
        else:
          print("Índice inválido.")
    elif choice == '4':
      save_macros(macros, filename)
      print("Funciones guardadas correctamente.")
    elif choice == '5':
      macros = load_macros(filename)
      print("Funciones cargadas desde archivo.")
    elif choice == '6':
      print("Saliendo...")
      break
    else:
      print("Opción inválida.")

if __name__ == "__main__":
  main()
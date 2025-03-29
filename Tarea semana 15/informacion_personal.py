# Crear el diccionario
informacion_personal = {"nombre": "Carlos Gómez","edad": 35,"ciudad": "Ambato","profesion": "Abogado"}
print(informacion_personal)
#modificarlo
informacion_personal["ciudad"] = "Cuenca"
print(informacion_personal)
# Verificar si la clave "telefono" existe en el diccionario. Si no, agregarla con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminar la clave "edad" ya que no es necesaria
del informacion_personal["edad"]

# Imprimir el diccionario final después de realizar todas las operaciones
print(informacion_personal)
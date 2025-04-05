
# Abrimos el archivo 'my_notes.txt' en modo escritura ('w')
with open("my_notes.txt", "w") as file:

    # Escribimos tres líneas de notas personales en el archivo
    file.write("Hoy aprendí a trabajar con archivos en Python.\n")
    file.write("Estudio en la Universidad Estatal Amazonica.\n")
    file.write("Me gusta jugar videojuegos con mis amigos.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo 'my_notes.txt' en modo lectura ('r')
file = open("my_notes.txt", "r")

# Leemos y mostramos el contenido línea por línea usando readline()
print("Contenido del archivo:")
line = file.readline()  # Lee la primera línea
while line:
    print(line.strip())  # .strip() elimina el salto de línea al final
    line = file.readline()  # Lee la siguiente línea

# Cierre de Archivo
file.close()

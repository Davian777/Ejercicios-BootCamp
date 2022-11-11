file = open('Archivo_Texto_1.txt', 'w')
file.write('He creado un archivo de texto\n')
file.close

file = open('Archivo_Texto_1.txt', 'r+')
file.readline()
file.write('Segunda vez que lo abro, y escribo en el.\n')

file.seek(0)
print(file.read())
file.close()
import matplotlib.pyplot as plt  # Para crear gráficos
import csv  # Para leer archivos CSV o texto delimitado

# Inicializamos listas vacías para almacenar los datos del archivo
nombres = []  # Lista para las etiquetas (categorías)
valores = []  # Lista para los valores numéricos asociados

# Abrimos el archivo de texto que contiene los datos
with open('/home/mauri/uni/UTN/temasDadosClasesUTN/practicasUTN/mercedes/ejercicios/torta/datos.txt', 'r') as archivo:
    lector = csv.reader(archivo)  # Creamos un lector CSV
    next(lector)  # Saltamos la primera línea (encabezado)
    for fila in lector:
        nombres.append(fila[0])           # Primer columna: nombre o etiqueta
        valores.append(int(fila[1]))      # Segunda columna: valor numérico (convertido a entero)

# Crear gráfico de torta
plt.figure(figsize=(6, 6))  # Define el tamaño de la figura (6x6 pulgadas)

# Dibuja el gráfico de torta con etiquetas y porcentajes
plt.pie(
    valores,                # Valores para cada porción
    labels=nombres,         # Etiquetas para cada porción
    autopct='%1.1f%%',      # Muestra el porcentaje con 1 decimal
    startangle=90           # Empieza la torta desde el ángulo 90 (arriba)
)

plt.title('Resultados del Juego')  # Título del gráfico

plt.axis('equal')  # Hace que el gráfico se vea como un círculo perfecto

plt.tight_layout()  # Ajusta los márgenes automáticamente para que no se solapen

plt.show()  # Muestra el gráfico en pantalla

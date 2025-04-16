
# Normalizar columnas(.CSV y .xlsx)

import pandas as pd
import unicodedata
import re

def normalizar_nombre(col):
    # Convertir a minúsculas
    col = col.lower()
    #  Quitar acentos
    col = unicodedata.normalize('NFKD', col).encode('ASCII', 'ignore').decode('utf-8')
    # Reemplazar espacios por guiones bajos
    col = col.replace(" ", "_")
    # Eliminar caracteres especiales
    col = re.sub(r'[^a-z0-9_]', '', col)
    return col

# Cargar el archivo
df = pd.read_csv('datos.csv')  # o pd.read_excel('datos.xlsx')

# Aplicar la normalización a los nombres de columna
df.columns = [normalizar_nombre(col) for col in df.columns]

# Mostrar los nuevos nombres
print("Nombres de columnas normalizados:")
print(df.columns)

# Guardar el archivo limpio
df.to_csv('datos_columnas_normalizadas.csv', index=False)
print("\nArchivo guardado como 'datos_columnas_normalizadas.csv'")

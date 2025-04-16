
#Script para limpiar datos (.CSV) (eliminar nulos y duplicados) y guardar en un nuevo archivo .CSV

import pandas as pd

# poner la ruta del archivo
ruta_archivo = 'datos.csv'
df = pd.read_csv(ruta_archivo .csv .xlsx)

# Mostrar información general antes de la limpieza
print("Antes de la limpieza:")
print(df.info())
print("\nDuplicados encontrados:", df.duplicated().sum())
print("Nulos por columna:\n", df.isnull().sum())

# Eliminar filas duplicadas
df = df.drop_duplicates()

# Eliminar filas con valores nulos
df = df.dropna()

# Mostrar información después de la limpieza
print("\nDespués de la limpieza:")
print(df.info())

# Guardar el archivo limpio (opcional)
df.to_csv('datos_limpios.csv', index=False)
print("\nArchivo limpio guardado como 'datos_limpios.csv'")


#Para limpiar datos de un excel sustituir el .csv por .xlsx y usar el método read_excel() de pandas#

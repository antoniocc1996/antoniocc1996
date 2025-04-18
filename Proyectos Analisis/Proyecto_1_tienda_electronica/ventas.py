
#PRACTICA SOBRE LAS VENTAS DE UNA TIENDA A NIVEL ESPAÑOL

import pandas as pd

df = pd.read_csv('Proyectos Analisis/Proyecto_1_tienda_electronica/ventas_50_filas.csv')

#print(df.head())

duplicados = df.duplicated().sum()

#print(duplicados)  #0 duplicados

nulos = df.notnull().sum()

#print(nulos) # 0 nulos

df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Fecha'] = df['Fecha'].dt.strftime('%d-%m-%Y')

# Crear una nueva columna 'Venta Total' que multiplica 'Cantidad' por 'Precio_unitario'

df['Venta Total'] = (df['Cantidad'] * df['Precio_Unitario'])

#print(df.head(20))

metodo_de_pago = df['Metodo_Pago'].value_counts()
print(f'Numero de veces que se han usado los diferentes metodos de pago: ', metodo_de_pago)


#--------------------------------------------------------------------------------------------------------------------#

# Grafico de ventas totales por ciudad

import matplotlib.pyplot as plt

ventas_por_ciudad = df.groupby('Ciudad')['Venta Total'].sum()

plt.xlabel('Ciudad')
plt.ylabel('Ventas Totales')
plt.title('Ventas Totales por Ciudad')
plt.bar(ventas_por_ciudad.index, ventas_por_ciudad.values, color='blue')
plt.show()

# Grafico de ventas totales por producto

ventas_producto = df.groupby('Producto')['Venta Total'].sum()

plt.xlabel('Producto')
plt.ylabel('Ventas Totales')
plt.title('Ventas Totales por producto')
plt.bar(ventas_producto.index, ventas_producto.values, color =  'green')
plt.show()

# Producto mas vendido

producto_mas_vendido = df.groupby('Producto')['Cantidad'].sum()

plt.xlabel('Producto')
plt.ylabel('Cantidad')
plt.title('Producto mas vendido')
plt.bar(producto_mas_vendido.index, producto_mas_vendido.values, color = 'red')
plt.show()




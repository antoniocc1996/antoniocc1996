# 🛍️ Análisis de Ventas de una Tienda Electrónica en España

Este proyecto es una práctica de análisis de datos con **Python** y tiene como objetivo explorar y visualizar datos de ventas simuladas de una tienda electrónica que opera en distintas ciudades de España. Utiliza un dataset de 50 registros con información sobre productos vendidos, fechas, cantidades, precios y métodos de pago.

---

## 📁 Archivos del proyecto

- `ventas_50_filas.csv`: contiene los datos simulados de ventas.
- `ventas.py`: script en Python que realiza limpieza, transformación, análisis y visualización de los datos.

---

## 🔧 Tecnologías y librerías utilizadas

- Python
- Pandas
- Matplotlib

---

## 🔎 Análisis realizados

El script realiza los siguientes pasos:

1. **Carga y limpieza de datos**
   - Conversión de la columna `Fecha` a formato día-mes-año.
   - Verificación de duplicados y valores nulos.
   - Cálculo de una nueva columna `Venta Total` (Cantidad × Precio Unitario).

2. **Estadísticas básicas**
   - Conteo de métodos de pago utilizados.

3. **Visualizaciones**
   - Ventas totales por ciudad.
   - Ventas totales por producto.
   - Cantidad total vendida por producto (producto más vendido).

---

## 📊 Ejemplos de gráficos

- 📍 Ventas por ciudad  
- 📦 Ventas por producto  
- 🥇 Producto más vendido  


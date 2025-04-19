

#ANALISIS DE LOS PARTICIPANTES DE UNA CARRERA DE ATLETISMO

import pandas as pd

df = pd.read_csv('Proyectos Analisis/Proyecto_2_carreraatletismo/participantes_carrera.csv')

#print(df.head(10))

#Revisamos si hay valores nulos

nulos = df.isnull().sum()
#print(nulos)

#Cambiamos el formato de la fecha a DD-MM-YYYY

df['Fecha de inscripción'] = pd.to_datetime(df['Fecha de inscripción'])
df['Fecha de inscripción'] = df['Fecha de inscripción'].dt.strftime('%d-%m-%Y')
#print(df.head())

#Nueva columna de edades

df['Grupo_Edades'] = pd.cut(df['Edad'], bins=[18, 25, 35, 45, 55, 64], 
                    labels=['18-25', '26-35', '36-45', '46-55', '56-64'])
#print(df.head())


#Participantes masculinos

masculinos = df.value_counts('Género').loc['M']

#print(masculinos)

#Participantes femeninos 

femeninos = df.value_counts('Género').loc['F']

#print(femeninos)

#Mejores tiempos por Género para masculinos

primeros_masc = df.loc[df['Género'] == 'M'].sort_values('Tiempo (min)', ascending=True)

print(primeros_masc.head(5))

#Mejores tiempos por Género para femeninos

primeros_fem = df.loc[df['Género'] == 'F'].sort_values('Tiempo (min)', ascending=True)

print(primeros_fem.head(5))


#-----------------------------------------------------------------------------------------------------------#

import matplotlib.pyplot as plt

#Participantes totales por género

participantes_totales = (masculinos + femeninos)
plt.xlabel('Género')
plt.ylabel('participantes_totales')
plt.title('Participantes por Género')
plt.bar(['Masculinos', 'Femeninos'], [masculinos, femeninos], color=['blue', 'pink'])
plt.savefig('Proyectos Analisis/Proyecto_2_carreraatletismo/participantes_por_genero.png')
plt.show()
#plt.close()

#Participantes totales por edades

participantes_por_edad = df['Grupo_Edades'].value_counts().sort_index()
plt.xlabel('Grupo de Edades')
plt.ylabel('ID')
plt.title('Participantes por Grupo de Edades')
plt.bar(participantes_por_edad.index.astype(str), participantes_por_edad.values, color=['blue', 'pink'])
plt.savefig('Proyectos Analisis/Proyecto_2_carreraatletismo/participantes_por_edad.png')
plt.show()
#plt.close()

#Participacion Masculina y Edades

participantes_masc = df.loc[df['Género'] == 'M']['Grupo_Edades'].value_counts().sort_index()
plt.xlabel('Grupo de Edades')
plt.ylabel('ID')
plt.title('Participantes Masculinos por Grupo de Edades')
plt.bar(participantes_masc.index.astype(str), participantes_masc.values, color=['blue'])
plt.savefig('Proyectos Analisis/Proyecto_2_carreraatletismo/participantes_masculinos_por_edad.png')
plt.show()
#plt.close()

#Participacion Femenina y Edades

participantes_fem = df.loc[df['Género'] == 'F']['Grupo_Edades'].value_counts().sort_index()
plt.xlabel('Grupo de Edades')
plt.ylabel('ID')
plt.title('Participantes Femeninos por Grupo de Edades')
plt.bar(participantes_fem.index.astype(str), participantes_fem.values, color=['pink'])
plt.savefig('Proyectos Analisis/Proyecto_2_carreraatletismo/participantes_femeninos_por_edad.png')
plt.show()
#plt.close()
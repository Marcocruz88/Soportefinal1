# -*- coding: utf-8 -*-
"""Proyecto1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aFSx_USGOm-m5P4VTyI8OJvihneyQ9Gv
"""

#Importación de librerías Requeridas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
import numpy as np

#Lectura del data frame
df = pd.read_csv('datos_Con_date_Seasons.csv')

#Visualización general del data frame
df.head()



"""# Exploración de Datos"""

co = df['Temperature(C)'].corr(df['Rented Bike Count'])
co1 = df['Humidity(%)'].corr(df['Rented Bike Count'])
co2 = df['Wind speed (m/s)'].corr(df['Rented Bike Count'])
co3= df['Visibility (10m)'].corr(df['Rented Bike Count'])
co4 = df['Dew point temperature(C)'].corr(df['Rented Bike Count'])
co5 = df['Solar Radiation (MJ/m2)'].corr(df['Rented Bike Count'])


correw = [co, co1, co2, co3, co4, co5]
variables = ['Temperatura', 'Humedad', 'Velocidad del Viento', 'Visibilidad', 'Punto de Rocío', 'Radiación Solar']

correlation_df = pd.DataFrame(correw, index=variables, columns=['Correlación'])

# Crear el mapa de calor
plt.figure(figsize=(6, 8))  # Ajustar el tamaño del gráfico
sns.heatmap(correlation_df, annot=True, cmap="Blues", linewidths=0.5)

# Añadir título y etiquetas de los ejes
plt.title("Correlaciones con Bicicletas Rentadas")
plt.xlabel("Valores")
plt.ylabel("Propiedades")

# Mostrar el gráfico
plt.show()

#Estadisticas de variable "Rented Bike Count"
df['Rented Bike Count'].describe()

#Agrupación por regla de Sturges
N = len(df['Rented Bike Count'])
binss = int(np.ceil(np.log2(N) + 1))

#Histograma de la variable "Rented Bike Count"
plt.figure(figsize=(10,6))
sns.histplot(df['Rented Bike Count'], bins=binss, kde=True)
plt.title('Histogram of Rented Bike Count')
plt.xlabel('Rented Bike Count')
plt.ylabel('Frequency')

#Diagrama de dispersión
plt.figure(figsize=(10,6))
sns.scatterplot(data = df['Rented Bike Count'])
plt.title('Dispertion of Rented Bike Count')
plt.xlabel('Rented Bike Count')
plt.show

#Estadísticas descriptivas de Hour
# Crear el diagrama
plt.figure(figsize=(20,12))
sns.boxplot(x = df['Hour'], y = df['Rented Bike Count'], data = df)

plt.title('Total Number of Bikes Rented by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Bikes Rented')
plt.show()

#Tabla de valores
stats = df.groupby('Hour')['Rented Bike Count'].agg(['mean', 'std', 'min', 'max'])
stats = stats.round(2)

stats.columns = ['Promedio', 'Desviación Estándar', 'Min', 'Max']

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=stats.values,
                 colLabels=stats.columns,
                 rowLabels=stats.index,
                 cellLoc='center',
                 loc='center')

plt.title('Statistics of Bike Rentals by Hour')
plt.show()

#Relación Temporada-Hora
# Agrupar los datos por hora y estación, y sumar el número de bicicletas alquiladas
hourly = df.groupby(['Hour', 'Seasons'])['Rented Bike Count'].sum().unstack()

# Crear una figura con subgráficos para cada estación
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(30, 12), sharex=True, sharey=True)
fig.suptitle('Total Number of Bikes Rented by Hour and Season')

seasons = hourly.columns

for i, season in enumerate(seasons):
    ax = axs[i // 2, i % 2]  # Determinar la posición del subgráfico
    ax.bar(hourly.index, hourly[season], color='skyblue')
    ax.set_title(season)
    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel('Number of Bikes Rented')
    ax.grid(axis='y')

    # Añadir los valores en las barras
    for x, valor in enumerate(hourly[season]):
        ax.text(x, valor + 0.5, str(valor), ha='center', va='bottom')

    # Rotar y ajustar las etiquetas del eje x para que sean legibles
    ax.set_xticks(hourly.index)
    ax.set_xticklabels(hourly.index, rotation=45, ha='right')

# Ajustar el diseño para evitar el solapamiento
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Mostrar el gráfico
plt.show()

#Estadísticas descriptivas de Seasons
season_stats = df.groupby('Seasons')['Rented Bike Count'].agg(
    Rentas_Totales = 'sum',
    Promedio = 'mean',
    Desviación = 'std',
    Maximo = 'max',
    Minimo = 'min'
)

# Mostrar la tabla
print(season_stats)

# Agrupar los datos por Seasons y sumar la cantidad de bicicletas alquiladas
season_rentals = df.groupby('Seasons')['Rented Bike Count'].sum()

# Crear el gráfico de torta
plt.figure(figsize=(8,8))
plt.pie(season_rentals, labels=season_rentals.index, autopct='%1.1f%%', startangle=90, counterclock=False)
plt.title('Percentage of Bikes Rented by Season')
plt.show()

#Estadísticas descriptivas de Holiday
season_stats = df.groupby('Holiday')['Rented Bike Count'].agg(
    Rentas_Totales = 'sum',
    Promedio = 'mean',
    Desviación = 'std',
    Maximo = 'max',
    Minimo = 'min'
)

print(season_stats)

# Agrupar los datos por Holiday y sumar la cantidad de bicicletas alquiladas
season_rentals = df.groupby('Holiday')['Rented Bike Count'].sum()

# Crear el gráfico de torta
plt.figure(figsize=(8,8))
plt.pie(season_rentals, labels=season_rentals.index, autopct='%1.1f%%', startangle=90, counterclock=False)
plt.title('Percentage of Bikes Rented by Holiday')
plt.show()
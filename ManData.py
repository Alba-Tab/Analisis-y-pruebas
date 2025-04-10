import pandas as pd

personas =[
    {'nombre': "Juan", 'edad': 25},
    {'nombre': "Ana", 'edad': 30},
    {'nombre': "Luis", 'edad': 22},
    {'nombre': "Maria", 'edad': 28},
]

# Convertir la lista de diccionarios a un DataFrame de pandas
df = pd.DataFrame(personas)
# Guardar el DataFrame en un archivo CSV    
print(df)

#filtrar por edad mayor a 25
df_mayores_25 = df[df['edad'] > 25]
print(df_mayores_25)

# Supongamos que tenés una columna "ciudad"
df['ciudad'] = ['Santa Cruz', 'Cochabamba', 'La Paz', 'Santa Cruz']
promedios = df.groupby('ciudad')['edad'].mean()
print ('Promedios por ciudad:')
print(promedios)


# Guardar el DataFrame filtrado en un nuevo archivo CSV
df_mayores_25.to_csv('personas_mayores_25.csv', index=False)

# ahora vamos con numpy
import numpy as np

edades = df['edad'].values  # pasa a array numpy
print("Desviación estándar:", np.std(edades))
print("Mediana:", np.median(edades))

#filtramos personas por rango de edad
# por ejemplo entre 22 y 28
df_rango=df[(df['edad'] >= 22) & (df['edad'] <= 28)]
print("Personas entre 22 y 28 años:")
print(df_rango)
import pandas as pd

df= pd.read_csv('personas.csv')
# Mostrar los primeros datos
print("\n📋 Primeras entradas:")
print(df.head())
# Ordenar por nombre
print("\n🔠 Ordenado por nombre:")
print(df.sort_values(by='Nombre'))
# Ordenar por edad
print("\n🔢 Ordenado por edad:")
print(df.sort_values(by='Edad'))
# Promedio de edad
print("\n📈 Promedio de edades:")
print(df['Edad'].mean())
# Total de respuestas
print("\n📊 Número total de respuestas:")
print(len(df))

print("\n🔠 Nombres ordenados alfabéticamente:")
print(df.sort_values(by='Nombre')[['Nombre']])
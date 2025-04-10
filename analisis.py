import pandas as pd


#leer el archivo csv
df = pd.read_csv('historial_clima.csv')

# Mostrar los primeros datos
print("\n📋 Primeras entradas:")
print(df.head())

# Número total de consultas
print(f"\n🔢 Total de consultas: {len(df)}")

# Ciudades más consultadas
print("\n🏙️ Ciudades más consultadas:")
print(df['ciudad'].value_counts())

# Temperatura promedio por ciudad
print("\n🌡️ Temperatura promedio por ciudad:")
print(df.groupby('ciudad')['temperatura'].mean().round(2))

# Últimas consultas
print("\n🕓 Últimas consultas:")
print(df.tail(1))
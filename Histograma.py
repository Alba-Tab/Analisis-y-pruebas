import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('personas.csv')

#histograma de edades
#        columna de datos,rangos de edades, bordes de cada barras
plt.hist(df['Edad'], bins=3, edgecolor='black')
plt.xlabel('Edad')
plt.ylabel('Frecuencia de personas')
plt.title('Distribucion de Edades')

plt.show()

#guardar el histograma como imagen
plt.savefig('histograma_edades.png')
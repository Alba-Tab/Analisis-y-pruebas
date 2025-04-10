import csv,json
import os

if not os.path.exists('Personas.csv'):
    with open('personas.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Nombre', 'Edad', 'Ciudad'])
        writer.writerow(['Juan', 30, 'Madrid'])
        writer.writerow(['Ana', 25, 'Barcelona'])
        writer.writerow(['Luis', 35, 'Valencia'])
        writer.writerow(['Maria', 28, 'Sevilla'])
        writer.writerow(['Pedro', 40, 'Bilbao'])
        writer.writerow(['Laura', 32, 'Granada'])
        writer.writerow(['Javier', 29, 'Zaragoza'])

with open('personas.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    print("📋 Primeras entradas .csv:")
    next(reader)  # Saltar la cabecera
    for row in reader:
        print(row)
#trabajando con json

data=[{'nombre':'alba','edad':23,'ciudad':'madrid'},
        {'nombre':'gar','edad':54,'ciudad':'Valencia'},    
        {'nombre':'marta','edad':45,'ciudad':'Barcelona'},
        {'nombre':'pablo','edad':23,'ciudad':'Bilbao'},
        {'nombre':'laura','edad':34,'ciudad':'Granada'},
        {'nombre':'javier','edad':29,'ciudad':'Zaragoza'}]
        

with open('datos.json', mode='w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

with open('datos.json', mode='r', encoding='utf-8') as f:
    data = json.load(f)
    print("\n📋 Primeras entradas .json:")
    for item in data:
        print(item)
#agregando datos a un json
with open('datos.json', mode='r', encoding='utf-8') as f:
    data = json.load(f)
data.append({'nombre':'marta','edad':45,'ciudad':'Barcelona'})
with open('datos.json', mode='w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
with open('datos.json', mode='r', encoding='utf-8') as f:
    data = json.load(f)
    print("\n📋 Datos actualizados en .json:")
    for item in data:
        print(item)
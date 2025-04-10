from flask import Flask, request, jsonify
import requests
import logging
import csv
from datetime import datetime
import os

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("clima.log"),
        logging.StreamHandler()
    ]
)

# Configurar CSV
CSV_FILENAME = 'historial_clima.csv'
# Si el archivo no existe, escribimos la cabecera
if not os.path.exists(CSV_FILENAME):
    with open(CSV_FILENAME, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['fecha_hora', 'ciudad', 'temperatura', 'descripcion'])

app = Flask(__name__)
API_KEY = '08e37084880be7b13f4465cf4142efb4'  # Tu API key de OpenWeatherMap

@app.route('/clima', methods=['GET'])
def clima():
    ciudad = request.args.get('ciudad')
    
    if not ciudad:
        logging.warning("Consulta sin parámetro 'ciudad'")
        return jsonify({'error': 'Falta el parámetro ciudad'}), 400

    logging.info(f"Consulta recibida para la ciudad: {ciudad}")

    url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es'
    
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logging.error(f"Ciudad no encontrada o error HTTP ({ciudad}): {e}")
        return jsonify({'error': 'Ciudad no encontrada'}), 404
    except Exception as e:
        logging.critical(f"Error inesperado al consultar clima: {e}")
        return jsonify({'error': 'Error interno del servidor'}), 500

    data = r.json()
    resultado = {
        'ciudad': ciudad,
        'temperatura': data['main']['temp'],
        'descripcion': data['weather'][0]['description']
    }

    logging.info(f"Respuesta enviada para {ciudad}: {resultado}")

    # Guardar en CSV
    with open(CSV_FILENAME, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ciudad,
            resultado['temperatura'],
            resultado['descripcion']
        ])

    return jsonify(resultado)

if __name__ == '__main__':
    logging.info("Servidor Flask iniciado")
    app.run(debug=True)

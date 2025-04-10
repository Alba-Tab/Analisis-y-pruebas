# 🧪 Proyecto: API del Clima + Registro de Encuestas

Este proyecto combina una API con Flask para consultar el clima y un sistema de registro de encuestas que almacena datos en archivos `.csv` y `.json`. Además, permite analizar los datos usando `pandas`.
Tambien usamos `numpy`
---

## 🚀 Cómo iniciar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/tu-proyecto.git
cd tu-proyecto
```

### 2. Crear entorno virtual y activarlo

```bash
python -m venv env
# Activar entorno en Linux/macOS
source env/bin/activate
# Activar entorno en Windows
env\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Si no tenés el archivo `requirements.txt`, también podés instalar manualmente:

```bash
pip install flask requests pandas
```
>Tambien luego puedes crear tu archivo requirements con:
```
pip freeze > requirements.txt
```
---

## 🧪 Ejecutar la API de clima

```bash
python app.py
```

Probar la API desde consola:

```bash
curl "http://127.0.0.1:5000/clima?ciudad=La%20Paz"
```

O abrí esta URL en tu navegador:  
[http://127.0.0.1:5000/clima?ciudad=La%20Paz](http://127.0.0.1:5000/clima?ciudad=La%20Paz)

---

## 📝 Registro de encuestas (CSV y JSON)

El archivo `registro.py` registra una persona con su nombre y edad, y guarda los datos en:

- `personas.csv` → para análisis con pandas
- `personas.json` → respaldo estructurado

Podés modificar `registro.py` para hacerlo interactivo con `input()`.

---

## 📊 Análisis con pandas

El script `analisis.py` permite:

- Ver los primeros registros
- Ordenar por nombre o edad
- Calcular el promedio de edad
- Mostrar la cantidad total de respuestas

### Ejemplo de uso:

```bash
python analisis.py
```

---

## 📁 Estructura recomendada

```
📁 tu-proyecto/
├── app.py
├── registro.py
├── analisis.py
├── personas.csv
├── personas.json
├── clima.log
├── requirements.txt
└── README.md
```

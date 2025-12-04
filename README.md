# Análisis Interactivo de Vehículos en Venta (USA)

## 📌 Descripción del proyecto
Esta aplicación web, desarrollada con **Streamlit**, permite analizar de forma visual e interactiva un conjunto de datos real de anuncios de vehículos en venta en Estados Unidos.  
El objetivo es ofrecer al usuario herramientas intuitivas para explorar precios, kilometrajes, años de modelo y tipos de vehículos, todo a través de gráficos dinámicos y filtros personalizables.

Además, la aplicación integra estadísticas clave y visualizaciones que permiten entender mejor el comportamiento del mercado automotriz.

## 🚗 ¿Qué puedes hacer en la aplicación?

### 🔍 Filtros interactivos
- Seleccionar un **rango de años** del modelo.
- Establecer un **rango de precios** según presupuesto.
- Elegir un **tipo de vehículo** (SUV, sedan, pickup, etc.).

### 📊 Estadísticas automáticas
La app calcula dinámicamente según los filtros:
- Total de vehículos disponibles.
- Precio **promedio**, **mínimo** y **máximo**.
- Kilometraje promedio.

### 📈 Visualizaciones disponibles
- Histograma del kilometraje.
- Histograma del año del modelo.
- Boxplot de precios por tipo de vehículo.

### 📁 Contexto del dataset
El dataset contiene información real de anuncios publicados en plataformas de venta de vehículos en Estados Unidos.  
Incluye columnas como:
- `price`
- `model_year`
- `odometer`
- `type`
- `fuel`
- `transmission`

Esto permite realizar análisis exploratorios útiles para compradores, vendedores o entusiastas del mercado automotriz.

## 🛠 Tecnologías utilizadas
- Python  
- Pandas  
- Plotly  
- Streamlit  


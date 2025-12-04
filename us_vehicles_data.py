import pandas as pd
import plotly.express as px
import streamlit as st

# ---------------------------------------------------------
# TÍTULO Y DESCRIPCIÓN GENERAL
# ---------------------------------------------------------
st.title("🚗 Análisis Interactivo de Vehículos en Venta (USA)")
st.write("""
Esta aplicación permite explorar un conjunto de datos reales sobre vehículos en venta en Estados Unidos.  
Puedes filtrar por año, precio y tipo de vehículo, y visualizar estadísticas y gráficos interactivos.
""")

# ---------------------------------------------------------
# CARGA DEL DATASET
# ---------------------------------------------------------
try:
    car_data = pd.read_csv("vehicles_us.csv")

    # Manejo de valores nulos (recomendación del revisor)
    car_data = car_data.dropna(subset=["price", "model_year", "odometer"])

    st.success("Los datos se han cargado correctamente.")

except Exception as e:
    st.error("Error al cargar el archivo.")
    st.stop()

# ---------------------------------------------------------
# DESCRIPCIÓN DEL DATASET
# ---------------------------------------------------------
st.subheader("📁 Descripción del dataset")
st.write("""
El dataset contiene información de vehículos publicados para la venta.  
Incluye atributos como precio, tipo, kilometraje, año del modelo y otros datos relevantes del anuncio.
""")

# ---------------------------------------------------------
# FILTROS INTERACTIVOS
# ---------------------------------------------------------
st.subheader("🔍 Filtros de búsqueda")

col1, col2 = st.columns(2)

with col1:
    year_min = int(car_data["model_year"].min())
    year_max = int(car_data["model_year"].max())
    year_range = st.slider("Selecciona rango de años", year_min, year_max, (year_min, year_max))

with col2:
    price_min = int(car_data["price"].min())
    price_max = int(car_data["price"].max())
    price_range = st.slider("Selecciona rango de precios ($)", price_min, price_max, (price_min, price_max))

# Tipo de vehículo
vehicle_types = ["Todos"] + sorted(car_data["type"].dropna().unique().tolist())
selected_type = st.selectbox("Tipo de vehículo", vehicle_types)

# ---------------------------------------------------------
# APLICACIÓN DE FILTROS
# ---------------------------------------------------------
filtered = car_data[
    (car_data["model_year"].between(year_range[0], year_range[1])) &
    (car_data["price"].between(price_range[0], price_range[1]))
]

if selected_type != "Todos":
    filtered = filtered[filtered["type"] == selected_type]

# ---------------------------------------------------------
# ESTADÍSTICAS PRINCIPALES
# ---------------------------------------------------------
st.subheader("📊 Estadísticas generales")

st.write(f"**Total de vehículos encontrados:** {len(filtered)}")

if len(filtered) > 0:
    colA, colB, colC = st.columns(3)

    with colA:
        st.metric("Precio promedio", f"${int(filtered['price'].mean()):,}")
        st.metric("Precio mínimo", f"${int(filtered['price'].min()):,}")

    with colB:
        st.metric("Precio máximo", f"${int(filtered['price'].max()):,}")
        st.metric("Kilometraje promedio", f"{int(filtered['odometer'].mean()):,} mi")

    with colC:
        st.metric("Año más común", int(filtered["model_year"].mode()[0]))

# ---------------------------------------------------------
# GRÁFICOS
# ---------------------------------------------------------
st.subheader("📈 Visualizaciones")

# Histograma de kilometraje
if st.button("Mostrar histograma de kilometraje"):
    fig = px.histogram(filtered, x="odometer", title="Distribución de kilometraje")
    st.plotly_chart(fig, use_container_width=True)

# Boxplot por tipo
if st.checkbox("Mostrar boxplot de precios por tipo de vehículo"):
    fig2 = px.box(filtered, x="type", y="price", title="Precio por tipo de vehículo")
    st.plotly_chart(fig2, use_container_width=True)

# Histograma de años
if st.checkbox("Mostrar histograma de años del modelo"):
    fig3 = px.histogram(filtered, x="model_year", title="Distribución por año del modelo")
    st.plotly_chart(fig3, use_container_width=True)
# 
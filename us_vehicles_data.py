import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la app
st.title("Análisis de vehículos en venta (USA)")

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')
st.success("Archivo cargado correctamente")

# --- FILTROS INTERACTIVOS ---
st.sidebar.header("Filtros de vehículos")

# Rango de años
min_year = int(car_data['model_year'].min())
max_year = int(car_data['model_year'].max())
year_range = st.sidebar.slider("Rango de año del modelo", min_year, max_year, (min_year, max_year))

# Rango de precio
min_price = int(car_data['price'].min())
max_price = int(car_data['price'].max())
price_range = st.sidebar.slider("Rango de precio ($)", min_price, max_price, (min_price, max_price))

# Tipo de vehículo
vehicle_types = car_data['type'].dropna().unique()
selected_type = st.sidebar.selectbox("Tipo de vehículo", options=["Todos"] + list(vehicle_types))

# --- FILTRAR DATOS SEGÚN LOS CRITERIOS ---
filtered_data = car_data[
    (car_data['model_year'] >= year_range[0]) & (car_data['model_year'] <= year_range[1]) &
    (car_data['price'] >= price_range[0]) & (car_data['price'] <= price_range[1])
]

if selected_type != "Todos":
    filtered_data = filtered_data[filtered_data['type'] == selected_type]

# --- ESTADÍSTICAS RÁPIDAS ---
st.subheader("Estadísticas rápidas")
st.write(f"Total de vehículos cargados: {filtered_data.shape[0]}")
st.write(f"Precio promedio: ${filtered_data['price'].mean():,.0f}")
st.write(f"Precio mínimo: ${filtered_data['price'].min():,.0f}")
st.write(f"Precio máximo: ${filtered_data['price'].max():,.0f}")
st.write(f"Kilometraje promedio: {filtered_data['odometer'].mean():,.0f} km")

# --- BOTÓN PARA HISTOGRAMA ---
hist_button = st.button('Construir histograma de kilometraje')
if hist_button:
    st.write('Histograma de kilometraje de los vehículos filtrados')
    fig_hist = px.histogram(filtered_data, x="odometer", nbins=30)
    st.plotly_chart(fig_hist, use_container_width=True)

# --- BOXPLOT DE PRECIOS POR TIPO DE VEHÍCULO ---
st.subheader("Boxplot de precios por tipo de vehículo")
fig_box = px.box(filtered_data, x="type", y="price", points="all", color="type")
st.plotly_chart(fig_box, use_container_width=True)

# --- HISTOGRAMA DE AÑOS DE MODELOS ---
st.subheader("Histograma de años de los modelos")
fig_year = px.histogram(filtered_data, x="model_year", nbins=20)
st.plotly_chart(fig_year, use_container_width=True)

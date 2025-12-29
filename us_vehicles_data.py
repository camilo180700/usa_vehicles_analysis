import pandas as pd
import plotly.express as px
import streamlit as st

# ---------------------------------------------------------
# TITLE AND GENERAL DESCRIPTION
# ---------------------------------------------------------
st.title("🚗 Interactive Analysis of Vehicles for Sale (USA)")
st.write("""
This application allows users to explore a real dataset of vehicles for sale in the United States.  
You can filter the data by model year, price range, and vehicle type, and visualize key statistics 
and interactive charts.
""")

# ---------------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------------
try:
    car_data = pd.read_csv("vehicles_us.csv")

    # Handle missing values (recommended for data quality)
    car_data = car_data.dropna(subset=["price", "model_year", "odometer"])

    st.success("Data loaded successfully.")

except Exception:
    st.error("Error loading the dataset. Please check the file path.")
    st.stop()

# ---------------------------------------------------------
# DATASET DESCRIPTION
# ---------------------------------------------------------
st.subheader("📁 Dataset Overview")
st.write("""
The dataset contains information about vehicles listed for sale.  
It includes attributes such as price, vehicle type, mileage, model year,
and other relevant details from the listings.
""")

# ---------------------------------------------------------
# INTERACTIVE FILTERS
# ---------------------------------------------------------
st.subheader("🔍 Search Filters")

col1, col2 = st.columns(2)

with col1:
    year_min = int(car_data["model_year"].min())
    year_max = int(car_data["model_year"].max())
    year_range = st.slider(
        "Select model year range",
        year_min,
        year_max,
        (year_min, year_max)
    )

with col2:
    price_min = int(car_data["price"].min())
    price_max = int(car_data["price"].max())
    price_range = st.slider(
        "Select price range ($)",
        price_min,
        price_max,
        (price_min, price_max)
    )

# Vehicle type filter
vehicle_types = ["All"] + sorted(car_data["type"].dropna().unique().tolist())
selected_type = st.selectbox("Vehicle type", vehicle_types)

# ---------------------------------------------------------
# APPLY FILTERS
# ---------------------------------------------------------
filtered_data = car_data[
    (car_data["model_year"].between(year_range[0], year_range[1])) &
    (car_data["price"].between(price_range[0], price_range[1]))
]

if selected_type != "All":
    filtered_data = filtered_data[filtered_data["type"] == selected_type]

# ---------------------------------------------------------
# KEY STATISTICS
# ---------------------------------------------------------
st.subheader("📊 Key Statistics")

st.write(f"**Total vehicles found:** {len(filtered_data)}")

if len(filtered_data) > 0:
    colA, colB, colC = st.columns(3)

    with colA:
        st.metric("Average price", f"${int(filtered_data['price'].mean()):,}")
        st.metric("Minimum price", f"${int(filtered_data['price'].min()):,}")

    with colB:
        st.metric("Maximum price", f"${int(filtered_data['price'].max()):,}")
        st.metric("Average mileage", f"{int(filtered_data['odometer'].mean()):,} mi")

    with colC:
        st.metric(
            "Most common model year",
            int(filtered_data["model_year"].mode()[0])
        )

# ---------------------------------------------------------
# VISUALIZATIONS
# ---------------------------------------------------------
st.subheader("📈 Visualizations")

# Mileage histogram
if st.button("Show mileage distribution"):
    fig = px.histogram(
        filtered_data,
        x="odometer",
        title="Mileage Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

# Price by vehicle type
if st.checkbox("Show price distribution by vehicle type"):
    fig2 = px.box(
        filtered_data,
        x="type",
        y="price",
        title="Price by Vehicle Type"
    )
    st.plotly_chart(fig2, use_container_width=True)

# Model year histogram
if st.checkbox("Show model year distribution"):
    fig3 = px.histogram(
        filtered_data,
        x="model_year",
        title="Model Year Distribution"
    )
    st.plotly_chart(fig3, use_container_width=True)

import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.title("AI Smart Irrigation System")

st.write("Enter farm details")

# 1 Soil Type
soil_type = st.selectbox(
"Soil Type",
["Clay","Loamy","Sandy","Silt"]
)

# 2 Soil pH
soil_ph = st.number_input("Soil pH", value=6.5)

# 3 Soil Moisture
soil_moisture = st.number_input("Soil Moisture", value=30.0)

# 4 Organic Carbon
organic_carbon = st.number_input("Organic Carbon", value=0.5)

# 5 Electrical Conductivity
electrical_conductivity = st.number_input("Electrical Conductivity", value=0.3)

# 6 Temperature
temperature = st.number_input("Temperature (°C)", value=25.0)

# 7 Humidity
humidity = st.number_input("Humidity", value=50.0)

# 8 Rainfall
rainfall = st.number_input("Rainfall (mm)", value=500.0)

# 9 Sunlight Hours
sunlight = st.number_input("Sunlight Hours", value=8.0)

# 10 Wind Speed
wind_speed = st.number_input("Wind Speed (km/h)", value=5.0)

# 11 Crop Type
crop_type = st.selectbox(
"Crop Type",
["Cotton","Maize","Potato","Rice","Sugarcane","Wheat"]
)

# 12 Crop Growth Stage
growth_stage = st.selectbox(
"Crop Growth Stage",
["Sowing","Vegetative","Flowering","Harvest"]
)

# 13 Season
season = st.selectbox(
"Season",
["Kharif","Rabi","Zaid"]
)

# 14 Irrigation Type
irrigation_type = st.selectbox(
"Irrigation Type",
["Rainfed","Canal","Drip","Sprinkler"]
)

# 15 Water Source
water_source = st.selectbox(
"Water Source",
["Reservoir","River","Rainwater","Groundwater"]
)

# 16 Field Area
field_area = st.number_input("Field Area (hectare)", value=1.0)

# 17 Mulching Used
mulching_used = st.selectbox(
"Mulching Used",
["Yes","No"]
)

# 18 Previous Irrigation
previous_irrigation = st.number_input("Previous Irrigation (mm)", value=20.0)

# 19 Region
region = st.selectbox(
"Region",
["North","South","East","West","Central"]
)


# manual encoding (must match training)

soil_map = {"Clay":0,"Loamy":1,"Sandy":2,"Silt":3}

crop_map = {"Cotton":0,"Maize":1,"Potato":2,"Rice":3,"Sugarcane":4,"Wheat":5}

growth_stage_map = {
"Sowing":0,
"Vegetative":1,
"Flowering":2,
"Harvest":3
}

season_map = {"Kharif":0,"Rabi":1,"Zaid":2}

irrigation_type_map = {
"Rainfed":0,
"Canal":1,
"Drip":2,
"Sprinkler":3
}

water_source_map = {
"Reservoir":0,
"River":1,
"Rainwater":2,
"Groundwater":3
}

mulching_map = {"No":0,"Yes":1}

region_map = {"North":0,"South":1,"Central":2,"East":3,"West":4}

irrigation_result_map = {
0:"Low",
1:"Medium",
2:"High"
}


if st.button("Predict Irrigation Need"):

    input_dict = {

        "Soil_Type": soil_map[soil_type],
        "Soil_pH": soil_ph,
        "Soil_Moisture": soil_moisture,
        "Organic_Carbon": organic_carbon,
        "Electrical_Conductivity": electrical_conductivity,
        "Temperature_C": temperature,
        "Humidity": humidity,
        "Rainfall_mm": rainfall,
        "Sunlight_Hours": sunlight,
        "Wind_Speed_kmh": wind_speed,
        "Crop_Type": crop_map[crop_type],
        "Crop_Growth_Stage": growth_stage_map[growth_stage],
        "Season": season_map[season],
        "Irrigation_Type": irrigation_type_map[irrigation_type],
        "Water_Source": water_source_map[water_source],
        "Field_Area_hectare": field_area,
        "Mulching_Used": mulching_map[mulching_used],
        "Previous_Irrigation_mm": previous_irrigation,
        "Region": region_map[region]

    }

    input_df = pd.DataFrame([input_dict])

    input_df = input_df[columns]

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)

    result = irrigation_result_map[prediction[0]]

    if result == "High":
        st.error("High irrigation required")

    elif result == "Medium":
        st.warning("Moderate irrigation required")

    else:
        st.success("Low irrigation required")
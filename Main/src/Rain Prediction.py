import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

scaler = joblib.load('Main/src/model/scaler.joblib')
model = tf.keras.models.load_model('Main/src/model/fnn_model.h5')
encoders = joblib.load('Main/src/model/encoders.pkl')
feature_columns = joblib.load("Main/src/model/feature_columns.pkl")

def encode_data(df, encoders):
    for col, encoder in encoders.items():
        if col in df.columns:
            df[col] = df[col].apply(lambda x: encoder.transform([x])[0] if x in encoder.classes_ else -1)
    return df

def get_temp_weight(temp):
    if temp < 15:
        return 0.4
    elif 15 <= temp <= 25:
        return 0.0
    else:
        return -0.4

def get_humidity_weight(humidity):
    if humidity > 80:
        return 0.3
    elif 60 <= humidity <= 80:
        return 0.0
    else:
        return -0.3

def get_pressure_weight(pressure):
    if pressure < 1000:
        return 0.3
    elif 1000 <= pressure <= 1020:
        return 0.0
    else:
        return -0.3

def get_wind_weight(wind_speed, wind_direction):
    return 0.2 if wind_speed > 30 else 0.0

def predict_rain(data):
    data_encoded = encode_data(data, encoders)
    data_encoded = data_encoded[feature_columns]
    data_scaled = scaler.transform(data_encoded)
    prediction = model.predict(data_scaled)

    temp_weight = get_temp_weight(data['MaxTemp'][0])
    humidity_weight = get_humidity_weight(data['Humidity9am'][0])
    pressure_weight = get_pressure_weight(data['Pressure9am'][0])
    wind_weight = get_wind_weight(data['WindSpeed9am'][0], data['WindGustDir'][0])

    weighted_prediction = prediction[0] + (temp_weight + humidity_weight + pressure_weight + wind_weight) * 0.5

    return "Hujan Besok" if weighted_prediction > 0.5 else "Tidak Hujan Besok"

st.title("☀️ Rain Prediction System ⛈️")
st.write("Masukan Data untuk Memprediksi Hujan Esok Hari")

# Input fields with additional descriptions
min_temp = st.number_input('Min Temp (\u00b0C)', value=15.0)
st.write("❄️ Temperature yang rendah cenderung meningkatkan kemungkinan hujan, suhu di bawah 15°C seringkali memicu hujan.")

max_temp = st.number_input('Max Temp (\u00b0C)', value=25.0)
st.write("🌞 Suhu yang lebih tinggi cenderung mengurangi kemungkinan hujan sementara sekitar 25°C cukup stabil.")

rainfall = st.number_input('Rainfall (mm)', value=0.0)
st.write("🌧️ Curah hujan yang tinggi dapat mempengaruhi keberlangsungan cuaca.")

evaporation = st.number_input('Evaporation (mm)', value=4.0)
st.write("💧 Evaporasi yang tinggi berarti kelembaban lebih rendah, hal tersebut dapat mengurangi kemungkinan hujan.")

sunshine = st.number_input('Sunshine (hours)', value=8.0)
st.write("🌅 Cahaya matahari yang banyak berhubungan dengan cuaca cerah, semakin banyak cahaya maka lebih sedikit hujan.")

wind_gust_dir = st.selectbox('Wind Gust Direction', options=['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
st.write("🌬️ Arah angin bisa mempengaruhi hujan. Angin dari laut sering membawa kelembaban dan hujan.")

wind_gust_speed = st.number_input('Wind Gust Speed (km/h)', value=40.0)
st.write("🌪️ Kecepatan angin yang tinggi bisa menunjukkan cuaca buruk atau hujan yang mendekat.")

wind_dir_9am = st.selectbox('Wind Direction at 9am', options=['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
st.write("💨 Angin yang datang dari laut bisa membawa hujan.")

wind_speed_9am = st.number_input('Wind Speed at 9am (km/h)', value=10.0)
st.write("🌬️ Kecepatan angin di pagi hari yang lebih tinggi bisa menandakan cuaca yang buruk atau hujan.")

# Adding Wind Direction at 3pm and Wind Speed at 3pm
wind_dir_3pm = st.selectbox('Wind Direction at 3pm', options=['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
st.write("💨 Arah angin sore hari bisa menunjukkan perubahan cuaca dan arah angin dari laut lebih mungkin membawa hujan.")

wind_speed_3pm = st.number_input('Wind Speed at 3pm (km/h)', value=12.0)
st.write("🌬️ Kecepatan angin sore hari yang lebih tinggi dapat menandakan hujan yang akan datang.")

humidity_9am = st.number_input('Humidity at 9am (%)', value=60.0)
st.write("💧 Kelembaban tinggi di pagi hari (di atas 80%) meningkatkan kemungkinan hujan ⛈️.")

humidity_3pm = st.number_input('Humidity at 3pm (%)', value=55.0)
st.write("💦 Kelembaban sore hari yang tinggi juga meningkatkan kemungkinan hujan.")

pressure_9am = st.number_input('Pressure at 9am (hPa)', value=1010.0)
st.write("🌀 Tekanan udara rendah cenderung menunjukkan cuaca hujan. Perhatikan jika tekanannya lebih rendah dari 1000 hPa.")

pressure_3pm = st.number_input('Pressure at 3pm (hPa)', value=1012.0)
st.write("🌫️ Tekanan udara rendah bisa jadi tanda cuaca buruk atau hujan yang mendekat.")

temp_9am = st.number_input('Temp at 9am (\u00b0C)', value=18.0)
st.write("🌡️ Suhu rendah di pagi hari cenderung meningkatkan peluang hujan ⛈️.")

temp_3pm = st.number_input('Temp at 3pm (\u00b0C)', value=22.0)
st.write("☀️ Suhu yang lebih tinggi di sore hari menurunkan kemungkinan hujan.")

data = pd.DataFrame([{
    'MinTemp': min_temp,
    'MaxTemp': max_temp,
    'Rainfall': rainfall,
    'Evaporation': evaporation,
    'Sunshine': sunshine,
    'WindGustDir': wind_gust_dir,
    'WindGustSpeed': wind_gust_speed,
    'WindDir9am': wind_dir_9am,
    'WindDir3pm': wind_dir_3pm,
    'WindSpeed9am': wind_speed_9am,
    'WindSpeed3pm': wind_speed_3pm,
    'Humidity9am': humidity_9am,
    'Humidity3pm': humidity_3pm,
    'Pressure9am': pressure_9am,
    'Pressure3pm': pressure_3pm,
    'Temp9am': temp_9am,
    'Temp3pm': temp_3pm
}])

data = data.reindex(columns=feature_columns, fill_value=0)

if st.button('Prediksi Hujan Besok'):
    result = predict_rain(data)
    if result == "Hujan Besok":
        st.markdown(f"""
        <div style="background-color: #6c757d; color: #ffffff; padding: 20px; border-radius: 8px;">
            <h3>Rain Alert for Tomorrow ⛈️</h3>
            <p>Perkiraan hujan pada sekitar pukul 12:00 PM.</p>
            <p><strong>Saran:</strong></p>
            <ul>
                <li>Bawalah jas hujan atau payung 🧥</li>
                <li>Berkendaralah dengan hati-hati 🚘</li>
                <li>Selalu waspada terhadap angin yang kencang 🌪️</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background-color: #ffc107; color: #ffffff; padding: 20px; border-radius: 8px;">
            <h3>No Rain Expected Tomorrow ☀️</h3>
            <p>Perkiraan cuaca cerah sepanjang hari.</p>
            <p><strong>Saran:</strong></p>
            <ul>
                <li>Anda dapat merencanakan aktivitas outdoor dengan tenang 🌳</li>
                <li>Jangan lupa untuk memakai sunscreen jika beraktivitas di luar 🧴</li>
                <li>Pastikan tetap terhidrasi dengan baik 💧</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

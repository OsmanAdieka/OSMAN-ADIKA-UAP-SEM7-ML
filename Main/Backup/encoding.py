import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import joblib

# Membaca dataset
df = pd.read_csv('Main\src\dataset\weatherAUS.csv')  # Sesuaikan dengan path dataset Anda

# Menangani missing values
categorical_columns = df.select_dtypes(include=[object]).columns
for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Pisahkan fitur kategorikal
categorical_features = ['WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday']

# Inisialisasi encoder
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

# Fit encoder
X_encoded = encoder.fit_transform(df[categorical_features])

# Simpan encoder
joblib.dump(encoder, 'encoder.joblib')

print("Encoder berhasil disimpan.")

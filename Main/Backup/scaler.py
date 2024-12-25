import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Membaca dataset
df = pd.read_csv('Main\src\dataset\weatherAUS.csv')  # Sesuaikan dengan path dataset Anda

# Menangani missing values untuk data numerik
numeric_columns = df.select_dtypes(include=[float, int]).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Pisahkan data numerik
X = df[numeric_columns]

# Inisialisasi scaler
scaler = StandardScaler()

# Fit scaler
X_scaled = scaler.fit_transform(X)

# Simpan scaler
joblib.dump(scaler, 'scaler.joblib')

print("Scaler berhasil disimpan.")

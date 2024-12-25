import joblib
from sklearn.preprocessing import LabelEncoder

# Daftar nilai kategori untuk masing-masing kolom
wind_gust_dir_values = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
wind_dir_9am_values = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
wind_dir_3pm_values = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

# Membuat encoder untuk WindGustDir
wind_gust_dir_encoder = LabelEncoder()
wind_gust_dir_encoder.fit(wind_gust_dir_values)
joblib.dump(wind_gust_dir_encoder, 'Main/src/model/wind_gust_dir_encoder.pkl')

# Membuat encoder untuk WindDir9am
wind_dir_9am_encoder = LabelEncoder()
wind_dir_9am_encoder.fit(wind_dir_9am_values)
joblib.dump(wind_dir_9am_encoder, 'Main/src/model/wind_dir_9am_encoder.pkl')

# Membuat encoder untuk WindDir3pm
wind_dir_3pm_encoder = LabelEncoder()
wind_dir_3pm_encoder.fit(wind_dir_3pm_values)
joblib.dump(wind_dir_3pm_encoder, 'Main/src/model/wind_dir_3pm_encoder.pkl')

print("Encoders untuk WindGustDir, WindDir9am, dan WindDir3pm berhasil dibuat dan disimpan.")

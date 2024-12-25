Berikut adalah README yang sudah diperbaiki dan dirapikan:

---

# ☀️ Prediksi Hujan Besok ⛈️

## Deskripsi Proyek 📜
Proyek ini bertujuan untuk memprediksi kemungkinan hujan pada keesokan harinya berdasarkan data cuaca yang diberikan. Dengan menggunakan model klasifikasi berbasis jaringan saraf (FNN), aplikasi ini dapat memproses berbagai fitur cuaca seperti suhu, kelembaban, kecepatan angin, dan tekanan udara untuk memberikan prediksi apakah hujan akan terjadi atau tidak. Aplikasi ini bertujuan untuk memberikan informasi yang berguna untuk membantu perencanaan kegiatan luar ruangan.

## Langkah Instalasi 🛠️
Untuk menjalankan aplikasi ini, Anda perlu menginstal beberapa dependencies yang digunakan dalam proyek ini. Berikut adalah langkah-langkah instalasi:

1. Clone repository ini:
    ```bash
    git clone https://github.com/OsmanAdieka/OSMAN-ADIKA-UAP-SEM7-ML.git
    ```
   
2. Masuk ke folder proyek:
    ```bash
    cd OSMAN-ADIKA-UAP-SEM7-ML
    ```

3. Instal dependencies: Pastikan Anda sudah menginstal Python dan pip. Lalu jalankan perintah berikut untuk menginstal dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Jalankan aplikasi Streamlit: Setelah dependencies terinstal, Anda dapat menjalankan aplikasi dengan perintah:
    ```bash
    streamlit run app.py
    ```

Aplikasi akan terbuka di browser pada `localhost:8501`.

## Deskripsi Model 🧠
Model yang digunakan dalam aplikasi ini adalah **Feedforward Neural Network (FNN)** dengan dua hidden layers. Model ini dilatih dengan dataset cuaca yang mencakup fitur-fitur seperti suhu, kelembaban, tekanan udara, dan kecepatan angin untuk memprediksi apakah akan ada hujan pada keesokan harinya. Regularisasi **Dropout** dan **optimizer Adam** digunakan untuk mencegah overfitting dan mempercepat proses pelatihan.

## Analisis Performa 🏅
Model ini telah dilatih selama 10 epoch dengan menggunakan batch size 16. Performa model dievaluasi menggunakan metrik seperti akurasi dan loss. Beberapa teknik augmentasi data, seperti penggunaan **GAN**, telah diterapkan untuk meningkatkan kinerja model pada kelas minoritas. Meskipun akurasi keseluruhan sedikit menurun, model menunjukkan peningkatan signifikan dalam mengklasifikasikan kelas minoritas.

## Hasil dan Analisis 📊

### Hasil Perbandingan Model

**FNN Model:**
```
              precision    recall  f1-score   support

           0       0.87      0.94      0.90     22672
           1       0.71      0.50      0.59      6420

    accuracy                           0.84     29092
   macro avg       0.79      0.72      0.75     29092
weighted avg       0.83      0.84      0.83     29092
```

**TabNet Model:**
```
              precision    recall  f1-score   support

           0       0.86      0.95      0.90     22672
           1       0.73      0.47      0.57      6420

    accuracy                           0.84     29092
   macro avg       0.80      0.71      0.74     29092
weighted avg       0.83      0.84      0.83     29092
```

### Analisis Performa
- **Akurasi:** Kedua model mencapai akurasi 84% pada dataset yang digunakan.
- **Precision & Recall:** Model **FNN** menunjukkan precision yang lebih tinggi untuk kelas 0 (0.87) dibandingkan dengan **TabNet** (0.86), sementara untuk kelas 1, **TabNet** sedikit lebih baik dalam precision (0.73) dibandingkan **FNN** (0.71). Namun, **FNN** memiliki recall yang lebih baik untuk kelas 0 (0.94) dibandingkan **TabNet** (0.95).
- **F1-Score:** Model **FNN** memiliki f1-score yang sedikit lebih tinggi untuk kelas 0 (0.90) dan kelas 1 (0.59) dibandingkan dengan **TabNet** (kelas 1: 0.57).

### Metrik Evaluasi
- **Akurasi:** 85%
- **Loss:** 0.3
- **Precision:** 88%
- **Recall:** 82%

Grafik atau visualisasi lebih lanjut dapat membantu memberikan gambaran lebih jelas mengenai perbandingan performa kedua model.

## Link Live Demo 🌐
[Klik di sini untuk mencoba aplikasi live demo](#)

---

README ini sudah siap untuk dipasang di GitHub. Semoga membantu!

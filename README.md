☀️ Prediksi Hujan Besok ⛈️
Deskripsi Proyek 📜
Proyek ini bertujuan untuk memprediksi kemungkinan hujan pada keesokan harinya berdasarkan data cuaca yang diberikan. Dengan menggunakan model klasifikasi berbasis jaringan saraf (FNN), aplikasi ini dapat memproses berbagai fitur cuaca seperti suhu, kelembaban, kecepatan angin, dan tekanan udara untuk memberikan prediksi apakah hujan akan terjadi atau tidak. Aplikasi ini bertujuan untuk memberikan informasi yang berguna untuk membantu perencanaan kegiatan luar ruangan.

Langkah Instalasi 🛠️
Untuk menjalankan aplikasi ini, Anda perlu menginstal beberapa dependencies yang digunakan dalam proyek ini. Berikut adalah langkah-langkah instalasi:

Clone repository ini:

bash
Copy code
git clone https://github.com/OsmanAdieka/OSMAN-ADIKA-UAP-SEM7-ML.git
Masuk ke folder proyek:

bash
Copy code
cd OSMAN-ADIKA-UAP-SEM7-ML
Instal dependencies: Pastikan Anda sudah menginstal python dan pip. Lalu jalankan perintah berikut untuk menginstal dependencies:

bash
Copy code
pip install -r requirements.txt
Jalankan aplikasi Streamlit: Setelah dependencies terinstal, Anda dapat menjalankan aplikasi dengan perintah:

bash
Copy code
streamlit run app.py
Aplikasi akan terbuka di browser pada localhost:8501.

Deskripsi Model 🧠
Model yang digunakan dalam aplikasi ini adalah Feedforward Neural Network (FNN) dengan dua hidden layers. Model ini dilatih dengan dataset cuaca yang mencakup fitur-fitur seperti suhu, kelembaban, tekanan udara, dan kecepatan angin untuk memprediksi apakah akan ada hujan pada keesokan harinya. Regularisasi Dropout dan optimizer Adam digunakan untuk mencegah overfitting dan mempercepat proses pelatihan.

Analisis Performa 🏅
Model ini telah dilatih selama 10 epoch dengan menggunakan batch size 16. Performa model dievaluasi menggunakan metrik seperti akurasi dan loss. Beberapa teknik augmentasi data, seperti penggunaan GAN, telah diterapkan untuk meningkatkan kinerja model pada kelas minoritas.

Hasil dan Analisis 📊
Hasil perbandingan model beserta metrik evaluasi dapat dilihat di bawah:

Metrik	Nilai
Akurasi	85%
Loss	0.3
Precision	88%
Recall	82%
Grafik di bawah ini menunjukkan perbandingan performa antara model dasar dan model setelah augmentasi data.


Link Live Demo 🌐

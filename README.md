# 🚴‍♂️ Dashboard Penyewaan Sepeda  

Dashboard ini dikembangkan menggunakan **Streamlit** untuk menganalisis dan memvisualisasikan data penyewaan sepeda berdasarkan berbagai faktor lingkungan dan kondisi cuaca.  

## 📌 Fitur Dashboard  
✅ **Tren Penyewaan Sepeda**: Menampilkan pola penyewaan berdasarkan hari kerja dan akhir pekan.  
✅ **Faktor Lingkungan**: Analisis hubungan antara suhu, kelembapan, dan kecepatan angin terhadap jumlah penyewaan.  
✅ **Pengaruh Kondisi Cuaca**: Melihat bagaimana kondisi cuaca (cerah, berkabut, hujan) mempengaruhi penyewaan sepeda.  
✅ **Filter Interaktif**: Memilih bulan dan hari kerja/akhir pekan untuk analisis yang lebih spesifik.

# 📌 Cara Menjalankan Dashboard
## 1️⃣ Clone Repository
Jika belum memiliki kode, clone repository ini terlebih dahulu:

```bash
git clone https://github.com/AlwanFauzi/dashboard-analisis-penyewaansepeda.git
cd dashboard-analisis-penyewaansepeda
```

## 2️⃣ Siapkan Virtual Environment (Opsional tapi Direkomendasikan)

```bash
conda create --name main-ds python=3.12
conda activate main-ds
```

## 3️⃣ Install Dependencies
Pastikan semua dependensi sudah terinstal dengan menjalankan perintah:

```bash
pip install -r requirements.txt
```

## 4️⃣ Jalankan Aplikasi Streamlit

```bash
streamlit run dashboard.py
```

🚀 Aplikasi akan berjalan di [http://localhost:8501](http://localhost:8501)

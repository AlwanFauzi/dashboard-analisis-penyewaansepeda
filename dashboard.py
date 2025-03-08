import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    # Sesuaikan dengan dataset yang digunakan
    df = pd.read_csv("day.csv")  # Ganti dengan path dataset yang sesuai
    return df

df = load_data()

# Judul Dashboard
st.title("📊 Dashboard Penyewaan Sepeda 🚴")

# **1. Distribusi Penyewaan Sepeda: Hari Kerja vs Akhir Pekan**
st.subheader("Distribusi Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
fig, ax = plt.subplots()
sns.boxplot(x=df['workingday'], y=df['cnt'], palette=['blue', 'orange'])
ax.set_xlabel('Tipe Hari (0=Akhir Pekan, 1=Hari Kerja)')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)

# **2. Tren Penyewaan Sepeda per Bulan**
st.subheader("Tren Penyewaan Sepeda per Bulan (2011-2012)")
fig, ax = plt.subplots()
sns.lineplot(x=df['mnth'], y=df['cnt'], hue=df['workingday'], marker='o', palette=['blue', 'orange'])
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)

# **3. Hubungan Faktor Lingkungan dengan Penyewaan Sepeda**
st.subheader("Hubungan Faktor Lingkungan dengan Penyewaan Sepeda")
col1, col2 = st.columns(2)

# Hubungan suhu dengan penyewaan sepeda
with col1:
    st.write("📈 Hubungan Suhu dengan Penyewaan Sepeda")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df['temp'], y=df['cnt'])
    ax.set_xlabel('Suhu Terstandarisasi')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

# Hubungan kelembapan dengan penyewaan sepeda
with col2:
    st.write("💦 Hubungan Kelembapan dengan Penyewaan Sepeda")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df['hum'], y=df['cnt'])
    ax.set_xlabel('Kelembapan')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

# Hubungan kecepatan angin dengan penyewaan sepeda
st.write("🌬️ Hubungan Kecepatan Angin dengan Penyewaan Sepeda")
fig, ax = plt.subplots()
sns.scatterplot(x=df['windspeed'], y=df['cnt'])
ax.set_xlabel('Kecepatan Angin Terstandarisasi')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# **4. Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda**
st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots()
sns.boxplot(x=df['weathersit'], y=df['cnt'], palette=['lightblue', 'gray', 'salmon'])
ax.set_xlabel('Kondisi Cuaca (1=Cerah, 2=Berkabut, 3=Hujan)')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# **Kesimpulan**
st.markdown("""
### 🔍 **Kesimpulan**
1. **Suhu berpengaruh signifikan** terhadap jumlah penyewaan sepeda. Semakin hangat, semakin banyak yang menyewa.
2. **Cuaca hujan menurunkan jumlah penyewaan secara drastis**.
3. **Hari kerja memiliki jumlah penyewaan yang lebih tinggi dibandingkan akhir pekan**.
4. **Kelembapan dan kecepatan angin tidak terlalu berpengaruh**, tetapi penyewaan sedikit lebih rendah pada kelembapan tinggi.
""")

st.write("🚴‍♂️ **Terima kasih telah menggunakan dashboard ini!**")

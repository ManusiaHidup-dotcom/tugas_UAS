import streamlit as st

st.title("Kalkulator Volume Bangun Ruang")
st.subheader("Nama: Yudhistira Baskoro Adi Admojo | NIM: 24.83.1094")
st.write("Aplikasi sederhana menghitung volume menggunakan Python & Streamlit")

bangun = st.selectbox(
    "Pilih Bangun Ruang",
    ("Kubus", "Balok", "Tabung")
)

if bangun == "Kubus":
    sisi = st.number_input("Masukkan panjang sisi", min_value=0.0)
    volume = sisi ** 3
    st.write(f"Volume Kubus = {volume}")

elif bangun == "Balok":
    panjang = st.number_input("Masukkan panjang", min_value=0.0)
    lebar = st.number_input("Masukkan lebar", min_value=0.0)
    tinggi = st.number_input("Masukkan tinggi", min_value=0.0)
    volume = panjang * lebar * tinggi
    st.write(f"Volume Balok = {volume}")

elif bangun == "Tabung":
    jari_jari = st.number_input("Masukkan jari-jari", min_value=0.0)
    tinggi = st.number_input("Masukkan tinggi", min_value=0.0)
    volume = 3.14 * (jari_jari ** 2) * tinggi
    st.write(f"Volume Tabung = {volume}")

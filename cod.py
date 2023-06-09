import streamlit as st
import pandas as pd

st.set_page_config(page_title='Perhitungan Kadar COD', page_icon=':memo:', layout='wide')

st.title('Perhitungan Kadar COD')

st.write('''
    Hallo! Website ini dibuat untuk memudahkan kamu dalam menghitung kadar COD sebelum melakukan analisa. Website ini sangat membantu dalam pengolahan data jika menjadi sebuah alat yang sangat berkembang pesat. Perkembangan ini membawa dampak positif bagi kampus yang berkembang''')

st.header('Pengertian COD')
st.write('''
    Chemical Oxygen Demand (COD) adalah metode analisis kimia yang digunakan untuk mengukur jumlah bahan organik yang teroksidasi dalam sampel air atau limbah cair. Metode ini digunakan sebagai indikator kualitas air untuk menentukan sejauh mana air tersebut tercemar oleh bahan-bahan organik terlarut.

Metode COD sering digunakan dalam pengujian kualitas air limbah, industri, dan lingkungan. Nilai COD dapat digunakan sebagai indikator awal untuk menentukan proses pengolahan air yang dibutuhkan sebelum dibuang ke lingkungan atau digunakan kembali.
''')

st.subheader('Kelompok 5')
st.write ('''
    Agnia Zahara (2230424) \n
    Arya Dhemas Pambudhi (2230435) \n
    Ghaniyyu Halmar Indrahani (2230442) \n
    Karira Anindya (2230447) \n
    Sekar Laras (2230470) \n''')

def cod_calculator(app_mode):
    if app_mode == "Calculate COD":
        st.header("Perhitungan Kadar COD")
        st.write("Masukkan nilai untuk menghitung Kadar COD")

        volume_blanko = st.number_input("Masukkan volume blanko (mL)")
        volume_pereaksi = st.number_input("Masukkan volume pereaksi (mL)")
        normalitas = st.number_input("Masukkan nilai normalitas (grek/mL)")
        berat_ekivalen_oksigen = st.number_input("Masukkan berat ekivalen oksigen (mL) (Tetapan dalam SNI 8000)")
        volume_sampel = st.number_input("Masukkan nilai volume sampel (mL)")

        if volume_sampel !=0:
            cod = (volume_blanko - volume_pereaksi) * normalitas * berat_ekivalen_oksigen / volume_sampel
            st.write(f"Nilai COD adalah {cod:.2f} mg/L") # add this line

def cod_calculator(app_mode):
    if app_mode == "Calculate cod":
        st.header("Calculate cod")
        st.write("Masukkan nilai untuk menghitung COD")

        # Add your input fields and calculations for cod here

app_mode = st.sidebar.selectbox("Pilih mode", ["Calculate COD", "Calculate cod"])
if app_mode == "Calculate COD":
    cod_calculator(app_mode)
elif app_mode == "Calculate COD":
    cod_calculator(app_mode)

    
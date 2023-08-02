import pickle
import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

model = pickle.load(open('prediksi_co2.sav', 'rb')) # manggil file sav nya, rb = read binary

# untuk menampilkan dataset
df = pd.read_excel('CO2 dataset.xlsx')

# coodingan dari ipynb untuk merubah tahun
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index(['Year'], inplace=True)

# untuk menentukan tahun yang akan di prediksi
st.title('Forecasting kualitas udara')
year = st.slider('TENTUKAN BATAS TAHUN UNTUK DI PREDIKSI ', 1, 30, step=1) # memiliki batas 30 tahun kedepan

# model prediksi
pred = model.forecast(year) # year mengambil dari slider
# untuk menghasilkan dari data frame nya atau datasetnya 
pred = pd.DataFrame(pred, columns=['CO2'])

if st.button("Predict "):
    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred) # untuk menampilkan table datfremnya
    with col2:
        fig, ax = plt.subplots() # untuk menampilkan grafiknya atau diagram plotnya
        df['CO2'].plot(style='--', color='green', legend=True, label='known') # sebelum di prediksi
        pred['CO2'].plot(color='blue', legend=True, label='prediction') # setelah di prediksi
        st.pyplot(fig)
# Ketika Anda menggunakan with statement, itu akan membuka suatu konteks atau sumber daya (seperti membuka file, koneksi database, atau penguncian suatu objek), melakukan operasi yang Anda perlukan dalam blok with, dan kemudian otomatis menutupnya setelah blok with selesai dieksekusi.
        
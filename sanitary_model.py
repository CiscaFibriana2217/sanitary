import pickle
import streamlit as st

# Membaca model
sanitary_model = pickle.load(open('sanitary_model.sav','rb'))

# Judul web
st.title('Tingkat Sanitasi pada Negara di Dunia')

# Membagi kolom
col1, col2 = st.columns(2)

with col1:
    Year = st.text_input('Input Nilai Tahun')

with col2:
    Country = st.text_input('Input Negara')

with col1:
    Residence_Area_Type = st.text_input('Input Residence Area Type')

with col2:
    Display_Value = st.text_input('Input Nilai Display Value')

with col1:
    WHO_region = st.text_input('Input WHO Region')

# Inisialisasi variabel untuk hasil prediksi
sanitary_level = ''

# Membuat tombol untuk prediksi
if st.button('Lihat Akurasi'):
    if Year and WHO_region and Country and Residence_Area_Type and Display_Value:
        sanitary_prediction = sanitary_model.predict([[Year, WHO_region, Country, Residence_Area_Type, Display_Value]])

        if sanitary_prediction[0] == 0:
            sanitary_predict = 'Tingkat Sanitasi Rendah'
        else:
            sanitary_predict = 'Tingkat Sanitasi Tinggi'

        st.success(sanitary_predict)
    else:
        st.error("Harap isi semua kolom input.")

    st.success()
    

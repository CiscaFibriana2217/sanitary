import pickle
import streamlit as st

# membaca model
sanitary_model = pickle.load(open('sanitary_model.sav','rb'))

# Path ke file model
file_path = 'sanitary_model.sav'

# Membuka file dan memuat model dengan aman
try:
    with open(file_path, 'rb') as file:
        sanitary_model = pickle.load(file)
        print("Model loaded successfully!")
except FileNotFoundError:
    print(f"File {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

    
# judul web
st.title('Tingkat Sanitasi pada Negara di Dunia')

# membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Year = st.text_input ('Input Nilai Tahun')

with col2 :
    Country = st.text_input ('Input Negara')

with col1 :
    Residence_Area_Type = st.text_input ('Input Residence Area Type')

with col2 :
    Display_Value = st.text_input ('Input Nilai Display Value')


# code untuk prediksi
sanitary_level = ''

# membuat tombol untuk prediksi
if st.button('Lihat Akurasi'):
    sanitary_prediction = sanitary_model.predict([[Year,'WHO region','Country','Residence Area Type','Display Value']])

    if(sanitary_prediction[0] == 0):
        sanitary_predict = 'Tingkat Sanitasi Rendah'
    else :
        sanitary_predict = 'Tingkat Sanitasi Tinggi'

    st.success()
    

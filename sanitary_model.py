import pickle
import streamlit as st

# Fungsi utama untuk aplikasi Streamlit
def main():
    st.title("Prediksi Tingkat Sanitasi")

    # Memuat data dan melatih model
    data = load_data()
    model, scaler, label_encoders = train_model(data)

    # Input pengguna
    st.header("Input Data")
    year = st.number_input("Tahun", min_value=2000, max_value=2023, value=2020)
    country = st.selectbox("Negara", data['Country'].unique())
    residence_area = st.selectbox("Area Tempat Tinggal", data['Residence Area Type'].unique())
    display_value = st.number_input("Nilai Display", min_value=0.0, max_value=100.0, value=50.0)

    # Melakukan prediksi saat tombol diklik
    if st.button("Prediksi"):
        input_data = (year, country, residence_area, display_value)
        result = predict(model, scaler, label_encoders, input_data)
        
        if result < 0.5:
            st.write('Tingkat Sanitasi Rendah')
        else:
            st.write('Tingkat Sanitasi Tinggi')

# Menjalankan aplikasi Streamlit
if __name__ == "__main__":
    main()


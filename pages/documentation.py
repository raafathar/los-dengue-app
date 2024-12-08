import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page


def main():

    st.set_page_config(
        page_title="Deteksi Penyakit Dini Anemia Pada Ibu Hamil",
        page_icon="👩‍👦",
        initial_sidebar_state="collapsed")

    st.markdown(
        """
        <style>
            [data-testid="collapsedControl"] {
                display: none
            }
        </style>
        """, unsafe_allow_html=True,
    )

    if st.button("👈 Kembali ke Halaman Utama"):
        switch_page("app")

    st.header("Dokumentasi")
    st.write("Berikut merupakan beberapa dokumentasi riset yang mendasari aplikasi ini dapat dibuat")
    # st.image("assets/get-started.png")

    tab1, tab2= st.tabs(
        ["(1) Ringkasan Penelitian", "(2) Tentang"])

    with tab1:

        st.subheader("1.1 Latar Belakang")
        st.write(
            " Demam berdarah adalah penyakit arbovirus yang ditularkan melalui gigitan nyamuk, terdapat 2 jenis nyamuk yang dapat menularkan penyakit demam berdarah antara lain Aedes Albopictus dan Aedes Aegypti. Demam berdarah telah dialami oleh jutaan orang terutama di negara tropis atau yang memiliki iklim lebih hangat (Wijayanti et al., 2025). Penderita demam berdarah ini seringkali diharuskan untuk menjalani rawat inap beberapa hari di rumah sakit. Lama rawat inap pasien demam berdarah sangat bervariatif sesuai dengan kondisi demam yang dialami, rata-rata pasien demam berdarah adalah antara 4 hari . Faktor lama rawat inap pasien demam berdarah ini dipengaruhi oleh beberapa hal seperti usia, jenis kelamin dan beberapa parameter dari hasil laboratorium (Arianti et al., 2019). Beberapa parameter dari hasil laboratorium yang dimaksud adalah trombosit, hematokrit dan hemoglobin. Secara keseluruhan ketiga parameter ini saling terkait dalam menilai faktor keadaan klinis pasien dan tingkat keparahan yang dialami. Untuk memprediksi lama rawat inap pasien demam berdarah, teknik data mining dapat digunakan untuk melakukan analisis hubungan antara variabel atau faktor yang dapat mempengaruhi lama rawat inap dari masing-masing pasien (Wiratmadja et al., 2018). Metode prediktif memungkinkan kita mengidentifikasi seberapa besar pengaruh masing-masing faktor terhadap lama tinggal di rumah sakit.")

        st.subheader("1.2 Tujuan")
        st.write(
            "Mengevaluasi kinerja masing-masing model dalam memprediksi lama rawat inap pasien demam berdarah dan Menganalisis bagaimana penggunaan Ensemble Stacking untuk menghasilkan prediksi yang lebih akurat dari beberapa gabungan model single-classifier."
        )

        st.subheader("1.3 Hasil Penelitian")
        st.write("Data yang digunakan pada penelitian ini merupakan data sekunder yang didapatkan dari beberapa sumber antara lain: RSUD Syarifah Ambami Rato Ebu, RSU Anna Medika dan Puskesmas Pucuk. Data yang didapatkan berupa hasil rekam medis pasien demam berdarah disertai dengan lama rawat inap pasien pasien tersebut. Terdapat hubungan yang signifikan antara hasil rekam medis dengan lama rawat inap pasien, sehingga data ini nantinya akan dianalisis kemudian dibuatkan suatu model prediksi untuk menentukan lama rawat inap pasien demam berdarah berdasarkan rekam medisnya. ")
        st.image("assets/result.jpg")
        st.write("Hasil terbaik menggunakan metode Ensemble Stacking, yaitu pada Stacking 1 (Metode KNN sebagai Meta-Clasifier) dan Stacking 2 (Metode SVM sebagai Meta-Clasifier)  di dua pengujian yang berbeda. Kedua model stacking tersebut memiliki hasil evaluasi pengujian yang sama dengan nilai akurasi sebesar 0.789, presisi sebesar 0.913, recall sebesar 0.778 dan f1-score sebesar 0.84.")
        
        st.subheader("1.4 Kesimpulan")
        st.write("Penggunaan kombinasi beberapa model dasar yang dilatih secara terpisah dan digabungkan melalui meta-classifier memungkinkan model untuk memanfaatkan kekuatan masing-masing metode, sehingga menghasilkan performa yang lebih baik. Hasil yang diperoleh menunjukkan bahwa Ensemble Stacking tidak hanya meningkatkan akurasi, tetapi juga presisi, recall, dan f1-score, yang menjadikannya pilihan yang lebih optimal pada studi kasus prediksi lama rawat inap pasien demam berdarah dalam penelitian ini. Secara keseluruhan, metode Ensemble Stacking ini memiliki hasil yang lebih optimal jika dibandingkan dengan metode tunggal.")
        
        st.subheader("Referensi")
        st.write("Alahmar, A., Mohammed, E., & Benlamri, R. (2018). Application of Data Mining Techniques to Predict the Length of Stay of Hospitalized Patients with Diabetes. 2018 4th International Conference on Big Data Innovations and Applications (Innovate-Data), 38-43. https://doi.org/10.1109/Innovate-Data.2018.00013")
        st.write("Riya, N. J., Chakraborty, M., & Khan, R. (2024). Artificial Intelligence-Based Early Detection of Dengue Using CBC Data. IEEE Access, 12, 112355–112367. https://doi.org/10.1109/ACCESS.2024.344329")
        st.write("Shahid Ansari, Md., Jain, D., Harikumar, H., Rana, S., Gupta, S., Budhiraja, S., & Venkatesh, S. (2021). Identification of predictors and model for predicting prolonged length of stay in dengue patients. Health Care Management Science, 24(4), 786-798. https://doi.org/10.1007/s10729-021-09571-3")
        st.write("Wiratmadja, I. I., Salamah, S. Y., & Govindaraju, R. (2018). Healthcare Data Mining: Predicting Hospital Length of Stay of Dengue Patients. Journal of Engineering and Technological Sciences, 50(1), 110-126. https://doi.org/10.5614/j.eng.technol.sci.2018.50.1.8")
        st.write("Wulandari, D. A. P., Permana, K. A. B., & Sudarma, M. (2018). Prediction of Days in Hospital Dengue Fever Patients using K-Nearest Neighbor. International Journal of Engineering and Emerging Technology, 3(1), 23-25.")

    with tab2:
        st.warning('Cooming soon', icon="⚠️")


if __name__ == '__main__':
    main()
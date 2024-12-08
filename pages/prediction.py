import streamlit as st
import pandas as pd
import time
import joblib
from sklearn.metrics import DistanceMetric
from streamlit_extras.switch_page_button import switch_page


def main():

    st.set_page_config(
        page_title="Prediksi Lama Rawat Inap Pasien Demam Berdarah",
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

    st.image("assets/banner-prediction.png")
    st.write("Masukkan beberapa isian yang digunakan untuk melakukan prediksi lama rawat inap pasien demam berdarah. Pastikan isian yang anda masukkan benar!")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:

        umur = st.text_input('Umur')
        tb = st.text_input('Trombosit')
        hb = st.text_input('Hemoglobin')

    with col2:

        jenis_kelamin = st.selectbox(
            "Jenis Kelamin",
            ("Laki-Laki", "Perempuan"),
            index=None,
            placeholder="Pilih jenis kelamin ... ",
        )

        hct = st.text_input('Hematokrit')
        jenis_demam = st.selectbox(
            "Jenis Demam",
            ("Demam Dengue", "Demam Berdarah Dengue ", "Dengue Shock Syndrome"),
            index=None,
            placeholder="Pilih jenis demam yang dialami pasien ... ",
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Hasil Prediksi"):
        if umur and tb and hb and jenis_kelamin and jenis_demam:

            umur = int(umur)
            tb   = int(tb)
            hb   = float(hb)
            hct  = float(hb)

            if jenis_kelamin == "Laki-Laki":
                sex = 1
            else:
                sex = 0

            if jenis_demam == "Demam Dengue":
                diagnosis = 0
            elif jenis_demam == "Demam Berdarah Dengue":
                diagnosis = 1
            else:
                diagnosis = 2

            get_data    = normalized_data(umur, sex, tb, hb, hct, diagnosis)
            result      = get_final_predict(get_data) 
            
            st.markdown("<br>", unsafe_allow_html=True)
            if result == 0:
                with st.expander('Berdasarkan prediksi didapatkan hasil: '):
                    st.success("Rawat Inap Pendek (Kurang dari 4 Hari)")
            else:
                with st.expander('Berdasarkan hasil prediksi didapatkan hasil: '):
                    st.error("Rawat Inap Panjang (Lebih dari 4 hari)")

            # except ValueError:
            #     time.sleep(0.5)
            #     st.toast('Teks harus berisikan angka', icon='🤧')

        else:
            time.sleep(.5)
            st.toast('Masukkan teks terlebih dahulu', icon='🤧')





def normalized_data(umur, sex, tb, hb, hct, diagnosis):
    
    df = pd.DataFrame({
        'YEARS': [umur],
        'SEX': [sex],
        'TROMBOSIT': [tb],
        'HCT': [hct],
        'HB': [hb],
        'DIAGNOSIS': [diagnosis]
    })

    scaler = joblib.load('model/minmax_scaler_model.joblib')
    numerical_features = ['YEARS', 'TROMBOSIT', 'HCT', 'HB']

    minmax = scaler.transform(df[numerical_features])

    df_scaled = pd.DataFrame(minmax, columns=numerical_features)
    df_scaled['SEX'] = df['SEX']
    df_scaled['DIAGNOSIS'] = df['DIAGNOSIS']

    model_feature_order = ['YEARS', 'SEX', 'TROMBOSIT', 'HCT', 'HB', 'DIAGNOSIS']
    df_scaled = df_scaled[model_feature_order]

    return df_scaled

def get_single_prediction(model, data):
    prediction = model.predict(data)
    return prediction

def get_final_predict(data):

    lr    = joblib.load('model/lr_model.joblib')
    svm   = joblib.load('model/svm_model.joblib')
    mlp   = joblib.load('model/mlp_model.joblib')

    prediction_lr   = get_single_prediction(lr, data)
    prediction_svm  = get_single_prediction(svm, data)
    prediction_mlp  = get_single_prediction(mlp, data)

    meta_data = pd.DataFrame({
        'Prediction LR' : [prediction_lr],
        'Prediction SVM': [prediction_svm],
        'Prediction MLP': [prediction_mlp],
    })

    final_model = joblib.load('model/knn_meta.pkl')
    prediction = final_model.predict(meta_data)

    return prediction


if __name__ == '__main__':
    main()
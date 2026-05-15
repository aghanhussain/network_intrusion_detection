import streamlit as st
import pandas as pd
import pickle
st.set_page_config(
    page_title="Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide"
)
col1, col2 = st.columns([1, 5])

with col1:
    st.image(
        "security.png",
        width=300,
        
    )

with col2:
    st.title("Network Intrusion Detection System")
    st.subheader("Nasir Hussain | Saad Yar Khan | Abdul Subhan")
    st.subheader("CT-530 : Data Mining")
    st.subheader("Course By: Dr. Muhammad Imran")
    

    st.markdown(
        """
        Detect malicious network traffic using Machine Learning and Intrusion Detection Models.
        """
    )


with open('best_intrusion_detection_pipeline.pkl', 'rb') as file:
    model = pickle.load(file)

st.write("Upload a CSV file to detect network attacks.")

uploaded_file = st.file_uploader(
                                "test_data.csv",
                                 type=['csv']
                               )



if uploaded_file is not None:    
    data = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data")
    st.dataframe(data.head())    
    predictions = model.predict(data)    
    prediction_labels = [
                        'Attack' if pred == 1 else 'Normal' for pred in predictions
                        ]    
    data['Prediction'] = prediction_labels

    st.subheader("Prediction Results")
    st.dataframe(data)

    
    attack_count = prediction_labels.count('Attack')
    normal_count = prediction_labels.count('Normal')

    st.write(f"Attacks Detected: {attack_count}")
    st.write(f"Normal Traffic: {normal_count}")

    
    csv = data.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="Download Results CSV",
        data=csv,
        file_name='prediction_results.csv',
        mime='text/csv'
    )
import streamlit as st
import pandas as pd
import pickle
import numpy as np
import sklearn
# Load the trained model
with open('insurance_model.pkl', 'rb') as f:
    model=pickle.load(f)    
st.title("Insurance Cost Prediction App")
st.write("This app predicts the insurance cost based on the given features.")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://plus.unsplash.com/premium_photo-1671482215421-360cbc885c0a?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fGJsYWNrJTIwYWVzdGhldGljfGVufDB8fDB8fHww");
        background-size: cover;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# User inputs
age = st.number_input("1. Age", min_value=18, max_value=100, step=1)
bp = st.selectbox("2. Blood Pressure Problems", [0, 1])  # 0 = No, 1 = Yes
diabetes = st.selectbox("3. Diabetes", [0, 1])
allergies = st.selectbox("4. Known Allergies", [0, 1])
cancer = st.selectbox("5. History of Cancer in Family", [0, 1])
transplant = st.selectbox("6. Any Transplants", [0, 1])
chronic = st.selectbox("7. Any Chronic Diseases", [0, 1])
surgeries=st.selectbox("8. Any Major Surgeries", [0, 1])
bmi=st.number_input("9. BMI", min_value=0.0, max_value=100.0, step=0.1)
weight=st.number_input("10. Weight", min_value=0, max_value=300, step=1)
height=st.number_input("11. Height", min_value=0, max_value=300, step=1)
bmi_category = st.selectbox("12. BMI Category", ['Underweight', 'Normal', 'Overweight', 'Obese'])
bmi_category_dict = {'Underweight': 0, 'Normal': 1, 'Overweight': 2, 'Obese': 3}
bmi_category_encoded = bmi_category_dict[bmi_category]
age_group=st.selectbox("13. Age Group", ['18-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100'])
age_group_dict = {'18-30': 0, '31-40': 1, '41-50': 2, '51-60': 3, '61-70': 4, '71-80': 5, '81-90': 6, '91-100': 7}
age_group = age_group_dict[age_group]
    
# Button to predict
if st.button("Predict Insurance Premium"):
    input_data = np.array([[age, bp, diabetes, allergies, cancer, transplant, chronic,surgeries,bmi,weight,height,bmi_category_encoded,age_group]])
    prediction = model.predict(input_data)
    st.success(f"💰 Predicted Premium Price: {prediction[0]:.2f}")
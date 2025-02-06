import streamlit as st
import joblib
import pandas as pd

# Load the trained multi-output model
model = joblib.load("xgboost_multi_output_model.pkl")
st.title('# Stroke and Heart Disease Detected')

st.markdown("### Enter Patient Details")

# User input fields
bmi = st.number_input("BMI", min_value=12, max_value=100)
smoker = st.selectbox("Are you a smoker?", ["No", "Yes"])
drink = st.selectbox("Do you drink?", ["No", "Yes"])
ph = st.number_input("Rate your Physical Health", min_value=0, max_value=30)
mh = st.number_input("Rate your Mental Health", min_value=0, max_value=30)
diffWalking = st.selectbox("Do you have difficulty walking?", ["No", "Yes"])
sex = st.selectbox("Gender", ["Female", "Male"])
age = st.selectbox("Age", ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59','60-64', '65-69', '70-74', '75-79', '80 or older'])
race = st.selectbox("Race", ["White", "Black",  'Asian', 'American Indian/Alaskan Native', 'Other', 'Hispanic'])
diabetic = st.selectbox("Are you diabetic?", ["No", "Yes", 'No, borderline diabetes', 'Yes (during pregnancy)'])
physical = st.selectbox("Do you engage in physical activities?", ["No", "Yes"])
gen_health = st.selectbox("Rate your health overall(i.e General Health)", ['Poor', 'Fair', 'Good', 'Very good', 'Excellent'])
sleep = st.number_input("How many hours do you sleep?", min_value=0, max_value=24)
asthma = st.selectbox("Are you asthmatic?", ["No", "Yes"])
kidney = st.selectbox("Do you have Kidney Disease?", ["No", "Yes"])
skin = st.selectbox("Do you have Skin Cancer?", ["No", "Yes"])

# Convert input into DataFrame
input_data = pd.DataFrame([[bmi, 1 if smoker == "Yes" else 0, 1 if drink == "Yes" else 0, ph, mh, 1 if diffWalking == "Yes" else 0, 1 if sex == "Male" else 0,
                            0 if age == '18-24' else 1 if age == '25-29' else 2 if age == '30-34' else 3 if age == '35-39' else 4 if age == '40-44' else 5 if age == '45-49' else 6 if age == '50-54' else 7 if age == '55-59' else 8 if age == '60-64' else 9 if age == '65-69' else 10 if age == '70-74' else 11 if age == '75-79' else 12, 
                            0 if race == "White" else 1 if race == "Black" else 2 if race == "Asian" else 3 if race == "American Indian/Alaskan Native" else 4 if race == "Other" else 5 , 0 if diabetic == "No" else 1 if diabetic == "Yes" else 2 if diabetic == "No, borderline diabetes" else 3, 1 if physical == "Yes" else 0, 0 if gen_health == "Poor" else 1 if gen_health == "Fair" else 2 if gen_health == "Good" else 3 if gen_health == "Very good" else 4 , sleep, 1 if asthma == "Yes" else 0, 1 if kidney == "Yes" else 0, 1 if skin == "Yes" else 0]] , columns = ['BMI', 'Smoking', 'AlcoholDrinking','PhysicalHealth', 'MentalHealth', 'DiffWalking', 'Sex', 'AgeCategory', 'Race', 'Diabetic', 'PhysicalActivity', 'GenHealth', 'SleepTime', 'Asthma', 'KidneyDisease', 'SkinCancer'])


# Predict when button is clicked
if st.button("Predict"):
    prediction = model.predict(input_data)

    # Display results
    stroke_result = "Positive" if prediction[0][0] == 1 else "Negative"
    hd_result = "Positive" if prediction[0][1] == 1 else "Negative"

    st.success(f"Stroke Prediction: **{stroke_result}**")
    st.success(f"Heart Disease Prediction: **{hd_result}**")

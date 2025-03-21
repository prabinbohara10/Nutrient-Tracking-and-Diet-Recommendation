import streamlit as st

from raw_to_train import RawtoTrain, RawtoTrainLabel, RawtoTrainLabelOneHot
from logic import Patient
import time

st.title("Healthy Diet Recommendataion System")

st.subheader("Please enter your details!")

name = st.text_input("Enter Your Name", "Prabin")
age = int(st.text_input("Enter Your Age", "25"))

gender = st.radio("Select Gender", ("Male", "Female"))

height_cm = int(st.text_input("Enter your Height in cm", "172"))
weight_kg = int(st.text_input("Enter your Weight in kg", "72"))

print("type of height_cm : ", type(height_cm), "weight_kg : ", type(weight_kg))
print(height_cm, weight_kg)
blood_pressure = st.selectbox("Blood Pressure", 
                              ["Normal", "Low", "High"])
cholesterol_level = st.selectbox("Cholesterol Level", 
                              ["Optimal", "Borderline", "High"])
blood_sugar_level = st.selectbox("Blood Sugar Level", 
                              ["Normal", "Low", "High"])

daily_steps = int(st.text_input("Daily steps you walk or run","8400"))
sleep_hours = int(st.text_input("Daily sleep hours","7"))

alcohol_consumption = st.radio("Do you consume alcohol?", ("No", "Yes"))
alcohol_consumption = True if alcohol_consumption == "Yes" else False
smoking_habit = st.radio("Do you smoke?", ("No", "Yes"))
smoking_habit = True if smoking_habit == "Yes" else False

dietary_habit = st.selectbox("What is your dietary habit?",
                             ["Regular", "Vegetarian", "Keto", "Vegan"])



patient_current = Patient(
    name= name,
    age= age,
    gender= gender,
    height_cm =height_cm,
    weight_kg = weight_kg,
    blood_pressure= blood_pressure,
    cholesterol_level = cholesterol_level,
    blood_sugar_level = blood_sugar_level,
    daily_steps = daily_steps,
    sleep_hours= sleep_hours,
    alcohol_consumption = alcohol_consumption ,
    smoking_habit = smoking_habit,
    dietary_habit= dietary_habit
)
print(patient_current.user_input_dict)

if (st.button("Get Foods and Diet")):
    st.set_option('client.showErrorDetails', True)
    st.divider()
    st.success("See where you lie among all the people")
    with st.spinner("Ready to see where you lie in the distro?..."):
        time.sleep(1)  # Simulating loading time
        locate_fig = patient_current.locate_patient()
        st.pyplot(fig= locate_fig)

    st.divider()
    recommended_diet = patient_current.recommend_diet()[0]
    st.success(f"You need to have : {recommended_diet}")
    food_recommendations = patient_current.get_food_recommendation(recommended_diet)
    
    st.text("Following are the food recommendated to you:")
    food_md = ""
    for food in food_recommendations:
        food_md += "- " + food + "\n"
    
    print(food_md)
    st.markdown(food_md)
    st.divider()
    

    
    

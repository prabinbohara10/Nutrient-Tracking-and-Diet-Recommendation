import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import pickle
from joblib import dump, load

from raw_to_train import RawtoTrain, RawtoTrainLabel, RawtoTrainLabelOneHot

raw_to_train = None
target_label_converter = None
processed_df = None


# Load the model
dt_model = load('models/dt_model.joblib')


with open("models/inference_dict.pickle", "rb") as file:
    loaded_inference_pickle = pickle.load(file)
    print(loaded_inference_pickle)

raw_to_train = loaded_inference_pickle["raw_to_train"]
target_label_converter = loaded_inference_pickle["target_label_converter"]
processed_df = loaded_inference_pickle["processed_df"]



import random

class Patient:
    
    def __init__(self, name: str, 
                age: int, 
                gender: str, 
                height_cm: float, 
                weight_kg: float, 
                blood_pressure: str, 
                cholesterol_level:str, 
                blood_sugar_level: str, 
                daily_steps: int = 8400,
                sleep_hours : int = 7, 
                alcohol_consumption : bool = False, 
                smoking_habit : bool = False,
                dietary_habit: str = "Regular"
                ):
        self.name = name
        self.age = age
        self.gender = gender
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.blood_pressure = blood_pressure
        self.cholesterol_level = cholesterol_level
        self.blood_sugar_level = blood_sugar_level
        self.daily_steps = daily_steps
        self.sleep_hours = sleep_hours
        self.alcohol_consumption = alcohol_consumption
        self.smoking_habit = smoking_habit
        self.dietary_habit = dietary_habit
        self.user_input_dict = self.__user_to_train_feature_conv()


    def __user_to_train_feature_conv(self):
        user_input_dict = {
            "Age" : self.age,
            "BMI" : raw_to_train.bmi_converter(self.height_cm, self.weight_kg),
            "Daily_Steps" : self.daily_steps,
            "Sleep_Hours" : self.sleep_hours,
            
            "Gender_Male" : 1 if self.gender == "Male" else 0,
            "Gender_Female" : 1 if self.gender == "Female" else 0,
            "Gender_Other" : 1 if self.gender == "Other" else 0,

            "Alcohol_Consumption_Yes" : 1 if self.alcohol_consumption else 0,
            "Alcohol_Consumption_No" : 0 if self.alcohol_consumption else 1,

            "Smoking_Habit_Yes" : 1 if self.smoking_habit else 0,
            "Smoking_Habit_No" : 0 if self.smoking_habit else 1,

            "Dietary_Habits_Regular" : 1 if self.dietary_habit == "Regular" else 0,
            "Dietary_Habits_Vegetarian" : 1 if self.dietary_habit == "Vegetarian" else 0,
            "Dietary_Habits_Keto" : 1 if self.dietary_habit == "Keto" else 0,
            "Dietary_Habits_Vegan" : 1 if self.dietary_habit == "Vegan" else 0,
            
            "blood_pressure_converted_Low" : 1 if self.blood_pressure == "Low" else 0,
            "blood_pressure_converted_Normal" : 1 if self.blood_pressure == "Normal" else 0,
            "blood_pressure_converted_High" : 1 if self.blood_pressure == "High" else 0,
            
            
            "cholesterol_level_converted_Borderline" : 1 if self.cholesterol_level == "Borderline" else 0,
            "cholesterol_level_converted_Optimal" : 1 if self.cholesterol_level == "Optimal" else 0,
            "cholesterol_level_converted_High" : 1 if self.cholesterol_level == "High" else 0,
            

            "blood_sugar_level_converted_Low" : 1 if self.blood_sugar_level == "Low" else 0,
            "blood_sugar_level_converted_Normal" : 1 if self.blood_sugar_level == "Normal" else 0,
            "blood_sugar_level_converted_High" : 1 if self.blood_sugar_level == "High" else 0
        }

        return user_input_dict
    
    def recommend_diet(self):
        user_input_df = pd.DataFrame(self.user_input_dict, index = [0])
        prediction = dt_model.predict(user_input_df)
        
        return target_label_converter.convert_index_to_label(prediction)

    def get_food_recommendation(self, diet_type: str):
        diet = {
            "Balanced Diet": {
                "Vegetables": ["Carrots", "Broccoli", "Spinach"],
                "Fruits": ["Apple", "Banana", "Orange"],
                "Protein": ["Chicken", "Fish", "Eggs"],
                "Carbohydrates": ["Rice", "Bread", "Pasta"],
                "Dairy": ["Milk", "Cheese", "Yogurt"],
                "Fats": ["Avocado", "Nuts", "Seeds"],
            },
            "Low-Carb Diet": {
                "Vegetables": ["Carrots", "Broccoli", "Spinach"],
                "Fruits": ["Apple", "Banana", "Orange"],
                "Protein": ["Chicken", "Fish", "Eggs"],
                "Carbohydrates": [],
                "Dairy": ["Milk", "Cheese", "Yogurt"],
                "Fats": ["Avocado", "Nuts", "Seeds"],
            },
            "High-Protein Diet": {
                "Vegetables": ["Carrots", "Broccoli", "Spinach"],
                "Fruits": ["Apple", "Banana", "Orange"],
                "Protein": ["Chicken", "Fish", "Eggs"],
                "Carbohydrates": ["Rice", "Bread", "Pasta"],
                "Dairy": ["Milk", "Cheese", "Yogurt"],
                "Fats": ["Avocado", "Nuts", "Seeds"],
            },
            "Low-Fat Diet": {
                "Vegetables": ["Carrots", "Broccoli", "Spinach"],
                "Fruits": ["Apple", "Banana", "Orange"],
                "Protein": ["Chicken", "Fish", "Eggs"],
                "Carbohydrates": ["Rice", "Bread", "Pasta"],
                "Dairy": ["Milk", "Cheese", "Yogurt"],
                "Fats": ["Avocado", "Nuts", "Seeds"],
            },
        }
    
        recommended_foods = []
        for _, items in diet[diet_type].items():
            if len(items):
                # recommended_foods[category] = random.choice(items)
                recommended_foods.append(random.choice(items))
    
        return recommended_foods
    
    def get_original_values(self):
        """Extracts the original values only"""
        
        original_values = {
            "Age": self.age,
            "Height_cm": self.height_cm,
            "Weight_kg" : self.weight_kg,
            "BMI": raw_to_train.bmi_converter(self.height_cm, self.weight_kg),
            "Daily_Steps": self.daily_steps,
            "Sleep_Hours": self.sleep_hours,
            "Gender": self.gender,
            "Alcohol_Consumption": "Yes" if self.alcohol_consumption else "No",
            "Smoking_Habit": "Yes" if self.smoking_habit else "No",
            "Dietary_Habits": self.dietary_habit,
            "blood_pressure_converted": self.blood_pressure,
            "cholesterol_level_converted": self.cholesterol_level,
            "blood_sugar_level_converted": self.blood_sugar_level
        }

        return original_values
    
    def locate_patient(self):
        numerical_cols = processed_df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        categorical_cols = processed_df.select_dtypes(include=['object']).columns.tolist()
        all_columns = numerical_cols + categorical_cols

        user_values = self.get_original_values()

        num_plots = len(all_columns)
        num_cols = 3
        num_rows = math.ceil(num_plots / num_cols)

        fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(15, 5 * num_rows))
        axes = axes.flatten()

        for i, col in enumerate(all_columns):
            patient_value = user_values.get(col, None)

            if col in numerical_cols:
                sns.histplot(processed_df[col], bins=20, kde=True, color='skyblue', edgecolor='black', ax=axes[i])
                
                if patient_value is not None:
                    axes[i].axvline(x=patient_value, color='red', linestyle='dashed', linewidth=2)
                    axes[i].text(patient_value, axes[i].get_ylim()[1] * 0.9, f'{self.name}: {patient_value}', color='red', fontsize=10)
            
            else:  # forCategorical data
                sns.countplot(x=processed_df[col], hue=processed_df[col], palette="viridis", legend=False, ax=axes[i])
                axes[i].tick_params(axis='x', rotation=45)
                
                unique_values_this = processed_df[col].unique()
                if patient_value in unique_values_this:
                    patient_index = list(unique_values_this).index(patient_value)
                    axes[i].axvline(x=patient_index, color='red', linestyle='dashed', linewidth=2)
                    axes[i].text(patient_value, axes[i].get_ylim()[1] * 0.9, f'{self.name}: {patient_value}', color='red', fontsize=10)

            axes[i].set_title(f"Distribution of {col}")
            axes[i].set_xlabel(col)
            axes[i].set_ylabel("Count" if col in categorical_cols else "Density")

        #Removing unsed sbplots
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])

        plt.tight_layout()
        plt.show()
        
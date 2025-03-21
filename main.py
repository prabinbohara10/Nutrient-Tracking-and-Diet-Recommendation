import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from sklearn.model_selection import train_test_split

from raw_to_train import RawtoTrain, RawtoTrainLabel,RawtoTrainLabelOneHot

per_diet_recom_path = "../datasets/Personalized Medical Diet Recommendations Dataset/Personalized_Diet_Recommendations.csv"

features=['Age','Gender','Height_cm','Weight_kg','BMI','Blood_Pressure_Systolic','Blood_Pressure_Diastolic','Cholesterol_Level','Blood_Sugar_Level', 'Daily_Steps','Sleep_Hours','Alcohol_Consumption','Smoking_Habit','Dietary_Habits']
target_name = "Recommended_Meal_Plan"

blood_pressure_mapping = {
    "Low" : 1,
    "Normal" : 2,
    "High" : 2
}
cholestrol_mapping = {
    "Optimal" : 1,
    "Borderline" : 2,
    "High" : 3
}

blood_sugar_mapping = {
    "Low" : 1,
    "Normal": 2,
    "High": 3
}


#functions
def preprocessing():
    original_df = pd.read_csv(per_diet_recom_path)
    df = original_df[features]

    raw_to_train = RawtoTrain(blood_pressure_mapping, cholestrol_mapping, blood_sugar_mapping)
    df = raw_to_train.raw_to_train_feature_conv(df)

    processed_df = df.copy()

    df.drop(columns= ["Height_cm", "Weight_kg"], inplace= True)

    ## Custom dummies function:
    column_name_unique_val_map = {
        "Gender" : ["Male", "Female", "Other"],
        "Alcohol_Consumption" : ["Yes", "No"],
        "Smoking_Habit" : ["Yes", "No"],
        "Dietary_Habits" : ["Regular", "Vegetarian", "Keto", "Vegan"],
        "blood_pressure_converted" : ["Low", "Normal", "High"],
        "cholesterol_level_converted" : ["Borderline", "Optimal", "High"],
        "blood_sugar_level_converted" : ["Low", "Normal", "High"]
    }

    for col_name, unique_val in column_name_unique_val_map.items():
        one_hot_encode = RawtoTrainLabelOneHot(df, column_name= col_name, unique_values= unique_val)
        df = one_hot_encode.convert_label_to_onehot()

    final_feature_names = df.columns

    target_df = original_df[target_name]
    ## Converting target column to index:
    target_label_converter = RawtoTrainLabel(target_df)
    target_col = target_label_converter.convert_label_to_index(target_df)

    
    X_train, X_test, y_train, y_test = train_test_split(df, target_col, test_size=0.2, random_state=42)
    X_train

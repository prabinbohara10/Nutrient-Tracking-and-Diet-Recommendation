import pandas as pd
import numpy as np

class RawtoTrain:
    def __init__(self, blood_pressure_mapping, cholestrol_mapping, blood_sugar_mapping):
        self.blood_pressure_mapping = blood_pressure_mapping
        self.cholestrol_mapping = cholestrol_mapping
        self.blood_sugar_mapping = blood_sugar_mapping

    
    def bmi_converter(self, height_cm: int, weight_kg: int):
        return (weight_kg * 10000) / height_cm ** 2

    
    def blood_pressure_converter(self, systolic: int, diastolic: int):
        if systolic < 90 or diastolic < 60:
            value = "Low"
        elif 90 <= systolic <= 129 and 60 <= diastolic <= 79:
            value = "Normal"
        elif systolic > 129 or diastolic > 79:
            value =  "High"
        else:
            value = "Normal"
        
        return value
        
   
    def cholesterol_converter(self, cholesterol_level: int):
        if cholesterol_level < 200:
            value = "Optimal"
        elif 200 <= cholesterol_level < 240:
            value = "Borderline"
        else:
            value = "High"
        
        #return self.cholestrol_mapping[value]
        return value

    
    def blood_sugar_converter(self, blood_sugar_level: int):
        if blood_sugar_level < 70:
            value = "Low"
        elif 70 <= blood_sugar_level <= 99:
            value = "Normal"
        else:  #blood_sugar_level >= 100
            value = "High"
        
        #return self.blood_pressure_mapping[value]
        return value
    
    def __drop_converted_features(self, df):
        columns_to_be_dropped = ["Blood_Pressure_Systolic", "Blood_Pressure_Diastolic","Cholesterol_Level", "Blood_Sugar_Level"]
        df = df.drop(columns= columns_to_be_dropped)
        return df

    def raw_to_train_feature_conv(self, df):
        '''
        Takes in the original dataframe and returns the transformed df that is ready to train.
        Convert df into user required data format
        i.e numerical data into categorical
        '''
        
        df["blood_pressure_converted"] = df.apply(lambda row: self.blood_pressure_converter(row["Blood_Pressure_Systolic"], row["Blood_Pressure_Diastolic"]), axis = 1)
        df["cholesterol_level_converted"] = df.apply(lambda row: self.cholesterol_converter(row["Cholesterol_Level"]), axis = 1)
        df["blood_sugar_level_converted"] = df.apply(lambda row: self.blood_sugar_converter(row["Blood_Sugar_Level"]), axis= 1)

        df = self.__drop_converted_features(df)
        
        return df
        
class RawtoTrainLabel:
    def __init__(self, single_column):
        self.label_to_index = {}
        self.index_to_label = {}
        self.single_column = single_column
        self.__create_mapping()
    
    def __create_mapping(self):
        unique_values = sorted(set(self.single_column))
        self.label_to_index = {unique_value : idx +1 for idx, unique_value in enumerate(unique_values)}
        self.index_to_label = {idx+ 1 : unique_value for idx, unique_value in enumerate(unique_values)}
    
    def convert_label_to_index(self, column):
        return [self.label_to_index[value] for value in column]

    def convert_index_to_label(self, column):
        return [self.index_to_label[value] for value in column]
    

class RawtoTrainLabelOneHot:
    def __init__(self, df, column_name, unique_values):
        self.df = df
        self.column_name = column_name
        self.unique_values = unique_values

    def convert_label_to_onehot(self):
        df = self.df
        new_columns = [self.column_name + "_" + unique_value for unique_value in self.unique_values]
        print(f"new columns list : {new_columns}")
        new_df = pd.DataFrame(0, index = np.arange(df.shape[0]), columns=new_columns)

        for idx, row in enumerate(df[self.column_name]):
            new_df_col_name = self.column_name + "_" + row
            new_df.loc[idx, new_df_col_name] = 1
        
        df.drop(columns=[self.column_name], inplace= True)
        
        # print("newdf ", new_df)
        # print("df", df)
        df = pd.concat([df, new_df], axis= 1)
        return df
import pandas as pd

data = {
    'Gender': ['Infant(male or female)', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Age (years)': ['under 2', '2-9', '2-9', '10-19', '10-19', '20-29', '20-29', '30-39', '30-39', '40-49', '40-49', '50 - 59', '50 - 59', '60-100', '60-100'],
    'Recommended BMI': ['Refer growth chart using weight-for-length measurements', '16.2- 17.8', '16.4 - 17.6', '17.8-22.6', '17.6-22.5', '18.5 – 24.9', '18.5 – 24.9', '18.5 – 24.9', '18.5 – 24.9', '18.5 – 24.9', '18.5 – 24.9', '18.5 – 24.9', '18.5 – 24.9', '22.0 – 27.0', '22.0 – 27.0'],
    'Calories (kcal)': ['800-900', '1200-1400', '1200-1600', '1800-2000', '2000-2400', '2000-2200', '2400-2800', '2000-2200', '2400-2600', '1800-2200', '2200-2400', '1800-2000', '2000-2400', '1600-1800', '2000-2200'],
    'Protein (g)': ['11', '38-113', '38-113', '34-46', '34-52', '46', '56', '46', '56', '46', '56', '46', '56', '46', '56'],
    'Carbohydrates (g)': ['95', '169-244', '169-244', '260', '260', '260', '260', '260', '260', '260', '260', '260', '260', '260', '260'],
    'Fat (g)': ['30–40', '42-58', '42-58', '65', '65', '70', '70', '70', '70', '70', '70', '70', '70', '65–70', '65–70'],
    'Fiber (g)': ['Varies', '14-21', '14-21', '25', '38', '25', '38', '25', '38', '25', '38', '25', '38', '30–38', '30–38'],
    'Sugars (g)': ['<25', '<25', '<25', '<25', '<36', '<25', '<36', '<25', '<36', '<25', '<36', '<25', '<36', '<25', '<36'],
    'Sodium (mg)': ['<800', '<1200', '<1200', '<1500', '<1500', '<2300', '<2300', '<2300', '<2300', '<2300', '<2300', '<2300', '<2300', '<2300', '<2300'],
    'Cholesterol (mg)': ['<100', '<170', '<170', '<200', '<200', '<300', '<300', '<300', '<300', '<300', '<300', '<300', '<300', '<200', '<200'],
    'Water_Intake (ml)': ['Varies', '1300-1700', '1300-1700', '2700-3000', '3000', '2700', '3700', '2700', '3700', '2700', '3700', '2700', '3700', '2700', '3000']
}


df = pd.DataFrame(data)


df.to_csv("Module B/2_nutrient_requirements.csv", index=False)

print("Excel file 'nutrient_requirements.csv' has been created successfully!")

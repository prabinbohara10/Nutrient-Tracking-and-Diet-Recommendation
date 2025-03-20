import pandas as pd

data = {
        'Gender': ['Infant(male or female)', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
        'Age (years)': ['under 2', '2-9', '2-9', '10-19', '10-19', '20-29', '20-29', '30-39', '30-39', '40-49', '40-49', '50 - 59', '50 - 59', '60-100', '60-100'],
        'Recommended BMI': ['Refer growth chart using weight-for-length measurements', '16.2- 17.8', '16.4 - 17.6', '17.8-22.6', '17.6-22.5', '18.5 – 24.9', '18.5 – 24.9', '18.5 – 24.9', '18.5 – 24.9', '18.5 – 24.9', '18.5 – 24.9', '18.5 – 24.9', '18.5 – 24.9', '22.0 – 27.0', '22.0 – 27.0'],
        'Fat( in g)': ['30–40 g', '42-58 g', '42-58 g', '65 g', '65 g', '70 g', '70 g', '70 g', '70 g', '70 g', '70 g', '70 g', '70 g', '65–70 g', '65–70 g'],
        'Carbohydrates( in g)': ['95 g', '169-244 g', '169-244 g', '260 g', '260 g', '260 g', '260 g', '260 g', '260 g', '260 g', '260 g', '260 g', '260 g', '260 g', '260 g'],
        'Protein( in g)': ['11 g', '38-113 g', '38-113 g', '34-46 g', '34-52 g', '46 g', '56 g', '46 g', '56 g', '46 g', '56 g', '46 g', '56 g', '46 g', '56 g'],
        'Dietary Fiber( in g)': ['not specific recommendation(introduce  fiber-rich foods)', '14-21 g', '14-21 g', '25 g', '38 g', '25 g', '38 g', '25 g', '38 g', '25 g', '38 g', '25 g', '38 g', '30–38 g', '30–38 g'],
        'Water( in litre)': ['adequate hydration from breast milk or formula milk', '1.3- 1.7 liters', '1.3- 1.7 liters', '2.7–3 L', '3 L', '2.7 L', '3.7 L', '2.7 L', '3.7 L', '2.7 L', '3.7 L', '2.7 L', '3.7 L', '2.7 L', '3 L'],
        'Vitamin A( in mg)': ['300 µg', '300-400 µg', '300-400 µg', '700 µg', '900 µg', '0.7 mg', '0.9 mg', '0.7 mg', '0.9 mg', '0.7 mg', '0.9 mg', '0.7 mg', '0.9 mg', '0.7 mg', '0.9 mg'],
        'Vitamin B11 (Folate)( in mg)': ['80 µg', '150-200 µg', '150-200 µg', '400 µg', '400 µg', '0.4 mg', '0.4 mg', '0.4 mg', '0.4 mg', '0.4 mg', '0.4 mg', '0.4 mg', '0.4 mg', '0.4 mg', '0.4 mg'],
        'Vitamin B12 (mg)': ['0.5 µg', '1.2-1.8 µg', '1.2-1.8 µg', '2.4 µg', '2.4 µg', '2.4 µg', '2.4 µg', '2.4 µg', '2.4 µg', '2.4 µg', '2.4 µg', '2.4 µg', '2.4 µg', '2.4 µg', '2.4 µg'],
        'Vitamin C': ['40 mg', '15-25 mg', '15-25 mg', '65 mg', '75 mg', '75 mg', '90 mg', '75 mg', '90 mg', '75 mg', '90 mg', '75 mg', '90 mg', '75 mg', '90 mg'],
        'Vitamin D( in mg)': ['10 µg', '15 µg', '15 µg', '15 µg', '15 µg', '15 µg', '15 µg', '15 µg', '15 µg', '15 µg', '15 µg', '15 µg', '15 µg', '15 µg', '15 µg'],
        'Vitamin E( in mg)': ['5 mg', '6-7 mg', '6-7 mg', '15 mg', '15 mg', '15 mg', '15 mg', '15 mg', '15 mg', '15 mg', '15 mg', '15 mg', '15 mg', '15 mg', '15 mg'],
        'Vitamin K( in mg)': ['2.5 µg', '55-60 µg', '55-60 µg', '75 µg', '75 µg', '0.09 mg', '0.12 mg', '0.09 mg', '0.12 mg', '0.09 mg', '0.12 mg', '0.09 mg', '0.12 mg', '0.09 mg', '0.12 mg'],
        'Calcium( in mg)': ['260 mg', '700-1000 mg', '700-1000 mg', '1300 mg', '1300 mg', '1000 mg', '1000 mg', '1000 mg', '1000 mg', '1000 mg', '1000 mg', '1200 mg', '1000 mg', '1200 mg', '1000 mg'],
        'Iron( in mg)': ['11 mg', '7-10 mg', '7-10 mg', '11 mg', '15 mg', '18 mg', '8 mg', '18 mg', '8 mg', '18 mg', '8 mg', '8 mg', '8 mg', '8 mg', '8 mg'],
        'Magnesium( in mg)': ['80 mg', '80-130 mg', '80-130 mg', '360 mg', '410 mg', '320 mg', '420 mg', '320 mg', '420 mg', '320 mg', '420 mg', '320 mg', '420 mg', '320 mg', '420 mg'],
        'Manganese( in mg)': ['0.6 mg', '1.2-1.5 mg', '1.2-1.5 mg', '1.6 mg', '2.2 mg', '1.8 mg', '2.3 mg', '1.8 mg', '2.3 mg', '1.8 mg', '2.3 mg', '1.8 mg', '2.3 mg', '1.8 mg', '2.3 mg']
    }


df = pd.DataFrame(data)


df.to_excel("Module B/nutrient_requirements_original_format.xlsx", index=False)

print("Excel file 'nutrient_requirements_original_format.csv' has been created successfully!")

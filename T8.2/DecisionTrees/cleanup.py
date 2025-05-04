# Cleanup for LR
# Dropping irrelevant columns
# Changing booleans to binary
# converted dates

import pandas as pd
import numpy as np
import sys

file_path = sys.argv[1] if len(sys.argv) > 1 else "Telepass.xlsx"
insurance_df = pd.read_excel(file_path, sheet_name="Insurance Quotes")

df = insurance_df.copy()

df.drop(columns=["quotation_id"], inplace=True)

df['car_immatriculation_date'] = pd.to_datetime(df['car_immatriculation_date'], errors='coerce')
df['insurance_expires_at'] = pd.to_datetime(df['insurance_expires_at'], errors='coerce')
df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce')

df['car_age'] = 2020 - df['car_immatriculation_date'].dt.year
df['customer_age'] = 2020 - df['birth_date'].dt.year

df.drop(columns=['car_immatriculation_date', 'insurance_expires_at', 'birth_date'], inplace=True)

df['purchased'] = df['issued'].map({True: 1, False: 0})
df.drop(columns=['issued'], inplace=True)

df.drop(columns=['price_sale', 'price_full', 'discount_percent'], inplace=True, errors='ignore')
df.drop(columns=['key_loss', 'vandalism', 'car_model', 'car_brand', 'county'], inplace=True, errors='ignore')
df.drop(columns=['policy_quoted_at'], inplace=True, errors='ignore')

for col in ['base_subscription', 'pay_subscription', 'premium_subscription']:
    if col in df.columns:
        df[col] = df[col].notna().astype(int)

df = df.dropna(thresh=int(df.shape[1] * 0.7))
for col in df.columns:
    if df[col].dtype in [np.float64, np.int64]:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

categorical_cols = df.select_dtypes(include='object').columns
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

df.to_csv("cleaned_telepass_insurance.csv", index=False)

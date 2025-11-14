import pandas as pd

df = pd.read_csv("marketing_campaign.csv", sep="\t") 
print("Original Shape:", df.shape)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

df.dropna(how='all', inplace=True)

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

df.drop_duplicates(inplace=True)
print("\nShape After Removing Duplicates:", df.shape)

text_cols = ['Education', 'Marital_Status']
for col in text_cols:
    df[col] = df[col].str.lower().str.strip()

df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], errors='coerce')
df['Dt_Customer'] = df['Dt_Customer'].dt.strftime('%d-%m-%Y')

df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("-", "_")

df['income'] = df['income'].astype(float)

df.to_csv("cleaned_marketing_campaign.csv", sep="\t", index=False)

print("\nData cleaning complete! Cleaned file saved as 'cleaned_marketing_campaign.csv'")

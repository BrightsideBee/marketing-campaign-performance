import pandas as pd

# Load the corrected dataset
file_path = "data/cleaned/marketing_campaign_cleaned_final.csv"
df = pd.read_csv(file_path)

print("DATASET INFO")
print("=" * 40)
print(df.info())

print("\nMISSING VALUES")
print("=" * 40)
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print("=" * 40)
print(df.duplicated().sum())
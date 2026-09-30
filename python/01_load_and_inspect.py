import pandas as pd

# Load the CSV
file_path = "data/cleaned/marketing_campaign_cleaned.csv"
df = pd.read_csv(file_path)

# Keep only the original 13 marketing dataset columns
df = df.iloc[:, :13]

# Standardize channel names
df["Channel"] = (
    df["Channel"]
    .str.strip()
    .str.lower()
    .replace({
        "google ads": "Google Ads",
        "instagram": "Instagram",
        "youtube": "YouTube",
        "facebook": "Facebook",
        "email": "Email"
    })
)

# Save the corrected CSV
output_path = "data/cleaned/marketing_campaign_cleaned_final.csv"
df.to_csv(output_path, index=False)

print("Corrected dataset saved successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("\nColumn names:")
print(df.columns.tolist())
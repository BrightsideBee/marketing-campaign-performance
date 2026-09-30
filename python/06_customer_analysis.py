import pandas as pd

# Load the corrected dataset
file_path = "data/cleaned/marketing_campaign_cleaned_final.csv"
df = pd.read_csv(file_path)


def calculate_segment_analysis(data, column_name):
    analysis = data.groupby(column_name).agg(
        total_ad_spend=("Ad_Spend", "sum"),
        total_revenue=("Revenue", "sum"),
        total_impressions=("Impressions", "sum"),
        total_clicks=("Clicks", "sum"),
        total_leads=("Leads", "sum"),
        total_conversions=("Conversions", "sum")
    ).reset_index()

    analysis["CTR"] = (
        analysis["total_clicks"] /
        analysis["total_impressions"] * 100
    )

    analysis["Conversion_Rate"] = (
        analysis["total_conversions"] /
        analysis["total_leads"] * 100
    )

    analysis["CAC"] = (
        analysis["total_ad_spend"] /
        analysis["total_conversions"]
    )

    analysis["ROI"] = (
        (analysis["total_revenue"] -
         analysis["total_ad_spend"]) /
        analysis["total_ad_spend"] * 100
    )

    return analysis.round(2)


# Age Group Analysis
age_analysis = calculate_segment_analysis(df, "Age_Group")

print("AGE GROUP ANALYSIS")
print("=" * 70)
print(age_analysis.to_string(index=False))


# Gender Analysis
gender_analysis = calculate_segment_analysis(df, "Gender")

print("\nGENDER ANALYSIS")
print("=" * 70)
print(gender_analysis.to_string(index=False))
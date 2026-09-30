import pandas as pd

# Load the corrected dataset
file_path = "data/cleaned/marketing_campaign_cleaned_final.csv"
df = pd.read_csv(file_path)

# Convert Date to proper date format
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Create monthly analysis
monthly_analysis = df.groupby(
    df["Date"].dt.to_period("M")
).agg(
    total_ad_spend=("Ad_Spend", "sum"),
    total_revenue=("Revenue", "sum"),
    total_impressions=("Impressions", "sum"),
    total_clicks=("Clicks", "sum"),
    total_leads=("Leads", "sum"),
    total_conversions=("Conversions", "sum")
).reset_index()

# Convert month back to readable text
monthly_analysis["Date"] = monthly_analysis["Date"].astype(str)

# Calculate KPIs
monthly_analysis["CTR"] = (
    monthly_analysis["total_clicks"] /
    monthly_analysis["total_impressions"] * 100
)

monthly_analysis["Conversion_Rate"] = (
    monthly_analysis["total_conversions"] /
    monthly_analysis["total_leads"] * 100
)

monthly_analysis["CAC"] = (
    monthly_analysis["total_ad_spend"] /
    monthly_analysis["total_conversions"]
)

monthly_analysis["ROI"] = (
    (monthly_analysis["total_revenue"] -
     monthly_analysis["total_ad_spend"]) /
    monthly_analysis["total_ad_spend"] * 100
)

print("MONTHLY TREND ANALYSIS")
print("=" * 80)
print(monthly_analysis.round(2).to_string(index=False))
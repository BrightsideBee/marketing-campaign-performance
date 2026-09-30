import pandas as pd

# Load the corrected dataset
file_path = "data/cleaned/marketing_campaign_cleaned_final.csv"
df = pd.read_csv(file_path)

# Calculate campaign-level performance
campaign_analysis = df.groupby("Campaign_Name").agg(
    total_ad_spend=("Ad_Spend", "sum"),
    total_revenue=("Revenue", "sum"),
    total_impressions=("Impressions", "sum"),
    total_clicks=("Clicks", "sum"),
    total_leads=("Leads", "sum"),
    total_conversions=("Conversions", "sum")
).reset_index()

# Calculate KPIs
campaign_analysis["CTR"] = (
    campaign_analysis["total_clicks"] /
    campaign_analysis["total_impressions"] * 100
)

campaign_analysis["Conversion_Rate"] = (
    campaign_analysis["total_conversions"] /
    campaign_analysis["total_leads"] * 100
)

campaign_analysis["CAC"] = (
    campaign_analysis["total_ad_spend"] /
    campaign_analysis["total_conversions"]
)

campaign_analysis["ROI"] = (
    (campaign_analysis["total_revenue"] -
     campaign_analysis["total_ad_spend"]) /
    campaign_analysis["total_ad_spend"] * 100
)

# Sort by revenue
campaign_analysis = campaign_analysis.sort_values(
    "total_revenue",
    ascending=False
)

print("CAMPAIGN PERFORMANCE ANALYSIS")
print("=" * 70)
print(campaign_analysis.round(2).to_string(index=False))
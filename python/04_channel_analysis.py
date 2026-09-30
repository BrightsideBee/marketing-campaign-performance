import pandas as pd

# Load the corrected dataset
file_path = "data/cleaned/marketing_campaign_cleaned_final.csv"
df = pd.read_csv(file_path)

# Calculate channel-level performance
channel_analysis = df.groupby("Channel").agg(
    total_ad_spend=("Ad_Spend", "sum"),
    total_revenue=("Revenue", "sum"),
    total_impressions=("Impressions", "sum"),
    total_clicks=("Clicks", "sum"),
    total_leads=("Leads", "sum"),
    total_conversions=("Conversions", "sum")
).reset_index()

# Calculate KPIs
channel_analysis["CTR"] = (
    channel_analysis["total_clicks"] /
    channel_analysis["total_impressions"] * 100
)

channel_analysis["Conversion_Rate"] = (
    channel_analysis["total_conversions"] /
    channel_analysis["total_leads"] * 100
)

channel_analysis["CAC"] = (
    channel_analysis["total_ad_spend"] /
    channel_analysis["total_conversions"]
)

channel_analysis["ROI"] = (
    (channel_analysis["total_revenue"] -
     channel_analysis["total_ad_spend"]) /
    channel_analysis["total_ad_spend"] * 100
)

# Sort by revenue
channel_analysis = channel_analysis.sort_values(
    "total_revenue",
    ascending=False
)

print("CHANNEL PERFORMANCE ANALYSIS")
print("=" * 60)
print(channel_analysis.round(2).to_string(index=False))
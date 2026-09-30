import pandas as pd

# Load the corrected dataset
file_path = "data/cleaned/marketing_campaign_cleaned_final.csv"
df = pd.read_csv(file_path)

# Convert Date from text to date format
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Calculate overall KPIs
total_ad_spend = df["Ad_Spend"].sum()
total_revenue = df["Revenue"].sum()
total_impressions = df["Impressions"].sum()
total_clicks = df["Clicks"].sum()
total_leads = df["Leads"].sum()
total_conversions = df["Conversions"].sum()

ctr = (total_clicks / total_impressions) * 100
conversion_rate = (total_conversions / total_leads) * 100
cac = total_ad_spend / total_conversions
roi = ((total_revenue - total_ad_spend) / total_ad_spend) * 100

print("OVERALL MARKETING KPIs")
print("=" * 40)

print(f"Total Ad Spend: ₹{total_ad_spend:,.2f}")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Impressions: {total_impressions:,}")
print(f"Total Clicks: {total_clicks:,}")
print(f"Total Leads: {total_leads:,}")
print(f"Total Conversions: {total_conversions:,}")
print(f"CTR: {ctr:.2f}%")
print(f"Conversion Rate: {conversion_rate:.2f}%")
print(f"CAC: ₹{cac:.2f}")
print(f"ROI: {roi:.2f}%")
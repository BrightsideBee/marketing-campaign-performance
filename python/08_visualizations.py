import pandas as pd
import matplotlib.pyplot as plt

# Load the corrected dataset
file_path = "data/cleaned/marketing_campaign_cleaned_final.csv"
df = pd.read_csv(file_path)

# -----------------------------------
# Chart 1: Revenue by Channel
# -----------------------------------

channel_revenue = (
    df.groupby("Channel")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
channel_revenue.plot(kind="bar")

plt.title("Revenue by Marketing Channel")
plt.xlabel("Channel")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("screenshots/revenue_by_channel.png", dpi=300)
plt.close()


# -----------------------------------
# Chart 2: Monthly Revenue Trend
# -----------------------------------

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

monthly_revenue = (
    df.groupby(df["Date"].dt.to_period("M"))["Revenue"]
    .sum()
)

plt.figure(figsize=(10, 6))
monthly_revenue.plot(kind="line", marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("screenshots/monthly_revenue_trend.png", dpi=300)
plt.close()

print("Both charts created successfully!")
print("1. screenshots/revenue_by_channel.png")
print("2. screenshots/monthly_revenue_trend.png")

# -----------------------------------
# Chart 3: Conversion Rate by Channel
# -----------------------------------

channel_conversion = (
    df.groupby("Channel")
    .apply(
        lambda x: x["Conversions"].sum() /
        x["Leads"].sum() * 100
    )
)

plt.figure(figsize=(10, 6))
channel_conversion.plot(kind="bar")

plt.title("Conversion Rate by Marketing Channel")
plt.xlabel("Channel")
plt.ylabel("Conversion Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("screenshots/conversion_rate_by_channel.png", dpi=300)
plt.close()

print("3. screenshots/conversion_rate_by_channel.png")

# -----------------------------------
# Chart 4: CAC by Channel
# -----------------------------------

channel_cac = (
    df.groupby("Channel")
    .apply(
        lambda x: x["Ad_Spend"].sum() /
        x["Conversions"].sum()
    )
)

plt.figure(figsize=(10, 6))
channel_cac.plot(kind="bar")

plt.title("Customer Acquisition Cost by Marketing Channel")
plt.xlabel("Channel")
plt.ylabel("CAC (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("screenshots/cac_by_channel.png", dpi=300)
plt.close()

print("4. screenshots/cac_by_channel.png")

# -----------------------------------
# Chart 5: ROI by Channel
# -----------------------------------

channel_roi = (
    df.groupby("Channel")
    .apply(
        lambda x: (
            (x["Revenue"].sum() - x["Ad_Spend"].sum())
            / x["Ad_Spend"].sum()
        ) * 100
    )
)

plt.figure(figsize=(10, 6))
channel_roi.plot(kind="bar")

plt.title("ROI by Marketing Channel")
plt.xlabel("Channel")
plt.ylabel("ROI (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("screenshots/roi_by_channel.png", dpi=300)
plt.close()

print("5. screenshots/roi_by_channel.png")

# -----------------------------------
# Chart 6: Revenue vs Ad Spend
# -----------------------------------

channel_financials = (
    df.groupby("Channel")[["Ad_Spend", "Revenue"]]
    .sum()
)

channel_financials.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Revenue vs Ad Spend by Marketing Channel")
plt.xlabel("Channel")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("screenshots/revenue_vs_ad_spend.png", dpi=300)
plt.close()

print("6. screenshots/revenue_vs_ad_spend.png")

# -----------------------------------
# Chart 7: Conversion Rate by Age Group
# -----------------------------------

age_conversion = (
    df.groupby("Age_Group")
    .apply(
        lambda x: x["Conversions"].sum() /
        x["Leads"].sum() * 100
    )
)

plt.figure(figsize=(10, 6))
age_conversion.plot(kind="bar")

plt.title("Conversion Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Conversion Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("screenshots/conversion_rate_by_age_group.png", dpi=300)
plt.close()

print("7. screenshots/conversion_rate_by_age_group.png")
-- Customer Segment Analysis
-- Marketing Campaign Performance Analytics

-- Age Group Analysis
SELECT
    Age_Group,
    SUM(Ad_Spend) AS total_ad_spend,
    SUM(Revenue) AS total_revenue,
    SUM(Impressions) AS total_impressions,
    SUM(Clicks) AS total_clicks,
    SUM(Leads) AS total_leads,
    SUM(Conversions) AS total_conversions,
    ROUND(SUM(Clicks) / NULLIF(SUM(Impressions), 0) * 100, 2) AS ctr_percent,
    ROUND(SUM(Conversions) / NULLIF(SUM(Leads), 0) * 100, 2) AS conversion_rate_percent,
    ROUND(SUM(Ad_Spend) / NULLIF(SUM(Conversions), 0), 2) AS cac,
    ROUND((SUM(Revenue) - SUM(Ad_Spend)) / NULLIF(SUM(Ad_Spend), 0) * 100, 2) AS roi_percent
FROM marketing_data
GROUP BY Age_Group
ORDER BY total_revenue DESC;


-- Gender Analysis
SELECT
    Gender,
    SUM(Ad_Spend) AS total_ad_spend,
    SUM(Revenue) AS total_revenue,
    SUM(Impressions) AS total_impressions,
    SUM(Clicks) AS total_clicks,
    SUM(Leads) AS total_leads,
    SUM(Conversions) AS total_conversions,
    ROUND(SUM(Clicks) / NULLIF(SUM(Impressions), 0) * 100, 2) AS ctr_percent,
    ROUND(SUM(Conversions) / NULLIF(SUM(Leads), 0) * 100, 2) AS conversion_rate_percent,
    ROUND(SUM(Ad_Spend) / NULLIF(SUM(Conversions), 0), 2) AS cac,
    ROUND((SUM(Revenue) - SUM(Ad_Spend)) / NULLIF(SUM(Ad_Spend), 0) * 100, 2) AS roi_percent
FROM marketing_data
GROUP BY Gender
ORDER BY total_revenue DESC;
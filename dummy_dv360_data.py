
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Define the schema
schema = {
    "Comment": "string",
    "data_source": "string",
    "total_cost_usd": np.float64,
    "partner_cost_usd": np.float64,
    "agency_profit_usd": np.float64,
    "media_cost_usd": np.float64,
    "non_media_cost_usd": np.float64,
    "platform_cost_usd": np.float64,
    "data_fee_usd": np.float64,
    "verification_fee_usd": np.float64,
    "seat_id": "string",
    "seat_name": "string",
    "advertiser_id": "string",
    "advertiser_name": "string",
    "master_business_unit_name": "string",
    "master_advertiser_name": "string",
    "date": "date",
    "campaign_id": "string",
    "campaign_name": "string",
    "line_item_id": "string",
    "line_item_name": "string",
    "package_group_id": "string",
    "package_group_name": "string",
    "ad_id": "string",
    "ad_name": "string",
    "creative_id": "string",
    "creative_name": "string",
    "creative_size": "string",
    "device_type": "string",
    "web_environment": "string",
    "ad_format": "string",
    "deal_id": "string",
    "raw_exchange_id": "string",
    "raw_exchange_name": "string",
    "master_exchange_name": "string",
    "market_type": "string",
    "impressions": "int64",
    "measurable_impressions": "int64",
    "viewable_impressions": "int64",
    "clicks": "int64",
    "video_starts": "int64",
    "video_completes": np.float64,
    "conversion_total": np.float64,
    "conversion_clickthrough": np.float64,
    "conversion_viewthrough": np.float64,
    "delivery_country": "string",
    "first_quartile_views_video": np.float64,
    "midpoint_views_video": np.float64,
    "third_quartile_views_video": np.float64
}

# Generate dummy data
# Generate dummy data with seasonality and variations
data = []
advertiser_mapping = {}
seat_mapping = {}
campaign_mapping = {}
line_item_mapping = {}
package_group_mapping = {}
ad_mapping = {}
exchange_mapping = {}

business_unit_mapping = {}
creative_size_mapping = {}
ad_format_mapping = {}





for _ in range(1000):
    row = {
        "Comment": "Great campaign!",
        "data_source": random.choice(["Google Ads", "Facebook Ads", "DV360"]),
        "total_cost_usd": round(random.uniform(100.0, 1000.0), 6),
        "partner_cost_usd": round(random.uniform(50.0, 500.0), 6),
        "agency_profit_usd": round(random.uniform(10.0, 100.0), 6),
        "media_cost_usd": round(random.uniform(50.0, 500.0), 6),
        "non_media_cost_usd": round(random.uniform(100.0, 1000.0), 6),
        "platform_cost_usd": round(random.uniform(10.0, 100.0), 6),
        "data_fee_usd": round(random.uniform(1.0, 10.0), 6),
        "verification_fee_usd": round(random.uniform(1.0, 10.0), 6),
        "seat_id": str(random.randint(1, 1000)),
        "seat_name": "Seat " + str(random.randint(1, 10)),
        "advertiser_id": str(random.randint(1, 10000)),
        "advertiser_name": "Advertiser " + str(random.randint(1, 100)),
        "master_business_unit_name": "Business Unit " + str(random.randint(1, 10)),
        "master_advertiser_name": "Advertiser " + str(random.randint(1, 100)),
        "date": (datetime.now() - timedelta(days=random.randint(1, 30))).date(),
        "campaign_id": str(random.randint(1, 10000)),
        "campaign_name": "Campaign " + str(random.randint(1, 100)),
        "line_item_id": str(random.randint(1, 10000)),
        "line_item_name": "Line Item " + str(random.randint(1, 100)),
        "package_group_id": str(random.randint(1, 1000)),
        "package_group_name": "Package Group " + str(random.randint(1, 10)),
        "ad_id": str(random.randint(1, 10000)),
        "ad_name": "Ad " + str(random.randint(1, 100)),
        "creative_id": str(random.randint(1, 10000)),
        "creative_name": "Creative " + str(random.randint(1, 100)),
        "creative_size": random.choice(["300x250", "728x90", "160x600"]),
        "device_type": random.choice(["Mobile", "Desktop", "Tablet"]),
        "web_environment": random.choice(["Web", "App"]),
        "ad_format": random.choice(["Display", "Video", "Native"]),
        "deal_id": str(random.randint(1, 1000)),
        "raw_exchange_id": "Exchange " + str(random.randint(1, 10)),
        "raw_exchange_name": "Exchange " + str(random.randint(1, 10)),
        "master_exchange_name": "Exchange " + str(random.randint(1, 10)),
        "market_type": random.choice(["public market", "private market"]),
        "impressions": random.randint(100, 1000),
        "measurable_impressions": random.randint(100, 1000),
        "viewable_impressions": random.randint(100, 1000),
        "clicks": random.randint(10, 100),
        "video_starts": random.randint(10, 100),
        "video_completes": round(random.uniform(0.0, 1.0), 6),
        "conversion_total": round(random.uniform(1.0, 100.0), 9),
        "conversion_clickthrough": round(random.uniform(1.0, 100.0), 9),
        "conversion_viewthrough": round(random.uniform(1.0, 100.0), 9),
        "delivery_country": random.choice(["US", "UK", "CA", "AU", "DE"]),
        "first_quartile_views_video": round(random.uniform(0.0, 1.0), 6),
        "midpoint_views_video": round(random.uniform(0.0, 1.0), 6),
        "third_quartile_views_video": round(random.uniform(0.0, 1.0), 6)
    }

    # Calculate total_cost_usd and agency_profit_usd based on the formula
    row["total_cost_usd"] = (
        row["partner_cost_usd"] + row["media_cost_usd"] + row["non_media_cost_usd"] +
        row["platform_cost_usd"] + row["data_fee_usd"] + row["verification_fee_usd"]
    )


     # Assign the same IDs to the same names
    if row["advertiser_name"] in advertiser_mapping:
        row["advertiser_id"] = advertiser_mapping[row["advertiser_name"]]
    else:
        advertiser_id = str(random.randint(1, 10000))
        row["advertiser_id"] = advertiser_id
        advertiser_mapping[row["advertiser_name"]] = advertiser_id

    if row["seat_name"] in seat_mapping:
        row["seat_id"] = seat_mapping[row["seat_name"]]
    else:
        seat_id = str(random.randint(1, 1000))
        row["seat_id"] = seat_id
        seat_mapping[row["seat_name"]] = seat_id

    if row["campaign_name"] in campaign_mapping:
        row["campaign_id"] = campaign_mapping[row["campaign_name"]]
    else:
        campaign_id = str(random.randint(1, 10000))
        row["campaign_id"] = campaign_id
        campaign_mapping[row["campaign_name"]] = campaign_id

    if row["line_item_name"] in line_item_mapping:
        row["line_item_id"] = line_item_mapping[row["line_item_name"]]
    else:
        line_item_id = str(random.randint(1, 10000))
        row["line_item_id"] = line_item_id
        line_item_mapping[row["line_item_name"]] = line_item_id

    if row["package_group_name"] in package_group_mapping:
        row["package_group_id"] = package_group_mapping[row["package_group_name"]]
    else:
        package_group_id = str(random.randint(1, 1000))
        row["package_group_id"] = package_group_id
        package_group_mapping[row["package_group_name"]] = package_group_id

    if row["ad_name"] in ad_mapping:
        row["ad_id"] = ad_mapping[row["ad_name"]]
    else:
        ad_id = str(random.randint(1, 10000))
        row["ad_id"] = ad_id
        ad_mapping[row["ad_name"]] = ad_id

    if row["raw_exchange_name"] in exchange_mapping:
        row["raw_exchange_id"] = exchange_mapping[row["raw_exchange_name"]]
    else:
        exchange_id = str(random.randint(1, 1000))
        row["raw_exchange_id"] = exchange_id
        exchange_mapping[row["raw_exchange_name"]] = exchange_id

    if row["creative_id"] in ad_format_mapping:
        row["ad_format"] = ad_format_mapping[row["creative_id"]]
    else:
        ad_format = random.choice(["Display", "Video", "Native"])
        row["ad_format"] = ad_format
        exchange_mapping[row["creative_id"]] = ad_format


# Set web_environment based on device_type

    if row["device_type"] in ["Desktop", "Tablet"]:
        row["web_environment"] = "Web"
    else:
        row["web_environment"] = "App"


################################## Instroduce some insights into the data ####################

    # Introduce seasonality in performance
    if row["data_source"] == "Google Ads":
        # Assume the dataset is for the month of July
        # Introduce higher impressions and conversions for campaigns during weekends (Saturday and Sunday)
        if row["date"].weekday() in [5, 6]:  # Saturday or Sunday
            row["impressions"] *= 1.3
            row["conversion_total"] *= 1.2
            
    data.append(row)

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Set the data types for the DataFrame columns based on the schema
# df = df.astype


print(df.head(5))

df.to_csv("dummy_dataset.csv", index=False)
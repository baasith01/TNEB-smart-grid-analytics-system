import pandas as pd
import numpy as np

consumers_df = pd.read_csv("data/raw/consumers.csv")

months = pd.date_range(
    start="2025-01-01",
    end="2025-12-01",
    freq="MS"
)

data = []

reading_id = 1

for _, consumer in consumers_df.iterrows():

    consumer_id = consumer["consumer_id"]
    consumer_type = consumer["consumer_type"]

    for month in months:

        if consumer_type == "Residential":
            units = np.random.randint(80, 600)

        elif consumer_type == "Commercial":
            units = np.random.randint(500, 3000)

        elif consumer_type == "Industrial":
            units = np.random.randint(3000, 15000)

        else:
            units = np.random.randint(200, 1500)

        peak_demand = round(
            units * np.random.uniform(0.01, 0.03),
            2
        )

        meter_status = np.random.choice(
            ["Normal", "Faulty", "No Reading"],
            p=[0.95, 0.03, 0.02]
        )

        data.append([
            reading_id,
            consumer_id,
            month.date(),
            units,
            peak_demand,
            meter_status
        ])

        reading_id += 1

meter_df = pd.DataFrame(
    data,
    columns=[
        "reading_id",
        "consumer_id",
        "reading_date",
        "units_consumed",
        "peak_demand_kw",
        "meter_status"
    ]
)

meter_df.to_csv(
    "data/raw/meter_readings.csv",
    index=False
)

print(meter_df.head())
print(f"\nTotal Records: {len(meter_df)}")
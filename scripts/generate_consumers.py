import pandas as pd
import numpy as np
from faker import Faker

fake = Faker("en_IN")

# Read regions dataset
regions_df = pd.read_csv("data/raw/regions.csv")

num_consumers = 100000

consumer_types = [
    "Residential",
    "Commercial",
    "Industrial",
    "Agricultural"
]

consumer_weights = [
    0.70,
    0.15,
    0.10,
    0.05
]

status_list = [
    "Active",
    "Inactive",
    "Disconnected"
]

status_weights = [
    0.90,
    0.07,
    0.03
]

data = []

for i in range(1, num_consumers + 1):

    consumer_id = 100000 + i

    consumer_name = fake.name()

    region_id = np.random.choice(
        regions_df["region_id"]
    )

    consumer_type = np.random.choice(
        consumer_types,
        p=consumer_weights
    )

    connection_date = fake.date_between(
        start_date="-15y",
        end_date="today"
    )

    if consumer_type == "Residential":
        load = round(
            np.random.uniform(1, 10),
            2
        )

    elif consumer_type == "Commercial":
        load = round(
            np.random.uniform(10, 50),
            2
        )

    elif consumer_type == "Industrial":
        load = round(
            np.random.uniform(50, 500),
            2
        )

    else:
        load = round(
            np.random.uniform(5, 25),
            2
        )

    meter_id = f"MTR{consumer_id}"

    status = np.random.choice(
        status_list,
        p=status_weights
    )

    data.append([
        consumer_id,
        consumer_name,
        region_id,
        consumer_type,
        connection_date,
        load,
        meter_id,
        status
    ])

consumers_df = pd.DataFrame(
    data,
    columns=[
        "consumer_id",
        "consumer_name",
        "region_id",
        "consumer_type",
        "connection_date",
        "sanctioned_load_kw",
        "meter_id",
        "status"
    ]
)

consumers_df.to_csv(
    "data/raw/consumers.csv",
    index=False
)

print(consumers_df.head())
print(f"\nTotal Records: {len(consumers_df)}")
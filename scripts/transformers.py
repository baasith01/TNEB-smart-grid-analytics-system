import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

regions_df = pd.read_csv("data/raw/regions.csv")

num_transformers = 5000

data = []

for i in range(1, num_transformers + 1):

    transformer_id = 500000 + i

    region_id = np.random.choice(
        regions_df["region_id"]
    )

    capacity_kva = np.random.choice(
        [25, 63, 100, 160, 250, 500, 1000]
    )

    installation_date = fake.date_between(
        start_date="-20y",
        end_date="-1y"
    )

    last_maintenance_date = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    failure_count = np.random.poisson(2)

    health_score = round(
        max(
            0,
            100 - (failure_count * np.random.uniform(5, 15))
        ),
        2
    )

    data.append([
        transformer_id,
        region_id,
        capacity_kva,
        installation_date,
        last_maintenance_date,
        failure_count,
        health_score
    ])

transformers_df = pd.DataFrame(
    data,
    columns=[
        "transformer_id",
        "region_id",
        "capacity_kva",
        "installation_date",
        "last_maintenance_date",
        "failure_count",
        "health_score"
    ]
)

transformers_df.to_csv(
    "data/raw/transformers.csv",
    index=False
)

print(transformers_df.head())
print(f"\nTotal Records: {len(transformers_df)}")
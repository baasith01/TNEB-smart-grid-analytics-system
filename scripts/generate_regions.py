import pandas as pd
import numpy as np

regions = [
    ("Chennai","North"),
    ("Coimbatore","West"),
    ("Madurai","South"),
    ("Tiruchirappalli","Central"),
    ("Salem","West"),
    ("Tirunelveli","South"),
    ("Erode","West"),
    ("Vellore","North"),
    ("Thoothukudi","South"),
    ("Dindigul","South"),
    ("Thanjavur","Central"),
    ("Karur","Central"),
    ("Namakkal","West"),
    ("Virudhunagar","South"),
    ("Kanchipuram","North"),
    ("Cuddalore","East"),
    ("Nagapattinam","East"),
    ("Dharmapuri","West"),
    ("Krishnagiri","West"),
    ("Ramanathapuram","South"),
    ("Sivagangai","South"),
    ("Ariyalur","Central"),
    ("Perambalur","Central"),
    ("Nilgiris","West"),
    ("Tenkasi","South")
]

data = []

for i, (district, zone) in enumerate(regions, start=101):

    population = np.random.randint(
        500000,
        8000000
    )

    consumer_count = int(
        population * np.random.uniform(
            0.18,
            0.35
        )
    )

    data.append([
        i,
        district,
        district,
        zone,
        population,
        consumer_count
    ])

regions_df = pd.DataFrame(
    data,
    columns=[
        "region_id",
        "region_name",
        "district",
        "zone",
        "population",
        "consumer_count"
    ]
)

regions_df.to_csv(
    "data/raw/regions.csv",
    index=False
)

print(regions_df.head())
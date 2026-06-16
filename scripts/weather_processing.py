import pandas as pd

df = pd.read_csv(
    r"D:\TNEB\TNEB_Data analytics_project\data\raw\external\TNweather_1.8M.csv"
)

weather_summary = (
    df.groupby("city")
    .agg(
        avg_temperature=("temperature_2m", "mean"),

        avg_humidity=("relative_humidity_2m", "mean"),

        total_rainfall=("rain", "sum"),

        avg_wind_speed=("wind_speed_10m", "mean")
    )
    .reset_index()
)

weather_summary.to_csv(
    r"D:\TNEB\TNEB_Data analytics_project\data\raw\external\weather_summary.csv",
    index=False
)

print(weather_summary.head())
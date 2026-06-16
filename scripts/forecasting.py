import pandas as pd
import matplotlib.pyplot as plt

meter_df = pd.read_csv(
    r"D:\TNEB\TNEB_Data analytics_project\data\raw\meter_readings.csv"
)

meter_df["reading_date"] = pd.to_datetime(
    meter_df["reading_date"]
)

monthly = (
    meter_df
    .groupby(
        meter_df["reading_date"].dt.month
    )["units_consumed"]
    .sum()
    .reset_index()
)

monthly.columns = [
    "month",
    "total_units"
]

print(monthly)

plt.figure(figsize=(8,4))

plt.plot(
    monthly["month"],
    monthly["total_units"]
)

plt.xlabel("Month")

plt.ylabel("Units")

plt.title("Monthly Electricity Demand Trend")



from sklearn.linear_model import LinearRegression

monthly["month_number"] = range(
    1,
    len(monthly)+1
)

X = monthly[["month_number"]]

y = monthly["total_units"]

model = LinearRegression()

model.fit(X, y)

future = pd.DataFrame({
    "month_number": [13]
})

prediction = model.predict(future)

print(
    "Predicted units for next month:",
    int(prediction[0])
)

plt.show()
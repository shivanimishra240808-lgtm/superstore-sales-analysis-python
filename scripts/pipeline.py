import pandas as pd
import matplotlib.pyplot as plt
import os


os.makedirs("output", exist_ok=True)

df = pd.read_csv("dataset/sales.csv")


df = df.loc[:, ~df.columns.str.contains('^Unnamed')]


print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()


df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="mixed")


df["Month"] = df["Order Date"].dt.month
df["Year"] = df["Order Date"].dt.year


category_sales = df.groupby("Category")["Sales"].sum()
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.savefig("output/category_sales.png")
plt.show()


region_profit = df.groupby("Region")["Profit"].sum()
region_profit.plot(kind="bar")
plt.title("Profit by Region")
plt.savefig("output/region_profit.png")
plt.show()


monthly_sales = df.groupby("Month")["Sales"].sum()
monthly_sales.plot(kind="line")
plt.title("Monthly Sales Trend")
plt.savefig("output/monthly_sales.png")
plt.show()


df.to_csv("output/cleaned_sales_data.csv", index=False)

print("Data pipeline completed successfully")

# import pandas as pd

# sales = pd.read_csv("sales_data_large.csv")
# print(sales)

# 3. Filtering Data
# print(sales[sales["Sales"] > 30000])

# 4. Data Analysis
# print(sales["Sales"].mean())

# 5. Reporting
# print(sales.groupby("Region")["Sales"].mean())

# 7.1 head()
# print(sales.head())
# print(sales.tail())
# print(sales.sample(3))
# print(sales.columns)
# print(sales.index)
# print(sales.dtypes)
# print(sales.info())
# print(sales.shape)
# print(sales.describe())


# 8. Selecting Data
# print(sales["Sales"])
# print(sales[["OrderID", "Sales"]])
# print(sales[0:5])

# 9. Indexing in Pandas
# loc[]
# Label based indexing.
# print(sales.loc[2])

# Specific value:
# print(sales.loc[0, "OrderID"])

# 10. Basic Filtering
# Single Condition

# print(sales[
#     sales["Sales"] > 40000
# ])

# Multiple Conditions
# AND (&)

# print(sales[
#     (sales["Sales"] > 30000)
#     &
#     (sales["Region"] == "North")
# ])

# OR (|)
# print(sales[
#     (sales["Region"] == "North")
#     |
#     (sales["Region"] == "West")
# ])

# 11. Sorting Data
# sort_values()
# print(sales.sort_values(
#     "Sales",
#     ascending=True
# ))

# sort_index()
# print(sales.sort_index())


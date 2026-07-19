# LECTURE 2

# import numpy as np

# arr = np.array([1,2,3,4,5,6])
# new_arr= arr.reshape(2,3)
# print(new_arr)


# arr = np.array([1,2,3,4,5,6])

# new_arr = arr.reshape(2,3)

# print(new_arr)

# Using -1 in Reshape

# arr = np.arange(12)

# print(arr.reshape(3,-1))

# 3. Flattening Arrays

# arr = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# print(arr.flatten())

# 3.2 ravel()

# print(arr.ravel())

# 4. Mathematical Operations

# 4.1 Addition
# Example:

# sales = np.array([10000,15000,20000])

# print(sales + 5000)
# print(sales - 2000)
# print(sales * 2)
# print(sales / 2)

# salary = np.array([25000,30000,35000])
# bonus = np.array([2000,3000,4000])

# print(salary + bonus)

# 5. Aggregation Functions

# sales = np.array([1000,2000,3000])

# print(sales.sum())
# print(sales.mean())
# print(sales.min())
# print(sales.max())
# print(sales.std())
# print(sales.var())

# 6. Statistical Functions

# marks = np.array([60,70,80,90])

# print(np.mean(marks))
# print(np.median(marks))
# print(np.percentile(marks,50))

# 6.4 Correlation Coefficient

# sales = np.array([10,20,30,40])
# marketing = np.array([2,4,6,8])

# print(np.corrcoef(sales,marketing))


# 7. Filtering with Conditions (Boolean Masking)

# salary = np.array([20000,35000,50000,70000])

# print(salary > 40000)

# Extract Actual Values
# print(salary[salary > 40000])

# Example 2: Sales Above Target
# sales = np.array([12000,18000,25000,9000])

# print(sales[sales > 15000])

# Multiple Conditions

# salary = np.array([20000,30000,40000,50000,60000])

# print(salary[(salary > 25000) & (salary < 55000)])

# OR Condition
# print(salary[(salary < 25000) | (salary > 55000)])

# 8. Handling Missing Values

# arr = np.array([10,20,np.nan,40])

# print(arr)

# Detect Missing Values
# print(np.isnan(arr))

# Mean Ignoring Missing Values
# print(np.nanmean(arr))

# Sum Ignoring Missing Values

# print(np.nansum(arr))

# 9. Sorting Arrays

# Using sort()
# arr = np.array([50,20,90,10])

# print(np.sort(arr))
# print(np.sort(arr)[::-1])

# 10. Unique Values

# department = np.array([
#     'HR','IT','IT','Finance','HR'
# ])

# print(np.unique(department))

# Count Unique Values
# unique, count = np.unique(
#     department,
#     return_counts=True
# )

# print(unique)
# print(count)

# 11. Mini Real-World Case Study
# Employee Salary Dataset
# salary = np.array([
#     25000,
#     35000,
#     45000,
#     np.nan,
#     55000,
#     65000
# ])

# Tasks:

# Find average salary.
# Find highest salary.
# Find salaries above 40000.
# Sort salaries.
# Ignore missing values.

# print(np.nanmean(salary))
# print(np.nanmax(salary))
# print(salary[salary > 40000])
# print(np.sort(salary))

# salary = np.array([
#     25000,
#     35000,
#     45000,
#     np.nan,
#     55000,
#     65000
# ])

# print(np.nanmean(salary))
# print(np.nanmax(salary))
# print(salary[salary > 40000])
# print(np.sort(salary))

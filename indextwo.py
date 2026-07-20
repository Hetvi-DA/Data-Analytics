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

                        # Practice Questions
# Basic

# 1. Create array from 1–20 and reshape into 4×5.
# arr = np.arange(1, 21).reshape(4, 5)
# print(arr)

# 2. Find sum, mean, min, max.
# print("Sum:", np.sum(arr))
# print("Mean:", np.mean(arr))
# print("Minimum:", np.min(arr))
# print("Maximum:", np.max(arr))

# 3. Find standard deviation
# print("Standard Deviation:", np.std(arr))

# 4. Filter values greater than 50.
# print(arr[arr > 50])

# 5. Sort array.
# sorted_arr = np.sort(arr)
# print(sorted_arr)

# Intermediate

# 1. Create salary dataset with missing values.
# salary = np.array([25000, 40000, np.nan, 55000, 70000, np.nan, 45000])

# print(salary)

# 2. Find average salary ignoring null values.
# average_salary = np.nanmean(salary)
# print("Average Salary:", average_salary)


# 3. Extract salaries between 30K–60K.
# filtered_salary = salary[(salary >= 30000) & (salary <= 60000)]

# print(filtered_salary)

# 4. Find unique departments.
# departments = np.array([
#     "HR",
#     "IT",
#     "Finance",
#     "HR",
#     "Sales",
#     "IT",
#     "Finance"
# ])

# print(np.unique(departments))

# 5. Calculate percentile.
# print("75th Percentile:", np.nanpercentile(salary, 75))


# Homework Assignment


# print("Salary Dataset:")
# print(salary)

# print("\nDepartments:")
# print(departments)

# 1. Mean Salary
# print("Mean Salary:", np.nanmean(salary))

# 2. Maximum Salary
# print("Maximum Salary:", np.nanmax(salary))

# 3. Salary > 40K
# print("Salary Greater than 40K:")
# print(salary[salary > 40000])

# 4. Sorting
# print("Sorted Salary:")
# print(np.sort(salary))

# # 5. Missing Value Handling
# print("Average Salary (Ignoring Missing Values):")
# print(np.nanmean(salary))

# # 6. Unique Department Count
# print("Unique Departments:", np.unique(departments))
# print("Total Unique Departments:", len(np.unique(departments)))
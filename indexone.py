# LECTURE 1

# arr = np.array([10,20,30])

# print(arr + arr)

# import numpy as np

# salary = np.array([20000, 30000, 40000])

# print(salary * 1.10)

#  Creating Arrays in NumPy

#  Creating 1D Array

# import numpy as np

# marks = np.array([85, 90, 78, 92])

# print(marks)

# 5.2 Creating 2D Array

# Rows and columns.
# import numpy as np
# employee_data = np.array([
#     [101, 25000],
#     [102, 30000],
#     [103, 35000]
# ])

# print(employee_data)

# 5.3 Creating Array using zeros()

# np.zeros(5)

# 2D Example:

# np.zeros((3,4))

# 5.4 Creating Array using ones()

# print(np.ones(5))

# 2D Example:

# print(np.ones((2,3)))

# 5.5 Using arange()
# Like Python range().

# print(np.arange(1,11))

# Step Example:

# print(np.arange(0,20,2))

# 5.6 Using linspace()
# Creates evenly spaced values

# print(np.linspace(1,10,5))

# 5.7 Random Number Generation

# Random Integers
# print(np.random.randint(1,100,10))

# Random Decimal Values
# print(np.random.random(5))

# 6. Array Properties
# 6.1 ndim

# arr = np.array([[1,2],[3,4]])

# print(arr.ndim)

# 6.2 shape

# 6.2 shape

# print(arr.shape)

# 6.3 size

# print(arr.size)

# 6.4 dtype

# print(arr.dtype)

# 7. Indexing in NumPy

# 7.1 Indexing in 1D Array

# sales = np.array([10000,15000,20000,25000])

# print(sales[0])
# print(sales[2])

# print(sales[-1])

# 8. Slicing in NumPy

# arr = np.array([10,20,30,40,50])

# print(arr[1:4])

# Step Slicing
# print(arr[0:5:2])

# 9. 2D Array Indexing & Slicing

# employee = np.array([
#     [101,25000],
#     [102,30000],
#     [103,35000]
# ])

# Access Row
# print(employee[1])

# Access Specific Value
# print(employee[1,1])

# Access Full Column

# print(employee[:,1])


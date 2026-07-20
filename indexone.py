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


                        #  PRACTICE QUESTIONS
# BASIC 

# 1. Create an array of numbers from 1 to 20
# arr= np.arange(1,21)
# print(arr)

# 2. Create a 2D employee salary dataset.
# employees = np.array([
#     [101,50000],
#     [102,70000],
#     [103,40000],
#     [104,60000]
# ])  
# print(employees) 

# 3. Print datatype of array.
# print(arr.dtype)

# 4. Extract last element.
# print(arr[-1])

# 5. Slice first 5 values.
# print(arr[:5])


# INTERMEDIATE

# 6. Create random salary data.
# salary = np.random.randint(30000, 100000, size=10)
# print(salary)

# 7. Extract complete salary column.
# salary_column = employees[:,1]
# print(salary_column)

# 8. Create matrix using zeros.
# zero_matrix = np.zeros((3, 3))
# print(zero_matrix)

# 9. Create matrix using ones.
# one_matrix = np.ones((3, 3))
# print(one_matrix)

# 10. Generate even numbers till 100
# even = np.arange(2, 101, 2)
# print(even)

                         # Homework Assignment
# students = np.array([
#     [101, 85],
#     [102, 90],
#     [103, 78],
#     [104, 88],
#     [105, 95]
# ])
# print("Student Dataset:")
# print(students)

# 1. Find total students
# print("Total Students:", students.shape[0])

# 2. Check datatype
# print("Datatype:", students.dtype)

# 3. Print dimensions
# print("Dimensions:", students.ndim)

# 4. Extract marks of second student
# print("Marks of Second Student:", students[1, 1])

# 5. Print only marks column
# print("Marks Column:")
# print(students[:, 1])

# 6. Slice first three records
# print("First Three Records:")
# print(students[:3])


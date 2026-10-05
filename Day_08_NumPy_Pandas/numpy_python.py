# NUMPY:

import numpy as np

# 1. Create a NumPy array
numbers = np.array([10, 20, 30, 40, 50])
print("Array:", numbers)

# 2. Create arrays using arange
arr = np.arange(1, 11)
print("Range array:", arr)

# 3. Create arrays of zeros and ones
zeros = np.zeros(5)
ones = np.ones(5)

print("Zeros:", zeros)
print("Ones:", ones)

# 4. Create an array with equally spaced values
values = np.linspace(0, 1, 5)
print("Linspace:", values)

# 5. Check array properties
print("Shape:", numbers.shape)
print("Number of dimensions:", numbers.ndim)
print("Data type:", numbers.dtype)
print("Number of elements:", numbers.size)

# 6. Indexing
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])

# 7. Slicing
print("First three:", numbers[:3])
print("From index 2:", numbers[2:])
print("Index 1 to 3:", numbers[1:4])

# 8. Change array values
numbers[0] = 100
print("After changing first value:", numbers)

# 9. Mathematical operations
arr = np.array([10, 20, 30, 40, 50])

print("Add 5:", arr + 5)
print("Subtract 5:", arr - 5)
print("Multiply by 2:", arr * 2)
print("Divide by 2:", arr / 2)

# 10. Array-to-array operations
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)
print("Multiplication:", a * b)

# 11. Aggregate functions
numbers = np.array([10, 20, 30, 40, 50])

print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Standard deviation:", np.std(numbers))
print("Variance:", np.var(numbers))

# 12. Boolean filtering
numbers = np.array([10, 25, 40, 55, 70])

print("Greater than 40:", numbers[numbers > 40])
print("Less than 50:", numbers[numbers < 50])

# 13. Multiple conditions
print("Between 20 and 60:", numbers[(numbers >= 20) & (numbers <= 60)])

# 14. Two-dimensional array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Matrix:\n", matrix)
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)

# 15. Access rows and columns
print("First row:", matrix[0])
print("Second row:", matrix[1])
print("First column:", matrix[:, 0])
print("Second column:", matrix[:, 1])

# 16. Access individual elements
print("Element at row 1, column 2:", matrix[1, 2])

# 17. 2D array slicing
print("First two rows:\n", matrix[:2])
print("First two columns:\n", matrix[:, :2])

# 18. Reshape
numbers = np.array([1, 2, 3, 4, 5, 6])

reshaped = numbers.reshape(2, 3)
print("Reshaped array:\n", reshaped)

# 19. Flatten an array
flattened = reshaped.flatten()
print("Flattened array:", flattened)

# 20. Transpose
print("Original matrix:\n", matrix)
print("Transpose:\n", matrix.T)

# 21. Random numbers
random_numbers = np.random.randint(1, 100, 5)
print("Random integers:", random_numbers)

# 22. Random decimal values
random_values = np.random.rand(5)
print("Random decimals:", random_values)

# 23. Sorting
numbers = np.array([50, 10, 40, 20, 30])

print("Sorted:", np.sort(numbers))

# 24. Find positions using where
numbers = np.array([10, 20, 30, 40, 50])

positions = np.where(numbers > 25)
print("Positions where value > 25:", positions)

# 25. Unique values
numbers = np.array([10, 20, 20, 30, 30, 30])

print("Unique values:", np.unique(numbers))

# 26. Concatenate arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

combined = np.concatenate((a, b))
print("Combined array:", combined)

# 27. Stack arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Vertical stack:\n", np.vstack((a, b)))
print("Horizontal stack:", np.hstack((a, b)))

# 28. Copy an array
original = np.array([10, 20, 30])
copied = original.copy()

copied[0] = 100

print("Original:", original)
print("Copied:", copied)

# 29. Handling missing values with NaN
numbers = np.array([10, 20, np.nan, 40, 50])

print("Array:", numbers)
print("Is NaN:", np.isnan(numbers))
print("Mean ignoring NaN:", np.nanmean(numbers))

# 30. Practical example: Student marks analysis
marks = np.array([78, 85, 92, 67, 88, 74, 95])

print("Marks:", marks)
print("Average marks:", np.mean(marks))
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Students scoring above 80:", marks[marks > 80])
print("Number of students above 80:", np.sum(marks > 80))
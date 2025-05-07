# numpy_basics.py

import numpy as np

# Create arrays
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])

# Array attributes
print("Array a:", a)
print("Shape of b:", b.shape)
print("Data type of a:", a.dtype)

# Basic operations
print("a + 5:", a + 5)
print("a * 2:", a * 2)
print("Dot product:", np.dot(a, a))

# Useful functions
z = np.zeros((2, 3))
o = np.ones((2, 3))
r = np.random.rand(2, 3)

print("Zeros:\n", z)
print("Ones:\n", o)
print("Random:\n", r)

# Indexing and slicing
print("First element of a:", a[0])
print("Second row of b:", b[1])
print("Element b[1,0]:", b[1, 0])

# Reshaping
c = np.arange(9).reshape((3, 3))
print("Reshaped array:\n", c)
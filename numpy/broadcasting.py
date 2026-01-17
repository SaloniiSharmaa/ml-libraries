import numpy as np

# broadcasting allows numpy to perform operations on arrays with different shapes by virtually expanding dimensions.
# so the match the larger array's shape
# the dimensions should have the same size or one of the dimensions must be 1.

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

# both the arrays are compatible as the row dimension has 1 and the column dimension also has 1 in one of the dimension.

print(array1*array2)




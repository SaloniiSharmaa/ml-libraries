import numpy as np

array = np.array([1,2,3])
# scalar arithmatic

print( array + 1)
print( array - 2)
print( array * 3)
print( array / 4)
print( array ** 5)

# vectorized math functions
print(np.sqrt(array))

array2  = np.array([1.01,2.63,3.41])
print(np.round(array2))
print(np.floor(array2)) # to round down
print(np.ceil(array2)) # to round up

print(np.pi)

# exercise
radii = np.array([1,2,3,4,5])
print(np.pi*radii**2)

# element wise arithmatic
print(array + array2)
print(array - array2)
print(array * array2)
print(array / array2)
print(array ** array2)

# comparison operators

scores = np.array([91,55,100,73,82,64])

print(scores == 100)
print(scores >= 60)
print(scores < 60)

scores[scores<60] = 0
print(scores)



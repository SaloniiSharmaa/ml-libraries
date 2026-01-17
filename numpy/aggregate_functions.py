import numpy as np

# aggregate functions summarize data and typically returns a single value.
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])


print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.median(array))
print(np.var(array))
print(np.max(array))
print(np.min(array))
print(np.argmin(array))
print(np.argmax(array))

print(np.sum(array,axis=0)) # axis 0 says that it will sum the columns
print(np.sum(array,axis=1)) # axis 1 says that it will sum the rows




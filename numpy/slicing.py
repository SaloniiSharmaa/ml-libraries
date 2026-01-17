import numpy as np

# make a 2d array
array = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16] ])

# slicing can be done as: array[start:end:step], remember that the ending index is exclusive which means the ending index will also be sliced
# when you want to include everything from the starting index up until the end then the ending index value is left blank

# row selection

print(array[0:4:2])

print(array[:4:1]) #to include from the very start

print(array[::2])  #to include everything from start to end

print(array[::-1]) #to get a reversed order


# column selection

# for  column selection of 2 d array we need to indexes separated by comma

print(array[0,0])

print(array[:,1]) # the colon here will include every row and will select index 1 of every row

print(array[:,-1])

print(array[:,0:3]) # this includes all rows because of : and includes the indexes of column 0 to 2 of every row.
# as our array is 2d so the indexing should have only 2 commas and not 3

print(array[:,1:]) # this will include every row and will include everything from index 1 of each row upto the end

print(array[:,::2]) # this will include every row and every element of every column with a step of 2
print(array[:,1::2]) # this will start at column 1

print(array[:,::-1]) # to reverse the order
print(array[:,::-2])


# both row and column selection
print(array[0:2,0:2]) #the left side of comma commands to include rows from index 0 uptill 2
# the right side of comma commands to include columns from index 0 uptill 2
print(array[0:2,2:])
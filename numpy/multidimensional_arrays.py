import numpy as np

#zero dimensional array
array = np.array('A')
print (array.ndim)

#one dimensional array
array1 = np.array(['a','b','c'])
print(array1.ndim)

#two dimensional array
array2 = np.array([['a','b','c'],['d','e','f']])
print(array2.ndim)

#three dimensional array
array3 = np.array([
    [['a','b','c'],['d','e','f']],
    [['g','h','i'],['j','k','l']],
    [['m','n','o'],['p','q','r']],
    [['s','t','u'],['v','w','x']],
    [['y','z','_'],['w','x','_']]
    ])
print(array3.ndim)

# to know the dimensions of array
print(array.shape)
print(array1.shape)
print(array2.shape)
print(array3.shape)

# chain indexing
print(array3[2][1][1])
print(array2[1][1])

# multidimensional indexing (faster than chain indexing)
print(array3[2,1,1])

# excercise to form a word using multidimensional indexing and string concatenation
word = array3[1,0,0] + array3[2,0,2] + array3[2,0,2] + array3[0,1,0]
print(word)







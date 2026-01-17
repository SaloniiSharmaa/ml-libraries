import numpy as np

rng = np.random.default_rng() # you can also set the SEED here.

print(rng.integers(low = 1, high = 7))

# to get a few random numbers , set a size. we can even set dimensions.
print(rng.integers(low = 1, high = 100, size = 5))
print(rng.integers(low = 1, high = 100, size = (5,3)))

# to get floating point numbers

np.random.seed(1)
print(np.random.uniform(low = -1, high = 1, size = (2,3)))

# learn to shuffle an array
array = np.array([1,2,3,4])
rng.shuffle(array)
print(array)

# to get a random choice
fruits = np.array(["apple", "banana", "cherry", "kiwi", "coconut"])
fruit = rng.choice(fruits) # you can also set the size or dimensions here
print(fruit)
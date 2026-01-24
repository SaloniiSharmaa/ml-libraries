import pandas as pd

coffee = pd.read_csv(r"C:\Users\saloni\Python_Lib\Pandas\Raw_data\coffee.csv")
print(coffee)

#print(coffee.sample()) # by default give one random answer but we can input the no. of random answers we want e.g sample(10)
# can also add random state to get same data everytime for ex print(coffee.sample(10, random_state = 1 ))

# loc and iloc

# loc allows us to filter rows and columns of our dataframe. e.g coffee.loc[rows,columns]

print(coffee.loc[0])
print(coffee.loc[[0,1,2]])
print(coffee.loc[[0,1,5]])
print(coffee.loc[0:5])
print(coffee.loc[0:8,["Day", "Units Sold"]])

# iloc is similar to loc but it just uses index number
print(coffee.iloc[0:5,[1,2]])
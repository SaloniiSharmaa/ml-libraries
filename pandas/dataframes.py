import pandas as pd

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a', 'b', 'c'])

print(df.head())  # by default gives the top 5 rows but can give any if provided by a no. like head(2)
print(df.tail())  # by default gives the last 5 rows but can give any if provided by a no. like tail(2)

print(df.columns) # to see what the column headers are.
print(df.index)  # to see what the row headers are.
print(df.index.tolist()) # to get the list of row headers.

print(df.info()) # to get the info of our data frames.
print(df.describe()) # to get some meaningful mathematical info from the data.

print(df.nunique()) # to get unique the no. of unique element from each column.
print(df['a'].nunique())

print(df.shape)
print(df.size)


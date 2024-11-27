import pandas as pd
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
data

data['b']

'a' in data

data.keys()

list(data.items())

data['e'] = 1.25
data

# slicing by explicit index, here 'c' will not be excluding
data['a':'c']

# slicing by implicit integer index, here 2 will be exclusive
data[0:2]

# masking
data[(data > 0.3) & (data < 0.8)]

# fancy indexing
data[['a', 'e']]

data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
data

# explicit index when indexing by keys
data[1]

# implicit index when slicing by index
data[1:3]

data.loc[1]
data.loc[1:3]

data.iloc[1]
data.iloc[1:3]

area = pd.Series({'California': 423967, 'Texas': 695662,
                 'New York': 141297, 'Florida': 170312, 'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                'New York': 19651127, 'Florida': 19552860, 'Illinois': 12882135})
data1 = pd.DataFrame({'area1': area, 'pop1': pop})
print(data1)
print('*' * 30)
